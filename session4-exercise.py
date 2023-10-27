import random
 
 
pc_number =random.randint(0,10)
n=0
while True :
 user_number= int(input("Enter num;"))  
 n+=1
 if user_number==pc_number:
  print("Dorost hads zadi :)))))) ")
  break
 if user_number < pc_number:
  print("Adade bozorgtar bezan")
 if user_number>pc_number:
  print("Adade kamtar bezan")
print("adade entekhab shode",pc_number)
print ("the number of guesses", n )