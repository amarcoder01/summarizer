# Email Functionality for Legal Document Assistant

This document explains how to set up and use the email functionality in the Legal Document Assistant application.

## Setup Instructions

### 1. Configure Streamlit Secrets

Create a file named `.streamlit/secrets.toml` using the provided template:

```toml
# API Keys
[api]
GEMINI_API_KEY = "your-gemini-api-key-here"

# Email Configuration
[email]
SMTP_SERVER = "smtp.gmail.com"  # For Gmail
SMTP_PORT = 587
SENDER_EMAIL = "your-email@gmail.com"
SENDER_PASSWORD = "your-app-password"  # For Gmail, use an App Password
```

### 2. Gmail Setup (if using Gmail)

If you're using Gmail, you need to create an App Password:

1. Enable 2-Step Verification in your Google Account
   - Go to your Google Account > Security
   - Enable 2-Step Verification

2. Generate an App Password
   - Go to your Google Account > Security > App Passwords
   - Select "App" as "Mail" and Device as "Other"
   - Enter "Streamlit Legal Assistant" as the name
   - Copy the generated password and use it in your secrets.toml file

### 3. Test the Configuration

1. Start the application
2. Upload a document
3. Generate a summary or risk analysis
4. Go to the sidebar and find the "Email Analysis" section
5. Enter a recipient email and test sending

## Features

The email functionality allows users to:

1. Send document summaries and risk analyses via email
2. Select which content to include (summary, risk analysis)
3. Choose the format (Text or PDF)
4. Send to any valid email address

## Troubleshooting

If you encounter issues:

1. Check that your SMTP settings are correct
2. Verify that your email password is correct (use App Password for Gmail)
3. Ensure your email provider allows SMTP access
4. Check that your account doesn't have security features blocking SMTP

## Security Considerations

- The email credentials are stored in the Streamlit secrets file, which should be kept private
- Do not commit the secrets.toml file to version control
- Consider using a dedicated email account for the application
- Regularly rotate your app passwords for better security

## Support

If you need assistance with the email functionality, please refer to:

- Streamlit documentation on secrets management
- Python's smtplib documentation
- Your email provider's SMTP documentation 