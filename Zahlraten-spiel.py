import random
number = random.randrange(1,100)
raten = int(input("geben Sie ein Nummer Zwichen 1,100 ein:  "))
while raten != number:
    if raten > number:
        print("geben Sie eine kleine Nummer \n")
        raten= int (input("- versuchen Sie noch einmal : "))
    else:
        print("geben Sie größe Nummer,und versuch noch ein mal\n")
        raten =int (input("- versuchen Sie richtig zu Raten : "))

print("Glückwünsch !! Sie haben gewonnen .")
