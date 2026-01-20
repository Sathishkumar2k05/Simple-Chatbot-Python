def ChatBox(user):

    if user == "HI" or user == "HELLO":

        print("Hey there! How can i help you.")

    elif user == "HOW ARE YOU":

        print("I'm fine what about you?")

    elif user == "WHAT IS YOUR NAME":

        print("I am a basic python chatbox.")

    elif user == "BYE":

        print("Bye! Have a nice day.")

    else:

        print("Sorry, I don't understand.")

while True:

    print("exit enter 1")

    print()

    inp = input("start : ")

    user = inp.upper()

    if user == "1":

        print("Exiting...")

        break

    elif not user:

        print("start chat.")

    else:

        ChatBox(user)