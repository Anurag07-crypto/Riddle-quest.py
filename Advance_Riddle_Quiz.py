import pandas as pd

print("Welcome To The Riddle Quiz Game!")
user_name = input("Enter your username: ")
score = 0

def level_1():
    global score
    print(f"Let's start, {user_name} 🧠")
    print("Q1: What has to be broken before you can use it?")
    ans = input("Answer: ")
    if ans.lower() == "egg":
        score += 1

    print("Q2: I’m tall when I’m young, and I’m short when I’m old. What am I?")
    ans = input("Answer: ")
    if ans.lower() == "candle":
        score += 1

    print("Q3: What is always in front of you but can’t be seen?")
    ans = input("Answer: ")
    if ans.lower() == "future":
        score += 1

def level_2():
    global score
    print("Q1: What gets bigger when more is taken away?")
    ans = input("Answer: ")
    if ans.lower() == "hole":
        score += 1

    print("Q2: What invention lets you look right through a wall?")
    ans = input("Answer: ")
    if ans.lower() == "window":
        score += 1

    print("Q3: If you’ve got me, you want to share me; if you share me, you haven’t kept me. What am I?")
    ans = input("Answer: ")
    if ans.lower() == "secret":
        score += 1

def level_3():
    global score
    print("Q1: What can you catch, but not throw?")
    ans = input("Answer: ")
    if ans.lower() == "cold":
        score += 1

    print("Q2: I am a word of letters three; add two and fewer there will be. What word am I?")
    ans = input("Answer: ")
    if ans.lower() == "few":
        score += 1

    print("Q3: What is so fragile that saying its name breaks it?")
    ans = input("Answer: ")
    if ans.lower() == "silence":
        score += 1

def start_game():
    print("Menu:\nStart -> Type 's' or 'S'\nExit -> Type anything else")
    choice = input("Enter your choice: ")

    if choice.lower() == "s":
        print("Level 1 (Unlocked)\nLevel 2 - 🔒\nLevel 3 - 🔒")
        try:
            level = int(input("Choose level (1, 2, or 3): "))
            if level == 1:
                level_1()
                print("✅ Level 1 completed!")
                print("Unlocking Level 2...\n")
                level_2()
                print("✅ Level 2 completed!")
                print("Unlocking Level 3...\n")
                level_3()
                print("✅ Game Completed!")

                # Final results
                results = pd.DataFrame({"Player": [user_name], "Score": [score]})
                results.to_csv("The_Scorecard.xlsx", index=False)
                print("\n🎉 Final Scoreboard 🎉")
                print(results)
                

                answers = pd.DataFrame({
                    "Level_1": ["Egg", "Candle", "Future"],
                    "Level_2": ["Hole", "Window", "Secret"],
                    "Level_3": ["Cold", "Few", "Silence"]
                })

                print("\n✅ Correct Answers:")
                print(answers)
                print("📁 Scorecard saved as 'The_Scorecard.xlsx'")
                
            else:
                print("Only Level 1 is unlocked. Try again 😅")

        except ValueError:
            print("Please enter a valid number (1, 2, or 3) 😵")
    else:
        print("Bye bye 👋")

start_game()
replay = input("Wanna play again? (y/n): ")
if replay.lower() == 'y':
    start_game()


    

        
