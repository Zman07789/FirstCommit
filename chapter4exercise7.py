score = input("Enter Score: ")
def computegrade(score):
    sIn = float(score)
    if sIn >= 0.9 and sIn <= 1.0: 
        print("A")
    elif sIn >= 0.8 and sIn < 0.9:
        print("B")
    elif sIn >= 0.7 and sIn < 0.8:
        print("C")
    elif sIn == 0.6 and sIn < 0.7:
        print("D")
    elif sIn < 0.6:
        print("F")
    else:
        print('Bad Score')
    
computegrade(score)
