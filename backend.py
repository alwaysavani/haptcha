from flask import Flask, flash, request, redirect, url_for,render_template
from werkzeug.utils import secure_filename
import webbrowser
import fingers
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/new1')
def run1():
    check=0	
    for i in range(0,3):
     text=fingers.fingermain()
     if text=="ONE":
      webbrowser.open_new_tab('https://www.wcs.org/96-elephants')
      check=1
      return "CAPTCHA SUCCESSFULL"	
    if check==1:
     return "Captcha Successful"
    else:
     return "unsuccessful capctha!! Are you a robot??? "
@app.route('/new3')
def run2():
    check=0	
    for i in range(0,3):
     text=fingers.fingermain()
     if text=="THREE":
      webbrowser.open_new_tab('http://www.sgsits.ac.in/')
      check=1
      return "CAPTCHA SUCCESSFULL"	
    if check==1:
     return "Captcha Successful"
    else:
     return "unsuccessful capctha Are you a robot??? "
@app.route('/new2')
def run3():
    check=0	
    for i in range(0,3):
     text=fingers.fingermain()
     if text=="TWO":
      webbrowser.open_new_tab('http://www.sgsits.ac.in/')
      check=1
      return "CAPTCHA SUCCESSFULL"	
    if check==1:
     return "Captcha Successful"
    else:
     return "unsuccessful capctha Are you a robot??? "	
@app.route('/new4')
def run4():
    check=0	
    for i in range(0,3):
     text=fingers.fingermain()
     if text=="FOUR":
      webbrowser.open_new_tab('http://www.sgsits.ac.in/')
      check=1
      return "CAPTCHA SUCCESSFULL"	
    if check==1:
     return "Captcha Successful"
    else:
     return "unsuccessful capctha Are you a robot??? "	
@app.route('/new5')
def run5():
    check=0	
    for i in range(0,3):
     text=fingers.fingermain()
     if text=="FIVE":
      webbrowser.open_new_tab('http://www.sgsits.ac.in/')
      check=1
      return "CAPTCHA SUCCESSFULL"	
    if check==1:
     return "Captcha Successful"
    else:
     return "unsuccessful capctha Are you a robot??? "
if __name__ == '__main__':
    app.run(debug=True)
