import csv
import argparse
import operator


class SortingData:
    def __init__(self):
        self.data = []

    def read_csv_to_data(self, input_file):
        """
        takes the csv data, reads it and appends it to the data in innit
        :param input_file: the csv file
        :return: appended list
        """
        csv_reader = csv.reader(input_file, delimiter=",")
        for w in csv_reader:
            self.data.append(w)
        return self.data

    def emumerate_lists(self, sorted_list):
        """
        this function enumerates the lists once they are sorted
        :param sorted_list: takes the sorted list provided
        :return: returns the enumerated list that's passed
        """
        for j in sorted_list:
            enumerated_list = enumerate(j)
            print(list(enumerated_list))
        return enumerated_list

    def sort_by_ascending_amount(self, data):
        """
        this function sorts the data by ascending amount
        :param data: the unsorted data
        :return: prints sorted and enumerated data
        """
        print("sorting by ascending amount")
        sorted_list = sorted(data, key=operator.itemgetter(2))
        return list(self.emumerate_lists(sorted_list))

    def sort_by_ascending_product_color_amount(self, data):
        """
        this function sorts the data by product, color and then ascending amount
        :param data: the unsorted data
        :return: prints sorted and enumerated data
        """
        print("sorting by ascending product, color, amount")
        sorted_list = sorted(data, key=operator.itemgetter(0, 1, 2))
        return list(self.emumerate_lists(sorted_list))

    def sort_by_descending_product_color_amount(self, data):
        """
        this function sorts the data by product, color and then descending amount
        :param data: the unsorted data
        :return: prints sorted and enumerated data
        """
        print("sorting by descending product, color, amount")
        sorted_list = sorted(data, key=operator.itemgetter(0, 1, 2), reverse=True)
        return list(self.emumerate_lists(sorted_list))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", type=argparse.FileType('r'))
    args = parser.parse_args()
    parser.add_argument('-i', '--input_file', type=str, required=True, help="reading file from input")
    data_sorter = SortingData()
    engager = data_sorter.read_csv_to_data(args.input_file)
    data_sorter.sort_by_ascending_amount(engager)
    data_sorter.sort_by_ascending_product_color_amount(engager)
    data_sorter.sort_by_descending_product_color_amount(engager)
