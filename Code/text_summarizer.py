import nltk
from transformers import pipeline
from typing import Tuple
import textwrap

class TextSummarizer:
    """
    A text summarization tool that uses NLP to generate concise summaries from lengthy articles.
    """
    
    def __init__(self, model_name: str = "facebook/bart-large-cnn"):
        """
        Initialize the summarizer with a pre-trained model.
        
        Args:
            model_name (str): Name of the pre-trained summarization model.
                             Default is "facebook/bart-large-cnn" which is good for abstractive summarization.
        """
        try:
            self.summarizer = pipeline("summarization", model=model_name)
        except Exception as e:
            raise Exception(f"Failed to load the summarization model: {str(e)}")
        
        # Download required NLTK data for text processing
        try:
            nltk.data.find('tokenizers/punkt')
        except LookupError:
            nltk.download('punkt')
    
    def summarize(self, text: str, max_length: int = 130, min_length: int = 30) -> Tuple[str, str]:
        """
        Generate a summary from the input text.
        
        Args:
            text (str): Input text to summarize
            max_length (int): Maximum length of the summary
            min_length (int): Minimum length of the summary
            
        Returns:
            Tuple[str, str]: Original text (formatted) and generated summary
        """
        if not text.strip():
            raise ValueError("Input text cannot be empty")
        
        # Clean and format the input text
        formatted_original = self._format_text(text)
        
        # Generate summary
        try:
            summary = self.summarizer(
                text,
                max_length=max_length,
                min_length=min_length,
                do_sample=False
            )[0]['summary_text']
        except Exception as e:
            raise Exception(f"Summarization failed: {str(e)}")
        
        return formatted_original, summary
    
    def _format_text(self, text: str, width: int = 80) -> str:
        """
        Format text for better display by wrapping lines and adding separators.
        
        Args:
            text (str): Text to format
            width (int): Maximum line width
            
        Returns:
            str: Formatted text
        """
        # Split into paragraphs
        paragraphs = text.split('\n\n')
        
        # Wrap each paragraph
        wrapped_paragraphs = []
        for para in paragraphs:
            if para.strip():
                wrapped = textwrap.fill(para.strip(), width=width)
                wrapped_paragraphs.append(wrapped)
        
        # Join with double newlines
        formatted_text = "\n\n".join(wrapped_paragraphs)
        
        # Add separators
        separator = "\n" + "=" * width + "\n"
        formatted_text = f"{separator}ORIGINAL TEXT:{separator}{formatted_text}"
        
        return formatted_text
    
    def display_results(self, original: str, summary: str, width: int = 80):
        """
        Display the original text and summary in a readable format.
        
        Args:
            original (str): Formatted original text
            summary (str): Generated summary
            width (int): Maximum line width
        """
        separator = "\n" + "=" * width + "\n"
        
        # Format the summary
        formatted_summary = textwrap.fill(summary, width=width)
        formatted_summary = f"{separator}GENERATED SUMMARY:{separator}{formatted_summary}"
        
        # Print both
        print(original)
        print(formatted_summary)


def get_user_input():
    """
    Get multi-line input from user with a clear termination method.
    """
    print("Text Summarization Tool")
    print("Enter your content below. Press Enter twice to finish input.\n")
    
    lines = []
    empty_line_count = 0
    
    while True:
        line = input()
        if not line.strip():
            empty_line_count += 1
            if empty_line_count >= 2:
                break
        else:
            empty_line_count = 0
        lines.append(line)
    
    return '\n'.join(lines)


def main():
    try:
        # Read input from user
        input_text = get_user_input()
        
        if not input_text.strip():
            print("Error: No input text provided.")
            return
        
        # Initialize summarizer
        summarizer = TextSummarizer()
        
        # Generate and display summary
        original, summary = summarizer.summarize(input_text)
        summarizer.display_results(original, summary)
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()