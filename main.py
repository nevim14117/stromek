from flask import Flask, render_template

app = Flask(__name__, static_folder='static', template_folder='templates')


@app.route('/')
def home():
    """Render the index.html template for route '/'.

    This file is a minimal Flask app. You can run it with:
        python main.py

    Or with the Flask CLI:
        $env:FLASK_APP = 'main.py'; flask run
    """
    return render_template('index.html')


if __name__ == '__main__':
    # Use debug=True for development; remove or set to False in production
    app.run(host='127.0.0.1', port=5000, debug=True)