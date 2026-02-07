due_tomorrow = False
motivated = True ## fixed naming
understand_material = True
have_time = True
tired = True

mentally_ready = motivated and understand_material and not tired
good_timing = have_time or due_tomorrow

start_assignment = mentally_ready or good_timing

print("mentally_ready:", mentally_ready)
print("good_timing:", good_timing)
print("start_assignment:", start_assignment)

number = input("enter a number greater than 0: ")
intNumber = int(number)

if intNumber > 0:
    total = 100 / intNumber
else:
    print("user ID:10T Error") # that was funny