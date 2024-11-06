#Flask es nuestra biblioteca de backend
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/git')
def git():
    return render_template('git.html')

@app.route('/impresion3D')
def impresion3D():
    return render_template('impresion3D.html')

@app.route('/sobremi')
def sobremi():
    return render_template('sobremi.html')

@app.route('/arVrEr')
def arVrEr():
    return render_template('arVrEr.html')

@app.route('/apps')
def apps():
    return render_template('apps.html')

@app.route('/ahorcado')
def ahorcado():
    return render_template('ahorcado.html')

@app.route('/desarrollo')
def desarrollo():
    return render_template('desarrollo.html')

@app.route('/Tarea')
def Tarea():
    return render_template('Tarea.html')

@app.route('/servidores')
def servidores():
    return render_template('servidores.html')


if __name__ == '__main__' :
    app.run(debug=True)




