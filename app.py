from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/historico")
def historico():
    return render_template("historico.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/projetosfac")
def projetosfac():
    return render_template("projetosfac.html")

if __name__ == '__main__':
    app.run(debug=True)