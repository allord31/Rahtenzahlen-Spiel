import random
number = random.randrange(0,100)
raten = int(input("geben Sie eine Nummer Zwischen 0 und 100 ein: "))

while raten != number:
    if     raten  <0 or raten >=101  :
        raten = int(input("Die eingegebene Nummer ist entwieder großer als 100 oder kleiner als 0 "
                          "\n bitte versuchen Sie eine Nummer Zwischen 1 bis 100 einzugeben  "))
    elif  raten > number:
        print("geben Sie eine kleinere Nummer \n")
        raten= int (input("- versuchen Sie noch ein Mal : "))
    else:
        print("geben Sie größere Nummer,und versuch noch ein Mal\n")
        raten =int (input("- versuchen Sie richtig zu Raten : "))

print("Glückwünsch !! Sie haben gewonnen .")

