import google.generativeai as genai
import logging
import streamlit as st

# Configure logging
logging.basicConfig(level=logging.INFO)

# Fetch API key securely from Streamlit secrets
try:
    api_key = st.secrets["api"]["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
except Exception as e:
    logging.error("Gemini API key is missing or incorrect. Please check your secrets file.")

def summarize_document(text):
    """Summarizes the given text using Google Gemini API in a concise, bullet-point format."""
    if not text:
        return "No text provided for summarization."
    
    prompt = (
        "Please provide a concise, well-organized summary of the following document. "
        "Present the summary as a list of bullet points (no more than 5 bullets) highlighting the key points.\n\n"
        f"{text}"
    )
    
    try:
        model = genai.GenerativeModel("gemini-1.5-flash-latest")
        response = model.generate_content(prompt)
        if response and hasattr(response, "text"):
            return response.text.strip()
        else:
            return "No summary generated."
    
    except Exception as e:
        logging.error(f"Summarization error: {str(e)}")
        return f"Error during summarization: {str(e)}"

def identify_risks(text):
    """Identifies risks in the document using Google Gemini API."""
    if not text:
        return "No text provided."

    try:
        model = genai.GenerativeModel("gemini-1.5-flash-latest")
        prompt = f"Analyze the following legal document and identify potential risks in a clear and organized manner:\n\n{text}"
        response = model.generate_content(prompt)
        return response.text.strip() if response and hasattr(response, "text") else "No risks identified."
    except Exception as e:
        logging.error(f"Risk analysis error: {str(e)}")
        return f"Error occurred during risk analysis: {str(e)}"

def chat_with_document(text, query):
    """Allows users to chat with the document using Google Gemini API with a futuristic, interactive style."""
    if not text or not query:
        return "No text or query provided."

    try:
        model = genai.GenerativeModel("gemini-1.5-flash-latest")
        prompt = (
            "You are a futuristic, dynamic, interactive AI legal assistant. "
            "Your tone is friendly, engaging, and highly informative. Use clear language, "
            "bullet points when appropriate, and even suggest follow-up questions to the user. \n\n"
            "Based on the document provided below and the user's query, provide a thoughtful, conversational answer.\n\n"
            "Document (first 3000 characters):\n"
            f"{text[:3000]}...\n\n"
            "User Question:\n"
            f"{query}\n\n"
            "Answer in a dynamic, engaging style:"
        )
        
        response = model.generate_content(prompt)
        
        if response and hasattr(response, "text"):
            return response.text.strip()
        else:
            return "No response generated."
    
    except Exception as e:
        logging.error(f"Chat error: {str(e)}")
        return f"Error during chat interaction: {str(e)}"
