import numpy as np
def FizzBuzz(start, finish):
    nums = np.arange(start, finish+1)
    obj = nums.astype(object)
    fizz = nums % 3 == 0
    buzz = nums % 5 == 0
    obj[fizz] = "fizz"
    obj[buzz] = "buzz"
    obj[fizz & buzz] = "fizzbuzz"
    return obj
