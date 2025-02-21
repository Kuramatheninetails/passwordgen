from flask import Flask, render_template, request, jsonify
import random
import string

app = Flask(__name__)

def generate_password(length=12):
    """Generate a strong password with uppercase, lowercase, digits, and special characters."""
    if length < 4:
        return "Error: Password length must be at least 4."

    uppercase = random.choice(string.ascii_uppercase)
    lowercase = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    special = random.choice(string.punctuation)

    all_chars = string.ascii_letters + string.digits + string.punctuation
    remaining_chars = ''.join(random.choice(all_chars) for _ in range(length - 4))

    password = list(uppercase + lowercase + digit + special + remaining_chars)
    random.shuffle(password)

    return ''.join(password)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    try:
        length = int(request.form['length'])
        password = generate_password(length)
        return jsonify({'password': password})
    except ValueError:
        return jsonify({'error': 'Invalid input. Enter a valid number.'})

if __name__ == '__main__':
    app.run(debug=True)
