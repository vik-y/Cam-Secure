import subprocess
import datetime, time 
import pynotify

''' Utility Functions start here '''

def desktop_notify(title, message):
	'''
	This function can be used to send notification to the user regarding
	anything 
	'''
	pynotify.init("Test")
	notice = pynotify.Notification(title, message)
	notice.show()
    
def runCommand(comm):
	'''
	Using the subprocess library this runs the command passed 
	'''
	proc = subprocess.Popen(comm.split(), stdout=subprocess.PIPE)
	outputstr = ''
	for line in proc.stdout.readlines():
		    outputstr+=line.rstrip()+"\n"	    
	return outputstr[:-1]		
    
''' Utility Functions end here '''


def checkWebCam():
	'''
	Runs a shell command to check if the camera is being used or not 
	'''
	status = runCommand("lsof -t /dev/video0")
	if status=="":
		print "No process using webcam found"
		return status
	else:
		print "Webcam is being used by pids:"
		print status
		return status.split('\n')

def identifyProcess(pid):
	'''
	Given a pid, this process finds out the binary which is executing that process
	so that we can narrow down and identify the processes which are using that resource
	ps -p pid -> Might be useful here 
	ps -a pid -> Might also be useful here 
	Find out more commands so that you can use adavanced analytics
	'''
	return "a list of the binary locations"

def killProcess(pid):
	'''
	Given a process this function should kill it
	Should be used to kill the webcam using process 
	'''
	return runCommand("kill "+pid) 
	

def killAllCams():
	'''
	Running this function will kill all the process which are running webcam
	'''
	status = checkWebCam()
	if status=="":
		print "No processes running webcam found"
	else:
		print "Started to kill processes"
		for pid in status:
			print killProcess(pid)





#killAllCams() 
	
