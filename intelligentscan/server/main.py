"""
IntelligentScan MCP Server
AI-powered code intelligence platform for vulnerability scanning, ARB compliance, and AI-readiness analysis.
"""

import os
import json
from datetime import datetime
from pathlib import Path
from typing import Optional, List, Dict, Any
from fastmcp import FastMCP
from loguru import logger

# Configure logging
logger.add("intelligentscan.log", rotation="1 day", retention="7 days", level="INFO")

# Initialize MCP server
mcp = FastMCP("IntelligentScan", version="0.1.0")

# Import scanners (will be implemented next)
from intelligentscan.scanners.vulnerability_scanner import VulnerabilityScanner
from intelligentscan.scanners.arb_scanner import ARBScanner
from intelligentscan.scanners.ai_readiness_scanner import AIReadinessScanner
from intelligentscan.utils.knowledge_graph import KnowledgeGraphBuilder
from intelligentscan.utils.report_generator import ReportGenerator


class ScanSession:
    """Manages a scanning session with state"""

    def __init__(self, repo_path: str, scan_id: str):
        self.repo_path = repo_path
        self.scan_id = scan_id
        self.start_time = datetime.now()
        self.results = {}
        self.knowledge_graph = None

    def add_result(self, scan_type: str, result: Dict[str, Any]):
        """Add scan results"""
        self.results[scan_type] = result

    def to_dict(self) -> Dict[str, Any]:
        """Convert session to dictionary"""
        return {
            "scan_id": self.scan_id,
            "repo_path": self.repo_path,
            "start_time": self.start_time.isoformat(),
            "duration_seconds": (datetime.now() - self.start_time).total_seconds(),
            "results": self.results,
            "knowledge_graph": self.knowledge_graph
        }


# Global session storage (in production, use Redis)
active_sessions: Dict[str, ScanSession] = {}


@mcp.tool()
async def scan_vulnerabilities(
    repo_path: str,
    vulnerability_types: Optional[List[str]] = None
) -> Dict[str, Any]:
    """
    Scan repository for security vulnerabilities

    Args:
        repo_path: Absolute path to the repository to scan
        vulnerability_types: Optional list of specific vulnerabilities to check
                           (e.g., ["log4j", "hardcoded_secrets", "sql_injection"])
                           If None, checks all vulnerability types

    Returns:
        Dictionary containing:
        - vulnerabilities_found: List of vulnerability details
        - severity_breakdown: Count by severity (critical, high, medium, low)
        - files_affected: Number of files with vulnerabilities
        - scan_metadata: Scan timing and configuration info

    Example:
        scan_vulnerabilities("/path/to/repo", ["log4j", "hardcoded_secrets"])
    """
    logger.info(f"Starting vulnerability scan for: {repo_path}")

    try:
        # Validate repository path
        if not os.path.exists(repo_path):
            return {"error": f"Repository path does not exist: {repo_path}"}

        # Create scan session
        scan_id = f"vuln_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        session = ScanSession(repo_path, scan_id)
        active_sessions[scan_id] = session

        # Initialize scanner
        scanner = VulnerabilityScanner(repo_path)

        # Perform scan
        results = await scanner.scan(vulnerability_types=vulnerability_types)

        # Store results
        session.add_result("vulnerability", results)

        logger.info(f"Vulnerability scan completed. Found {len(results.get('vulnerabilities_found', []))} issues")

        return {
            "scan_id": scan_id,
            "status": "completed",
            "summary": {
                "total_vulnerabilities": len(results.get("vulnerabilities_found", [])),
                "critical": results.get("severity_breakdown", {}).get("critical", 0),
                "high": results.get("severity_breakdown", {}).get("high", 0),
                "medium": results.get("severity_breakdown", {}).get("medium", 0),
                "low": results.get("severity_breakdown", {}).get("low", 0),
                "files_affected": results.get("files_affected", 0),
            },
            "vulnerabilities": results.get("vulnerabilities_found", []),
            "scan_time_seconds": results.get("scan_metadata", {}).get("duration_seconds", 0)
        }

    except Exception as e:
        logger.error(f"Error during vulnerability scan: {str(e)}")
        return {
            "error": str(e),
            "status": "failed"
        }


