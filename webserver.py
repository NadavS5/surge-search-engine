from flask import Flask, render_template, request
from database import Database 
from Keywords import Tokenizer 
app = Flask(__name__)

db = Database()
tk = Tokenizer()
@app.route("/",  methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        quary = request.form['prompt']
        result = str(db.search(tk.do2(" ",quary)))
        print(result)
        return f"<p>{result}</p>"
