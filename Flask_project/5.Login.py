from flask import *  
app = Flask(__name__)  
  
@app.route('/login',methods = ['POST'])  
def login():  
      uname=request.form['uname']  
      passwrd=request.form['pass']  
      if uname=="chan" and passwrd=="pass":  
          return "Welcome %s" %uname 

'''
@app.route('/login',methods = ['GET'])  
def login():  
      uname=request.args.get('uname')  
      passwrd=request.args.get('pass')  
      if uname=="chan" and passwrd=="chan":  
          return "Welcome %s" %uname            
'''
   
if __name__ == '__main__':  
   app.run(debug = True)  