import random
import time
import string


class Dice:
    def __init__(self, n_sides: int = 6) -> None:
        self.sides: int = n_sides
        self.faces = range(1, self.sides + 1)
        
    def roll(self) -> int:
        number: int = random.randint(1, self.sides)
        return number



def main() -> None:
    apresentation = r"""
+-----------------------------------------+
|                                         |
|                                         |
|   _____ _           ______ _            |
|  |_   _| |          |  _  (_)           |
|    | | | |__   ___  | | | |_  ___ ___   |
|    | | | '_ \ / _ \ | | | | |/ __/ _ \  |
|    | | | | | |  __/ | |/ /| | (_|  __/  |
|    \_/ |_| |_|\___| |___/ |_|\___\___|  |
|                                         |
|                                         |
+-----------------------------------------+

DO a Choice:

1 - Send a number of dice-sides
2 - Roll the Dice
3 - Bye          
"""

    
    
    while True:
        time.sleep(1)
        print(apresentation)

        try:
            choice = input("\n>>> ")

            if choice not in ("1", "2", "3"):

                while True:
                    print(apresentation)
                    choice = (input("\n>>> "))

                    if choice in ("1", "2", "3"):
                        break
            
            match int(choice):
                
                case 1:
                    print("Write number of sides for your dice\n")
                    sides = input(">>> ")

                    while sides in string.ascii_letters:
                        print("Write number of sides for your dice\n")
                        sides = input(">>> ")

                    condition = int(sides) > 0 and int(sides) % 2 == 0

                    if not condition:

                        while True:
                            print("Dices require a positive-integer for your sides\n")
                            sides = input(">>> ")
                            condition = int(sides) > 0 and int(sides) % 2 == 0

                            if condition:
                                break
                    
                    dice = Dice(int(sides))
                    print(f"You created a D{dice.sides}")

                case 2:
                    print("rolling.")
                    time.sleep(1)
                    print("rolling..")
                    time.sleep(1)
                    print("rolling...")

                    roll = dice.roll()
                    print(f"Side: {roll}.")

                case _:
                    print(r"""
   ____   __   __U _____ u        ____   __   __U _____ u  _   
U | __")u \ \ / /\| ___"|/     U | __")u \ \ / /\| ___"|/U|"|u 
 \|  _ \/  \ V /  |  _|"        \|  _ \/  \ V /  |  _|"  \| |/ 
  | |_) | U_|"|_u | |___         | |_) | U_|"|_u | |___   |_|  
  |____/    |_|   |_____| _      |____/    |_|   |_____|  (_)  
 _|| \\_.-,//|(_  <<   >>(")    _|| \\_.-,//|(_  <<   >>  |||_ 
(__) (__)\_) (__)(__) (__)\|   (__) (__)\_) (__)(__) (__)(__)_)
""")
                    break
            
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()