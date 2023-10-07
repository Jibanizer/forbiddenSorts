# Inspiration: https://www.youtube.com/watch?v=ktgxMtWMflU

data = [1, 2, 3, 4, 5]
data2 = [1, 2, 1, 3, 4, 1, 5]
data3 = [0, 1, 2, 4, 3, 3, 3, 2, 5, 6, 7, 7, 7, 8, 0, 10]

# Stalin Sort
def stalinSort(input : list[int]) -> list[int]:
    """
    Input: random list of integers
    Output: sorted list of integers
    Algorithm: Stalin sends all elements out of order into a Gulag in Siberia. This does possibly reduce the size array. :)
    """
    output : list[int] = []
    temp_val : int = 0
    selected : list[int] = []
    temp = [(input, [])]
    for index, value in enumerate(input):
        if index == 0:
            output.append(value)
            temp_val = value
            selected.append(index)
        else:
            selected.append(index)
            if value >= temp_val:
                output.append(value)
                temp_val = value
                selected.pop(0)
        temp.append((output + input[index+1:], selected))
        # Something is still wrong with the selected indices
        print(temp)
    return output

# Sleep Sort

# Bogo Sort

# Bozo Sort

# Bogobogo Sort

# Quantum Bogo Sort

# Schrödinger Sort

# Intelligent Design Sort

# Miracle Sort
# Use HolyC?