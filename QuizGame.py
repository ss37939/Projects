gamePlay = True
while gamePlay == True:
    
    print("Welcome to my computer quiz!")
    score = 0

    #question1
    answer = input("What does CPU stand for? ")
    if answer.lower() == "central processing unit":
        print("Correct")
        score += 1
    else:
        print("Incorrect")

    #question2
    answer = input("What does GPU stand for? ")
    if answer.lower() == "graphics processing unit":
        print("Correct")
        score += 1
    else:
        print("Incorrect")

    #question3
    answer = input("What does RAM stand for? ")
    if answer.lower() == "random access memory":
        print("Correct")
        score += 1
    else:
        print("Incorrect")

    #question4
    answer = input("What does PSU stand for? ")
    if answer.lower() == "power supply unit":
        print("Correct")
        score += 1
    else:
        print("Incorrect")

    #question5
    answer = input("Which component of a computer is responsible for storing data permanently? ")
    if answer.lower() == "hard drive":
        print("Correct")
        score += 2
    else:
        print("Incorrect")

    #question6
    answer = input("What is the function of a firewall in a computer? ")
    if answer.lower() == "to block unauthorized access":
        print("Correct")
        score += 2
    else:
        print("Incorrect")

    #question7
    answer = input("What is the purpose of a firewall? ")
    if answer.lower() == "to block unwanted traffic":
        print("Correct")
        score += 2
    else:
        print("Incorrect")

    print("You got ", (score), " points!")
    print("You scored ", ((score / 7) * 100), "%.")


    play = input("Would you like to play again? ")
    if play.lower() != "yes":
        quit()
    
    print("Okay! Let's Play Then")
   
