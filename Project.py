from flask import Flask, render_itemplate
from grovepi import *

app = Flask(__name__)

button1 = On
button2 = Off

LED Light = Port D4


index app.route("/")

def index():
   grovepi.digitalRead(button1)
   grovepi.digitalRead(button2)    
   grovepi.digitalRead(4)
   
   return f'Welcome to this Project'
   
   templateData = {
  'button1' : 'LED Light is Turned On.', 
  'button2' : 'LED Light is Turned Off.',
  } 
    return render_template('index.html', **templateData)


app.route('/turnLEDOn')
def light_on():   
	grovepi.digitalWrite(button1)
	grovepi.digitalWrite(4,val)
	
	return f'Led Light is On'
	
	
	templateData = {
	'button1 : LED Light is Turned On.', 
	}
	
   return render_template('index.html', **templateData)

app.route('/turnLEDOff')
def light_off():    
	grovepi.digitalWrite(button2)
	grovepi.digitalWrite(4,val)
	
	return f'Led Light is On'
	
	templateData = {
	'button2 : LED Light is Turned Off.', 
	}
	
   return render_template('index.html', **templateData)



if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)

