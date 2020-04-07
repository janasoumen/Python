featureSet = {}
featureSet[0]="InstaPOC"
featureSet[1]="MissedCallAlert"
featureSet[2]="CallEndedAlert"
featureSet[3]="LocationSubscription"
featureSet[4]="SupervisoryOverride"
featureSet[5]="BroadCast Group Service"
featureSet[6]="Support Media reconnect on 3G"
featureSet[7]="QPP-PTX Feature"
featureSet[8]="Session Participants to Originator"
featureSet[9]="Status Messaging Feature"
featureSet[10]="SIP Push-Notify Feature"
featureSet[11]="Premium Web-Dispatch Feature"
featureSet[12]="Reserved for future use"
featureSet[13]="Reserved for future use"
featureSet[14]="TU SMS"
featureSet[15]="XCAP Doc-diff"
featureSet[16]="PoC over wifi"
featureSet[17]="HTTPS support"
featureSet[18]="Paging Message support"
featureSet[19]="Relogin message support"
featureSet[20]="Talk Group Select Scanning server"
featureSet[21]="Presence update reduction"
featureSet[22]="Jitter stats"
featureSet[23]="History Based Presence"
featureSet[24]="Decouple Presence/Call"
featureSet[25]="Periodic client logs/report"
featureSet[26]="On demand client logs"
featureSet[27]="On demand location"
featureSet[28]="Talk Group Scanning client"
featureSet[29]="Battery Usage Optimization"
featureSet[30]="Client UI Stats"
featureSet[31]="Talk Group Select client"
featureSet[32]="Pre-Call CQI (Call Quality Indicator) feature"
featureSet[33]="PushToText feature"
featureSet[34]="PushToMultimedia feature"
featureSet[35]="PushToLocation feature"
featureSet[36]="Urgent-message origination"
featureSet[37]="Reserved for future use"
featureSet[38]="Group Member Location feature"
featureSet[39]="Geo fence feature"
featureSet[40]="GCM Push Notify"
featureSet[41]="In-Call CQI (Call Quality Indicator) feature"
featureSet[42]="UFMI Support"
featureSet[43]="RemotePushNotification"
featureSet[44]="PTT Radio Client"
featureSet[45]="XCAP Couchbase Client"
featureSet[46]="Voice message fallback feature"
featureSet[47]="PTT Recording On Client"
featureSet[48]="Multiple Simultaneous Session support"
featureSet[49]="Bread-Crumb feature"
featureSet[50]="InstaDRX"
featureSet[51]="BlockCallsWifi"
featureSet[52]="BlockCallsCellular"
featureSet[53]="LMR Interop"
featureSet[54]="Ambient Listening"
featureSet[55]="Discreet Listening"
featureSet[56]="User-Check"
featureSet[57]="User Service Enable-Disable"
featureSet[58]="Emergency"
featureSet[59]="Area-Based Group-member Privilege"
featureSet[60]="Area-Based Group Owner Privilege"
featureSet[61]="Large Group Support"
featureSet[62]="Dynamic QoS"
featureSet[63]="Presence Notifications for clients in Foreground"
featureSet[64]="MCData SDS"
featureSet[65]="MCData FD"
featureSet[66]="Operational Status Messaging"
featureSet[67]="MCVideoTX"
featureSet[68]="MCVideoRX"
featureSet[69]="MCVideoGroupRX"
featureSet[70]="MCVideoConfirmedPull"
featureSet[71]="MCVideoUnconfirmedPull"
featureSet[72]="PSCSRestriction"
featureSet[73]="LMRInteropROIP"
featureSet[74]="LMRInteropP25"
featureSet[75]="LMRInteropWRG"
featureSet[76]="UserProfileMgmt"
featureSet[77]="E2E Encryption & SRTP"
featureSet[78]="Affiliation Feature"
featureSet[79]="Affiliation Monitoring Feature"
featureSet[80]="Remote Group Affiliation (REGA) Feature"
featureSet[81]="MCPTT User"
featureSet[82]="MCPTT via GW"
featureSet[83]="MCPTT location trigger via GW"
featureSet[84]="MC Device"
featureSet[85]="Manual answer"
featureSet[86]="FTA Origination"
featureSet[87]="Secure Full duplex"
featureSet[88]="Reserved for future use"
featureSet[89]="Reserved for future use"

f = input("Enter feature bit in Hex. (e.g. 2080000061CE150DC033): ")
dec = int(f, 16)
b = bin(dec)
bin_s = b[2:]

if len(bin_s) != len(featureSet):
    diff = len(featureSet)-len(bin_s)
    zero =''.join([str(0) for i in range(0,diff)])
bin_s = zero+bin_s

print("\n")
print("Binary value of", f, "is: ")
print(bin_s)
bin_val = bin_s[::-1]

print("\n")
flag = 0
p = int(input("Enter Bit position (e.g. 27): "))
if p < 90:
    for i in range(len(bin_val)):
        if i == p:
            if int(bin_val[i])==1:
                print("\n")
                print(featureSet[i]+" >>> Enabled")
                flag = 1
            else:
                print("\n")
                print(featureSet[i]+" >>> Disabled")
                flag = 2
else:
    print("\n")
    print("Bit position you have entered out of range. Please try again...")
    flag = 3
                    
lst = [int(bin_val[i]) for i in range(len(bin_val))]

if flag == 1:
    print("\n")
    x = input("Bit is Enabled. Would you like to Disable (y/n) :")
    while True:
        if x == "n":
            break
            
        elif x == "y":
            lst[p] = 0
            new_bin_en = ''.join([str(ele) for ele in lst])
            new_bin_en_re = new_bin_en[::-1]
            print("\n")
            print("Binary value after bit",p, "is disabled: ")
            print(new_bin_en_re)
            dec_en = int(new_bin_en_re,2)
            hex_en = hex(dec_en)
            print("\n")
            print("Hexadecimal value after disabling the bit: ",hex_en[2:])
            break
            
        else:
            print("\n")
            print("In valid entry, Please try again....")
            break
elif flag == 3:
        print("\n")
            
else:
    print("\n")
    x = input("Bit is Disabled. Would you like to Enable (y/n) :")
    while True:
        if x == "n":
            break
            
        elif x == "y":
            lst[p] = 1
            new_bin_en = ''.join([str(ele) for ele in lst])
            new_bin_en_re = new_bin_en[::-1]
            print("\n")
            print("Binary value after bit",p, "is enabled: ")
            print(new_bin_en_re)
            dec_en = int(new_bin_en_re,2)
            hex_en = hex(dec_en)
            print("\n")
            print("Hexadecimal value after enabling the bit: ",hex_en[2:])
            #print(hex_en[2:])
            break
        else:
            print("\n")
            print("In valid entry, Please try again....")
            break
            

print("\n")
input("WhiteBox@motorolasolutions.com")    


