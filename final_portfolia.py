import csv
import random
from colours import colours as col


class DataStruct:
    """
    Represents a single Coromon data entry.

    Attributes:
        name (str): The name of the Coromon.
        chartype (str): The type of the Coromon.
        hp (int): The HP of the Coromon.
        attack (int): The attack stat of the Coromon.
        sp_attack (int): The special attack stat of the Coromon.
        defence (int): The defense stat of the Coromon.
        sp_defence (int): The special defense stat of the Coromon.
        speed (int): The speed stat of the Coromon.
        stamina_points (int): The stamina points of the Coromon.

        CSV structure:
            0, 1, 2, 3, 4, 5, 6, 7, 8
            name, type, hp, attack, sp attack, defence, sp defence, speed, stamina points
    """

    def __init__(self, name, chartype, hp, attack, sp_attack, defence, sp_defence, speed, stamina_points):
        """
        Initializes a new DataStruct object with the given data. I'll use this for structural purposes.

        TODO: rename chartype to something better maybe?

        Args:
            name (str): The name of the Coromon.
            chartype (str): The type of the Coromon.
            hp (int): The HP of the Coromon.
            attack (int): The attack stat of the Coromon.
            sp_attack (int): The special attack stat of the Coromon.
            defence (int): The defense stat of the Coromon.
            sp_defence (int): The special defense stat of the Coromon.
            speed (int): The speed stat of the Coromon.
            stamina_points (int): The stamina points of the Coromon.
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


# create an empty list for data storage
data_struct_list = []

# read Coromon data from the CSV file
with open("CoromonDataset.csv", "r") as file:
    # use csv reader for reading
    reader = csv.reader(file)
    # we can skip the header row because it will count as an entry later on if not skipped
    next(reader)

    # iterate over each row of data in the CSV file
    for line in reader:
        # create a DataStruct object from each row of data
        data_struct = DataStruct(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8])

        # add the DataStruct object to the list
        data_struct_list.append(data_struct)

"""
Main Tasks:
    1. How many Coromons exists.
    2. Select a Coromon randomly and display its information.
    3. The different types of Coromons.
    4. For each Common type display the average value for each of its properties across all of the Coromon that belong to that type.
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
count = data_struct_list.__len__()
print(f"There are {col.OKBLUE}{count}{col.ENDC} Coromon in the dataset.")

random_coromon = [attribute for attribute in random.choice(data_struct_list).__dict__.values()]
random_coromon = ", ".join(random_coromon)
# you may also wish to use random.randint() to get a random index and then use that to get a random Coromon
print(f"Random Coromon: {col.OKBLUE}{random_coromon}{col.ENDC}.")

types = {character_type.chartype for character_type in data_struct_list}
print(f"Types: {col.OKBLUE}" + ", ".join(types) + f"{col.ENDC}.")
