import subprocess
from datetime import datetime

meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])
data = meta_data.decode('utf-8', errors = "blackslashreplace")
data = data.split('\n')
profiles = []
dwfp = open('wifi.txt', 'a+')
for i in data:
    if "All User Profile" in i:
        i = i.split(":")
        i = i[1]
        i = i[1:-1]
        profiles.append(i)
print("{:<30} | {:<}".format("Wifi Name", "Password"))
print("--------------------------------------------")
t1 = datetime.now()
dwfp.write("{:<30} | {:<}".format("Wifi Name", "Password\n"))
dwfp.write("--------------------------------------------\n")

for i in profiles:
    try:
        results = subprocess.check_output(['netsh','wlan','show','profile',i,'key=clear']).decode('UTF-8', errors = "blackslashreplace").split('\n')
        results = [b.split(':') [1] [1:-1] for b in results if "Key Content" in b]
        try:
            print('{:<30} | {:<}'.format(i,results[0]))            
            dwfp.write('{:<30} | {:<}\n'.format(i,results[0]))
        except IndexError:
            print("{:<30} | {:<}".format(i, ""))
    except subprocess.CalledProcessError:
        print("Decoding Error Occured!!!")
        dwfp.write("Decoding Error Occured!!!\n")
t2 = datetime.now()
total = t2 -t1
print()
print("Time taken to Extract Information: ", total)
dwfp.write("\n")
dwfp.write("="*44)
dwfp.write("\nTime Taken To Extract Information: ")
dwfp.write(str(total))
dwfp.write("\n")
dwfp.write("="*44)
dwfp.write("\n")
dwfp.write("\n")
print()