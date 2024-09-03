
from Phidget22.PhidgetException import *
from Phidget22.Phidget import *
from Phidget22.Devices.Log import *
from Phidget22.LogLevel import *
from Phidget22.Devices.SoundSensor import *
import traceback
import time
import tkinter as tk
from tkinter import *
from customtkinter import * 
from tkinter import ttk


def app_body	():
    app=tk.Tk()

    nb = ttk.Notebook(app)
    frame1= ttk.Frame(nb)
    frame2= ttk.Frame(nb)

    label1 = ttk.Label(frame1, text="Sound Level")
    label1.pack(pady=50,padx=20)

    frame1.pack(fill=BOTH,expand=True)
    nb.add(frame1,text = "Sound Meter")

    frame2 = ttk.Frame(nb)
    label2=ttk.Label(frame2)
    label2.pack(pady=50,padx=20)
    nb.insert("end",frame2,text="Settings")
    nb.pack(padx=5,pady=5, expand=True)
    return app

app = app_body()


def onSoundSensor0_Attach(self):
	print("Attach!")
	
def onSoundSensor0_Detach(self):
	print("Detach!")

def onSoundSensor0_Error(self, code, description):
	print("Code: " + ErrorEventCode.getName(code))
	print("Description: " + str(description))
	print("----------")
	
def onSoundSensor0_SPLChange(self, dB, dBA, dBC, octaves):
	print("DB: " + str(dB))
	print("DBA: " + str(dBA))
	print("DBC: " + str(dBC))
	print("Octaves: \t"+ str(octaves[0])+ "  |  "+ str(octaves[1])+ "  |  "+ str(octaves[2]))
	print("\t\t"+ str(octaves[3])+ "  |  "+ str(octaves[4])+ "  |  "+ str(octaves[5]))
	print("\t\t"+ str(octaves[6])+ "  |  "+ str(octaves[7])+ "  |  "+ str(octaves[8]))
	print("\t\t"+ str(octaves[9]))
	print("----------")
def main():
	try:
		Log.enable(LogLevel.PHIDGET_LOG_INFO, "phidgetlog.log")
		#Create your Phidget channels
		soundSensor0 = SoundSensor()

		#Set addressing parameters to specify which channel to open (if any)

		#Assign any event handlers you need before calling open so that no events are missed.
		soundSensor0.setOnSPLChangeHandler(onSoundSensor0_SPLChange)
		soundSensor0.setOnAttachHandler(onSoundSensor0_Attach)
		soundSensor0.setOnDetachHandler(onSoundSensor0_Detach)
		soundSensor0.setOnErrorHandler(onSoundSensor0_Error)

		#Open your Phidgets and wait for attachment
		soundSensor0.openWaitForAttachment(5000)

		#Do stuff with your Phidgets here or in your event handlers.

		try:
			input("Press Enter to Stop\n")
		except (Exception, KeyboardInterrupt):
			pass

		#Close your Phidgets once the program is done.
		soundSensor0.close()

	except PhidgetException as ex:
		#We will catch Phidget Exceptions here, and print the error informaiton.
		traceback.print_exc()
		print("")
		print("PhidgetException " + str(ex.code) + " (" + ex.description + "): " + ex.details)

main()

app.mainloop()

#Declare any event handlers here. These will be called every time the associated event occurs.








