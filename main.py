from flask import Flask, render_template, request

app = Flask(__name__, static_folder='static', template_folder='templates')

# Mapování voleb na soubory overlay
OVERLAY_MAP = {
    'candles': 'Svíčky',
    'chain': 'Řetěz',
    'balls': 'Koule'
}


@app.route('/')
def home():
    """Render the index.html template for route '/'.

    This file is a minimal Flask app. You can run it with:
        python main.py

    Or with the Flask CLI:
        $env:FLASK_APP = 'main.py'; flask run
    """
    # Načíst vybrané volby z query stringu
    selected = request.args.getlist('volby')
    
    # Filtrovat pouze existující volby
    selected = [v for v in selected if v in OVERLAY_MAP]
    
    # Připravit data pro šablonu
    overlays = [
        {'key': key, 'label': OVERLAY_MAP[key]}
        for key in selected
    ]
    
    return render_template('index.html', selected=selected, overlays=overlays)


if __name__ == '__main__':
    # Use debug=True for development; remove or set to False in production
    app.run(host='127.0.0.1', port=5000, debug=True)