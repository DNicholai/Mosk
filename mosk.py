#!/usr/bin/python
# Script to lauch mosquitto_sub to monitor a mqtt topic -- SYNTAX : mosk topic

import subprocess 
import sys

debug = 0   ## Debug to print the output

total = len(sys.argv)
cmdargs = str(sys.argv)

if debug == 1 : 
   print ("The total numbers of args passed to the script: %d " % total)
   print ("Args list: %s " % cmdargs)
   # Pharsing args one by one 
   print ("Script name: %s" % str(sys.argv[0]))
   print ("First argument: %s" % str(sys.argv[1]))

topic = str(sys.argv[1])

if debug == 1 : 
   print "The selected topic is " , topic

cmd = "mosquitto_sub -h 192.168.1.100 -v -t " + topic + " | ts" 
print "The command which was executed is : " , cmd

def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            print output.strip()
    rc = process.poll()
    return rc

run_command(cmd) #This is the lauch of the actual command
