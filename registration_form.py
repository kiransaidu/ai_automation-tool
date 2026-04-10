from flask import Flask, render_template_string, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'replace-with-a-secure-secret-key'

# Simple HTML template for the registration form
FORM_HTML = '''
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Registration Form</title>
    <style>
        body {font-family: Arial, sans-serif; margin: 2rem;}
        .error {color: red;}
        .success {color: green;}
        form {max-width: 400px;}
        label {display: block; margin-top: 1rem;}
        input {width: 100%; padding: 0.5rem;}
        button {margin-top: 1rem; padding: 0.5rem 1rem;}
    </style>
</head>
<body>
    <h2>Register</h2>
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            {% for category, message in messages %}
                <p class="{{ category }}">{{ message }}</p>
            {% endfor %}
        {% endif %}
    {% endwith %}
    <form method="POST" action="{{ url_for('register') }}">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>

        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required>

        <button type="submit">Register</button>
    </form>
</body>
</html>
'''

@app.route('/', methods=['GET'])
def index():
    return redirect(url_for('register'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')

        # Basic validation (you can expand this as needed)
        if not username or not email or not password:
            flash('All fields are required.', 'error')
            return render_template_string(FORM_HTML)
        if len(password) < 6:
            flash('Password must be at least 6 characters long.', 'error')
            return render_template_string(FORM_HTML)

        # Here you would normally save the user to a database.
        # For this simple example, we just display a success message.
        flash(f'Registration successful! Welcome, {username}.', 'success')
        return redirect(url_for('register'))

    # GET request – show the form
    return render_template_string(FORM_HTML)

if __name__ == '__main__':
    # Run the Flask development server
    app.run(debug=True, host='0.0.0.0', port=5000)
