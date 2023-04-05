# Author: Jenny Zhong
# GitHub username: jenzhng
# Date: 1/11/2023
# Description: Class named Student with two data members: name and grade.
#              Function named basic_states that returns mean, median, and mode, given parameter that is a list of Student objects

from statistics import mean, median, mode


class Student:
    '''
    Represents Student 
    '''
    def __init__(self, name, grade):
        '''
        Creates a Student object with two data members: name and grade.
        '''
        self._name = name
        self._grade = grade
    
    def get_grade(self):
        '''
        Returns the grade.
        '''
        return self._grade
        
def basic_stats(student):
        '''
        Returns mean, median, and mode of student grades.
        '''
        arr = []
        
        #iterate through student list for grades
        for i in range(0,len(student)):
            num = int(student[i].get_grade())
            arr.append(num)
            
        s_mean = mean(arr)
        s_median = median(arr)
        s_mode = mode(arr)
        
        s_tuple = tuple((s_mean, s_median, s_mode))
        
        return s_tuple
