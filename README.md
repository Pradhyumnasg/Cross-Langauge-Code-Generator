# 🚀 Cross Language Code Generation

## 🌟 Overview
The **Cross Language Code Generation** is a web application built using **Streamlit** and **Google Generative AI (Gemini 1.5 Pro)**. It allows users to input a task description in English and generates equivalent code in their selected programming language.

## 🎯 Features
✅ Accepts natural language descriptions of coding tasks.  
✅ Supports multiple programming languages including Python, JavaScript, Java, C++, C#, Ruby, Go, PHP, Swift, Kotlin, HTML and SQL.  
✅ Uses **Google Generative AI** to generate accurate and efficient code.  
✅ Displays generated code with syntax highlighting.  
✅ Handles errors gracefully (e.g., missing API key, invalid input).  

## 🛠 Technologies Used
- 🐍 **Python** (Streamlit for UI)
- 🤖 **Google Generative AI API** (Gemini 1.5 Pro)
- 🔐 **dotenv** (for environment variable management)
- 📂 **OS Module** (for handling environment variables)

## 📌 Installation
### 📋 Prerequisites
Ensure you have **Python 3.8+** installed on your system.

### 🔽 Step 1: Clone the Repository
```sh
git clone https://github.com/yourusername/cross-language-code-generation.git
cd cross-language-code-generation
```

### 🏗 Step 2: Create a Virtual Environment (Optional but Recommended)
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 📦 Step 3: Install Dependencies
```sh
pip install -r requirements.txt
```

### 🔑 Step 4: Set Up API Key
Create a `.env` file in the project directory and add your **Google API Key**:
```env
GOOGLE_API_KEY=your_google_api_key_here
```

### 🚀 Step 5: Run the Application
```sh
streamlit run app.py
```

## 🎮 Usage
1. ✍️ Enter the task description in English.
2. 🖥 Select the target programming language from the dropdown.
3. ⚡ Click **Generate Code**.
4. 📜 View the generated code and copy it as needed.

## 📂 Project Structure
```
cross-language-code-generation/
│── app.py               # Main Streamlit application
│── requirements.txt     # Python dependencies
│── .env                 # Environment variables (API Key)
│── README.md            # Project documentation
```

## 🛡 Error Handling
- ❌ **Missing API Key**: Displays an error message if the `GOOGLE_API_KEY` is not set.
- ⚠️ **Invalid Input**: Warns the user if the task description is empty.
- 🔄 **API Failure**: Catches and displays any API errors during the code generation process.

## 🚀 Future Enhancements
- 🏆 Add support for more programming languages.
- ⚙️ Allow users to customize code generation preferences.
- 🗄 Implement a database to store generated code snippets.
- 🎨 Improve UI/UX with enhanced styling.

## 📜 License
This project is licensed under the **MIT License**.

## 🙌 Acknowledgments
- 🤖 **Google Generative AI (Gemini 1.5 Pro)** for powering the code generation.
- 🏗 **Streamlit** for making web development easy with Python.

---
Feel free to contribute, raise issues, or suggest improvements! 🚀

