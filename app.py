from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/myApps')  
def my_apps():
    return render_template('my_apps.html')

if __name__ == '__main__':
    app.run()