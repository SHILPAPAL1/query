from flask import *  
app = Flask(__name__)  
  
@app.route('/user/<stringparameter>')  
def message(stringparameter):  
      return render_template('seventh_view.html',key1=stringparameter)  

@app.route('/table/<int:num>')  
def table(num):  
      return render_template('seventh_printtable_view.html',key2=num)  

@app.route('/cssdemo')  
def display():  
      return render_template('seventh_css_view.html')  

if __name__ == '__main__':  
   app.run(debug = True)  