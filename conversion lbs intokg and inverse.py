w=int(input('enter a weight: '))
ch=(input('enter (l) or (k): '))


if ch.upper()=="L":
    converted=w * 0.45
    print(f"wight in {converted}kg")
else:
    converted=w / 0.45
    print(f"weight is {converted}lbs")

