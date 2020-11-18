#!/usr/bin/env python3

class StringManager:

    @staticmethod
    def get_average_len(strings):
        total_avg = sum(map(len, strings)) / len(strings)
        return total_avg

    @staticmethod
    def print_list(strings):
        for string in strings:
            print(string)

    @staticmethod
    def file_to_string_list(path):
        file1 = open(path, 'r')
        lines = file1.readlines()
        only_pwd_list = []

        # Remove /n from password
        for line in lines:
            only_pwd_list.append(line.strip())

        return only_pwd_list

    @staticmethod
    def getDuplicatesWithCount(listOfElems):
        ''' Get frequency count of duplicate elements in the given list '''
        dictOfElems = dict()
        # Iterate over each element in list
        for elem in listOfElems:
            # If element exists in dict then increment its value else add it in dict
            if elem in dictOfElems:
                dictOfElems[elem] += 1
            else:
                dictOfElems[elem] = 1

                # Filter key-value pairs in dictionary. Keep pairs whose value is greater than 1 i.e. only duplicate elements from list.
        dictOfElems = {key: value for key, value in dictOfElems.items() if value > 1}
        # Returns a dict of duplicate elements and thier frequency count
        return dictOfElems