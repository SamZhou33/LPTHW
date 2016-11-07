from sys import argv
from sys import exit
import time
script, name = argv
tools = []


def start():
    print """
Hey %s! I have a bad news for you. You are now wanted by police.
I don't know what you did, but I trust you.
The police will come very soon.
You have to escape to a safe place as soon as possible,
and then you will have chance to find out the truth.
I can offer you some help. So do you trust me?
""" % name
    choice = raw_input("> ")

    if "yes" in choice:
        escape()
    else:
        wait()


def shot(why):
    print why
    print """
    [BREAKING NEWS: "After tense investigation and tracing,
    the local police locked %s who was linked to a murder case,
    and finally %s and a comrade were shot down because of resistance...]
    """ % (name, name)
    exit(0)

def dead(why):
    print why
    print """
    [BREAKING NEWS: "After tense investigation and tracing,
    the local police locked %s who was linked to a murder case,
    but when police reached %s's home, %s was found already dead...]
    """ % (name, name, name)
    exit(0)

def arrest(why):
    print why
    print """
    [BREAKING NEWS: "After tense investigation and tracing,
    the local police arrested %s who was linked to a murder case...]
    """ % name
    exit(0)

def end():
    print """
Thank god. We're safe now, your parents will offer you more help.

    [To be continued...]
    """
    exit(0)

def wait():
    print "\nWell, good luck boy."
    time.sleep(2)
    print "\n[10min later] The police came! You should do something! Would you rush out?\n"
    choice = raw_input("> ")

    if "yes" in choice:
        print "\nAll right, let's go! God will bless us."
        for i in range(0,6):
            print "."
            time.sleep(0.5)
        shot("Oh fxxk! They pull the trigger!!!...")
    else:
        arrest("\nAh! It's too late, you lose the chance to the freedom!")


def escape():
    print "\nThanks for trust. Now let's decide the direction."
    print "Through the gate, the roof or the backyard?\n"
    choice = raw_input('> ')

    if choice == "gate":
        gate()
    elif choice == "roof":
        roof()
    else:
        backyard()

def gate():
    print "\nOh Jesus! Someone change the password of the lock!"
    print "We only have 1 minute to figure it out!"

    global tools
    if "hammer" in tools:
        print """
Well, don't worry. We have hammer. Destroy the lock directly!
        """
        out()
    else:
        print """
    [FIGURE IT OUT]
    The password is a 8-digit number.
    On odd digits are not odd numbers.
    Every odd-digit number is different,
    and they are in ascending sort.
    The first digit is bigger than the second one.
    The first three even-digit numbers could compose a multiple of both 5 and 7.
    The last three even-digit numbers could compose a multiple of 17.
    The last number is not even.
        """
        lock_count = 0
        while lock_count <= 60:
            time.sleep(1)
            lock_count += 10

        print "Time's over, your answer is?"
        password = raw_input ("> ")

        if password == "21406581":
            print "\nGood job man! It's correct."
            gate_out()
        else:
            print "\nAh damn it's wrong! Try again, but it might be our last chance!"
            password_again = raw_input ("> ")
            if password_again == "21406581":
                print "\nGood job man! We did it! Let's move."
                out()
            else:
                arrest("\nStill wrong... Oh no, police are coming!")

def roof():
    print """
Well, it's too obvious if we keep staying on the roof.
We have to have find a way to leave here.
How about jump to that lower house, or climb down?
"""
    choice = raw_input("> ")

    if "jump" in choice:
        print "\nOK, now 1, 2, 3 jump!"
        for i in range(0,3):
            print "."
            time.sleep(0.5)
        dead("Bastard! It's too far! AHHHHHHHH!!!!")
    else:
        print "\nSo we are now back to the backyard"
        backyard()

def backyard():
    print """
Fxxk, how can you make the yard so messy?
But maybe these stuff would help us.
Wow, hammer, screwdriver, electric saw, weeder, ladder and gloves...
Let's choose three tools to help us.
"""
    global tool1, tool2, tool3
    tool1 = raw_input("Tool1 > ")
    tool2 = raw_input("Tool2 > ")
    tool3 = raw_input("Tool3 > ")
    global tools
    tools = [tool1, tool2, tool3]

    print """
Great, now we have some tools. Let's get out,
Shall we climb over the wall or go through the gate?
"""
    choice = raw_input("> ")

    if "wall" in choice:
        wall()
    else:
        gate()

def wall():
    if "ladder" in tools:
        print "\nWell, we have ladder, it will help us."
        for i in range(0,6):
            print "."
            time.sleep(0.5)
        wall_out()
    else:
        print """
I think we have to use ladder to climb over the wall.
Shall we change one of our tools?
    """
        choice = raw_input("> ")
        if "yes" in choice:
            print "\nSo which one would you replace? %s, %s, or %s?\n" % (tool1, tool2, tool3)
            tool_replace = raw_input("> ")
            j = 0
            while j < 3:
                if tool_replace == tools[j]:
                    tools[j] = "ladder"
                    j += 1
                else:
                    j += 1
            wall()
        else:
            print "\nAlright. So let's go back to the gate."
            gate()

def out():
    print """
Great, we finally come out.
Now where are you going? How about go to my place?
"""
    choice = raw_input("> ")

    if "yes" in choice:
        for i in range(0,6):
            print "."
            time.sleep(0.5)
        print "Oh no! Police! How do they know I'm together with you!"
        print "Shall we run away?\n"
        sub_choice = raw_input("> ")
        if "yes" in sub_choice:
            shot("\nFxxk! They pull the trigger!...")
        else:
            arrest("\nToo late to run...")
    else:
        out2()

def wall_out():
    tools.remove("ladder")
    print "Good job. Now we are out."
    print """
See? There's a strange person. What's he doing?
Shall we go and ask?
"""
    choice = raw_input("> ")
    if "yes" in choice:
        print "\nHey man, what's up?"
        for i in range(0,3):
            print "."
            time.sleep(0.5)
        arrest("Damn! YOU ARE......POLICE!!!")
    else:
        print "\nThat's wise. Let's leave here."
        out()

def out2():
    print """
Well, now what's your plan?
Go to your parents' place or your another house?
"""
    choice = raw_input("> ")
    if "parent" in choice:
        end()
    else:
        print "\nThat it is. [OPEN THE DOOR]..."
        for i in range(0,3):
            print "."
            time.sleep(0.5)
        arrest("\nHow do police get in here?!...")


print """
    %s, welcome to 'FUGITIVE' chapter one
""" % name
begin = raw_input("press RETURN to begin the game")
start()
