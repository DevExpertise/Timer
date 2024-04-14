
import time#import time module
print("Set timer.")
my_time_h=int(input("Enter  Hour:"))#take time in hour
my_time_h=3600*my_time_h#hour in second

my_time_m=int(input("Enter  Minute:"))#take time in minute
my_time_m=60*my_time_m#convert in second
my_time_s=int(input("Enter  second:"))#take time in second
#Sum of  all time in second
my_time=my_time_m+my_time_s+my_time_h
for i in range(my_time,0,-1):
#calculate second, minute and hour
    seconds=i%60
    minutes=i//60
    hours=int(i/3600)
    #print the result
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    #sleep for 1 second
    time.sleep(1)
print("Time's up")

