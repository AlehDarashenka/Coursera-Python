import sys
digit_string = sys.argv[1]

def digit_sum(text):
    return sum([int(digit)for digit in text])


print(digit_sum(digit_string))