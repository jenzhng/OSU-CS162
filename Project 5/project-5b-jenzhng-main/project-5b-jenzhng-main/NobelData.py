
# Author: Jenny Zhong
# GitHub username: jenzhng
# Date: 2/8/2023
# Description: Class named NobelData that reads a JSON file containing data on Nobel Prizes
#              and allows user to search that data.

import json

class NobelData:
    """
    Class named NobelData that reads a JSON file containing data on Nobel Prizes
    and allows user to search that data.
    """
    def __init__(self, filename='nobels.json', data_dict=None):
        if data_dict is None:
            data_dict = {}
        else:
            self._data_dict = data_dict
        self._filename = filename
        self._data_dict = data_dict
        with open(filename, 'r') as infile:
            self._data_dict = json.load(infile)

    def get_data_dict(self):
        """
        Returns data_dict
        :return:
        """
        return self._data_dict
    def search_nobel(self, year, category):
        """
        Method search_nobel that takes parameters year and category and
        searches data_dict
        :return:
        """
        winner_list = []
        i = 0
        for key in self._data_dict['prizes']:
            if key['year'] == year and key['category'] == category:
                while i < len(key['laureates']):
                    winner_list.append(key['laureates'][i]['surname'])
                    i += 1

        winner_list.sort()
        return winner_list




def main():
    #filename = 'nobels.json'
    print(NobelData().search_nobel("2001", "economics"))
if __name__ == '__main__':
    main()
