from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <style>
            body { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); height: 100vh; display: flex; justify-content: center; align-items: center; font-family: sans-serif; margin: 0; }
            .card { background: rgba(255, 255, 255, 0.2); backdrop-filter: blur(10px); border-radius: 20px; padding: 40px; box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37); color: white; text-align: center; border: 1px solid rgba(255, 255, 255, 0.18); }
            h1 { font-size: 3em; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Bonjour à tous !</h1>
            <p>Ceci est une simple application conteneurisée avec Docker par <br>
                <strong>Wilfried Adjaba</strong></p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)