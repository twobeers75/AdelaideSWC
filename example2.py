import sys

input_string = 'hello my name is Johnny j'
input_string2 = 'hello my name is Johnny the so-called bioinformatician'
isLower = input_string.lower()
is2Lower = input_string2.lower()
my_set_len = len(set(isLower))
print my_set_len
print set(isLower)
print set(isLower).intersection(set(is2Lower))
print set(isLower) - set(is2Lower)
print set(is2Lower) - set(isLower)

