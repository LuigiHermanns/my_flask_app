# app.py
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', title="Página Inicial", description="Bem-vindo ao Flask App")

@app.route('/about')
def about():
    return render_template('about.html', title="Sobre nós", description="Essa é uma página sobre nós!	")

@app.route('/contact')
def contact():
    return render_template('contact.html', title="Página de Contato", description="Entre em contato conosco!")

@app.route('/Felicidade')
def lp():
    return "Eu amo Linguagens de Programação!"

if __name__ == '__main__':
    app.run(debug=True)