# Deployment Guide for AI Legal Document Assistant

This guide provides instructions for deploying the AI Legal Document Assistant application on Streamlit Cloud.

## Prerequisites

- A GitHub account
- A Streamlit Cloud account (sign up at https://streamlit.io/cloud)
- A Google AI Studio account with a Gemini API key

## Steps for Deployment

### 1. Prepare Your Repository

1. Make sure your repository is properly pushed to GitHub and contains all required files:
   - app.py
   - requirements.txt
   - .streamlit/secrets.toml (with your API keys)
   - .streamlit/config.toml
   - All other Python modules used by the application

2. Ensure your secrets.toml file is listed in .gitignore to prevent API keys from being exposed:
   ```
   # .gitignore
   .streamlit/secrets.toml
   ```

### 2. Deploy on Streamlit Cloud

1. Log in to Streamlit Cloud (https://streamlit.io/cloud)
2. Click on "New app" button
3. Connect your GitHub repository
4. Fill in the details:
   - Repository: Your GitHub repository URL
   - Branch: main (or master)
   - Main file path: app.py
5. Click "Deploy"

### 3. Configure Secrets on Streamlit Cloud

Since your secrets.toml file should not be in the GitHub repository, you need to add secrets manually:

1. In your deployed app settings on Streamlit Cloud, go to "Secrets"
2. Add the following configuration:
   ```toml
   [api]
   GEMINI_API_KEY = "your_gemini_api_key_here"
   ```
3. Click "Save"

### 4. Advanced Deployment Options

#### Custom Subdomain
You can set a custom subdomain for your app in the app settings.

#### Resource Limits
Adjust compute resources if needed:
- Memory: Default should be sufficient
- CPU: Default should be sufficient

#### Environment Variables
If needed, you can set additional environment variables in the app settings.

## Troubleshooting

### Common Issues

1. **Missing dependencies**: Ensure all required packages are listed in requirements.txt with their versions.

2. **API key issues**: If you see "API key missing" errors, check that your secrets are correctly configured on Streamlit Cloud.

3. **File upload size limits**: The default upload limit is 200MB. If you need larger uploads, contact Streamlit support.

4. **Memory errors**: If your app crashes with memory errors, try optimizing your code or request more resources.

### Getting Help

For further assistance:
- Streamlit documentation: https://docs.streamlit.io/
- Streamlit community forum: https://discuss.streamlit.io/

## Maintenance

After deployment, regularly:
1. Monitor app usage and performance
2. Check for any security updates
3. Update API keys if they expire
4. Update dependencies as needed

## Local Testing Before Deployment

Always test your application locally before deploying:

```bash
streamlit run app.py
```

Make sure all features work as expected with both sample and real documents. 