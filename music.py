class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds
        self.name = self  # Kyle: how can I make this be the musician's name taken from the object name?

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end=" ")
        print()


class Bassist(Musician):  # The Musician class is the parent of the Bassist class
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Bump", "Badump", "Baba"])


class Guitarist(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Duh", "DaDuh", "Blam"])

    def tune(self):
        print("Be with you in a moment")



class Drummer(Musician):
    def __init__(self):
        super().__init__(["Boom", "Chica", "Pow"])

    def count(self):
        print("1, 2, 3, 4")

    def combust(self):
        print("The drummer self combusted....Rock n Roll!")


class Band(object):
    def __init__(self):
        self.members = []

    def hire(self, member):
        self.members.append(member)
        print("The band hired a musician")

    def fire(self, member):
        self.members.remove(member)
        print("The band fired a musician")

    def play(self):
        canPlay = False
        for member in self.members:
            if isinstance(member, Drummer) == True:
                member.count()
                canPlay = True
                for member in self.members:
                    member.solo(20)
        if canPlay == False:
            print("We need to hire a drummer")


nigel = Drummer()
david = Guitarist()
derek = Bassist()
john = Drummer()
theBand = Band()
theBand.hire(nigel)
theBand.hire(david)
theBand.hire(derek)
theBand.play()
nigel.combust()
theBand.fire(nigel)
theBand.hire(john)
