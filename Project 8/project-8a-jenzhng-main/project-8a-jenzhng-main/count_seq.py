
# Author: Jenny Zhong
# GitHub username: jenzhng
# Date: 3/1/2023
# Description: Generator function count_seq that generates a sequence.
#              To get a term of the sequence, count how many there are of each
#              digit (in a row) in the previous term.
def count_seq():
  """Generates a sequence of numbers that count how many of each digit in previous term."""
  n = 1
  while True:
      if n == 1:
          yield "2"
      elif n == 2:
          yield "12"
      else:
          start = "12"
          for i in range(3, n + 1):
              start = start + "$"
              start_len = len(start)
              n_count = 1
              addon = ""
              for j in range(1, start_len):
                  if start[j] != start[j - 1]:
                      addon = addon + str(n_count)
                      addon = addon + start[j - 1]
                      n_count = 1
                  else:
                      n_count += 1
              start = addon
          yield start
      n += 1
  

def main():
    my_gen = count_seq()
    for i in range(10):
        print(next(my_gen))


if __name__ == '__main__':
    main()
