
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mail import Mail, Message
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Mail config (update with real credentials)
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'you@example.com'
app.config['MAIL_PASSWORD'] = 'password'
app.config['MAIL_USE_TLS'] = True

mail = Mail(app)

@app.route('/')
def home():
    return redirect(url_for('doctor_login'))

@app.route('/doctor/login', methods=['GET', 'POST'])
def doctor_login():
    if request.method == 'POST':
        session['doctor'] = request.form['email']
        return redirect(url_for('dashboard'))
    return render_template('doctor_login.html')

@app.route('/doctor/register', methods=['GET', 'POST'])
def doctor_register():
    if request.method == 'POST':
        return redirect(url_for('doctor_login'))
    return render_template('doctor_register.html')

@app.route('/patient/register', methods=['GET', 'POST'])
def patient_register():
    if request.method == 'POST':
        return redirect(url_for('dashboard'))
    return render_template('patient_register.html')

@app.route('/dashboard')
def dashboard():
    if 'doctor' not in session:
        return redirect(url_for('doctor_login'))
    return render_template('dashboard.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # use PORT from Render or fallback to 5000
    app.run(host='0.0.0.0', port=port)

