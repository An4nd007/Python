def create_exchanged_string(s):
    if len(s) < 2:  
        return s  
    return s[-1] + s[1:-1] + s[0]


input_string = "Hello, World"
output_string = create_exchanged_string(input_string)
print(output_string)  
