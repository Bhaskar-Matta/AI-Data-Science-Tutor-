# AI-Data-Science-Tutor-# 🤖 AI Data Science Tutor

Welcome to **AI Data Science Tutor**! 🧠 This is an interactive AI-powered assistant built with **Streamlit** and **Google Gemini LLM** to help users with data science queries, machine learning insights, and code debugging.

## 🚀 Features

✅ **AI-Powered Q&A:** Ask any data science question and get responses at three levels:

- **Easy** 🟢 - Beginner-friendly explanation.
- **Medium** 🟡 - Detailed answer with some technical depth.
- **Advanced** 🔴 - In-depth explanation with precise technical details.

✅ **Code Debugging** 🐍 - Paste your Python code and get debugging insights instantly.

✅ **ML Model Evaluation** 🤖 - Upload your machine learning model (Pickle file) and get AI-powered analysis.

✅ **Chat History** 📜 - Stores previous conversations for future reference.

✅ **PDF Export** 📥 - Download the chat history as a PDF file.

✅ **Secure Login System** 🔑 - Users must log in with a role before accessing features.

## 🏗️ Tech Stack

- **Streamlit** 🎨 - UI framework for building the web app.
- **Google Gemini LLM** 🤖 - AI model for answering queries.
- **LangChain** 🔗 - Manages AI interactions and chat history.
- **SQLite** 🗄️ - Stores user data and interactions.
- **Plotly** 📊 - Data visualization support.
- **FPDF** 📄 - Export chat history as PDFs.

## 🔧 Installation

1️⃣ **Clone the Repository**

```bash
git clone https://github.com/your-username/ai-data-science-tutor.git
cd ai-data-science-tutor
```

2️⃣ **Create a Virtual Environment** (Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3️⃣ **Install Dependencies**

```bash
pip install -r requirements.txt
```

4️⃣ **Set Up API Key**
Create a `.env` file and add your **Google GenAI API Key**:

```bash
GEMINI_API_KEY=your_api_key_here
```

5️⃣ **Run the App**

```bash
streamlit run app.py
```

---

💡 **Developed with ❤️ by [Your Name]**

