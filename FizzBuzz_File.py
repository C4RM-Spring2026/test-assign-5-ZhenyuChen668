import numpy as np
def FizzBuzz(start, finish):
    nums = np.arange(start, finish)
    obj = nums.astype(object)

    fizz = nums % 3 == 0
    buzz = nums % 5 == 0

    obj[fizz] = "Fizz"
    obj[buzz] = "Buzz"
    obj[fizz & buzz] = "FizzBuzz"
    return obj
