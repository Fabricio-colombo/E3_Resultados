from flask import Flask, url_for, render_template

# inicialização
app = Flask(__name__)

# rotas
@app.route('/')
def home():
    return render_template('index.html')

# execução
app.run(debug=True)