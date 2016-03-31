'''
Created Feb 2, 2014
BOOOKEEPING:
1) ONE folder per action
2) Use descriptive names for the png's
3) Set timer class, to start, pause and stop as needed

References:
1) timer: http://stackoverflow.com/questions/4152969/genrate-timer-in-python
2) http://stackoverflow.com/questions/12320444/how-to-execute-a-code-for-a-given-time-period

@author: carlos
'''

import os, sys
import threading
import time


def get_input_labels(root = "../data"):
    done = False
    while not done:
        var = raw_input("Enter: 'actor' 'action' ").lower()
        v = var.split(" ")
        if len(v) < 2:
            print "Please type: [actor] [action] labels"
            print "example: carlos walk"
        elif len(v) > 2:
            print "Error, exceeded number of arguments! Please try again"
        else:
            actor = v[0]
            action= v[1]
            print "Entered: ", actor, action
            done = True
    return actor, action
# getinputlabels


def create_view_folder(actor, action, angle):
    folder_name = action+"_"+actor+"_"+str(angle)
    #folder = os.path.join(root, action, actor, angle)
    folder = os.path.join(root, folder_name)
    if not os.path.exists(folder):
        os.makedirs(folder) # mkdir DOES NOT WORK!
        print "created: ", folder
#createviewfolder


def compute_something(stopped, actor, action, angle):
    now = time.time()
    while not stopped:
        #DATA COLLECTION HERE!
        i =1
    create_view_folder(actor, action, angle)
    later=time.time()
    print "elapsed code execution [s]: %.2f" %(later-now)
# compute_something


if __name__ == '__main__':    # Execution & sleep/pause time in seconds
    execution_time = 10
    sleep_time = 2
    actor, action = get_input_labels()

    for angle in xrange(0,360,180):
        print "Begin recording for view: "+str(angle)+" in "+str(sleep_time)+" secs"
        stopped = []
        threading.Timer(execution_time, stopped.append, args=[True]).start()
        compute_something(stopped, actor, action, angle)
        now = time.time()
        print "you have "+str(sleep_time)+ " secs to face new orientation"
        time.sleep(sleep_time)
        later=time.time()
        print "elapsed pause[s]: %.2f" %(later-now)