def getdayindex(x,y) :
    x = x + y
    if x > 6 : return (x-7)
    return x

def weekdayconfig(new_time, startday,days) :
    weekdayslist = ["Sunday","Monday","Tuesday","Wednesday","Thurday","Friday","Saturday"]
    weekdaysdist = { "sunday":0, "monday":1, "tuesday":2, "wednesday":3, "thursday":4, "friday":5, "saturday":6}
    new_time = new_time + ", " + weekdayslist[getdayindex(weekdaysdist[startday.lower()],(days%7))] + " " + daysConfig(days)
    return new_time    

def daysConfig(days) :
    if days==0 : return ("")
    if days==1 : return ("(next day)")
    return ("({} days later)".format(days))
def add_time(start, duration, startday=None):
    start, startformat = start.split()
    days = 0
    start = list(map(int,start.split(':')))
    duration = list(map(int, duration.split(':')))
    days = duration[0]//24
    duration[0]%=24
    while(duration[0]>0) :
        if duration[0]<12 :
            start[0] += duration[0]
            duration[0] = 0
            if start[0]>=12 :
                if startformat=="AM" :
                    startformat = "PM"
                else :
                    startformat = "AM"
                    days += 1
                start[0] = 12 if start[0]%12==0 else start[0]%12
        else :
            if startformat=="PM" :
                startformat="AM"
                days+=1
            else : startformat="PM"
            duration[0]-=12

    start[1]+=duration[1]
    if start[1]>=60 :
        start[0]+=1
        if start[0]>=12 :
            if startformat=="AM" :
                startformat = "PM"
            else :
                startformat = "AM"
                days += 1
            start[0] = 12 if start[0]%12==0 else start[0]%12
        start[1] = 0 if start[1]%60==0 else start[1]%60
    new_time = " ".join([str(start[0]) +':'+ str(start[1]).rjust(2,'0'),startformat])
    if startday==None : new_time = " ".join([new_time,daysConfig(days)])
    else : new_time = weekdayconfig(new_time,startday,days)
    
    return (new_time.strip())