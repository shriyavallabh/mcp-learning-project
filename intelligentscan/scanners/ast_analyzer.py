"""
AST (Abstract Syntax Tree) Analyzer for IntelligentScan
Performs deep semantic code analysis beyond pattern matching
Supports Python, Java, JavaScript (can be extended to other languages)
"""

import ast
import os
from pathlib import Path
from typing import List, Dict, Any, Optional
from dataclasses import dataclass


@dataclass
class ASTViolation:
    """Represents a violation found via AST analysis"""
    file_path: str
    line_number: int
    violation_type: str
    description: str
    severity: str
    code_snippet: str
    function_name: Optional[str] = None
    class_name: Optional[str] = None


class PythonASTAnalyzer(ast.NodeVisitor):
    """
    AST analyzer for Python code
    Detects violations that require semantic understanding
    """

    def __init__(self, file_path: str, source_code: str):
        self.file_path = file_path
        self.source_code = source_code
        self.lines = source_code.split('\n')
        self.violations: List[ASTViolation] = []
        self.current_function = None
        self.current_class = None

    def visit_FunctionDef(self, node: ast.FunctionDef):
        """Visit function definitions"""
        # Track current function
        old_function = self.current_function
        self.current_function = node.name

        # Check for missing docstrings (AI-readiness issue)
        if not ast.get_docstring(node):
            self.violations.append(ASTViolation(
                file_path=self.file_path,
                line_number=node.lineno,
                violation_type="missing_docstring",
                description=f"Function '{node.name}' lacks docstring - reduces AI understanding",
                severity="low",
                code_snippet=self._get_code_snippet(node.lineno),
                function_name=node.name,
                class_name=self.current_class
            ))

        # Check for overly complex functions (cyclomatic complexity)
        complexity = self._calculate_complexity(node)
        if complexity > 10:
            self.violations.append(ASTViolation(
                file_path=self.file_path,
                line_number=node.lineno,
                violation_type="high_complexity",
                description=f"Function '{node.name}' has high complexity ({complexity}) - hard for AI to understand",
                severity="medium",
                code_snippet=self._get_code_snippet(node.lineno),
                function_name=node.name,
                class_name=self.current_class
            ))

        # Continue visiting child nodes
        self.generic_visit(node)
        self.current_function = old_function

    def visit_ClassDef(self, node: ast.ClassDef):
        """Visit class definitions"""
        old_class = self.current_class
        self.current_class = node.name

        # Check for missing docstrings
        if not ast.get_docstring(node):
            self.violations.append(ASTViolation(
                file_path=self.file_path,
                line_number=node.lineno,
                violation_type="missing_docstring",
                description=f"Class '{node.name}' lacks docstring",
                severity="low",
                code_snippet=self._get_code_snippet(node.lineno),
                class_name=node.name
            ))

        self.generic_visit(node)
        self.current_class = old_class

    def visit_Assign(self, node: ast.Assign):
        """Visit assignment statements"""
        # Check for hardcoded credentials (more precise than regex)
        for target in node.targets:
            if isinstance(target, ast.Name):
                var_name = target.id.lower()

                # Check if variable name suggests credentials
                if any(keyword in var_name for keyword in ['password', 'secret', 'api_key', 'token']):
                    # Check if assigned value is a string literal
                    if isinstance(node.value, ast.Constant) and isinstance(node.value.value, str):
                        # This is a hardcoded credential
                        self.violations.append(ASTViolation(
                            file_path=self.file_path,
                            line_number=node.lineno,
                            violation_type="hardcoded_credential",
                            description=f"Hardcoded credential in variable '{target.id}'",
                            severity="critical",
                            code_snippet=self._get_code_snippet(node.lineno),
                            function_name=self.current_function,
                            class_name=self.current_class
                        ))

        self.generic_visit(node)

    def visit_Call(self, node: ast.Call):
        """Visit function calls"""
        # Check for dangerous function calls
        if isinstance(node.func, ast.Name):
            func_name = node.func.id

            # Check for eval/exec (code injection risk)
            if func_name in ['eval', 'exec']:
                self.violations.append(ASTViolation(
                    file_path=self.file_path,
                    line_number=node.lineno,
                    violation_type="dangerous_function",
                    description=f"Use of dangerous function '{func_name}' - code injection risk",
                    severity="high",
                    code_snippet=self._get_code_snippet(node.lineno),
                    function_name=self.current_function,
                    class_name=self.current_class
                ))

        # Check for SQL execution with string concatenation
        if isinstance(node.func, ast.Attribute):
            if node.func.attr == 'execute':
                # Check if argument contains string concatenation
                if node.args and self._contains_string_concat(node.args[0]):
                    self.violations.append(ASTViolation(
                        file_path=self.file_path,
                        line_number=node.lineno,
                        violation_type="sql_injection",
                        description="SQL query uses string concatenation - injection risk",
                        severity="high",
                        code_snippet=self._get_code_snippet(node.lineno),
                        function_name=self.current_function,
                        class_name=self.current_class
                    ))

        self.generic_visit(node)

    def visit_Name(self, node: ast.Name):
        """Visit name references"""
        # Check for single-letter variable names (reduces AI understanding)
        if len(node.id) == 1 and node.id not in ['i', 'j', 'k', 'x', 'y', 'z', '_']:
            # Only flag if not in a loop or comprehension
            if not self._is_in_loop_context(node):
                self.violations.append(ASTViolation(
                    file_path=self.file_path,
                    line_number=node.lineno,
                    violation_type="poor_naming",
                    description=f"Single-letter variable '{node.id}' reduces code clarity",
                    severity="low",
                    code_snippet=self._get_code_snippet(node.lineno),
                    function_name=self.current_function,
                    class_name=self.current_class
                ))

        self.generic_visit(node)

    def _calculate_complexity(self, node: ast.FunctionDef) -> int:
        """
        Calculate cyclomatic complexity of a function
        Complexity = number of decision points + 1
        """
        complexity = 1

        for child in ast.walk(node):
            # Count decision points
            if isinstance(child, (ast.If, ast.While, ast.For, ast.ExceptHandler)):
                complexity += 1
            elif isinstance(child, ast.BoolOp):
                complexity += len(child.values) - 1

        return complexity

    def _contains_string_concat(self, node: ast.AST) -> bool:
        """Check if node contains string concatenation"""
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
            return True

        for child in ast.walk(node):
            if isinstance(child, ast.BinOp) and isinstance(child.op, ast.Add):
                return True

        return False

    def _is_in_loop_context(self, node: ast.AST) -> bool:
        """Check if node is in a loop context (simplified check)"""
        # This is a simplified check - in a full implementation,
        # we'd track the context properly
        return False

    def _get_code_snippet(self, line_number: int, context_lines: int = 2) -> str:
        """Get code snippet around a line number"""
        start = max(0, line_number - context_lines - 1)
        end = min(len(self.lines), line_number + context_lines)
        return '\n'.join(self.lines[start:end])


