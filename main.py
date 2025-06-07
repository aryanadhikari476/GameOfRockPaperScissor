import random
choices = ["r", "p", "s"]
image = {"r": "🪨", "p": "📄", "s": "✂️"}

while True:
    try:
        ch = input("Do you want to play rock-paper-scissor(y/n): ").lower()
        if ch != "y" and ch != "n":
            print("Please enter 'y' or 'n'")
            continue
        if ch == "n":
            print("Thanks for playing!")
            break
            
        user = input("Enter rock, paper or scissor(r/p/s): ").lower()
        if user not in choices:
            print("Invalid choice! Please enter r, p, or s")
            continue
            
        computer = random.choice(choices)
        
        print(f"\nYou chose: {image[user]}")
        print(f"Computer chose: {image[computer]}")
        
        # Determine winner
        if user == computer:
            print("It's a tie! 🤝")
        elif (user == "r" and computer == "s") or \
             (user == "p" and computer == "r") or \
             (user == "s" and computer == "p"):
            print("You win! 🎉")
        else:
            print("Computer wins! 💻")
            
        print("\n" + "="*30 + "\n")
        
    except Exception as e:
        print("An error occurred:", str(e))
        print("Please try again!")
