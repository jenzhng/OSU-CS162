# Author: Jenny Zhong
# GitHub username: jenzhng
# Date: 2/2/2023
# Description: Box class whose init method takes three parameters and uses them to initialize
#              private length, width and height data members of a Box
#              Box class has method named volume that returns the volume of the Box
#              Box class has get methods: get_length, get_width and get_height
#              Separate function named box_sort that uses insertion sort to sort a list of Boxes
#              from greatest volume to least volume.

class Box:
    def __init__(self, length, width, height):
        '''
        Creates Box object with three data members: length, width, height.
        :param length:
        :param width:
        :param height:
        '''
        self._length = length
        self._width = width
        self._height = height

    def get_length(self):
        '''
        Returns the length.
        :return:
        '''
        return self._length

    def get_width(self):
        '''
        Returns the width.
        :return:
        '''
        return self._width

    def get_height(self):
        '''
        Returns the height.
        :return:
        '''
        return self._height

    def volume(self):
        '''
        Returns volume of box by multiplying length by width by height.
        :param length:
        :param width:
        :param height:
        :return:
        '''
        vol_b = self._length * self._width * self._height
        return vol_b

def box_sort(b_list):
    '''
    Function box_sort that uses insertion sort to sort a list of Boxes 
    from greatest volume to least volume.
    :param b_list:
    :return:
    '''
    for index in range(1, len(b_list)):
        value = b_list[index]
        value_vol = b_list[index].volume()
        pos = index - 1

        pos_vol = b_list[pos].volume()
        while pos >= 0 and value_vol > pos_vol:
            b_list[pos + 1] = b_list[pos]
            pos -= 1
        b_list[pos + 1] = value

def main():
    box_1 = Box(9,9,9)
    box_2 = Box(2,3,5)
    box_3 = Box(10,12,11)

    sample_list = []
    sample_list.append(box_1)
    sample_list.append(box_2)
    sample_list.append(box_3)

    print(sample_list)
    box_sort(sample_list)
    print(sample_list)


if __name__ == '__main__':
    main()
