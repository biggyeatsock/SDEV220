import calendar
import datetime
import os

# 13.1
file = open('today.txt', 'w')
file.write(str(datetime.datetime.now()))


# 13.2

with open('today.txt', 'r') as file:
    today_string = file.read()
    print(today_string)


# 13.3

today_date = datetime.datetime.strptime(today_string, '%Y-%m-%d %H:%M:%S.%f')
formatted_date = today_date.strftime('%Y-%m-%d %H:%M:%S')
print("\nFormatted Date:", formatted_date)

# 15.1
print("\n#15.1")
os.system(f'python {'15.1.py'}')