@mcp.tool()
async def check_arb_compliance(
    repo_path: str,
    arb_rules: Optional[List[str]] = None
) -> Dict[str, Any]:
    """
    Check repository against Architectural Review Board (ARB) guidelines

    Args:
        repo_path: Absolute path to the repository to scan
        arb_rules: Optional list of specific ARB rule IDs to check
                  (e.g., ["ARB-SEC-001", "ARB-PERF-005"])
                  If None, checks all ARB rules

    Returns:
        Dictionary containing:
        - violations_found: List of ARB rule violations
        - compliance_score: Overall compliance percentage (0-100)
        - violations_by_category: Grouped by security, performance, architecture, etc.
        - files_with_violations: Number of non-compliant files

    Example:
        check_arb_compliance("/path/to/repo", ["ARB-SEC-001"])
    """
    logger.info(f"Starting ARB compliance check for: {repo_path}")

    try:
        if not os.path.exists(repo_path):
            return {"error": f"Repository path does not exist: {repo_path}"}

        # Create scan session
        scan_id = f"arb_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        session = ScanSession(repo_path, scan_id)
        active_sessions[scan_id] = session

        # Initialize scanner
        scanner = ARBScanner(repo_path)

        # Perform scan
        results = await scanner.scan(rule_ids=arb_rules)

        # Store results
        session.add_result("arb_compliance", results)

        logger.info(f"ARB compliance check completed. Compliance score: {results.get('compliance_score', 0)}%")

        return {
            "scan_id": scan_id,
            "status": "completed",
            "compliance_score": results.get("compliance_score", 0),
            "summary": {
                "total_violations": len(results.get("violations_found", [])),
                "critical_violations": len([v for v in results.get("violations_found", [])
                                          if v.get("severity") == "critical"]),
                "files_checked": results.get("files_checked", 0),
                "files_with_violations": results.get("files_with_violations", 0)
            },
            "violations": results.get("violations_found", []),
            "violations_by_category": results.get("violations_by_category", {}),
        }

    except Exception as e:
        logger.error(f"Error during ARB compliance check: {str(e)}")
        return {
            "error": str(e),
            "status": "failed"
        }


@mcp.tool()
async def scan_ai_readiness(
    repo_path: str,
    include_suggestions: bool = True
) -> Dict[str, Any]:
    """
    Scan repository to determine AI-readiness (how well AI tools can understand the code)

    Args:
        repo_path: Absolute path to the repository to scan
        include_suggestions: If True, includes specific improvement suggestions

    Returns:
        Dictionary containing:
        - ai_readiness_score: Overall score 0-100
        - low_confidence_areas: Areas where AI struggles to understand
        - suggestions: List of improvements to make code more AI-friendly
        - knowledge_graph: Visual representation with red (low confidence) and green (good) nodes

    Example:
        scan_ai_readiness("/path/to/repo", include_suggestions=True)
    """
    logger.info(f"Starting AI-readiness scan for: {repo_path}")

    try:
        if not os.path.exists(repo_path):
            return {"error": f"Repository path does not exist: {repo_path}"}

        # Create scan session
        scan_id = f"ai_readiness_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        session = ScanSession(repo_path, scan_id)
        active_sessions[scan_id] = session

        # Initialize scanner
        scanner = AIReadinessScanner(repo_path)

        # Perform scan
        results = await scanner.scan(include_suggestions=include_suggestions)

        # Build knowledge graph
        graph_builder = KnowledgeGraphBuilder()
        knowledge_graph = graph_builder.build_from_scan_results(results)
        session.knowledge_graph = knowledge_graph

        # Store results
        session.add_result("ai_readiness", results)

        logger.info(f"AI-readiness scan completed. Score: {results.get('ai_readiness_score', 0)}")

        return {
            "scan_id": scan_id,
            "status": "completed",
            "ai_readiness_score": results.get("ai_readiness_score", 0),
            "summary": {
                "total_files_analyzed": results.get("total_files_analyzed", 0),
                "low_confidence_files": len(results.get("low_confidence_areas", [])),
                "suggestions_count": len(results.get("suggestions", [])) if include_suggestions else 0
            },
            "low_confidence_areas": results.get("low_confidence_areas", []),
            "suggestions": results.get("suggestions", []) if include_suggestions else [],
            "knowledge_graph": knowledge_graph
        }

    except Exception as e:
        logger.error(f"Error during AI-readiness scan: {str(e)}")
        return {
            "error": str(e),
            "status": "failed"
        }


