import csv
import random

from colours import colours as col


class DataStruct:
    """
    Represents a single Coromon data entry.
    TODO: use a better method of docstrings.

    CSV structure:
        0, 1, 2, 3, 4, 5, 6, 7, 8
        name, type, hp, attack, sp attack, defence, sp defence, speed, stamina points
    """

    def __init__(self, name: str, chartype: str, hp: int, attack: int, sp_attack: int, defence: int, sp_defence: int,
                 speed: int, stamina_points: int):
        """
        Initializes a new DataStruct object with the given data. I'll use this for structural purposes, over a dict.
        TODO: rename chartype to something better maybe?

        :param name: The name of the Coromon.
        :param chartype: The type of the Coromon.
        :param hp: The HP of the Coromon.
        :param attack: The attack stat of the Coromon.
        :param sp_attack: The special attack stat of the Coromon.
        :param defence: The defense stat of the Coromon.
        :param sp_defence: The special defense stat of the Coromon.
        :param speed: The speed stat of the Coromon.
        :param stamina_points: The stamina points of the Coromon.
        """

        self.name = name
        self.chartype = chartype
        self.hp = hp
        self.attack = attack
        self.sp_attack = sp_attack
        self.defence = defence
        self.sp_defence = sp_defence
        self.speed = speed
        self.stamina_points = stamina_points


class AverageDataPoints:
    """
    Represents the average data points for a given type of Coromon. Data types are irrelevant.
    TODO: pass the name along; add in dictionary for averages below.

    Args:
        ctype: The type of the Coromon.
        hp: The HP of the Coromon.
        attack: The attack stat of the Coromon.
        sp_attack: The special attack stat of the Coromon.
        defence: The defense stat of the Coromon.
        sp_defence: The special defense stat of the Coromon.
        speed: The speed stat of the Coromon.
    """
    def __init__(self, ctype, hp, attack, sp_attack, defence, sp_defence, speed):
        """
        Initializes a new AverageDataPoints object with the given data.
        :param ctype: The type of the Coromon.
        :param hp: The HP of the Coromon.
        :param attack: The attack stat of the Coromon.
        :param sp_attack: The special attack stat of the Coromon.
        :param defence: The defense stat of the Coromon.
        :param sp_defence: The special defense stat of the Coromon.
        :param speed: The speed stat of the Coromon.
        """
        self.ctype = ctype
        self.hp = hp
        self.attack = attack
        self.sp_attack = sp_attack
        self.defence = defence
        self.sp_defence = sp_defence
        self.speed = speed


# create an empty list for data storage
data_struct_list: list = []

# read Coromon data from the CSV file
with open("CoromonDataset.csv", "r") as file:
    # use csv reader for reading
    reader = csv.reader(file)
    # we can skip the header row because it will count as an entry later on if not skipped
    next(reader)

    # iterate over each row of data in the CSV file
    for line in reader:
        # create a DataStruct object from each row of data
        data_struct: object = DataStruct(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7],
                                         line[8])

        # add the DataStruct object to the list
        data_struct_list.append(data_struct)

"""
Main Tasks:
    1. How many Coromons exists.
    2. Select a Coromon randomly and display its information.
    3. The different types of Coromons.
    4. For each Coromon type display the average value for each of its properties across all of the Coromon that belong
       to that type.
    5. The Coromon type(s) with the highest average Health Points points.
    6. The Coromon type(s) with the lowest average Health Points points.
    7. The Coromon type(s) with the highest average Attack points.
    8. The Coromon type(s) with the lowest average Attack points.
    9. The Coromon type(s) with the highest average Special Attack points.
    10. The Coromon type(s) with the lowest average Special Attack points.
    11. The Coromon type(s) with the highest average Defense points.
    12. The Coromon type(s) with the lowest average Defense points.
    13. The Coromon type(s) with the highest average Special Defense points.
    14. The Coromon type(s) with the lowest average Special Defense points.
    15. The Coromon type(s) with the highest average Speed points.
    16. The Coromon type(s) with the lowest average Speed points.
"""

count: int = data_struct_list.__len__()
print(f"There are {col.OKBLUE}{count}{col.ENDC} Coromon in the dataset.")

random_coromon: list = [attribute for attribute in random.choice(data_struct_list).__dict__.values()]
random_coromon: str = ", ".join(random_coromon)
# you may also wish to use random.randint() to get a random index and then use that to get a random Coromon
print(f"Random Coromon: {col.OKBLUE}{random_coromon}{col.ENDC}.")

types: set = {character_type.chartype for character_type in data_struct_list}
print(f"Types: {col.OKBLUE}" + ", ".join(types) + f"{col.ENDC}.")

