import time#import time module
print("Set timer.")
my_time=int(input("Enter time in second:"))#take time in second
for i in range(my_time,0,-1):
#calculate second ,minute and hour
    seconds=i%60
    minutes=i//60
    hours=int(i/3600)
    #print the result
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    #sleep for 1 second
    time.sleep(1)
print("Time's up")
