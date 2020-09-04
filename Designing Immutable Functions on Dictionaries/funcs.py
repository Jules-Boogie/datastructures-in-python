"""
Module demonstrating immutable functions on dictionaries

All of these functions make use of accumulators.

Author: Juliet George
Date: 9/2/2020
"""


def average_grade(adict):
    """
    Returns the average grade among all students.

    The dictionary adict has netids for keys and numbers 0-100 for values.
    These represent the grades that the students got on the exam.  This function
    averages those grades and returns a value.

    Examples:
        average_grade({'wmw2' : 55, 'abc3' : 90, 'jms45': 86}) returns (55+90+86)/3 = 77
        average_grade({'wmw2' : 55}) returns 55
        average_grade({}) returns 0

    Parameter adict: the dictionary of grades
    Precondition: adict is dictionary mapping strings to ints
    """
    sum = 0
    length = len(adict)
    for value in adict.values():
        sum = sum + value
    return sum/length if length > 0 else 0.0


def letter_grades(adict):
    """
    Returns a new dictionary with the letter grades for each student.

    The dictionary adict has netids for keys and numbers 0-100 for values. These
    represent the grades that the students got on the exam. This function returns a
    new dictionary with netids for keys and letter grades (strings) for values.

    Our cut-off is 90 for an A, 80 for a B, 70 for a C, 60 for a D. Anything below 60
    is an F.

    Examples:
        letter_grades({'wmw2' : 55, 'abc3' : 90, 'jms45': 86}) returns
            {'wmw2' : 'F, 'abc3' : 'A', 'jms45': 'B'}.
        letter_grades({}) returns {}

    Parameter adict: the dictionary of grades
    Precondition: adict is dictionary mapping strings to ints
    """
    letter_dict = {}
    for key in adict:
	    if adict[key] >= 90:
		    letter_dict[key] = 'A'
	    elif 80 <= adict[key] < 90:
		    letter_dict[key] = 'B'
	    elif 70 <= adict[key] < 80:
		    letter_dict[key] = 'C'
	    elif 60 <= adict[key] < 70:
		    letter_dict[key] = 'D'
	    else:
		    letter_dict[key] = 'F'
    return letter_dict
