
# Author: Jenny Zhong
# GitHub username: jenzhng
# Date: 3/1/2023
# Description: A function called compare_sorts that takes the two decorated sort functions
#              (bubble sort and insertion sort) as parameters and produces a graph comparing
#              two series of data points



import random
import time
from functools import wraps
from matplotlib import pyplot

def sort_timer(func):
    def wrapper(*args, **kwargs):
        begin = time.perf_counter()
        func(*args, **kwargs)
        end = time.perf_counter()
        elapsed_time = end -  begin
        return elapsed_time

    return wrapper
@sort_timer
def bubble_sort(a_list):
  """
  Sorts a_list in ascending order
  """
  for pass_num in range(len(a_list) - 1):
    for index in range(len(a_list) - 1 - pass_num):
      if a_list[index] > a_list[index + 1]:
        temp = a_list[index]
        a_list[index] = a_list[index + 1]
        a_list[index + 1] = temp
@sort_timer
def insertion_sort(a_list):
  """
  Sorts a_list in ascending order
  """
  for index in range(1, len(a_list)):
    value = a_list[index]
    pos = index - 1
    while pos >= 0 and a_list[pos] > value:
      a_list[pos + 1] = a_list[pos]
      pos -= 1
    a_list[pos + 1] = value

def compare_sorts( bubble_func, insert_func):
    list_1 = []
    a = 1000
    list_1 = rand_int(a)
    list_b1 = list(list_1)
    list_i1 = list(list_1)
    data_b1 = bubble_sort(list_b1)
    data_i1 = insertion_sort(list_i1)
    print(data_b1, data_i1)

    b = 2000
    list_1 = rand_int(b)
    list_b2 = list(list_1)
    list_i2 = list(list_1)
    data_b2 = bubble_sort(list_b2)
    data_i2 = insertion_sort(list_i2)
    print(data_b2, data_i2)
    c = 3000
    list_1 = rand_int(c)
    list_b3 = list(list_1)
    list_i3 = list(list_1)
    data_b3 = bubble_sort(list_b3)
    data_i3 = insertion_sort(list_i3)
    print(data_b3, data_i3)
    d = 4000
    list_1 = rand_int(d)
    list_b4 = list(list_1)
    list_i4 = list(list_1)
    data_b4 = bubble_sort(list_b4)
    data_i4 = insertion_sort(list_i4)
    print(data_b4, data_i4)

    e = 5000
    list_1 = rand_int(e)
    list_b5 = list(list_1)
    list_i5 = list(list_1)
    data_b5 = bubble_sort(list_b5)
    data_i5 = insertion_sort(list_i5)
    print(data_b5, data_i5)

    f = 6000
    list_1 = rand_int(f)
    list_b6 = list(list_1)
    list_i6 = list(list_1)
    data_b6 = bubble_sort(list_b6)
    data_i6 = insertion_sort(list_i6)
    print(data_b6, data_i6)

    g = 7000
    list_1 = rand_int(g)
    list_b7 = list(list_1)
    list_i7 = list(list_1)
    data_b7 = bubble_sort(list_b7)
    data_i7 = insertion_sort(list_i7)
    print(data_b7, data_i7)

    h = 8000
    list_1 = rand_int(h)
    list_b8 = list(list_1)
    list_i8 = list(list_1)
    data_b8 = bubble_sort(list_b8)
    data_i8 = insertion_sort(list_i8)
    print(data_b8, data_i8)

    i = 9000
    list_1 = rand_int(i)
    list_b9 = list(list_1)
    list_i9 = list(list_1)
    data_b9 = bubble_sort(list_b9)
    data_i9 = insertion_sort(list_i9)
    print(data_b9, data_i9)

    j = 10000
    list_1 = rand_int(j)
    list_b10 = list(list_1)
    list_i10 = list(list_1)
    data_b10 = bubble_sort(list_b10)
    data_i10 = insertion_sort(list_i10)
    print(data_b10, data_i10)

    pyplot.plot([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],
                [data_b1, data_b2, data_b3, data_b4, data_b5, data_b6, data_b7, data_b8, data_b9, data_b10],
                'ro--', linewidth=2, label='bubble sort')
    pyplot.plot([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],
                [data_i1, data_i2, data_i3, data_i4, data_i5, data_i6, data_i7, data_i8, data_i9, data_i10],
                'go--', linewidth=2, label='insertion sort')
    pyplot.xlabel("number of elements sorted")
    pyplot.ylabel("time in seconds")
    pyplot.legend(loc='upper left')
    pyplot.show()

def rand_int(n):
    a_list = []
    for i in range(n):
        a_list.append(random.randint(3, 9))
    return a_list

# compare_sorts(bubble_sort, insertion_sort)

