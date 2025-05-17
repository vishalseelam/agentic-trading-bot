# Agentic Trading Bot

The Agentic Trading Bot is an AI-powered conversational system that combines document retrieval capabilities with real-time financial data integration. It uses Large Language Models (LLMs) and a graph-based agent architecture to provide intelligent responses to stock market queries.

## Features

- **Document Processing**: Upload and process financial PDFs and DOCXs
- **Knowledge Base Creation**: Automatically converts documents into a searchable vector database
- **Financial Data Integration**: Live data from Polygon API for real-time stock information
- **Agentic Architecture**: LangGraph-powered conversational workflow that can use tools
- **Web Search Capability**: Integration with Tavily for retrieving up-to-date market information
- **User-Friendly Interface**: Streamlit UI for easy interaction and document uploading
- **API Access**: FastAPI backend for programmatic access

## Architecture

The system uses a modular architecture:

1. **Data Ingestion Layer**: Processes uploaded documents and stores them in a vector database
2. **Agent Workflow Layer**: Manages the conversation flow and tool execution
3. **Tool Integration Layer**: Connects to external data sources (Polygon, Tavily, etc.)
4. **Model Layer**: Handles embeddings and LLM integration
5. **API Layer**: Provides endpoints for file upload and queries
6. **UI Layer**: Streamlit interface for user interaction

## Technologies Used

- **LangChain & LangGraph**: For LLM orchestration and agentic workflows
- **Groq**: High-performance LLM inference
- **Pinecone**: Vector database for document storage and retrieval
- **FastAPI**: Backend API framework
- **Streamlit**: User interface
- **Polygon API**: Financial data integration
- **Google Embeddings**: Document embedding for retrieval

## Installation & Setup

### Prerequisites

- Python 3.10+
- Conda (recommended)

### Environment Setup

```bash
# Create a conda environment
conda create -p env python=3.10 -y

# Activate the environment 
# For CMD:
conda activate <env_path>
# For Git Bash:
source activate ./env

# Install dependencies
pip install -r requirements.txt
```

### Required API Keys

Create a `.env` file in the root directory with these API keys:

```
POLYGON_API_KEY=your_polygon_api_key
GOOGLE_API_KEY=your_google_api_key
TAVILY_API_KEY=your_tavily_api_key
GROQ_API_KEY=your_groq_api_key
PINECONE_API_KEY=your_pinecone_api_key
```

## Usage

### Running the FastAPI Backend

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### Running the Streamlit UI

```bash
streamlit run streamlit_ui.py
```

### Using the Application

1. Navigate to the Streamlit UI
2. Upload financial documents (PDFs or DOCXs) in the sidebar
3. Click "Upload and Ingest" to process the documents
4. Ask questions about stocks, market trends, or information from your documents
5. The bot will provide responses based on document knowledge and live data

## API Endpoints

- `POST /upload`: Upload and process documents
  - Accepts multiple PDF/DOCX files
- `POST /query`: Send queries to the chatbot
  - Request body: `{"question": "your question here"}`
  - Returns: `{"answer": "bot response here"}`

## License

[Include your license information here]

## Contributing

[Include contribution guidelines here]
