import datetime
currentTime = datetime.datetime.now()
print("Current date and time : ", currentTime)

print("Year : ", currentTime.year)
print("Month : ", currentTime.month)
print("Day : ", currentTime.day)
print("Hour : ", currentTime.hour)
print("Minute : ", currentTime.minute)
print("Second : ", currentTime.second)

formatted_time = currentTime.strftime("%d-%m-%Y %H %M %S")
print("Formatted date and time : ", formatted_time)