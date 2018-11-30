runTimes = 0
x = 1
y = 1
while runTimes < 9:
    # l(x, y)
    # time.sleep(1)
    print("x :" + str(x))
    print("y :" + str(y))
    print("########################################" + str(runTimes))
    if y < 2:
        y = y + 1
    elif y >= 2:
        y = 1
        x = x + 1
    if x > 2:
        x = 1


    runTimes = runTimes + 1