# Complete this program to classify people by age
age = int(input("Enter age: "))
if age <= 12:
    print("You are a Child")
elif age <= 19:
    print("you are a Teenager")
elif age <=59 :
    print("you are an Adult")
else:
    print("you are a senior")


# Add your if-elif-else statements here
# 0-12: Child
@@ -8,6 +17,17 @@
# 60+: Senior

# Your code here:
age = int(input("Enter age: "))

if age <= 12:
    print("You are a Child")
elif age <= 19:
    print("you are a Teenager")
elif age <=59 :
    print("you are an Adult")
else:
    print("you are a senior")




@@ -28,6 +48,15 @@

        # Complete the menu logic here
        # Your code here:
        
        if choice == "4" :
            break
        elif choice == "1":
            print("Balance: ", balance, "บาท")              
        elif choice == "2":
            x = input("ถอนเท่าไหร่???")
            balance = balace - amount
        elif choice == "3":   
            amount = float(input("ฝากเท่าไหร่???"))
            balance = balance + amount
else:
    print("Invalid PIN")