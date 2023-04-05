# Author: Jenny Zhong
# GitHub username: jenzhng
# Date: 2/2/2023
# Description: Binary Search function that searches a list for target value.
#              If found, returns index of its position in the list.
#              If not found, raises TargetNotFound exception, indicating the target value isn't in the list


class TargetNotFound(Exception):
    pass
def bin_except(a_list, target):
  """
  Searches a_list for an occurrence of target
  If found, returns the index of its position in the list
  If not found, raises TargetNotFound exception, indicating the target value isn't in the list
  """
  first = 0
  last = len(a_list) - 1
  while first <= last:
    middle = (first + last) // 2
    if a_list[middle] == target:
      return middle
    if a_list[middle] > target:
      last = middle - 1
    else:
      first = middle + 1
  raise TargetNotFound

def main():
    list1 = [1,2,3,4,5]
    target1 = 3
    target2 = 7

    try:
        bin_except(list1, target2)
    except(TargetNotFound):
        print ("Not in list.")
    else:
        print("Target found.")

if __name__ == '__main__':
    main()
