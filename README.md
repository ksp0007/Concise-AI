# Text Summarization Web App

![Text Summarizer Demo](https://github.com/UmeshSamartapu/TEXT_SUMMARIZATION_TOOL/blob/main/text_summarizer_app/assets/Text%20Summarizer%20Frontend.png)

A web application that uses state-of-the-art NLP techniques to generate concise summaries from lengthy articles. Built with FastAPI, Transformers, and Uvicorn.

## Features

- **AI-Powered Summarization**: Uses Facebook's BART-large-CNN model for high-quality abstractive summaries
- **Dual Interface**: 
  - Web UI for interactive use
  - REST API for programmatic access
- **Customizable Output**: Adjust summary length with min/max parameters
- **Performance Metrics**: Tracks processing time for each request
- **Responsive Design**: Works on desktop and mobile devices

## Technology Stack

- **Backend**: FastAPI, Uvicorn
- **NLP**: Hugging Face Transformers, BART model
- **Frontend**: HTML5, CSS3, JavaScript
- **Text Processing**: NLTK, Textwrap

## Directory Structure
```bash
text_summarizer_app/
├── app/
│ ├── init.py
│ ├── main.py
│ ├── schemas.py
│ ├── services/
│ │ ├── init.py
│ │ └── summarizer.py
│ └── static/
│ ├── css/
│ │ └── style.css
│ └── js/
│ └── script.js
├── templates/
│ └── index.html
├── requirements.txt
├── README.md
└── run.py
```

## Installation

### 1. Clone the repository:
```bash
git clone https://github.com/yourusername/text-summarizer-app.git
cd text-summarizer-app
```
### 2.Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3.Install dependencies:
```bash
pip install -r requirements.txt
```

### 4.Download NLTK data:
```bash
python -c "import nltk; nltk.download('punkt')"
```

## Usage
### Running the Application

### Start the development server:
```bash
python run.py
```

### The application will be available at:
```bash
[python run.py](http://localhost:8000)
```

## API Endpoints
- **Web Interface:** GET /
- **Summarize via Web Form:** POST /summarize-web
- **Summarize via API:** POST /summarize


## Deployment
### For production deployment, consider using:
### 1.Docker:
```bash
dockerfile
FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
```
### 2.PM2 (for Node.js process manager):
```bash
pip install gunicorn
gunicorn -k uvicorn.workers.UvicornWorker app.main:app
pm2 start gunicorn --name "text-summarizer" --interpreter python
```


