from fastapi import FastAPI, UploadFile, File, Request
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from starlette.responses import JSONResponse
from data_ingestion.ingestion_pipeline import DataIngestion  # you already have this
from agent.workflow import GraphBuilder  # this should be your graph stream handler
from data_models.models import *

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # set specific origins in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload")
async def upload_files(files: List[UploadFile] = File(...)):
    try:
        ingestion = DataIngestion()
        ingestion.run_pipeline(files)
        return {"message": "Files successfully processed and stored."}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
    

@app.post("/query")
async def query_chatbot(request: QuestionRequest):
    try:
        graph_service = GraphBuilder()
        graph_service.build()
        graph = graph_service.get_graph()
        
        # Assuming request is a pydantic object like: {"question": "your text"}
        messages={"messages": [request.question]}
        
        result = graph.invoke(messages)
        
        # If result is dict with messages:
        if isinstance(result, dict) and "messages" in result:
            final_output = result["messages"][-1].content  # Last AI response
        else:
            final_output = str(result)
        
        return {"answer": final_output}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})