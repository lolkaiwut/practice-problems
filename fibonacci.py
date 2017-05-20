def fibonacci(int):
    if int < 2:
        return int
    
    else: 
    	first_num = 0
        second_num = 1
        
    for num in range(int - 1):
        current_num = second_num + first_num
        first_num = second_num
        second_num = current_num
        
    return current_num

print fibonacci(1)
print fibonacci(4)
print fibonacci(10)
    
