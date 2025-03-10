Advanced AI-Driven Legal Document Summarization and Risk Assessment

This project leverages cutting-edge AI and NLP techniques to analyze, summarize, and assess risks in legal documents. It assists legal professionals, businesses, and researchers by providing concise, insightful summaries while highlighting potential legal risks.

Table of Contents
Overview
Features
Installation
Usage
Use Cases
Contributing
License
Contact


1.Overview
In today's fast-paced legal landscape, manually reviewing and analyzing legal documents is both time-consuming and prone to human error. Our solution is designed to:

Summarize: Extract key insights from lengthy legal texts in seconds.
Assess Risks: Identify abnormal clauses and potential compliance issues.
Enhance Productivity: Automate the document review process for law firms, corporate legal departments, and small businesses.
This system is scalable, secure, and customizable to suit various legal contexts and document types.


2.Features
AI-Powered Summarization: Automatically distill complex legal texts into clear, concise summaries.
Risk Assessment Engine: Detect and flag potentially risky or non-standard contract clauses.
Multi-Language Support: Process legal documents in several languages.
Customizable Models: Fine-tune AI models to address specific legal domains and regulatory requirements.
User-Friendly Interface: Intuitive dashboard for document upload, review, and management.
Secure Data Handling: Ensures confidentiality and compliance with data protection standards.

3.Installation  Prerequisites
Python: Version 3.9 or higher (verify using python --version).
Git: Ensure Git is installed on your system.
Virtual Environment (Optional but Recommended): Use tools like venv or conda to manage project dependencies.
Google Gemini API Key: You will need an API key from Google AI Studio to use the Gemini features.
Steps

1.Clone the Repository:
git clone https://github.com/amarcoder01/Advanced-AI-Driven-Legal-Document-Summarization-and-Risk-Assessment.git
cd Advanced-AI-Driven-Legal-Document-Summarization-and-Risk-Assessment
2.Set Up a Virtual Environment:
On macOS/Linux
python3 -m venv venv
source venv/bin/activate
On Windows:
python -m venv venv
venv\Scripts\activate

3.Install Dependencies:
pip install -r requirements.txt

4.Configure API Key:
Create or edit the file .streamlit/secrets.toml and add your Google Gemini API key:
```
[api]
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY_HERE"
```

5.Run the Application Locally: Start the Flask backend (if separate) and the Streamlit frontend:
streamlit run app.py

Usage
After installation, launch the application using the command above. Once running, access the web interface (typically at http://localhost:8501 for Streamlit) to upload legal documents and view generated summaries and risk assessments.

Use Cases
Law Firms & Legal Departments: Automate contract review and risk assessment to streamline case preparations.
Corporate Compliance: Quickly analyze agreements to identify non-compliant clauses.
Small Businesses: Empower non-legal professionals to understand complex legal documents.
Legal Research: Accelerate data extraction and document analysis for academic or professional legal studies.

Contributing
Contributions are welcome! To contribute:

Fork the Repository
Create a New Branch:
git checkout -b feature/your-feature-name
Commit Your Changes:
Write clear, descriptive commit messages.
Push to Your Fork and Open a Pull Request
Please see CONTRIBUTING.md for more details.

License
This project is licensed under the MIT License. See the LICENSE file for more information.

Contact
For questions, suggestions, or collaborations, reach out via:

GitHub: amarcoder01
Email: amar01pawar80@gmail.com
LinkedIn: Amar Pawar

# Risk Visualizer View
elif st.session_state.risk_view == "visualizer":
    if st.button("← Back to Dashboard"):
        st.session_state.risk_view = "main"
        st.rerun()
    
    if st.session_state.get("risks"):
        visualize_risks_streamlit(st.session_state.risks)
    else:
        st.info("Please analyze the document first.")



