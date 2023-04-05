# Author: Jenny Zhong
# GitHub username: jenzhng
# Date: 2/8/2023
# Description: Function that takes as a parameter the name of a text file that contains a list of numbers, one to a line
#              and sums the values in the file and write the sum (just that number) to a text file named sum.txt

def file_sum(filename):
  """
  Function named file_sum that takes as a parameter the name of a text file that contains a list of numbers, one to a line
  and sums the values in the file and write the sum (just that number) to a text file named sum.txt
  """
  num_list = []
  sum = 0
  with open(filename, 'r') as infile:
    for line in infile:
        num_list.append(float(line.strip()))
  
  #add values altogether 
  for num in num_list:
      sum += num
      
  #write sum to output file 'sum.txt'
  with open('sum.txt', 'w') as outfile:
      outfile.write(str(sum))
      
def main():
    a = 'numbers.txt'
    print(file_sum(a))
if __name__ == '__main__':
    main()
