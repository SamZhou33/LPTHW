from sys import exit
from sys import argv
from random import randint
import time

class Tool(object):

    def __init__(self):
        tool_open = open ("tool.txt")
        self.tool = tool_open.read()

    def readtools(self):
        tools = {}
        tool_cache = self.tool.split()
        count = 1
        while count < 4:
            tools[count] = tool_cache[count-1]
            count += 1
        return tools

class Scene(object):

    def enter (self):
        pass
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('succeed')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Succeed(Scene):

    def enter(self):
        print "\n[Congratulation! You are more close to the truth now!]"
        print "To be continued..."
        return 'succeed'

class Dead(Scene):

    def enter(self):
        print """
        [BREAKING NEWS: "After tense investigation and tracing,
        the local police locked %s who was linked to a murder case,
        and finally %s and a comrade were shot down because of resistance...]
        """ % (name, name)
        exit(1)

class Arrest(Scene):

    def enter(self):
        print """
        [BREAKING NEWS: "After tense investigation and tracing,
        the local police arrested %s who was linked to a murder case...]
        """ % name
        exit(1)

class ParentsHome(Scene):

    def enter(self):
        print """
Now you are at your parents' home.
They seems really glad to see you.
And you tell them the whole incident.
Your dad suggests:

"Well, my kid. That's not your problem.
Maybe we need to trust police, they won't treat unjustly."

Would you accept his suggestion?
"""
        choice = raw_input("> ")
        while choice != 'yes' and choice != 'no' and choice != 'Let me think':
            print "\nYou have to make a clear decision."
            choice = raw_input("> ")

        if choice == 'yes':
            print "\nI agree with you, I hate the feeling of escaping."
            print "Let's go to the police."
            a = 0
            while a < 5:
                print "."
                time.sleep(0.3)
                a += 1
            print "...No! You can't arrest me! I'm innocent!!!"
            return 'arrest'
        elif choice == 'no':
            print "\nNo, papa, the police has treated me as a murderer."
            print "I have to find out the truth to prove my innocence."
            return 'parents_home2'
        elif choice == 'Let me think':
            print "\nIt's really hard to decide, papa. I don't want to escape anymore, either."
            print "Oh Jesus... Maybe God will tell me what to do."
            print "\nYou take out a coin. What would you like to choose?"
            print "The side to keep escaping is side 1 or side 2?"

            choice = int(raw_input("> "))
            random_side = randint(1,2)
            if choice == random_side:
                print "\nThe front side is side %s" % random_side
                print "\nWell, God says I have to keep escaping and find out the truth."
                return 'parents_home2'
            else:
                print "\nThe front side is side %s" % random_side
                print "\nWell, God says I can't keep this condition."
                print "Let's go to the police."
                a = 0
                while a < 5:
                    print "."
                    time.sleep(0.3)
                    a += 1
                print "...No! You can't arrest me! I'm innocent!!!"
                return 'arrest'

class ParentsHome2(Scene):

    def enter(self):
        print """
You seems have already decided, so dad dosen't say more.
At this time, your mum said:

"%s, alright, but you have to plan for your next step."

Have you already got any plans?
        """ % name
        choice = raw_input("> ")

        if choice == 'yes':
            print "\nSo what's your plan?"
            plan = raw_input("> ")
            while 'office' not in plan and 'jail' not in plan:
                print "\nNo, there's no possiblity. I have to think of something available."
                plan = raw_input("> ")

            if 'office' in plan:
                print "\nMummy, I think the truth must be hidden in the police office."
                print "I decided to dive into there to find out it."
                return 'police_office'
            elif 'jail' in plan:
                print "\nMummy, I think the truth must be hidden in the jail."
                print "I decided to dive into there to find out it."
                return 'jail'
            else:
                pass
        else:
            print "\nMummy provides some suggestions for you."
            print "What would you like to choose?"
            print "Go to the police office, Dive into the jail or Hide in parents home?\n"
            nextstep = raw_input("> ")
            if 'office' in nextstep:
                print "\nMummy, I think the truth must be hidden in the police office."
                print "I decided to dive into there to find out it."
                return 'police_office'
            elif  'jail' in plan:
                print "\nMummy, I think the truth must be hidden in the jail."
                print "I decided to dive into there to find out it."
                return 'jail'
            else:
                print "\nWell, mummy, papa, I think it would be better to hide in your house"
                print "until the incident cool down and then we would make further plan."
                k = 0
                while k < 10:
                    print "."
                    time.sleep(0.3)
                print "One hours later, the police knock on the door."
                print "They search the house and take you away."
                return 'arrest'

