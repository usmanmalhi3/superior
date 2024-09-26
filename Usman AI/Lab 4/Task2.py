def remove_punctuation(input_string):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    result = ''
    
    for char in input_string:
        if char not in punctuations:
            result += char
            
    return result


user_input = input("Enter a string with punctuation: ")
cleaned_string = remove_punctuation(user_input)
print("String without punctuation:", cleaned_string)
