
# Author: Jenny Zhong
# GitHub username: jenzhng
# Date: 2/8/2023
# Description: Class named SatData that reads a JSON file containing data on 2010 SAT results
#              for New York City and writes the data to a text file in CSV format.


import json

class SatData:
    """
    Class named SatData that reads a JSON file containing data on 2010 SAT results
    for New York City and writes the data to a text file in CSV format.
    """
    def __init__(self, filename='sat.json', data_dict=None):
        if data_dict is None:
            data_dict = {}
        else:
            self._data_dict = data_dict
        self._filename = filename
        self._data_dict = data_dict
        with open(filename, 'rb') as infile:
            self._data_dict = json.load(infile)

    def get_data_dict(self):
        """
        Returns data_dict
        :return:
        """
        return self._data_dict
    def save_as_csv(self, dbn_list):
        """
        Method search_nobel that takes parameters dbn_list and
        searches data_dict
        :return:
        """

        all_list = []
        i = 0
        all_list.append('DBN,School Name,Number of Test Takers,Critical Reading Mean,Mathematics Mean,Writing Mean\n')
        for key in self._data_dict['data']:
            while i < len(self._data_dict['data']):
                for item in dbn_list:
                    if str(self._data_dict['data'][i][8]) == item:
                            dbn_num = self._data_dict['data'][i][8]
                            
                            if self._data_dict['data'][i][10] != '':
                                sat_1 =  self._data_dict['data'][i][10]
                            else:
                                sat_1 = ''
                            if self._data_dict['data'][i][11] != '':
                                sat_2 = self._data_dict['data'][i][11]
                            else:
                                sat_2 = ''
                            if self._data_dict['data'][i][12] != '':
                                sat_3 = self._data_dict['data'][i][12]
                            else:
                                sat_3 = ''
                            if self._data_dict['data'][i][13] != '':
                                sat_4 = self._data_dict['data'][i][13]
                            else:
                                sat_4 = ''

                            if ("," in self._data_dict['data'][i][9]) == True:
                                school_name = '"' + self._data_dict['data'][i][9] + '"'
                            else:
                                school_name = self._data_dict['data'][i][9]

                            all_list.append(dbn_num + "," +
                                            school_name + "," +
                                            sat_1 + "," +
                                            sat_2 + "," +
                                            sat_3 + "," +
                                            sat_4 + "\n")

                i += 1

        with open('output.csv', 'w') as outfile:
            for line in all_list:
                outfile.write(line)






def main():
    sd = SatData()
    dbns = ["01M292", "01M448"]
    sd.save_as_csv(dbns)

if __name__ == '__main__':
    main()

