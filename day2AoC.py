#path to text file to be opened
path = 'day2AoCinput.txt'
# open file
file = open(path, 'r')
day2AoC_inputs = file.read().splitlines()
# # for ele in all_inputs:
# #     print(ele)


example_inputs = ['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc']

def password_validator(input_list):
    valid_passwords = 0
    for line in input_list:
        # Create list of each string separated by a space.
        # ['1-3', 'a:', 'abcde']
        words = line.split()
        # First part is then separated by the - character.
        # Left side is the low, and the right side is the high input.
        low, high = words[0].split('-')
        # Assign the first character of the [1] list element
        validator = words[1][0]
        # Assign the [2] element as the password.
        given_password = words[2]

        word_count = 0

        for char in given_password:
            if char == validator:
                word_count +=1
        if int(low) <= word_count <= int(high):
            valid_passwords += 1
    return valid_passwords

ex_password = password_validator(example_inputs)
day2AoC_answer = password_validator(day2AoC_inputs)

# print(ex_password)
# print(day2AoC_answer)


