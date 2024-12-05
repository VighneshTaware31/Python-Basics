is_batsman = False
is_bowler = True
#check if batsman and bowler : "you are all rounder"
if is_batsman and is_bowler:
    print("You are a All Rounder")

elif is_batsman and not is_bowler:
    print("you are an  good Batsman")

elif is_bowler and not is_batsman:
    print("You are an good Bowler")

else:
    print("You Have To  Learn Play Cricket")

   