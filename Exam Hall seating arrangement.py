from random import shuffle
from pprint import pprint as printf
from os import system
#import numpy as np
from copy import deepcopy as dc
#######################################################
##          Name      : Pradeep Suthar               ##
##          Reg. No.  : 11815262                     ##
##          Roll. No. : B:47                         ##
##          Section   : K18AP                        ##
#######################################################

starting_Roll_number = int(input('Enter Starting Roll Number :'))
ending_Roll_number = int(input('Enter Last Roll Number :'))
number_of_row_in_room = int(input('Enter Number of Rows Room :'))
number_of_col_in_room = int(input('Enter Number of Columns Room :'))

system('color 1')

number_of_Student_in_room = number_of_row_in_room * number_of_col_in_room
total_number_of_Student = ending_Roll_number - starting_Roll_number + 1
student_in_last_room = total_number_of_Student % number_of_Student_in_room
number_of_full_room_occupy = total_number_of_Student // number_of_Student_in_room

Student_Roll_List = [i for i in range(starting_Roll_number, ending_Roll_number + 1)]
roll_List_copy = dc(Student_Roll_List)
shuffle(roll_List_copy)
# print('student in last room',student_in_last_room)
fulled_Room = roll_List_copy[:-student_in_last_room]
# print('full rooms',len(fulled_Room))  
lastRoom = roll_List_copy[-student_in_last_room:]
nl = len(lastRoom)
del lastRoom

x, y, z = number_of_full_room_occupy, number_of_row_in_room, number_of_col_in_room
if student_in_last_room:
    seatingPlan = roll_List_copy + [0 for i in range(number_of_Student_in_room - nl)]
    arr = np.array(seatingPlan, dtype=int).reshape((x + 1, y, z))
else:
    seatingPlan = roll_List_copy
    arr = np.array(seatingPlan, dtype=int).reshape((x, y, z))

print()
printf(arr)
