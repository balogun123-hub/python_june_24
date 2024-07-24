'''
Write a program that takes a list of integers as input and returns the sum of all the integers in the list 
'''
def sum_of_integers(int_list):
    return sum(int_list)

# Example usage
numbers = [1, 2, 3, 4, 5]
total = sum_of_integers(numbers)
print("The sum of the integers is:", total)

# write a program that takes a list of integers as input and returns the average of all the integers in the list 
def average_of_integers(int_list):
    if not int_list:
        return 0  # Handle the case where the list is empty
    return sum(int_list) / len(int_list)

# Example usage
numbers = [1, 2, 3, 4, 5]
average = average_of_integers(numbers)
print("The average of the integers is:", average)

# Write a function that takes a string as input and returns that length of the string
def length_of_string(input_string):
    return len(input_string)

# Example usage
input_str = "Hello, world!"
length = length_of_string('Hello,World !')
print("The length of the string is:", length)

# Write a function that takes a list of integers as input and returns the maximum value in the list
def max_of_integers(int_list):
    if not int_list:
        return None  # Handle the case where the list is empty
    return max(int_list)

# Example usage
numbers = [1, 2, 3, 4, 5]
maximum = max_of_integers(numbers)
print("The maximum value in the list is:", maximum)

# Write a program that takes a list of integers as input and returns a new list that contains only the even integers from the original list
def filter_even_integers(int_list):
    return [num for num in int_list if num % 2 == 0]

# Example usage
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter_even_integers(numbers)
print("The even integers in the list are:", even_numbers)

# Write a program that takes two lists of integers as input and returns a new list that contains the intersection of the two lists (i.e., the element that are present in both lists)
def intersection_of_lists(list1, list2):
    return list(set(list1) & set(list2))

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
intersection = intersection_of_lists(list1, list2)
print("The intersection of the two lists is:", intersection)

# Write a function that takes a list of integers as input and returns a new list of integers as input and returns a new 
# list that contains the squres of all the integers in the original list

def square_integers(int_list):
    return [num ** 2 for num in int_list]

# Example usage
numbers = [1, 2, 3, 4, 5]
squared_numbers = square_integers(numbers)
print("The squares of the integers in the list are:", squared_numbers)

# Write a function that takes two integers as input and returns the sum of the two integers
def sum_of_two_integers(a, b):
    return a + b

# Example usage
num1 = 3
num2 = 5
total = sum_of_two_integers(num1, num2)
print("The sum of the two integers is:", total)




# Write a program that takes a list of integers as input and returns the sum of all the integers in the list 
def input(number_list):
    def input(number_list): #parameters
        for each_item in number_list:
            print(number_list.index,{each_item})




