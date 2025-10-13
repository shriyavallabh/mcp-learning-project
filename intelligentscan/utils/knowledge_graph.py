"""
Knowledge Graph Builder for IntelligentScan
Creates visual representations of code analysis results
Uses red/green color coding for low/high confidence areas
"""

import networkx as nx
from typing import Dict, List, Any, Optional
from pathlib import Path
import json


class KnowledgeGraphBuilder:
    """
    Builds knowledge graphs from scan results
    Nodes: Files, Modules, Functions, Classes, Rules, Violations
    Edges: Dependencies, Violations, Relationships
    Colors: Red (issues), Green (clean), Yellow (warnings)
    """

    def __init__(self):
        self.graph = nx.DiGraph()  # Directed graph
        self.node_counter = 0

    def build_from_scan_results(self, scan_results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Build knowledge graph from scan results

        Args:
            scan_results: Results from AI-readiness, vulnerability, or ARB scan

        Returns:
            Graph representation as JSON-serializable dict
        """
        self.graph.clear()
        self.node_counter = 0

        # Detect scan type and build accordingly
        if "ai_readiness_score" in scan_results:
            return self._build_ai_readiness_graph(scan_results)
        elif "vulnerabilities_found" in scan_results:
            return self._build_vulnerability_graph(scan_results)
        elif "violations_found" in scan_results:
            return self._build_arb_graph(scan_results)
        else:
            return {"error": "Unknown scan result type"}

    def _build_ai_readiness_graph(self, scan_results: Dict[str, Any]) -> Dict[str, Any]:
        """Build graph for AI-readiness scan"""

        # Add root node
        root_id = self._add_node(
            label="Codebase",
            node_type="root",
            color="blue",
            metadata={"ai_readiness_score": scan_results.get("ai_readiness_score", 0)}
        )

        # Add file nodes
        low_confidence_areas = scan_results.get("low_confidence_areas", [])

        for area in low_confidence_areas:
            file_path = area.get("file", "unknown")
            confidence = area.get("confidence", 0.5)

            # Determine color based on confidence
            if confidence >= 0.8:
                color = "green"
            elif confidence >= 0.5:
                color = "yellow"
            else:
                color = "red"

            # Add file node
            file_id = self._add_node(
                label=self._shorten_path(file_path),
                node_type="file",
                color=color,
                metadata={
                    "full_path": file_path,
                    "confidence": confidence,
                    "issues": area.get("issues", [])
                }
            )

            # Connect to root
            self._add_edge(root_id, file_id, edge_type="contains", label="")

            # Add issue nodes
            for issue in area.get("issues", []):
                issue_id = self._add_node(
                    label=issue.get("type", "issue"),
                    node_type="issue",
                    color="orange",
                    metadata={"description": issue.get("description", "")}
                )

                self._add_edge(file_id, issue_id, edge_type="has_issue", label=str(issue.get("line", "")))

        return self._graph_to_dict()

    def _build_vulnerability_graph(self, scan_results: Dict[str, Any]) -> Dict[str, Any]:
        """Build graph for vulnerability scan"""

        # Add root node
        root_id = self._add_node(
            label="Vulnerability Scan",
            node_type="root",
            color="blue",
            metadata={"total_vulnerabilities": len(scan_results.get("vulnerabilities_found", []))}
        )

        # Group vulnerabilities by file
        vulnerabilities_by_file = {}
        for vuln in scan_results.get("vulnerabilities_found", []):
            file_path = vuln.get("file", "unknown")
            if file_path not in vulnerabilities_by_file:
                vulnerabilities_by_file[file_path] = []
            vulnerabilities_by_file[file_path].append(vuln)

        # Add file nodes
        for file_path, vulns in vulnerabilities_by_file.items():
            # Determine file color based on severity of vulnerabilities
            max_severity = max((self._severity_to_number(v.get("severity", "low")) for v in vulns), default=0)

            if max_severity >= 3:  # Critical
                color = "red"
            elif max_severity >= 2:  # High
                color = "orange"
            else:
                color = "yellow"

            file_id = self._add_node(
                label=self._shorten_path(file_path),
                node_type="file",
                color=color,
                metadata={
                    "full_path": file_path,
                    "vulnerability_count": len(vulns)
                }
            )

            self._add_edge(root_id, file_id, edge_type="contains", label=f"{len(vulns)} issues")

            # Add vulnerability nodes
            for vuln in vulns:
                vuln_id = self._add_node(
                    label=vuln.get("type", "vulnerability"),
                    node_type="vulnerability",
                    color=self._severity_to_color(vuln.get("severity", "low")),
                    metadata={
                        "description": vuln.get("description", ""),
                        "severity": vuln.get("severity", "low"),
                        "line": vuln.get("line", 0),
                        "remediation": vuln.get("remediation", "")
                    }
                )

                self._add_edge(
                    file_id,
                    vuln_id,
                    edge_type="has_vulnerability",
                    label=f"line {vuln.get('line', '?')}"
                )

        return self._graph_to_dict()

    def _build_arb_graph(self, scan_results: Dict[str, Any]) -> Dict[str, Any]:
        """Build graph for ARB compliance scan"""

        # Add root node
        compliance_score = scan_results.get("compliance_score", 0)
        root_color = "green" if compliance_score >= 80 else "yellow" if compliance_score >= 50 else "red"

        root_id = self._add_node(
            label=f"ARB Compliance {compliance_score}%",
            node_type="root",
            color=root_color,
            metadata={"compliance_score": compliance_score}
        )

        # Group violations by category
        violations_by_category = scan_results.get("violations_by_category", {})

        for category, violations in violations_by_category.items():
            if not violations:
                continue

            # Add category node
            category_id = self._add_node(
                label=category.replace("_", " ").title(),
                node_type="category",
                color="purple",
                metadata={"violation_count": len(violations)}
            )

            self._add_edge(root_id, category_id, edge_type="contains", label=f"{len(violations)} violations")

            # Group by file
            violations_by_file = {}
            for violation in violations:
                file_path = violation.get("file", "unknown")
                if file_path not in violations_by_file:
                    violations_by_file[file_path] = []
                violations_by_file[file_path].append(violation)

            # Add file nodes
            for file_path, file_violations in violations_by_file.items():
                file_id = self._add_node(
                    label=self._shorten_path(file_path),
                    node_type="file",
                    color="red",
                    metadata={
                        "full_path": file_path,
                        "violation_count": len(file_violations)
                    }
                )

                self._add_edge(category_id, file_id, edge_type="violates_in", label="")

                # Add rule violation nodes
                for violation in file_violations:
                    rule_id = self._add_node(
                        label=violation.get("rule_id", "rule"),
                        node_type="rule_violation",
                        color="orange",
                        metadata={
                            "rule_title": violation.get("rule_title", ""),
                            "line": violation.get("line", 0),
                            "description": violation.get("description", "")
                        }
                    )

                    self._add_edge(
                        file_id,
                        rule_id,
                        edge_type="violates_rule",
                        label=f"line {violation.get('line', '?')}"
                    )

        return self._graph_to_dict()

    def _add_node(self, label: str, node_type: str, color: str, metadata: Dict[str, Any]) -> str:
        """Add a node to the graph"""
        node_id = f"node_{self.node_counter}"
        self.node_counter += 1

        self.graph.add_node(
            node_id,
            label=label,
            type=node_type,
            color=color,
            **metadata
        )

        return node_id

    def _add_edge(self, source: str, target: str, edge_type: str, label: str):
        """Add an edge to the graph"""
        self.graph.add_edge(source, target, type=edge_type, label=label)

    def _graph_to_dict(self) -> Dict[str, Any]:
        """Convert NetworkX graph to JSON-serializable dictionary"""

        nodes = []
        for node_id, node_data in self.graph.nodes(data=True):
            nodes.append({
                "id": node_id,
                "label": node_data.get("label", ""),
                "type": node_data.get("type", ""),
                "color": node_data.get("color", "gray"),
                "metadata": {k: v for k, v in node_data.items() if k not in ["label", "type", "color"]}
            })

        edges = []
        for source, target, edge_data in self.graph.edges(data=True):
            edges.append({
                "source": source,
                "target": target,
                "type": edge_data.get("type", ""),
                "label": edge_data.get("label", "")
            })

        # Calculate graph statistics
        stats = {
            "node_count": len(nodes),
            "edge_count": len(edges),
            "red_nodes": len([n for n in nodes if n["color"] == "red"]),
            "green_nodes": len([n for n in nodes if n["color"] == "green"]),
            "yellow_nodes": len([n for n in nodes if n["color"] == "yellow"])
        }

        return {
            "nodes": nodes,
            "edges": edges,
            "statistics": stats,
            "format": "graph_json_v1"
        }

    def _shorten_path(self, path: str, max_length: int = 30) -> str:
        """Shorten file path for display"""
        if len(path) <= max_length:
            return path

        parts = Path(path).parts
        if len(parts) <= 2:
            return path

        # Return first and last parts
        return f"{parts[0]}/.../{parts[-1]}"

    def _severity_to_number(self, severity: str) -> int:
        """Convert severity string to number for comparison"""
        severity_map = {"critical": 3, "high": 2, "medium": 1, "low": 0}
        return severity_map.get(severity.lower(), 0)

    def _severity_to_color(self, severity: str) -> str:
        """Convert severity to color"""
        color_map = {
            "critical": "red",
            "high": "orange",
            "medium": "yellow",
            "low": "lightblue"
        }
        return color_map.get(severity.lower(), "gray")

    def export_to_file(self, output_path: str, format: str = "json"):
        """
        Export graph to file

        Args:
            output_path: Path to save file
            format: Format (json, graphml, gexf)
        """
        if format == "json":
            graph_dict = self._graph_to_dict()
            with open(output_path, 'w') as f:
                json.dump(graph_dict, f, indent=2)

        elif format == "graphml":
            nx.write_graphml(self.graph, output_path)

        elif format == "gexf":
            nx.write_gexf(self.graph, output_path)

        else:
            raise ValueError(f"Unsupported format: {format}")


# Example usage
if __name__ == "__main__":
    # Test knowledge graph builder
    sample_scan_results = {
        "vulnerabilities_found": [
            {
                "type": "hardcoded_secret",
                "description": "Hardcoded API key",
                "severity": "critical",
                "file": "src/auth/login.py",
                "line": 42
            },
            {
                "type": "sql_injection",
                "description": "SQL injection risk",
                "severity": "high",
                "file": "src/db/queries.py",
                "line": 89
            }
        ]
    }

    builder = KnowledgeGraphBuilder()
    graph = builder.build_from_scan_results(sample_scan_results)

    print("=== Knowledge Graph ===")
    print(f"Nodes: {graph['statistics']['node_count']}")
    print(f"Edges: {graph['statistics']['edge_count']}")
    print(f"Red nodes (issues): {graph['statistics']['red_nodes']}")
    print(f"Green nodes (clean): {graph['statistics']['green_nodes']}")
    print(f"\nGraph structure:")
    print(json.dumps(graph, indent=2)[:500] + "...")
