    """
**Procedure:
1) Copy poc_app_logs.txt and script in same directory
2) Run "python spoc_app_filter.py"
3) Output filtered logs will be in "filtered_file.txt"
"""

import re
from os.path import abspath

"""
==============================================================================================================================
Comment line::  This Module gets the line and compare if the filter string is present or not. If present then it prints. 
==============================================================================================================================
"""
def filecheck(line_check):
    NWevent = ["Current IP address", "Received bear type is","Received Data state is","T-CONN-DW Dur:","PresenceUpdate UNAVAILABLE",
                "Received IP address is", "Current Client APP  state is", "debounce_timer_val","KN_MSG_TYPE_NETWORK_REG_SUCCESS",
                "TRANSPORT_MAX_FAILED", "calculateAndGetDebounceTimerValue", "on_connection_debounce_timer_exp: start login",
                "CDE _KN_StopEngine: Reason:"]

    
    for i in range (len (NWevent)):
        if re.match("(.*)" + NWevent[i] + "(.*)", line_check):
            #print line_check
            f = open("PTT\\log_snippet.txt", "a")
            f.write(line_check + "\n")
            f.close()

   
"""
==============================================================================================================================
This code does open the file and feed the file line to a module
==============================================================================================================================
"""

opened_poc_app_file = open("PTT\\poc_app_logs.txt", "r")
for line in opened_poc_app_file:
    filecheck(line)
opened_poc_app_file.close()
