#!/usr/bin/env python
#Get current working directory with os.getcwd()
print os.getcwd()

#Get the status of a file with os.stat()
print "Getting the status of: ", os.stat('/usr/bin/python')

#Execute a shell command with os.system()
os.system('ls -l')

#Return the current process id with os.getpid()
print os.getpid()
os.chmod(path, mode)

#Change the owner and group id of path to the numeric uid and gid with os.chown()
os.chown(path, uid, gid)

#Processes in the system run queue averaged over the last 1, 5, and 15 minutes
print os.getloadavg()

#Check if a path exists with os.path.exists()
if os.path.exists("file.txt"):
