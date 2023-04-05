
# Author: Jenny Zhong
# GitHub username: jenzhng
# Date: 2/8/2023
# Description: Class named NeighborhoodPets that has methods for adding a pet,
#              deleting a pet, searching for owner, saving data to a JSON file,
#              loading data from JSON file, and getting a set of all pet species.


import json

class NeighborhoodPets:
    """
    Class named NeighborhoodPets that has methods for adding a pet,
    deleting a pet, searching for owner, saving data to a JSON file,
    loading data from JSON file, and getting a set of all pet species
    """
    def __init__(self, filename='', pet_dict=None):
        if pet_dict is None:
            pet_dict = {}
        else:
            self._pet_dict = pet_dict
        self._filename = filename
        self._pet_dict = pet_dict
        # with open(filename, 'rb') as infile:
        #     self._pet_dict = json.load(infile)

    def get_pet_dict(self):
        """
        Returns pet_dict
        :return:
        """
        return self._pet_dict
    def add_pet(self, name, species, owner):
        """
        Method add_pet that takes parameters name, species, owner
        and adds pet to pet_dict
        :return:
        """
        if name not in self._pet_dict.keys():
            self._pet_dict[name] = {"Species":species,"Owner":owner}
        else:
            raise DuplicateNameError

    def delete_pet(self, name):
        """
        Deletes pet from pet_dict
        :param name:
        :return:
        """
        if name in self._pet_dict.keys():
            del self._pet_dict[name]

    def get_owner(self, name):
        """
        Finds owner of specific pet given name
        :param name:
        :return:
        """
        for key in self._pet_dict.keys():
            if key == name:
                return self._pet_dict[name]["Owner"]
    def save_as_json(self, filename):
        """
        Save current pet_dict as json
        :param filename:
        :return:
        """
        with open(filename, 'w') as outfile:
            json.dump(self._pet_dict, outfile)
    def read_json(self, filename):
        """
        Load specific json to pet_dict
        :param filename:
        :return:
        """
        with open(filename, 'r') as infile:
            self._pet_dict = json.load(infile)
    def get_all_species(self):
        """
        Returns all species as a set
        """
        species_list = []
        for key in self._pet_dict.keys():
            species_list.append(self._pet_dict[key]["Species"])
        species_set = set(species_list)
        return species_set
class DuplicateNameError(Exception):
    pass

def main():
    np = NeighborhoodPets()
    try:
        np.add_pet("Fluffy", "gila monster", "Oksana")
        np.add_pet("Tiny", "stegasaurus", "Rachel")
        np.add_pet("Spot", "zebra", "Farrokh")
    except DuplicateNameError:
        print('You tried to enter a pet with the same name as another pet.')
    print(np.get_pet_dict())
    np.delete_pet("Tiny")
    print(np.get_owner("Spot"))
    np.save_as_json("pets.json")
    np.read_json("other_pets.json")
    print(np.get_pet_dict())
    species_set = np.get_all_species()
    print(species_set)
    # try:
    #     np.add_pet("Fluffy", "gila monster", "Oksana")
    #     np.add_pet("Tiny", "stegasaurus", "Rachel")
    #     np.add_pet("Spot", "zebra", "Farrokh")
    # except DuplicateNameError:
    #     print('You tried to enter a pet with the same name as another pet.')
    # np.save_as_json("pets.json")
    # np.delete_pet("Tiny")
    # spot_owner = np.get_owner("Spot")
    # np.read_json("other_pets.json")  # where other_pets.json is a file it saved in some previous session
    # species_set = np.get_all_species()

if __name__ == '__main__':
    main()
