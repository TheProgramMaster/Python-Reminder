import time
txt = input("What shall I remind you about?: ")
local_time = int(input("In how many minutes?: "))
local_seconds = local_time * 60
time.sleep(local_seconds)
