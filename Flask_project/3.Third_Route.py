from flask import Flask  
app = Flask(__name__)  
 
@app.route('/home/<stringparameter>')  
def home(stringparameter):  
    return "hello,"+stringparameter;  
    
@app.route('/hotel/<int:age>')  
def hotel(age):  
    return "Age = %d"%age; 


#The add_url_rule() function
def about():  
    return "This is about page";  
  
app.add_url_rule("/about","about",about)  
    
  
if __name__ =="__main__":  
    app.run(debug = True)  