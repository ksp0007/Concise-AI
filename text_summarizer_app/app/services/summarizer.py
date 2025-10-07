import nltk
from transformers import pipeline
from typing import Tuple
import textwrap

class TextSummarizer:
    """A text summarization tool that uses NLP to generate concise summaries."""
    
    def __init__(self, model_name: str = "facebook/bart-large-cnn"):
        try:
            self.summarizer = pipeline("summarization", model=model_name)
        except Exception as e:
            raise Exception(f"Failed to load summarization model: {str(e)}")
        
        try:
            nltk.data.find('tokenizers/punkt')
        except LookupError:
            nltk.download('punkt')
    
    def summarize(self, text: str, max_length: int = 130, min_length: int = 30) -> dict:
        if not text.strip():
            raise ValueError("Input text cannot be empty")
        
        formatted_original = self._format_text(text)
        
        try:
            summary = self.summarizer(
                text,
                max_length=max_length,
                min_length=min_length,
                do_sample=False
            )[0]['summary_text']
        except Exception as e:
            raise Exception(f"Summarization failed: {str(e)}")
        
        return {
            "original_text": text,
            "formatted_original": formatted_original,
            "summary": summary
        }
    
    def _format_text(self, text: str, width: int = 80) -> str:
        paragraphs = text.split('\n\n')
        wrapped_paragraphs = []
        
        for para in paragraphs:
            if para.strip():
                wrapped = textwrap.fill(para.strip(), width=width)
                wrapped_paragraphs.append(wrapped)
        
        formatted_text = "\n\n".join(wrapped_paragraphs)
        separator = "\n" + "=" * width + "\n"
        return f"{separator}ORIGINAL TEXT:{separator}{formatted_text}"