@mcp.tool()
async def generate_report(
    scan_id: str,
    format: str = "json"
) -> Dict[str, Any]:
    """
    Generate a comprehensive report from a completed scan

    Args:
        scan_id: ID of the scan session to generate report for
        format: Output format ("json", "html", "markdown")

    Returns:
        Formatted report with all scan results, knowledge graph, and recommendations

    Example:
        generate_report("vuln_20250110_143022", format="html")
    """
    logger.info(f"Generating report for scan: {scan_id}")

    try:
        if scan_id not in active_sessions:
            return {"error": f"Scan session not found: {scan_id}"}

        session = active_sessions[scan_id]
        report_generator = ReportGenerator()

        report = report_generator.generate(
            session=session,
            output_format=format
        )

        return {
            "scan_id": scan_id,
            "status": "completed",
            "report": report,
            "format": format
        }

    except Exception as e:
        logger.error(f"Error generating report: {str(e)}")
        return {
            "error": str(e),
            "status": "failed"
        }


@mcp.tool()
async def scan_by_prompt(prompt: str) -> Dict[str, Any]:
    """
    Natural language interface for scanning

    Args:
        prompt: Natural language description of what to scan
               Examples:
               - "Check if my auth module has log4j vulnerability"
               - "Is my codebase following ARB security guidelines?"
               - "Scan for hardcoded passwords in the payment service"

    Returns:
        Scan results based on interpreted intent

    Example:
        scan_by_prompt("Check log4j vulnerability in ./myproject")
    """
    logger.info(f"Processing prompt: {prompt}")

    try:
        # TODO: Implement LLM-based intent parsing
        # For now, simple keyword matching

        prompt_lower = prompt.lower()

        # Detect scan type
        if any(keyword in prompt_lower for keyword in ["vulnerability", "vuln", "security", "log4j", "hardcoded"]):
            scan_type = "vulnerability"
        elif any(keyword in prompt_lower for keyword in ["arb", "compliance", "guideline", "architecture"]):
            scan_type = "arb_compliance"
        elif any(keyword in prompt_lower for keyword in ["ai-ready", "ai readiness", "copilot"]):
            scan_type = "ai_readiness"
        else:
            return {
                "error": "Could not determine scan type from prompt. Please be more specific.",
                "suggestions": [
                    "For vulnerability scanning, mention 'vulnerability' or specific issues like 'log4j'",
                    "For ARB compliance, mention 'ARB' or 'compliance'",
                    "For AI-readiness, mention 'AI-ready' or 'copilot'"
                ]
            }

        # Extract repository path (simple pattern matching)
        # TODO: Make this more robust with LLM
        repo_path = None
        words = prompt.split()
        for i, word in enumerate(words):
            if word.startswith("/") or word.startswith("./"):
                repo_path = word
                break

        if not repo_path:
            return {
                "error": "Could not detect repository path in prompt. Please provide a path like '/path/to/repo' or './myproject'"
            }

        # Execute appropriate scan
        if scan_type == "vulnerability":
            return await scan_vulnerabilities(repo_path)
        elif scan_type == "arb_compliance":
            return await check_arb_compliance(repo_path)
        else:
            return await scan_ai_readiness(repo_path)

    except Exception as e:
        logger.error(f"Error processing prompt: {str(e)}")
        return {
            "error": str(e),
            "status": "failed"
        }


# Resources (expose data via MCP protocol)

@mcp.resource("scan://sessions")
async def get_active_sessions() -> str:
    """Get list of all active scan sessions"""
    sessions_info = {
        scan_id: {
            "repo_path": session.repo_path,
            "start_time": session.start_time.isoformat(),
            "scan_types": list(session.results.keys())
        }
        for scan_id, session in active_sessions.items()
    }
    return json.dumps(sessions_info, indent=2)


@mcp.resource("report://latest")
async def get_latest_report() -> str:
    """Get the most recent scan report"""
    if not active_sessions:
        return json.dumps({"message": "No scans have been performed yet"})

    latest_session = list(active_sessions.values())[-1]
    return json.dumps(latest_session.to_dict(), indent=2)


@mcp.resource("graph://knowledge-graph/{scan_id}")
async def get_knowledge_graph(scan_id: str) -> str:
    """Get knowledge graph for a specific scan"""
    if scan_id not in active_sessions:
        return json.dumps({"error": f"Scan not found: {scan_id}"})

    session = active_sessions[scan_id]
    if not session.knowledge_graph:
        return json.dumps({"message": "Knowledge graph not available for this scan"})

    return json.dumps(session.knowledge_graph, indent=2)


# Main entry point
if __name__ == "__main__":
    logger.info("Starting IntelligentScan MCP Server...")
    mcp.run()