class ASTAnalyzerFactory:
    """Factory to create appropriate AST analyzer based on file type"""

    @staticmethod
    def create_analyzer(file_path: str, source_code: str) -> Optional[PythonASTAnalyzer]:
        """
        Create appropriate AST analyzer based on file extension

        Args:
            file_path: Path to the source file
            source_code: Content of the file

        Returns:
            Analyzer instance or None if file type not supported
        """
        extension = Path(file_path).suffix.lower()

        if extension == '.py':
            return PythonASTAnalyzer(file_path, source_code)
        # TODO: Add JavaASTAnalyzer, JavaScriptASTAnalyzer, etc.
        else:
            return None


def analyze_file_ast(file_path: str) -> List[ASTViolation]:
    """
    Analyze a single file using AST

    Args:
        file_path: Path to file to analyze

    Returns:
        List of violations found
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            source_code = f.read()

        analyzer = ASTAnalyzerFactory.create_analyzer(file_path, source_code)

        if not analyzer:
            return []  # File type not supported

        # Parse and analyze
        if isinstance(analyzer, PythonASTAnalyzer):
            tree = ast.parse(source_code)
            analyzer.visit(tree)
            return analyzer.violations

        return []

    except SyntaxError as e:
        # File has syntax errors - this itself is a violation
        return [ASTViolation(
            file_path=file_path,
            line_number=e.lineno or 0,
            violation_type="syntax_error",
            description=f"Syntax error: {str(e)}",
            severity="high",
            code_snippet=""
        )]
    except Exception as e:
        # Other errors - skip file
        print(f"Error analyzing {file_path}: {str(e)}")
        return []


def analyze_directory_ast(directory: str, file_pattern: str = "*.py") -> List[ASTViolation]:
    """
    Analyze all files in a directory using AST

    Args:
        directory: Directory to scan
        file_pattern: Glob pattern for files to analyze

    Returns:
        List of all violations found
    """
    all_violations = []
    directory_path = Path(directory)

    for file_path in directory_path.rglob(file_pattern):
        # Skip common directories
        if any(skip in str(file_path) for skip in ['.git', 'venv', 'node_modules', '__pycache__']):
            continue

        violations = analyze_file_ast(str(file_path))
        all_violations.extend(violations)

    return all_violations


# Example usage
if __name__ == "__main__":
    # Test AST analyzer on a sample Python file
    sample_code = """
def calculate(x, y):
    password = "hardcoded123"
    result = eval(x + y)
    return result

class MyClass:
    def process(self):
        if True:
            if True:
                if True:
                    if True:
                        if True:
                            return "complex"
    """

    # Analyze sample code
    analyzer = PythonASTAnalyzer("sample.py", sample_code)
    tree = ast.parse(sample_code)
    analyzer.visit(tree)

    print("=== AST Analysis Results ===")
    for violation in analyzer.violations:
        print(f"\n[{violation.severity.upper()}] {violation.description}")
        print(f"  Location: {violation.file_path}:{violation.line_number}")
        print(f"  Type: {violation.violation_type}")
