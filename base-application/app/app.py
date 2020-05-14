from flask import Flask
from app.src.blueprints.example_one_blueprint import example_one
from app.src.blueprints.example_two_blueprint import example_two
#from werkzeug.contrib.fixers import ProxyFix


app = Flask("base-application-template", static_folder="app/assets")
# transform everything in https
#app.wsgi_app = ProxyFix(app.wsgi_app)
# Register blueprints
app.register_blueprint(example_one, url_prefix='/api/one')  # URL should be http://server-ip:port/api/one
app.register_blueprint(example_two, url_prefix='/api/two')


@app.route("/")
def hello():
    return "Hello, you have successfully configured your application, now you can use your full URL's to enjoy your functionalities!!"
