# TechSolutions Website

A professional business website for a tech solutions company built with Flask, featuring responsive design and email contact functionality.

## Features

- Professional, responsive design
- Multiple page sections (Home, About, Services, Contact)
- Contact form with email integration
- Mobile-friendly layout

## Deployment on Vercel

### Prerequisites

- A GitHub account
- A Vercel account (you can sign up at [vercel.com](https://vercel.com) using your GitHub account)
- Email service credentials (for the contact form functionality)

### Deployment Steps

1. **Push to GitHub**

   First, create a new repository on GitHub and push your code:

   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/yourusername/techsolutions-website.git
   git push -u origin main
   ```

2. **Set Up Vercel**

   - Go to [vercel.com](https://vercel.com) and sign in with your GitHub account
   - Click "New Project"
   - Import your GitHub repository
   - Vercel will automatically detect that it's a Flask application

3. **Configure Environment Variables**

   Add the following environment variables in the Vercel project settings:

   - `SESSION_SECRET`: A secure random string for Flask sessions
   - `MAIL_SERVER`: Your email SMTP server (e.g., smtp.gmail.com)
   - `MAIL_PORT`: SMTP port (typically 587 for TLS)
   - `MAIL_USE_TLS`: Set to "True" to use TLS
   - `MAIL_USERNAME`: Your email address
   - `MAIL_PASSWORD`: Your email password or app password
   - `MAIL_DEFAULT_SENDER`: Email address to send from
   - `MAIL_RECIPIENT`: Email address to receive messages

4. **Deploy**

   - Click "Deploy"
   - Vercel will build and deploy your application
   - Once deployed, you can access your website at the provided Vercel URL

5. **Custom Domain (Optional)**

   - In your Vercel project settings, go to "Domains"
   - Add your custom domain and follow the instructions to set up DNS

## Local Development

To run this project locally:

1. Install dependencies:
   ```
   pip install flask flask-mail email-validator gunicorn
   ```

2. Set environment variables or create a `.env` file

3. Run the application:
   ```
   python app.py
   ```

4. Open `http://localhost:5000` in your browser

## File Structure

- `app.py`: Main Flask application
- `index.py`: Entry point for Vercel
- `vercel.json`: Vercel configuration
- `templates/`: HTML templates
- `static/`: CSS, JavaScript, and images
- `requirements-vercel.txt`: Project dependencies (rename to requirements.txt when deploying)