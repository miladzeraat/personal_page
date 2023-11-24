from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    app.run(debug=True)

