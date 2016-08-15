def fibonacci(n):
    # Initialize first two integers, i.e., o and 1
    a, b = 0, 1
    # Create an empty list to store results in order
    a_list = []
    for i in range(0,n):
        # Loop from 0 through n
        num = a
        a = b
        b = num + b
        a_list.append(b)
    return a_list
      
# Call the function
print(fibonacci(10))
