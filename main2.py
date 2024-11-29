# program to geberate a random date from the given start and end dates
import random
import time
def gen_of_ran(startdate,enddate):
    unknown=random.random()
    dateformat='%m/%d/%Y'
    starttime=time.mktime(time.strptime(startdate,dateformat))
    endtime=time.mktime(time.strptime(enddate,dateformat))
    randomtime= starttime+unknown*(endtime-starttime)
    randomdate= time.strftime(dateformat,time.localtime(randomtime))
    return randomdate
print("the random date is:",gen_of_ran("1/1/2013","12/12/2017"))