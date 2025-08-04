# Intro to MCP (Model Context Protocol)

A simple introduction project demonstrating how to build and interact with MCP clients and servers using Claude AI. This project showcases the fundamentals of MCP architecture, including document management, tool calling, and prompt templates.

## What This Project Does

This project implements a CLI-based chat application that demonstrates:

- **MCP Server**: A document management server that provides tools and resources for handling documents
- **MCP Client**: A client that connects to MCP servers and facilitates communication with Claude AI
- **Interactive CLI**: A rich terminal interface with auto-completion, command suggestions, and document references
- **Document Management**: CRUD operations on documents with formatting and summarization capabilities
- **Tool Integration**: Seamless integration between Claude AI and MCP tools

### Key Features

- 📄 **Document Management**: Read, edit, and manage documents through MCP resources
- 🔧 **Tool Calling**: Execute MCP tools directly from Claude AI conversations
- 💬 **Interactive Chat**: Chat with Claude AI using document context and MCP capabilities
- 🎯 **Command System**: Use `/format` and `/summarize` commands for document operations
- 📝 **Resource References**: Reference documents using `@document.ext` syntax

## Project Structure

```
├── core/                   # Core application modules
│   ├── chat.py            # Base chat functionality
│   ├── claude.py          # Claude AI integration
│   ├── cli_chat.py        # CLI-specific chat implementation
│   ├── cli.py             # Rich terminal interface
│   └── tools.py           # MCP tool management
├── main.py                # Application entry point
├── mcp_client.py          # MCP client implementation
├── mcp_server.py          # MCP server with document tools
└── pyproject.toml         # Project dependencies
```

## Setup

### Prerequisites

- Python 3.10+
- [uv](https://docs.astral.sh/uv/) package manager
- Anthropic API key

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Intro-To-MCP
   ```

2. **Install dependencies**
   ```bash
   uv sync
   ```

3. **Configure environment**
   Create a `.env` file with your configuration:
   ```env
   ANTHROPIC_API_KEY=your_anthropic_api_key_here
   CLAUDE_MODEL=claude-3-5-sonnet-20241022
   USE_UV=1
   ```

## Usage

### Starting the Application

```bash
uv run main.py
```

This will start the interactive CLI with the MCP server running in the background.

### Basic Commands

#### Document References
Reference documents in your chat using the `@` syntax:
```
> What does @report.pdf say about the condenser tower?
```

#### MCP Commands
Use slash commands to execute MCP prompts:
```
> /format report.pdf        # Format document as Markdown
> /summarize plan.md        # Summarize document content
```

#### Available Documents
The demo includes these sample documents:
- `deposition.md` - Legal deposition testimony
- `report.pdf` - Technical condenser tower report
- `financial.docx` - Project budget and expenditures
- `outlook.pdf` - System performance projections
- `plan.md` - Project implementation plan
- `spec.txt` - Technical equipment specifications

### Example Interactions

```bash
# Chat with document context
> Can you analyze the budget in @financial.docx?

# Format a document
> /format plan.md

# Ask questions about multiple documents
> Compare the timeline in @plan.md with the budget in @financial.docx
```

## How MCP Works in This Project

### Server-Client Architecture

1. **MCP Server** ([`mcp_server.py`](mcp_server.py))
   - Hosts document resources and tools
   - Provides `/format` and `/summarize` prompts
   - Manages document storage and retrieval

2. **MCP Client** ([`mcp_client.py`](mcp_client.py))
   - Connects to MCP servers via stdio transport
   - Handles tool calls and resource requests
   - Manages the communication protocol

3. **Chat Integration** ([`core/chat.py`](core/chat.py))
   - Orchestrates Claude AI conversations
   - Executes MCP tool calls automatically
   - Manages conversation context and history

### Tool Flow

1. User inputs query or command
2. [`CliChat`](core/cli_chat.py) processes input and extracts document references
3. [`ToolManager`](core/tools.py) handles tool discovery and execution
4. [`Claude`](core/claude.py) service processes the request with available tools
5. Results are displayed in the terminal

## Learning Objectives

This project demonstrates:

- **MCP Protocol Basics**: Understanding client-server communication
- **Tool Integration**: How AI models can execute external tools
- **Resource Management**: Serving and consuming MCP resources
- **Prompt Templates**: Creating reusable prompt patterns
- **Event-Driven Architecture**: Handling async operations in MCP
