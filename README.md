# 🤖 AI Data Science Tutor

AI Data Science Tutor is an interactive Streamlit application that provides AI-powered assistance for data science-related queries. It uses Google's **Gemini LLM** to generate structured answers at different levels of expertise and includes additional tools like code debugging and machine learning model evaluation.

---

## ✨ Features

- **🧠 AI-Powered Q&A**: Get detailed responses at **Easy**, **Medium**, and **Advanced** levels.
- **📜 Chat History**: View past interactions and export them as a **PDF**.
- **🐍 Code Debugger**: Analyze Python code for errors and improvements.
- **🤖 ML Model Evaluation**: Upload and assess machine learning models (.pkl files).
- **🔑 User Login**: Different roles (**User, Admin, Business Analyst, Data Scientist**) for personalized responses.
- **⏹ Stop Response**: Instantly halt AI responses when needed.
- **🚀 Secure API Access**: Uses `.env` file for securely storing API keys.

---

## 🛠 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/AI-Data-Science-Tutor.git
   cd AI-Data-Science-Tutor
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up API Key**
   - Create a `.env` file in the root directory.
   - Add your Google Gemini API key:
     ```
     GEMINI_API_KEY=your_api_key_here
     ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

---

## 🚀 Usage

- **Login:** Enter your username and select a role.
- **Ask Questions:** Type a data science-related query.
- **Stop Response:** Click **⏹ Stop Response** to halt AI output.
- **Debug Code:** Paste Python code into the debugger for analysis.
- **Evaluate ML Models:** Upload `.pkl` files to assess machine learning models.
- **Export Chat:** Download your conversation history as a PDF.

---

---

## 📞 Contact

For any questions or suggestions, feel free to reach out!

- GitHub: (https://github.com/Bhaskar-Matta)
- Email: bhaskarmatta77@gmail.com



