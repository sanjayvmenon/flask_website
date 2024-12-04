from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")
@app.route("/home")
def home():
    return render_template("home.html")
@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")
@app.route("/contactus")
def contactus():
    return render_template("contactus.html")
@app.route('/register', methods=['GET','POST'])
def register():
    name=request.form.get('txtName','no-name')
    email=request.form.get('txtEmail','no-name')
    mobile=request.form.get('txtMob','no-name')
    print(name+" "+email+" "+str(mobile))
    return name+" "+email+" "+str(mobile)