# CESlab

# TOPIC - Darkness prevention at work 

Hardware components:
--------------------------------------------------------------------------------------------------------
Arduino Uno
Breadboard
resistor (10K ohms)
LDR
Wires (10 pieces)
USB cable.

Basic Structure of the system:
--------------------------------------------------------------------------------------------------------
LDR and arduino circuit is made.
Arduino code is written on Arduino IDE and loaded to Arduino processsor.
Python app runs on System.
Arduino code on processor talks to Python App on System.
Python app takes necessary action based in input from Arduino.

Explanation:
--------------------------------------------------------------------------------------------------------
LDR senses the light from the surroundings and feeds it into the arduino as analog signals.
These analog signals are translated to digital form and are given to the arduino code on the processor.
Arduino code will have the business logic to judge if the light is low or not.
The result of the current status (NOK/OK) will be given to the Python App via the COM port
Python All reads this result and take necessary action.
	Actions Planned:
		-> Now the status OK so no action is taken by the python App and the user is using the computer system.
		-> Light in the room goes low. A status NOK is seen on the COM port by the Python APP - (python app action - )Now a Windows Toast           message is shown notifying this to the user. 
		-> (python app action - )If the state is still same after 2 minutes, Another toast is shown to the user asking to adjust the room           brigtness to avoid damage to the usr's eye sight while using the computer.
		-> When the user switches on the lights in the room, LDR senses it and Arduino gives an OK to the Python App then a toast is shown          telling lights are OK now and lets the user to continue working.
		-> (python app action - )If the state is still same after 2 more minutes (after a total of 4 minutes) Python App will put the system        to sleep
		
		
		
		
Circuit and Schematic Representation :  		

<a href="/DarknessProtection.pdf"></a>
DarknessProtection.pdf	DarknessProtection.pdf





