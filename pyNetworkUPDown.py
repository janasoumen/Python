"""
**Procedure:
1) Copy poc_app_logs.txt and script in same directory
2) Run "python spoc_app_filter.py"
3) Output filtered logs will be in "filtered_file.txt"
"""

import re
from os.path import abspath

def network():
    logEvent = ["Current IP address", "Received bear type is","Received Data state is","T-CONN-DW Dur:","PresenceUpdate UNAVAILABLE",
                "Received IP address is", "Current Client APP  state is", "debounce_timer_val","KN_MSG_TYPE_NETWORK_REG_SUCCESS",
                "TRANSPORT_MAX_FAILED", "calculateAndGetDebounceTimerValue", "on_connection_debounce_timer_exp: start login",
                "CDE _KN_StopEngine: Reason:"]

    #................NetWork UP DOWN related log copied to log_snippet.txt file................#
    file = open('PTT\\poc_app_logs.txt','r')
    f1 = open("PTT\\log_snippet.txt",'w')
    for line in file:
        for event in logEvent:        
            if re.findall(event, line):
                #print(line)
                f1.write(line)
    file.close()
    f1.close()
    print ("Log snippet path: ",abspath('log_snippet.txt'))

    #................Checking if client Presence become UNAVAILABLE in log file................#
    f2 = open("PTT\\log_snippet.txt",'r')
    read = f2.read()
    if re.search(logEvent[4], read):
        print("StopEngine Reason 6 called due to 20 sec NetWork down timer expired...")
        

    #.............................Getting timestamps for Network DOWN.............................#
    dicts = {
        "ip" : "Current IP address",
        "bearer" : "Received bear type is",
        "nwState" : "Received Data state is",
        "DWTimer" : "T-CONN-DW Dur:",
        "presence" : "PresenceUpdate UNAVAILABLE",
        "recIP" : "Received IP address is",
        "curIP" : "Current Client APP  state is",
        "debTimer" : "debounce_timer_val",
        "regSucc" : "KN_MSG_TYPE_NETWORK_REG_SUCCESS",
        "TPFail" : "TRANSPORT_MAX_FAILED",
        "debTimVal" : "calculateAndGetDebounceTimerValue",
        "debTimExp" : "on_connection_debounce_timer_exp: start login",
        "StopEngine" : "CDE _KN_StopEngine: Reason:"}
    
    f3 = open("PTT\\log_snippet.txt",'r')
    #x = re.findall(logEvent[12], read)
    x = re.findall(dicts["StopEngine"], read)
    print(x[0])
    for lines in f3:
        if x[0] in lines:
            time = re.findall("\d{1,2}:\d{1,2}:\d{1,2}:\d{1,3}",lines)
            print (time)

    
print(network())


