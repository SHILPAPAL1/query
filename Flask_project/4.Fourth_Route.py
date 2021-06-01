from flask import *  
   
app = Flask(__name__)  
  
@app.route('/admin')  
def admin():  
    return 'admin'  
  
@app.route('/librarion')  
def librarion():  
    return 'librarion'  
  
@app.route('/student')  
def student():  
    return 'student'  
  
@app.route('/user/<stringparameter>')  
def user(stringparameter):  
    if stringparameter == 'admin':  
        return redirect(url_for('admin'))  
    if stringparameter == 'librarion':  
        return redirect(url_for('librarion'))  
    if stringparameter == 'student':  
        return redirect(url_for('student'))  

if __name__ =='__main__':  
    app.run(debug = True)  