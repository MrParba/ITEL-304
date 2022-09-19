import username as username
from flask import Flask, request
from datetime import datetime

app = Flask (__name__)

@app.route("/")
def home():
        return """
            <html><body> 
             <form action="/input">
                 Your name? <input type='text' name='username'><br>
                 Your characteristic? <input type='text' name='char'><br> 
              <input type='submit' value='Continue'>
              </form>
              </body></html>
               """
@app.route('/input')
def greet():
    username = request.args.get("username","World")
    char =  request.args ['char']
    if char =='':
         msg= 'You did not enter your characteristc'
    else:
         msg = username + ' is ' + char 

    return """
        <html><body>
            <h2>{0}!</h2> 
             {1}
         </body></html> 
     """.format(username, msg)

app.run(host="localhost", debug=True)
