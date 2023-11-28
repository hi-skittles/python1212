import csv
import os.path
import random
from colours import colours as col
from typing import Dict


# realistically these classes would not be in the same file.
class DataStruct:
    """
    Represents a single Coromon data entry.
    TODO: use a better method of docstrings.
    Example: variable (type): description

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


def read_data(csv_file: str) -> list:
    """
    Reads the Coromon data from the CSV file and returns a list of DataStruct objects.
    :return: A list of DataStruct objects.
    """
    # prelim checks and exceptions
    if not os.path.exists(csv_file):
        raise FileNotFoundError(f"File {csv_file} does not exist.")

    if os.path.getsize(csv_file) == 0:
        raise ValueError(f"File {csv_file} is empty.")

    # create an empty list for data storage
    data_struct_list: list = []
    try:
        # read Coromon data from the CSV file
        with open(csv_file, "r") as file:
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
    except IndexError:
        raise IndexError("IndexError: list index out of range. Check your CSV file for errors.")
    except IOError:
        raise IOError(f"IOError: an error occurred while reading {csv_file}.")

    return data_struct_list


def get_total_count(data_struct_list: list) -> int:
    """
    Gets the total count of Coromon in the dataset.
    :param data_struct_list: A list of DataStruct objects.
    :return: The total count of Coromon in the dataset.
    """
    if not isinstance(data_struct_list, list):
        raise TypeError("TypeError: data_struct_list must be a list.")

    for item in data_struct_list:
        if not isinstance(item, DataStruct):
            raise TypeError("TypeError: data_struct_list must be a list of DataStruct objects.")
    return data_struct_list.__len__()


def get_random_coromon(data_struct_list: list) -> list:
    """
    Gets a random Coromon from the dataset.
    :param data_struct_list: A list of DataStruct objects.
    :return: A random Coromon from the dataset.
    """
    if len(data_struct_list) == 0:
        raise ValueError("ValueError: data_struct_list must not be empty.")

    # you may also wish to use random.randint() to get a random index and then use that to get a random Coromon
    return [attribute for attribute in random.choice(data_struct_list).__dict__.values()]


def types_of_coromon(data_struct_list_type: list) -> set:
    """
    Gets the types of Coromon in the dataset.
    :param data_struct_list_type: A list of DataStruct objects.
    :return: The types of Coromon in the dataset.
    """
    if len(data_struct_list_type) == 0:
        raise ValueError("ValueError: data_struct_list must not be empty.")

    # use a set comprehension to get the types of Coromon in the dataset
    return {character_type.chartype for character_type in data_struct_list_type}


def averages_(types: set, data_struct_list: list) -> list:
    if len(types) == 0 or len(data_struct_list) == 0:
        raise ValueError("ValueError: inputs must be filled first.")
    # init list
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
        print(f"Average Attack for {col.OKGREEN}{pulled_type}{col.ENDC} Coromon: {col.OKBLUE}{average_attack}"
              f"{col.ENDC}.")
        print(f"Average Special Attack for {col.OKGREEN}{pulled_type}{col.ENDC} Coromon: {col.OKBLUE}"
              f"{average_sp_attack}{col.ENDC}.")
        print(f"Average Defense for {col.OKGREEN}{pulled_type}{col.ENDC} Coromon: {col.OKBLUE}{average_defence}"
              f"{col.ENDC}.")
        print(f"Average Special Defense for {col.OKGREEN}{pulled_type}{col.ENDC} Coromon: {col.OKBLUE}"
              f"{average_sp_defence}{col.ENDC}.")
        print(f"Average Speed for {col.OKGREEN}{pulled_type}{col.ENDC} Coromon: {col.OKBLUE}{average_speed}{col.ENDC}.")

        # create a new AverageDataPoints object for each type of Coromon
        average_data_points: object = AverageDataPoints(pulled_type, average_hp, average_attack, average_sp_attack,
                                                        average_defence, average_sp_defence, average_speed)
        # add the AverageDataPoints object to the list
        averages.append(average_data_points)

    return averages


# read the data from the CSV file
data_struct_list = read_data("CoromonDataset.csv")

# gather counts
count: int = get_total_count(data_struct_list)
print(f"There are {col.OKBLUE}{count}{col.ENDC} Coromon in the dataset.")

# get a random Coromon
random_coromon: str = ", ".join(get_random_coromon(data_struct_list))
print(f"Random Coromon: {col.OKBLUE}{random_coromon}{col.ENDC}.")

types = types_of_coromon(data_struct_list)
print(f"Types: {col.OKBLUE}" + ", ".join(types) + f"{col.ENDC}.")


def print_highest_lowest(averages: Dict, stat_name: str) -> None:
    highest: int = max(averages.keys())
    lowest: int = min(averages.keys())
    print(f"Highest average {stat_name}: {col.OKGREEN}{averages.get(highest)}{col.ENDC}, with {col.OKBLUE}{highest}"
          f"{col.ENDC}.")
    print(f"Lowest average {stat_name}: {col.OKGREEN}{averages.get(lowest)}{col.ENDC}, with {col.OKBLUE}{lowest}"
          f"{col.ENDC}.")


averages: list = averages_(types, data_struct_list)

print("----------")

# single dictionary for all stats
averages_all: dict = {
    "HP": {t.hp: t.ctype for t in averages},
    "Attack": {t.attack: t.ctype for t in averages},
    "Sp Attack": {t.sp_attack: t.ctype for t in averages},
    "Defence": {t.defence: t.ctype for t in averages},
    "Sp Defence": {t.sp_defence: t.ctype for t in averages},
    "Speed": {t.speed: t.ctype for t in averages},
}

# Print highest and lowest for each stat using the function
print_highest_lowest(averages_all["HP"], "HP")
print_highest_lowest(averages_all["Attack"], "Attack")
print_highest_lowest(averages_all["Sp Attack"], "Special Attack")
print_highest_lowest(averages_all["Defence"], "Defense")
print_highest_lowest(averages_all["Sp Defence"], "Special Defense")
print_highest_lowest(averages_all["Speed"], "Speed")
