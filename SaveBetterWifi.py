import subprocess
from datetime import datetime
import threading

wp = open('wifipass.txt', 'a+')
a = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="ignore").split('\n')
a = [i.split(":")[1][1:-1] for i in a if "All User Profile" in i]
ti1 = datetime.now()
# wp.write("{:<30} | {:<}".format("Wifi Name", "Password\n"))
# wp.write("--------------------------------------------\n")
print("{:<30} | {:<}".format("Wifi Name", "Password\n"))
print("--------------------------------------------\n")
for i in a:
    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="ignore").split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            # wp.write("{:<30}|  {:<}\n".format(i, results[0]))
            t1 = threading.Thread(target=print("{:<30}|  {:<}".format(i, results[0])))
            t1.start()
            t1.join()
        except IndexError:
            # wp.write("{:<30}|  {:<}\n".format(i, ""))
            t2 = threading.Thread(target=print("{:<30}|  {:<}".format(i, "")))
            t2.start()
            t2.join()
    except subprocess.CalledProcessError:
        # wp.write("{:<30}|  {:<}".format(i, "ENCODING ERROR\n"))
        t3 = threading.Thread(target=print("{:<30}|  {:<}".format(i, "ENCODING ERROR\n")))
        t3.start()
        t3.join
ti2 = datetime.now()
total = ti2 -ti1
print("Time taken to Extract Information: ", total)
# wp.write("\n")
# wp.write("="*51)
# wp.write("\nTime Taken To Extract Information: ")
# wp.write(str(total))
# wp.write("\n")
# wp.write("="*51)
# wp.write("\n")
# wp.write("\n")