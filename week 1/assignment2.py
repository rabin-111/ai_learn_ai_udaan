# while loop 
# while loop is the looping statement that repeats until the condition in it is true.
#and condition is check in every iteration
#continue to skip one iteration and break to skip the loop

#while condition: 
# statement
##i=1
#while i<3 : 
  # print(i)
   #i=i+1
   # here there is the pre condition ie the value of i which is checked by while statement every time ie while i<3 when it is true it runs the statement inside it but if not true then we just donot execute the statement inside it 
   #i is incremented by 1 every time until true 

# reallife example where while loop is used ? 
# 1.password checker 
#password=""
#while password !=123:
 #  password =int(input("enter the correct password"))
#print("login successful")

#2.in game
choice =""
while choice!= "4":
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice =input("enter the choice")

3.
life =100
while life>0:
  damage = int(input("enter damage "))
  life = life - damage

print("you are dead!")
