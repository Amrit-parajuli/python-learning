command=""
started=False
while True:
    command=(input("> ")).lower()
    if command=="start":
        if started:
            print('already started')
        else:
            started=True
            print("car started")
        
    elif command=="stop":
        if not started:
            print(" it already stopped")
        else:
            started=False
            print("car stooped")
    elif command=="help":
        print("""
start-to star"t the car
stop-to stop the car
quit-to get out this game MF""")
    elif command=="quit":
        break
    else:
        print("I don't understood")

