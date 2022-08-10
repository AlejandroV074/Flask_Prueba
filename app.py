from flask import Flask, render_template

app = Flask(__name__)

@app.route("/index.html")
def index():
    return render_template("index.html")
    
@app.route("/contacto.html")
def contacto():
    return render_template("contacto.html")

if __name__ == "__main__":
    app.run(debug=True)

