from flask import Flask, render_template

def create_app(enviroment):
    app = Flask(__name__)    

    app.config.from_object(enviroment)

    with app.app_context():
        db.init_app(app)
        db.create_all()

    return app

enviroment = config["development"]
if config_decouple("PRODUCTION", default=False):
    enviroment = config["production"]
app = create_app(enviroment)

@app.route("/index.html")
def index():
    return render_template("index.html")
    
@app.route("/contacto.html")
def contacto():
    return render_template("contacto.html")

if __name__ == "__main__":
    app.run(debug=True)

