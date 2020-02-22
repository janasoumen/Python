import re

file = open('poc_app_logs.txt','r')
readFile = file.read()



########## Find if SIP/HTTP Method and Response present in log ##########

def isPresent(x):
    if re.search(x, readFile):
        return ("{} present in log file".format(x))
    return ("{} not present in log file".format(x))

#print(isPresent("RTSP"))

########## Check if SIP/HTTP Method and Response count from log ##########
def isCount(c):
    count = 0
    sipMethod = re.findall(c, readFile)
    for invite in sipMethod:
        count += 1
    return count

#print(isCount("=>INVITE"))


#################### SIP request and Cseq ####################

  
