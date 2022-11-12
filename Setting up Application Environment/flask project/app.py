from flask import Flask app=Flask(_name_)
@app.route('/')def
hello_world():
return '<h1>hello world!</h1>'
if __name__=='_main_:
app.run()