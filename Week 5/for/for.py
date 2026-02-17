import time

for j in range(3):
    time.sleep(j * j)
    password = input("Password attempt " + str(j + 1) + ": ")
    if "swordfish" == password:
        for k in range(3, 0, -1):
            print(k)
            time.sleep(1)
        print("Ignition")
        break