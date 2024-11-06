numbers_array = [0,0,5,8,0,1,0,4,12,0]
#               [5,8,1,4,12,0,0,0,0,0]
length_of_array = len(numbers_array)

def move_zeros(numbers):
    
    for i in range(length_of_array):
        for j in range(length_of_array-1):
            
            # check if number is zero move it to right by swapping it
            if numbers[j] == 0:
                temp = numbers[j+1]
                numbers[j+1] = numbers[j]
                numbers[j] = temp
                
    return numbers 

new_array = move_zeros(numbers_array)   
print(new_array)      
