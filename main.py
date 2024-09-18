from flask import Flask,url_for,render_template

app = Flask(__name__, static_folder='static')

@app.route('/')
def loginPage():
    return render_template('login.html')

@app.route('/upload/')
def uploadPage():
    return render_template('upload.html')

@app.route('/registro/')
def registroPage():
    return render_template('registro.html')
@app.route('/ultimasconsultas/')
def lastConsultPage():
    return render_template('ultimasConsultas.html')

if __name__ == '__main__':
    app.run(debug=True)