menu1 = ["Siomai Rice", 35, "Water"]
menu2 = ["Sisig Rice", 50, "Coke"]
menu3 = ["Burger", 40, "Mountain Dew"]

print("Type Mone for menu #1")
print("Type Mtwo for menu #2")
print("Type Mthree for menu #3")

Mone = menu1
Mtwo = menu2
Mthree = menu3

Yes = "yes"
No = "no"

while True:
   choose = str(input("You chose:"))
   choose = str(choose)
   if choose == "Mone":
        print(menu1)
        print("Are you sure?")
        print("Yes or No?")
        sure1 = str(input())
        sure1 = str(sure1)
        if sure1 == "yes":
            print("Your order is:", menu1)
        elif sure1 == "no":
            print("Please choose again.")

   elif choose == "Mtwo":
        print(menu2)
        print("Are you sure?")
        print("Yes or No")
        sure2 = str(input())
        sure2 = str(sure2)
        if sure2 == "yes":
            print("Your order is:", menu2)
        elif sure2 == "no":
            print("Please choose again.")
  
   elif choose == "Mthree":
        print(menu3)
        print("Are you sure?")
        print("Yes or No")
        sure3 = str(input())
        sure3 = str(sure3)
        if sure3 == "yes":
            print("Your order is:", menu3)
        elif sure3 == "no":
            print("Please choose again.")
            


    