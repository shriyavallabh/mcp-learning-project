# Official MCP Sources and References

## 🔗 Primary Sources

### Official Documentation
- **Main Documentation**: https://modelcontextprotocol.io
- **API Documentation**: https://docs.anthropic.com/en/docs/mcp
- **Protocol Specification**: https://spec.modelcontextprotocol.io

### GitHub Repositories
- **MCP Main Repository**: https://github.com/modelcontextprotocol
- **Python SDK**: https://github.com/modelcontextprotocol/python-sdk
- **TypeScript SDK**: https://github.com/modelcontextprotocol/typescript-sdk
- **Example Servers**: https://github.com/modelcontextprotocol/servers

### Package Repositories
- **PyPI (Python)**: https://pypi.org/project/mcp/
- **NPM (TypeScript)**: https://www.npmjs.com/package/@modelcontextprotocol/sdk
- **FastMCP 2.0**: https://pypi.org/project/fastmcp/

## 📅 Version Information

### Current Versions (as of December 2024)
- **MCP Protocol Version**: 0.1.0
- **JSON-RPC Version**: 2.0
- **Python SDK**: Latest (includes FastMCP 1.0)
- **FastMCP 2.0**: Separate enhanced version

### Important Dates
- **MCP Open-Sourced**: November 2024
- **SSE Transport Deprecated**: 2024-11-05
- **OAuth 2.1 Mandated**: 2024 (for remote HTTP servers)

## 🛠️ Implementation Libraries

### Python
```bash
# Official SDK (recommended)
pip install mcp

# FastMCP 2.0 (enhanced features)
pip install fastmcp
```

### TypeScript/JavaScript
```bash
npm install @modelcontextprotocol/sdk
```

## 📖 Specifications

### JSON-RPC 2.0
- **Official Spec**: https://www.jsonrpc.org/specification
- **Used by MCP**: Version 2.0 exactly

### Transport Protocols
1. **stdio**: Local subprocess communication
2. **Streamable HTTP**: Remote communication with optional SSE

### OAuth 2.1 (for security)
- **Required for**: Remote HTTP servers
- **Specification**: https://oauth.net/2.1/

## 🏢 Enterprise Resources

### Pre-built MCP Servers
Official servers available for:
- Google Drive
- Slack
- GitHub
- Git
- PostgreSQL
- Puppeteer

### Early Adopters
- Block
- Apollo
- Zed
- Replit
- Codeium
- Sourcegraph

## 📚 Learning Resources

### Official Tutorials
- **Getting Started**: https://modelcontextprotocol.io/docs/getting-started
- **Building Servers**: https://modelcontextprotocol.io/docs/build-server
- **Building Clients**: https://modelcontextprotocol.io/docs/build-client

### Community Resources
- **Discord**: MCP Community Discord
- **GitHub Discussions**: https://github.com/modelcontextprotocol/discussions

## ⚖️ License and Legal

- **License**: Open Source (check specific repository for details)
- **Maintained by**: Anthropic, PBC
- **Community Contributions**: Welcome via GitHub

## 🔍 Verification Tips

When fact-checking MCP information:
1. Always check the official modelcontextprotocol.io first
2. Verify version compatibility in GitHub releases
3. Check protocol specification for technical details
4. Review GitHub issues for known limitations
5. Consult official SDKs for implementation patterns

## ⚠️ Common Misconceptions to Avoid

1. **MCP ≠ LLM**: MCP servers don't contain LLMs
2. **FastMCP versions**: 1.0 is in SDK, 2.0 is separate
3. **SSE transport**: Deprecated as standalone (2024-11-05)
4. **Deterministic**: MCP servers are deterministic, not probabilistic
5. **Security**: Production requires OAuth 2.1 for remote servers

---

**Last Updated**: December 2024
**Verification Status**: All sources active and verified