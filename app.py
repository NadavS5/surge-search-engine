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
        result = db.search(tk.do2(" ",quary))

        print("template rendered")

        return render_template('results.html', results = result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)#, ssl_context=('/etc/ssl/certs/selfsigned.crt', '/etc/ssl/private/selfsigned.key'))
