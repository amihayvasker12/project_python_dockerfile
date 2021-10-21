from flask import Flask


app =Flask(__name__)
@app.route('/')
def Hellow_Amihay():
    return "hello Amihay"
app.run(host="0.0.0.0",port=5000)
