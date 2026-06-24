# 🧠 Query AI

Query AI is an AI-powered Document, Text, Code & Resume Intelligence Platform designed to help you extract insights, answer questions, analyze content, and generate summaries across various data types. Built with cutting-edge technologies, Query AI provides an intuitive interface to interact with your documents, text snippets, codebases, and resumes using natural language queries.

---

## 🚀 Features

### Document Intelligence
- 📄 Upload PDF documents  
- 🔍 Extract and process text from PDFs  
- ✂️ Smart text chunking for efficient retrieval  
- 🧠 Generate semantic embeddings for accurate search  
- 🔎 Semantic search using vector similarity  
- 🤖 AI-powered question answering and summarization  
- 📚 View source chunks used for answers  
- 💬 Session-based chat history  

### Text Intelligence
Perform advanced operations on plain text with these actions:  
- Summarize text  
- Extract key points  
- Generate questions and answers  
- Translate text  
- Paraphrase content  
- Sentiment analysis  
- Text classification  
- Named entity recognition (NER)  

### Code Intelligence
Analyze and interact with code snippets and repositories:  
- Explain code functionality  
- Generate code documentation  
- Detect bugs and suggest fixes  
- Refactor code snippets  
- Translate code between languages  
- Generate test cases  
- Summarize code changes  
- Answer code-related questions  

### Resume Intelligence
Tailored features for resume analysis and enhancement:  
- Extract key skills and experience  
- Summarize career highlights  
- Suggest improvements and optimizations  
- Match resumes to job descriptions  
- Generate interview questions  
- Analyze gaps and inconsistencies  
- Score resume relevance  
- Provide tailored career advice  

---

## 🛠️ Tech Stack

- **Language:** Python 3.12  
- **Frontend:** Streamlit  
- **Large Language Model:** Groq Llama 3.3 70B  
- **Embeddings:** Sentence Transformers (all-MiniLM-L6-v2)  
- **Vector Database:** ChromaDB  
- **PDF Processing:** PyMuPDF  
- **Text Chunking:** LangChain RecursiveCharacterTextSplitter  
- **Environment Management:** python-dotenv  

---

## 📂 Project Structure

```
ai-knowledge-assistant/
│
├── app/
│   ├── api/
│   ├── models/
│   ├── services/
│   │   ├── pdf_service.py
│   │   ├── chunk_service.py
│   │   ├── embedding_service.py
│   │   ├── chroma_service.py
│   │   └── llm_service.py
│   └── main.py
│
├── data/
│   ├── uploads/
│   └── chroma_db/
│
├── tests/
├── streamlit_app.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

1. **Clone the repository**

```bash
git clone <your-github-repo-url>
cd ai-knowledge-assistant
```

2. **Create a virtual environment**

```bash
python -m venv .venv
```

3. **Activate the environment**

- macOS / Linux

```bash
source .venv/bin/activate
```

- Windows

```bash
.venv\Scripts\activate
```

4. **Install dependencies**

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root with the following content:

```
GROQ_API_KEY=your_groq_api_key
```

Replace `your_groq_api_key` with your actual API key.

---

## ▶️ Running the Application

Start the Streamlit app with:

```bash
streamlit run streamlit_app.py
```

Then open your browser and navigate to:

```
http://localhost:8501
```

---

## 🧠 How It Works

1. Upload a document (PDF), text snippet, code, or resume.  
2. Extract and preprocess content (text extraction, chunking, embedding).  
3. Store embeddings in ChromaDB for efficient semantic search.  
4. Enter your natural language query or select an action.  
5. Retrieve relevant chunks or data based on semantic similarity.  
6. Use Groq LLM to generate accurate, context-aware responses.  
7. Display answers, summaries, or analyses along with source context.  

---

## 💡 Use Cases

- Quickly summarize lengthy reports, contracts, or research papers.  
- Extract actionable insights from meeting notes or emails.  
- Analyze and document codebases or snippets.  
- Improve resumes and prepare for interviews.  
- Automate question answering for internal knowledge bases.  
- Translate and paraphrase content for multilingual teams.  
- Detect bugs and improve code quality with AI suggestions.  
- Perform sentiment analysis and text classification on customer feedback.  

---

## 📈 Future Roadmap

- Enhanced multi-document and multi-format support  
- User authentication and personalized sessions  
- Citation-aware and explainable AI answers  
- REST API endpoints with FastAPI  
- Cloud deployment and containerization (Docker, Kubernetes)  
- Integration with external data sources and APIs  
- Real-time collaboration features  
- Advanced code intelligence with language-specific parsers  

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

Prasad Patil

Built as a portfolio project to demonstrate practical skills in Python, Generative AI, Retrieval-Augmented Generation (RAG), vector databases, and LLM integration.