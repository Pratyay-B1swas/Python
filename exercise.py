import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
hour = int(time.strftime('%H'))
if hour <= 4 and hour < 12:
    print("Good Morning")
elif(hour >= 12 and hour < 15):
        print("Good Noon")
elif hour >= 15 and hour < 17:
        print("Good Afternoon")
elif hour >= 17 and hour < 19:
          print("Good Evening")
else:
           print("Good Night")

