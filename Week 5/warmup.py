import sys
import time

MAX_ATTEMPTS = 3
CORRECT = "swordfish"  # this is the correct password
attempts = 0
password = ""
while (CORRECT != password) and (MAX_ATTEMPTS > attempts):
    time.sleep(attempts * attempts)
    password = input("Password to launch: ")
    attempts += 1
else:
    if MAX_ATTEMPTS == attempts:
        # raise SystemExit
        sys.exit("Lockdown initiated. Security has been notified. May God have mercy on your soul...")

i = 3
while i:
    print(str(i) + "...")
    i -= 1
    time.sleep(1)
else:
    print("Ignition")