import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("GOOGLE_API_KEY not found. Please set it in the environment.")
    st.stop()

genai.configure(api_key=api_key)

def generate_code(english_text, language):
    """Generates code in a specified language from English text."""
    model = genai.GenerativeModel("gemini-1.5-pro")

    prompt = f"""
    Generate code in {language} that accomplishes the task described in the following English text:

    {english_text}

    Provide only the code, without any additional explanations, comments, or language identifiers.
    """

    try:
        response = model.generate_content(prompt)
        code = response.text.strip()
        # Remove language identifier and code block markers
        code = code.replace(f"```{language.lower()}", "").replace("```", "").strip()
        return code
    except Exception as e:
        return f"Error generating code: {e}"

st.title("Cross Language Code Generator")

english_text = st.text_area("Enter the task description in English:")
language = st.selectbox("Select the target programming language:",
                        ["Python", "JavaScript", "Java", "C++", "C#", "Ruby", "Go", "PHP", "Swift", "Kotlin", "HTML", "CSS", "SQL"])

if st.button("Generate Code"):
    if english_text:
        with st.spinner("Generating code..."):
            generated_code = generate_code(english_text, language)

        if "Error" in generated_code:
            st.error(generated_code)
        else:
            st.subheader(f"Generated {language} Code:")
            st.code(generated_code, language=language.lower() if language not in ["C++", "C#"] else language.replace("#","sharp").lower())
    else:
        st.warning("Please enter a task description.")