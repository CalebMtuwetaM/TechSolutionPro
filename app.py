import os
import logging
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
import re

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Create Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key")

# Configure Flask-Mail
app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
app.config['MAIL_PORT'] = int(os.environ.get('MAIL_PORT', 587))
app.config['MAIL_USE_TLS'] = os.environ.get('MAIL_USE_TLS', 'True').lower() in ['true', 'yes', '1']
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME', '')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD', '')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_DEFAULT_SENDER', '')
app.config['MAIL_RECIPIENT'] = os.environ.get('MAIL_RECIPIENT', 'info@ourcompany.com')

# Initialize Flask-Mail
mail = Mail(app)

# Email validation regex pattern
EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# Routes
@app.route('/')
def index():
    return render_template('index.html', active='home')

@app.route('/about')
def about():
    return render_template('about.html', active='about')

@app.route('/services')
def services():
    return render_template('services.html', active='services')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        
        # Validate form inputs
        errors = []
        if not name or len(name.strip()) < 2:
            errors.append('Please enter a valid name (at least 2 characters)')
        
        if not email or not re.match(EMAIL_REGEX, email):
            errors.append('Please enter a valid email address')
        
        if not subject or len(subject.strip()) < 3:
            errors.append('Please enter a subject (at least 3 characters)')
        
        if not message or len(message.strip()) < 10:
            errors.append('Please enter a message (at least 10 characters)')
        
        if errors:
            for error in errors:
                flash(error, 'danger')
            return render_template('contact.html', 
                                  active='contact',
                                  form_data={
                                      'name': name,
                                      'email': email,
                                      'subject': subject,
                                      'message': message
                                  })
        
        # Send email
        try:
            msg = Message(
                subject=f"Contact Form: {subject}",
                recipients=[app.config['MAIL_RECIPIENT']],
                body=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}",
                sender=app.config['MAIL_DEFAULT_SENDER'] or email
            )
            mail.send(msg)
            flash('Your message has been sent successfully!', 'success')
            return redirect(url_for('success'))
        except Exception as e:
            app.logger.error(f"Error sending email: {str(e)}")
            flash('There was a problem sending your message. Please try again later.', 'danger')
            return redirect(url_for('error'))
    
    return render_template('contact.html', active='contact', form_data={})

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/error')
def error():
    return render_template('error.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', error_code=404, error_message="Page not found"), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('error.html', error_code=500, error_message="Internal server error"), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
