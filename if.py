price=1000000
goodcredit=False
if goodcredit:
    payment= 0.1*price
else:
   payment= 0.2*price
print(f"poor greedy: {payment}")