#For this task, you should return a roman numeral using the specified integer value ranging from 1 to 3999.
#Input: A number as an integer.
#Output: The Roman numeral as a string.

def convert_roman_numeral(num):
    roman_numeral = ""
    ROMANS = (('M', 1000),
              ('CM', 900),
              ('D', 500),
              ('CD', 400),
              ('C', 100),
              ('XC', 90),
              ('L', 50),
              ('XL', 40),
              ('X', 10),
              ('IX', 9),
              ('V', 5),
              ('IV', 4),
              ('I', 1))
    for roman, value in ROMANS:
        while num >= value:
            num -= value
            roman_numeral += roman
    print(roman_numeral)

convert_roman_numeral(11)