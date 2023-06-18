from email.policy import default
from re import T
from tracemalloc import start
import pyttsx3
import schedule
import time

text_speech = pyttsx3.init()

print("###################################")
print("welcome to the time telling")
print("let's do some configing")

isWeekEndWanted = False
if input("do you want the program to work during weekEnd, if yes enter 'y': ") == "y":
    isWeekEndWanted = True


print("====================================")
print("# now the period of telling if nothing was entered it will say the time of every hour #  ==+in 24 format+==")
stert = input("when do you want the time telling to start from which hour : ")
End = input("when do you want the time telling to End : ")



print("====================================")
evry = input("after what :" )
    





def isFrom_1AM_8AM_Wanted(timeNow):
    if stert == "" or End == "":
        return True
    
    if timeNow >= stert and timeNow <= End:
        return False
    return True

def isTheWeekEnd_Wanted(timeOpj):
    day = time.strftime("%A", timeOpj)
    if isWeekEndWanted == True:
        return True
    match day:
        case "Friday":
            return False
        case "Saturday":
            return False
    return True
    
def timeCheck():
    time_object = time.localtime()
    local_huor= int(time.strftime("%H", time_object))
    if local_huor >= 0 and local_huor < 12:
        #for the AM Format
        if local_huor == 0:
            local_time_hour = "12, AM"
        else:
            local_time_hour = f"{local_huor}, AM"
    else:
        #for the PM Format
        match local_huor:
            case 12:
                local_time_hour = "12, PM"
            case 13:
                local_time_hour = "1, PM"
            case 14:
                local_time_hour = "2, PM"
            case 15:
                local_time_hour = "3, PM"
            case 16:
                local_time_hour = "4, PM"
            case 17:
                local_time_hour = "5, PM"
            case 18:
                local_time_hour = "6, PM"
            case 19:
                local_time_hour = "7, PM"
            case 20:
                local_time_hour = "8, PM"
            case 21:
                local_time_hour = "9, PM"
            case 22:
                local_time_hour = "10, PM"
            case 23:
                local_time_hour = "11, PM"
        
    local_time_minute = time.strftime("%M", time_object)
    text = f"the time now is, {local_time_hour}, And {local_time_minute} minutes"
    if (isFrom_1AM_8AM_Wanted(local_huor) and isTheWeekEnd_Wanted(time_object)):
        print(text)
        text_speech.say(text)
        text_speech.runAndWait()



print("====================================")
print("select the wanted pariod")
print("1: seconds")
print("2: mintes")
print("3: houre")
interdPeriod = input("select :" )
match interdPeriod:
    case '1' :
        period = "seconds"
        schedule.every(int(evry)).seconds.do(timeCheck)
    case '2' :
        period = "minutes"
        schedule.every(int(evry)).minutes.do(timeCheck)
    case '3' :
        period = "hours"
        schedule.every(int(evry)).hours.do(timeCheck)
    case other:
        period = "hours"
        schedule.every(int(evry)).hours.do(timeCheck)


print("####################################")
print("####################################")
print("####################################")
print("the program time telling is running")
print(f"## the telling will be after evry {evry},  {period} ##")
print(f"## and it will start from {stert} antell {End} ##")
if isWeekEndWanted:
    print(f"## and the weekEnd is enabiled ##")
else:
    print(f"## and the weekEnd is desabiled ##")
timeCheck() 









while 1:
    schedule.run_pending()

