import random
 
while True:
   print("Roll a dice")
   dice=random.randint(1,6)
   print(dice)
   if dice==6:
      dice=random.randint(1,6)
      print(dice)
   break
   