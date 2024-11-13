"this function moves all 0 to the most right side of the list"

numbers_array = [0, 0, 5, 8, 0, 1, 0, 4, 12, 0]
#               [5,8,1,4,12,0,0,0,0,0]
LENGTH_OF_ARRAY = len(numbers_array)


def _move_zeros(numbers):

    for i in range(LENGTH_OF_ARRAY):
        for j in range(LENGTH_OF_ARRAY-1):

            # check if number is zero move it to right by swapping it
            if numbers[j] == 0:
                temp = numbers[j+1]
                numbers[j+1] = numbers[j]
                numbers[j] = temp

    return numbers


new_array = _move_zeros(numbers_array)
print(new_array)