class Jail(Scene):

    def enter(self):
        print """
You come to the jail behind the police office.
Here is well protected.
You can only go through the gate.

Have you prepared to go into it?
        """
        choice = raw_input("> ")
        if 'yes' in choice:
            print "\nYou walk to the gate as a common person."
            print "The soldier stops you and ask for the passsport."
            for i in range(0,4):
                print "."
                time.sleep(0.5)
            if PASSPORT == True:
                print "\nGood job, the passport you got from the chief works!"
                print "Then you walk into the jail..."
                return 'succeed'
            else:
                print "\nOh God! You don't have the passport."
                print "You are arrested!"
                return 'arrest'
        else:
            print "\nWell, maybe it would be better to go the police office first."
            return 'police_office'

class PoliceOffice(Scene):

    def enter(self):
        print """
You change clothes and dress up as a white collar
and go to the central police office,
pretending to deal with some business.

You are now sitting in the lobby of the reception office.
There are some police surrounding, they might notice
if there is some abnormal noise.

You have two choices:
ask someone to guide you to the chief,
dive into the chief's office quietly.

Which one would you choose?
"""
        choice = raw_input("> ")

        if 'guide' in choice:
            print "\n-Madam, would you please guide me to the chief's office?"
            print "I have an appointment with him. I'll be late now, but I can't find the place."
            print "-Sure, my pleasure, this way please."
            print "\nYou go after the policewoman, and she led you to a room."
            for i in range(0,5):
                print "."
                time.sleep(0.5)
            print "-Please sit here and wait for a while, chief will come soon."
            print "-OK, thank you."
            print "\nAt that moment, you find the policewoman's sight seems not very natural."
            print "Do you think you have to do something?"
            print "yes, she seems to recogonize me. I have to leave here."
            print "or"
            print "no, that's just suspiciousness, my disguise is perfect."
            do = raw_input("> ")
            if 'yes' in do:
                print "\nYou don't feel relieved, so you leave the room right after the policewoman."
                print "You decide to leave the police office, but at that moment"
                print "you see the chief's office, so would you like to go there?"
                print "yes, why not?"
                print "or"
                print "no, they recogonize me, I have to leave here immediately."
                leave = raw_input("> ")
                if 'no' in leave:
                    print "\nYou run outside quickly. But when you reach the gate,"
                    print "you find you are pointed by 5 guns. You tried to run,"
                    print "however, finally, the guns fire!"
                    return 'dead'
                else:
                    print "\nYou see it's dark inside, seems no one. You go inside."
                    print "Suddenly, the light's on, you see many police point the gun at you."
                    print "They have already prepared a trap!"
                    return 'arrest'
            else:
                print "\nYou sit in the room, and wait for chief coming."
                print "But 2 minutes later, police come in with guns. "
                print "The policewoman recogonized you!"
                return 'arrest'
        else:
            print "\nYou go upstairs and find chief's room easily."
            print "It's dark inside, seems no one. So you go into the room silently."
            print "The important files must be stored in drawers, you think."
            print "You try to open them. Nothing valuable in unlocked ones."
            print "Then it must be in the locked one."
            for i in range(0,3):
                print "."
                time.sleep(0.3)
            print "Yes! You have some tools!"
            tools = Tool().readtools()
            print tools
            print "Which one do you want to use to break the lock?"
            lock = raw_input("> ")
            while 'gloves' in lock or '3' in lock:
                print "\nIt seems not work. Try another one."
                lock = raw_input("> ")
            if 'hammer' in lock or '1' in lock:
                print "\nYou use hammer to break the lock."
                print "However, unfortunately, it's too loud and lead to police!"
                return 'arrest'
            elif 'screwdriver' in lock or '2' in lock:
                print "\nYou use screwdriver to easily break the lock."
                print "There are some files, with your name!"
                print "It shows there is a key person, but he is in the jail."
                for m in range(0,5):
                    print "."
                    time.sleep(0.3)
                print "Wait! This is... maybe the passport for the jail!"
                print "\nYou take the passport and go to the jail immediately."
                global PASSPORT
                PASSPORT = True
                return 'jail'
            else:
                print "You don't have this tool!"
                print "Someone comes! You're discovered!"
                return 'arrest'



class Map(object):

    scenes = {
    'parents_home': ParentsHome(),
    'parents_home2': ParentsHome2(),
    'police_office': PoliceOffice(),
    'jail':Jail(),
    'dead': Dead(),
    'succeed': Succeed(),
    'arrest': Arrest()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


script, name = argv
PASSPORT = False

print """
Welcome back to 'FUGITIVE' chapter two...
"""
time.sleep(0.5)

first_scene =  Map('parents_home')
game = Engine(first_scene)
game.play()
