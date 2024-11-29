
def replace_first_letter_with_dollar(s):
    if s:  
        return '$' + s[1:]  
    return s  

input_string = "Hello, World!"
output_string = replace_first_letter_with_dollar(input_string)
print(output_string)  
