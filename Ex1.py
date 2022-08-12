#Q1. Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.

def multiplication_or_sum(num1, num2):
    # product
    product = num1 * num2
    if product <= 1000:
        return product
    else:
        return num1 + num2

#Q2. Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.

print("Printing current and previous number and their sum in a range(10)")
previous_num = 0
for i in range(1, 11):
    x = previous_num + i#sum
    print("Current Number", i, "Previous Number ", previous_num, " Sum: ", x)
    previous_num = i

#Q3. Write a program to accept a string from the user and display characters that are present at an even index number.


word = input('Enter the word ')
print("Original String is ", word)
print("Printing only even index chars")

size = len(word)
for i in range(0, size - 1, 2):
    print("index[", i, "]", word[i])
    
#Q4. Write a program to remove characters from a string starting from zero up to n and return a new string.

def remove_chars(word, n):
    x = word[n:]
    return x

#Q5. Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.

def first_last_same(numberList):    
    first_num = numberList[0]
    last_num = numberList[-1]
    
    if first_num == last_num:
        return True
    else:
        return False
    
#Q6.Iterate the given list of numbers and print only those numbers which are divisible by 5

num_list = [10, 20, 33, 46, 55]
print("Given list:", num_list)
print('Divisible by 5:')
for num in num_list:
    if num % 5 == 0:
        print(num)

#Q7. Write a program to find how many times substring “Emma” appears in the given string.

str1 = "Emma is good developer. Emma is a writer"

c = str1.count("Emma")
print(c)

#Q8 Print the following pattern

for num in range(10):
    for i in range(num):
        print (num, end=" ") #print number
    # new line after each row to display pattern correctly
    print("\n")
    
#Q9.Write a program to check if the given number is a palindrome number.

def palindrome(number):
    print("original number", number)
    original_num = number
    
    # reverse the given number
    reverse_num = 0
    while number > 0:
        reminder = number % 10
        reverse_num = (reverse_num * 10) + reminder
        number = number // 10

    # check numbers
    if original_num == reverse_num:
        print("Given number palindrome")
    else:
        print("Given number is not palindrome")

palindrome(121)
palindrome(125)

#Q10. Create a new list from a two list using the following condition

def merge_list(list1, list2):
    result_list = []
    
    # iterate first list
    for num in list1:
        # check if current number is odd
        if num % 2 != 0:
            # add odd number to result list
            result_list.append(num)
    
    # iterate second list
    for num in list2:
        # check if current number is even
        if num % 2 == 0:
            # add even number to result list
            result_list.append(num)
    return result_list

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
print("result list:", merge_list(list1, list2))


Q11. Write a Program to extract each digit from an integer in the reverse order.

number = 7536
print("Given number", number)
while number > 0:
    # get the last digit
    digit = number % 10
    # remove the last digit and repeat the loop
    number = number // 10
    print(digit, end=" ")

#Q12. Calculate income tax for the given income by adhering to the below rules


income = 45000
tax_payable = 0
print("Given income", income)

if income <= 10000:
    tax_payable = 0
elif income <= 20000:
    # no tax on first 10,000
    x = income - 10000
    # 10% tax
    tax_payable = x * 10 / 100
else:
    # first 10,000
    tax_payable = 0

    # next 10,000 10% tax
    tax_payable = 10000 * 10 / 100

    # remaining 20%tax
    tax_payable += (income - 20000) * 20 / 100

print("Total tax to pay is", tax_payable)


#Q13 Print multiplication table form 1 to 10

for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end=" ")
    print("")

#Q14 Print downward Half-Pyramid Pattern with Star

for i in range(6, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("")
    
#Q15. Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.

def exponent(base, exp):
    num = exp
    result = 1
    while num > 0:
        result = result * base
        num = num - 1
    print(base, "raises to the power of", exp, "is: ", result)

exponent(5, 4)

