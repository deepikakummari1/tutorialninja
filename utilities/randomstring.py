import random
import string

def random_string_generator(size=5,chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for x in range(size))

print(random_string_generator())
# print(random.random())
# print(random.randint(1, 10))  # e.g. 7
# print(random.choice(['apple', 'banana', 'cherry']))  # e.g. 'banana'
#
# nums = [1, 2, 3, 4, 5]
# random.shuffle(nums)
# print(nums)

