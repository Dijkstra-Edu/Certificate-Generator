# 🎓 Certificate-Generator

**Certificate-Generator** is a FastAPI-powered backend application that generates personalized certificates in based on user data. It includes API endpoints to retrieve GitHub data and download certificates — perfect for automating certificates in bulk for events, competitions etc.

---

## 💻 Getting Started

To run this project locally, ensure you have **Python 3.10+** installed.

Clone the repository and navigate into the project folder:

```bash
git clone https://github.com/your-username/Certificate-Generator.git
cd Certificate-Generator
```

Create and activate a virtual environment:

```bash
python -m venv venv
.\venv\Scripts\activate        # On Windows
# OR
source venv/bin/activate       # On macOS/Linux
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing or incomplete, install dependencies manually:

```bash
pip install fastapi uvicorn httpx python-dotenv
```

Then, start the FastAPI server:

```bash
python -m uvicorn app.main:app --reload
```

You should see:

```
Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

---

## 🧪 Using the API

Once the server is running, you can access:

- **API Root:** `http://127.0.0.1:8000`
- **Interactive Docs (Swagger UI):**  
  👉 `http://127.0.0.1:8000/docs`  
  Use this to test endpoints for:
  - Downloading a certificate
  - Fetching GitHub data
  - Custom parameter search

... to be done 

---

## 📜 License

This project is released under the repository’s license.

---
