import random
def roll_dice ():
    print("DIGITAL DICE ROLLER")
    while True:
        #wait for user enter or quit
        choice=input ("PRESS ENTER  TO ROLL (OR Q TO QUIT ):").strip().upper()
        if choice=='Q':
            print ("THANK U FOR PLAYING")
            break
        # generate a randon number between 1 and 6
        roll = random.randint(1,6)
        print(f"🎆YOU GOT {roll}🎆 ")    
if __name__=="__main__":
 roll_dice ()   