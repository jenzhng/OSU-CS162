
# Author: Jenny Zhong
# GitHub username: jenzhng
# Date: 2/2/2023
# Description: Bubble sort that counts the number of comparisons and the number of exchanges made while sorting a list
#              and returns a tuple of the two values (comparisons first, exchanges second).
#              Insertion sort that counts the number of comparisons and the number of exchanges made while sorting a list
# #            and returns a tuple of the two values (comparisons first, exchanges second).

def bubble_count(a_list):
  """
  Sorts a_list and counts number of comparisons and number of exchanges made while sorting a_list
  """
  comp_num = 0
  exch_num = 0

  for pass_num in range(len(a_list) - 1):
    for index in range(len(a_list) - 1 - pass_num):
      if a_list[index] > a_list[index + 1]:
        comp_num += 1
        temp = a_list[index]
        a_list[index] = a_list[index + 1]
        a_list[index + 1] = temp
        exch_num += 1
      else:
        comp_num += 1
  num_tup = (comp_num, exch_num)
  return num_tup

def insertion_count(a_list):
  """
  Sorts a_list and counts number of comparisons and number of exchanges made while sorting a_list
  """
  comp_num = 0
  exch_num = 0
  for index in range(1, len(a_list)):
    value = a_list[index]
    pos = index - 1
    
    while pos >= 0 and a_list[pos] > value:
      comp_num += 1
      a_list[pos + 1] = a_list[pos]
      exch_num += 1
      pos -= 1
    a_list[pos + 1] = value
   
  num_tup = (comp_num, exch_num)
  return num_tup
def main():
    num_list = [2, 4, 6, 3]
    print(bubble_count(num_list))
    print(insertion_count(num_list))
if __name__ == '__main__':
    main()
