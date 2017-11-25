from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/hello', methods=['POST', 'GET'])
def index_laid_out():
    greeting = "Hello World"
    
    if request.method == "POST":
        name = request.form['name']
        greet = request.form['greet']
        greeting = "{}, {}".format(greet, name)
        
        return render_template("index_laid_out.html", greeting=greeting)
    else:
        return render_template("index_form_laid_out.html")
    
if __name__ == "__main__":
    app.run()