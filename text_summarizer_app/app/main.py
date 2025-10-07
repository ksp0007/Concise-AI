from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import time
from typing import Optional

from .services.summarizer import TextSummarizer
from .schemas import SummaryRequest, SummaryResponse

app = FastAPI(title="Text Summarization API")

# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/summarize", response_model=SummaryResponse)
async def create_summary(request_data: SummaryRequest):
    start_time = time.time()
    
    summarizer = TextSummarizer()
    result = summarizer.summarize(
        text=request_data.text,
        max_length=request_data.max_length,
        min_length=request_data.min_length
    )
    
    processing_time = time.time() - start_time
    
    return {
        **result,
        "processing_time": processing_time
    }

@app.post("/summarize-web", response_class=HTMLResponse)
async def summarize_via_web(
    request: Request,
    text: str = Form(...),
    max_length: int = Form(130),
    min_length: int = Form(30)
):
    start_time = time.time()
    
    summarizer = TextSummarizer()
    result = summarizer.summarize(
        text=text,
        max_length=max_length,
        min_length=min_length
    )
    
    processing_time = time.time() - start_time
    
    return templates.TemplateResponse("index.html", {
        "request": request,
        "original_text": text,
        "summary": result["summary"],
        "processing_time": f"{processing_time:.2f} seconds",
        "show_results": True
    })