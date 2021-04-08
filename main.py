from flask import Flask 
from flask import render_template, redirect, url_for
from flask import request
from blockchain import *

app = Flask (__name__)

@app.route('/', methods= ['POST', 'GET'])

def index():

    if request.method == "POST":
        lender = request.form["Lender"]
        borrower = request.form["borrower"]
        sum_ = request.form["sum"]
        write_block(amount = sum_, from_name= lender, to_name = borrower )

        return redirect(url_for('index'))
    return render_template('index.html')

{'/': 'index'}

@app.route('/checking', methods= ["GET"])
def checking():
    result = check_integrition()
    return render_template('index.html', results= result)

if __name__ == "__main__":
    
    app.run(debug= True)