averages: list = []
pulled_type: object
for pulled_type in types:
    """
        The way this works is I iterate through each type of character, represented in my primary for loop.
        I'm using my previous set comprehension because it doesn't have any duplicates.
        When cycling through each type, I create a new list of all the Coromon that match that type.
        When they are pulled into the list, they are pulled as DataStruct objects, so I can access their attributes.
        This could theoretically be done with a dictionary, but using objects was an opportunity to practice OOP and
            advance my skills into data structures.
        I then use a list comprehension to get the average of each attribute for each type of Coromon.
        To achieve this, I take the sum of each given attribute using comprehension, and then divide it by the length
            of the list of the type list, thus returning the average.
        We can then print each average.
    """
    # get all the Coromon of a certain type
    type_coromon: list = [coromon for coromon in data_struct_list if coromon.chartype == pulled_type]

    # get the average values for each of the properties
    average_hp: float = sum(int(coromon.hp) for coromon in type_coromon) / type_coromon.__len__()
    average_attack: float = sum(int(coromon.attack) for coromon in type_coromon) / type_coromon.__len__()
    average_sp_attack: float = sum(int(coromon.sp_attack) for coromon in type_coromon) / type_coromon.__len__()
    average_defence: float = sum(int(coromon.defence) for coromon in type_coromon) / type_coromon.__len__()
    average_sp_defence: float = sum(int(coromon.sp_defence) for coromon in type_coromon) / type_coromon.__len__()
    average_speed: float = sum(int(coromon.speed) for coromon in type_coromon) / type_coromon.__len__()

    # display the average values for each of the properties
    print(f"Average HP for {col.OKGREEN}{pulled_type}{col.ENDC} Coromon: {col.OKBLUE}{average_hp}{col.ENDC}.")
    print(f"Average Attack for {col.OKGREEN}{pulled_type}{col.ENDC} Coromon: {col.OKBLUE}{average_attack}{col.ENDC}.")
    print(f"Average Special Attack for {col.OKGREEN}{pulled_type}{col.ENDC} Coromon: {col.OKBLUE}{average_sp_attack}"
          f"{col.ENDC}.")
    print(f"Average Defense for {col.OKGREEN}{pulled_type}{col.ENDC} Coromon: {col.OKBLUE}{average_defence}{col.ENDC}.")
    print(f"Average Special Defense for {col.OKGREEN}{pulled_type}{col.ENDC} Coromon: {col.OKBLUE}{average_sp_defence}"
          f"{col.ENDC}.")
    print(f"Average Speed for {col.OKGREEN}{pulled_type}{col.ENDC} Coromon: {col.OKBLUE}{average_speed}{col.ENDC}.")

    # create a new AverageDataPoints object for each type of Coromon
    average_data_points: object = AverageDataPoints(pulled_type, average_hp, average_attack, average_sp_attack,
                                                    average_defence, average_sp_defence, average_speed)
    # add the AverageDataPoints object to the list
    averages.append(average_data_points)

averagesHP: dict = {t.hp: t.ctype for t in averages}
averagesAttack: dict = {t.attack: t.ctype for t in averages}
averagesSpAttack: dict = {t.sp_attack: t.ctype for t in averages}
averagesDefence: dict = {t.defence: t.ctype for t in averages}
averagesSpDefence: dict = {t.sp_defence: t.ctype for t in averages}
averagesSpeed: dict = {t.speed: t.ctype for t in averages}

print("----------")

# finish the last tasks
print(f"Highest average HP: {col.OKGREEN}{averagesHP.get(max(averagesHP.keys()))}{col.ENDC}, with {col.OKBLUE}"
      f"{max(averagesHP.keys())}{col.ENDC}.")
print(f"Lowest average HP: {col.OKGREEN}{averagesHP.get(min(averagesHP.keys()))}{col.ENDC}, with {col.OKBLUE}"
      f"{min(averagesHP.keys())}{col.ENDC}.")
print(f"Highest average Attack: {col.OKGREEN}{averagesAttack.get(max(averagesAttack.keys()))}{col.ENDC}, with "
      f"{col.OKBLUE}{max(averagesAttack.keys())}{col.ENDC}.")
print(f"Lowest average Attack: {col.OKGREEN}{averagesAttack.get(min(averagesAttack.keys()))}{col.ENDC}, with "
      f"{col.OKBLUE}{min(averagesAttack.keys())}{col.ENDC}.")
print(f"Highest average Special Attack: {col.OKGREEN}{averagesSpAttack.get(max(averagesSpAttack.keys()))}{col.ENDC}, "
      f"with {col.OKBLUE}{max(averagesSpAttack.keys())}{col.ENDC}.")
print(f"Lowest average Special Attack: {col.OKGREEN}{averagesSpAttack.get(min(averagesSpAttack.keys()))}{col.ENDC}, "
      f"with {col.OKBLUE}{min(averagesSpAttack.keys())}{col.ENDC}.")
print(f"Highest average Defense: {col.OKGREEN}{averagesDefence.get(max(averagesDefence.keys()))}{col.ENDC}, with "
      f"{col.OKBLUE}{max(averagesDefence.keys())}{col.ENDC}.")
print(f"Lowest average Defense: {col.OKGREEN}{averagesDefence.get(min(averagesDefence.keys()))}{col.ENDC}, with "
      f"{col.OKBLUE}{min(averagesDefence.keys())}{col.ENDC}.")
print(f"Highest average Special Defense: {col.OKGREEN}{averagesSpDefence.get(max(averagesSpDefence.keys()))}{col.ENDC}, "
      f"with {col.OKBLUE}{max(averagesSpDefence.keys())}{col.ENDC}.")
print(f"Lowest average Special Defense: {col.OKGREEN}{averagesSpDefence.get(min(averagesSpDefence.keys()))}{col.ENDC}, "
      f"with {col.OKBLUE}{min(averagesSpDefence.keys())}{col.ENDC}.")
print(f"Highest average Speed: {col.OKGREEN}{averagesSpeed.get(max(averagesSpeed.keys()))}{col.ENDC}, with "
      f"{col.OKBLUE}{max(averagesSpeed.keys())}{col.ENDC}.")
print(f"Lowest average Speed: {col.OKGREEN}{averagesSpeed.get(min(averagesSpeed.keys()))}{col.ENDC}, with "
      f"{col.OKBLUE}{min(averagesSpeed.keys())}{col.ENDC}.")
