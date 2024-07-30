# from Phidget22.PhidgetException import *
# from Phidget22.Phidget import *
# from Phidget22.Devices.Log import *
# from Phidget22.LogLevel import *
# from Phidget22.Devices.SoundSensor import *
import traceback
import time
import tkinter as tk
import customtkinter as ctk 
import tkinter.ttk as ttk
from tkinter.font import Font
import collections
import cmd


#system settings
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("dark-blue")


#app frame and contents
app=tk.Tk()
app.geometry("400x600")
app.title("Sound Level Meter")



#notebook (tabs)

nb=ttk.Notebook(app)
frame1=ttk.Frame(nb)
frame2=ttk.Frame(nb)

#declare fonts as class

font1=Font(family="Calibri",size=24,weight="bold")
font2=Font(family="Calibri",size=14)

#frame label
label1 = ttk.Label(frame1, text = "Sound Level",font=font2)
label1.pack(padx = 10, pady = 10)


frame1.pack(padx = 10, pady=10, expand=True, fill = tk.BOTH)
nb.add(frame1,text="Sound Level")


label2=ttk.Label(frame2,text="Settings", font=font2)
label2.pack(padx=10,pady=10, expand=True,side="top")
frame2.pack(padx=10,pady=10,expand=True,fill=tk.BOTH)
nb.insert("end",frame2,text="Settings")
nb.place(x=0, y=0)


#messages in frame1
msg_1=ttk.Label(frame1, text="Sound level (in decibels):", font=font2, wraplength=200)
msg_1.pack(padx=10,pady=10, expand=True)
msg_2=ttk.Label(frame1,text="Ideal Average is 65dB",font=font2)
msg_2.pack(padx=10,pady=10, expand=True)
msg_3=ttk.Label(frame1,text="(Except for songs)",font=font2)
msg_3.pack(padx=10, pady=10)
#messages in frame 2




#size grips

sizegrip = ttk.Sizegrip(frame1)
sizegrip.pack(expand = True, fill = tk.BOTH, anchor=tk.SE)
sizegrip = ttk.Sizegrip(frame2)
sizegrip.pack(expand = True, fill = tk.BOTH, anchor=tk.SE)

#settings tab options
	#set data interval from input or default to 250


#     di=ctk.CTkEntry(frame2, width=100, height=40, text="Enter value (in milisec, default is 250\nMin: 100  Max: 1000)")
# 	if ctk.CTkEntry() 
    


# #hpidgets set data interval

# def setDataInterval(dataInterval)
# 	di=get_di.get()
	
#  de=collections.deque(maxlen=1/)


#unused code, code for future use
#seperator:
	# seperator = ttk.Separator(frame, orient="horizontal")
	# seperator.pack(expand=True, fill=tk.X)


#Declare any event handlers here. These will be called every time the associated event occurs.

# def onSoundSensor0_SPLChange(self, dB, dBA, dBC, octaves):
# 	print("DB: " + str(dB))
# 	print("DBA: " + str(dBA))
# 	print("DBC: " + str(dBC))
# 	print("Octaves: \t"+ str(octaves[0])+ "  |  "+ str(octaves[1])+ "  |  "+ str(octaves[2]))
# 	print("\t\t"+ str(octaves[3])+ "  |  "+ str(octaves[4])+ "  |  "+ str(octaves[5]))
# 	print("\t\t"+ str(octaves[6])+ "  |  "+ str(octaves[7])+ "  |  "+ str(octaves[8]))
# 	print("\t\t"+ str(octaves[9]))
# 	print("----------")

# def onSoundSensor0_Attach(self):
# 	print("Attach!")

# def onSoundSensor0_Detach(self):
# 	print("Detach!")

# def onSoundSensor0_Error(self, code, description):
# 	print("Code: " + ErrorEventCode.getName(code))
# 	print("Description: " + str(description))
# 	print("----------")

# def main():
# 	try:
# 		Log.enable(LogLevel.PHIDGET_LOG_INFO, "phidgetlog.log")
# 		#Create your Phidget channels
# 		soundSensor0 = SoundSensor()

# 		#Set addressing parameters to specify which channel to open (if any)

# 		#Assign any event handlers you need before calling open so that no events are missed.
# 		soundSensor0.setOnSPLChangeHandler(onSoundSensor0_SPLChange)
# 		soundSensor0.setOnAttachHandler(onSoundSensor0_Attach)
# 		soundSensor0.setOnDetachHandler(onSoundSensor0_Detach)
# 		soundSensor0.setOnErrorHandler(onSoundSensor0_Error)

# 		#Open your Phidgets and wait for attachment
# 		soundSensor0.openWaitForAttachment(5000)

# 		#Do stuff with your Phidgets here or in your event handlers.

# 		try:
# 			input("Press Enter to Stop\n")
# 		except (Exception, KeyboardInterrupt):
# 			pass

# 		#Close your Phidgets once the program is done.
# 		soundSensor0.close()

# 	except PhidgetException as ex:
# 		#We will catch Phidget Exceptions here, and print the error informaiton.
# 		traceback.print_exc()
# 		print("")
# 		print("PhidgetException " + str(ex.code) + " (" + ex.description + "): " + ex.details)


app.mainloop()
#main()