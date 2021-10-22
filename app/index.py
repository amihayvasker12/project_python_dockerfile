from flask import Flask


app =Flask(__name__)
@app.route('/')
def Hellow_Amihay():
    return "hello Amihay"
@app.route('/moshe')
def  amihay_vasker():
    return "amihay vasker"
app.run(host="127.0.0.1",port=5000)