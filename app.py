import random
import os
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    data = request.get_json()
    user_guess = data.get('guess')

    if not isinstance(user_guess, int):
        return jsonify({'result': 'Invalid guess! Please enter a number.'}), 400

    # Get the target number from environment or generate a new one
    target = int(os.environ.get('TARGET_NUMBER', random.randint(1, 100)))

    if user_guess < target:
        result = 'Too low!'
    elif user_guess > target:
        result = 'Too high!'
    else:
        result = 'Correct! You won!'

    return jsonify({'result': result})

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
import random
import os
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    data = request.get_json()
    user_guess = data.get('guess')

    if not isinstance(user_guess, int):
        return jsonify({'result': 'Invalid guess! Please enter a number.'}), 400

    # Get the target number from environment or generate a new one
    target = int(os.environ.get('TARGET_NUMBER', random.randint(1, 100)))

    if user_guess < target:
        result = 'Too low!'
    elif user_guess > target:
        result = 'Too high!'
    else:
        result = 'Correct! You won!'

    return jsonify({'result': result})

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
