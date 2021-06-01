from flask import Flask  
app = Flask(__name__)  
 
@app.route('/home')  
def home():  
    return "hello, execute home function";  

@app.route('/hotel')  
def hotel():  
    return "hi, execute hotel function";  

  
if __name__ =="__main__":  
    app.run(debug = True)  