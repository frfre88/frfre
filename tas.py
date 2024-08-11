import random

a = "y"

while a == "y":

    num = random.randint(1, 6)


    if (num == 1):
        print("[     ]")
        print("[  0  ]")
        print("[     ]")

    if (num == 2):
        print("[  0  ]")
        print("[     ]")
        print("[  0  ]")

    if (num == 3):
        print("[  0  ]")
        print("[  0  ]")
        print("[  0  ]")

    if (num == 4):
        print("[0   0]")
        print("[     ]")
        print("[0   0]")

    if (num == 5):
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")

    if (num == 6):
        print("[0   0]")
        print("[0   0]")
        print("[0   0]")

    print("\n")

    a = input("Press Y to continue and Q to q to quit: ")
    
    if (a == "q"): break
a.mainloop()