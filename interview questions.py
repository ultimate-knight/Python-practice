# def count_frequencies(text):
#     # Initialize a list to store frequencies of letters a-z
#     frequency = [0] * 26
    
#     # Count frequencies
#     for char in text:
#         frequency[ord(char) - ord('a')] += 1
    
#     # Construct the output string
#     result = []
#     for i in range(26):
#         if frequency[i] > 0:
#             result.append(chr(i + ord('a')) + str(frequency[i]))
    
#     return ''.join(result)

# # Read input
# text = input().strip()

# # Compute and print the frequency count
# print(count_frequencies(text))




# n=int(input('enter a number'))
# def fibonacci_sequence(n):
#     a,b=0,1
#     sequence=[]
    
#     for i in range(n):
#         sequence.append(a)
#         a,b=b,a+b
#         n-=1
#     return sequence

# print(fibonacci_sequence(n))


# n=int(input('enter a number'))
# for i in range(10):
#     print(f"{n, 'X', i+1}", "=", {n*(i+1)})








# def compare_with_threshold():
#     import sys
#     input = sys.stdin.read
#     data = input().split()
    
#     # Read the size of the array
#     size_of_array = int(data[0])
    
#     # Read the array elements
#     array = list(map(int, data[1:size_of_array + 1]))
    
#     # Read the threshold
#     threshold = int(data[size_of_array + 1])
    
#     # Initialize counters
#     count_larger = 0
#     count_smaller = 0
    
#     # Count elements based on comparison with threshold
#     for num in array:
#         if num > threshold:
#             count_larger += 1
#         elif num < threshold:
#             count_smaller += 1
    
#     # Determine the result based on counts
#     if count_larger > count_smaller:
#         print("larger")
#     elif count_smaller > count_larger:
#         print("smaller")
#     else:
#         print("equal")

# # Example usage
# if __name__ == "__main__":
#     compare_with_threshold()














# def count_flipped_bits(P, Q, R):
#     # Convert P, Q, and R to binary strings
#     bin_P = bin(P)[2:]
#     bin_Q = bin(Q)[2:]
#     bin_R = bin(R)[2:]
    
#     # Pad the binary strings to make them of equal length
#     max_len = max(len(bin_P), len(bin_Q), len(bin_R))
#     bin_P = bin_P.zfill(max_len)
#     bin_Q = bin_Q.zfill(max_len)
#     bin_R = bin_R.zfill(max_len)
    
#     # Calculate P XOR Q
#     xor_result = int(bin_P, 2) ^ int(bin_Q, 2)
#     bin_xor_result = bin(xor_result)[2:].zfill(max_len)
    
#     # Count the number of differing bits between bin_xor_result and bin_R
#     flips_needed = 0
#     for bit_xor, bit_r in zip(bin_xor_result, bin_R):
#         if bit_xor != bit_r:
#             flips_needed += 1
    
#     return flips_needed

# # Input
# P = int(input())
# Q = int(input())
# R = int(input())

# # Output
# print(count_flipped_bits(P, Q, R))







# def create_zigzag(s, n):
#     if n == 1:  # If the width is 1, the pattern is just the original string
#         return s
    
#     # Create a list of empty strings for each row
#     zigzag = ['' for _ in range(n)]
#     row, step = 0, 1
    
#     for char in s:
#         zigzag[row] += char
#         if row == 0:
#             step = 1
#         elif row == n - 1:
#             step = -1
#         row += step
    
#     # Combine characters from all rows
#     return ''.join(zigzag)

# # Read input
# s = input().strip()
# n = int(input().strip())

# # Create zig-zag pattern and print the result
# password = create_zigzag(s, n)
# print(password)








# def find_special_word(input_string):
#     words = input_string.split()
    
#     # Initialize variables to track the special word
#     special_word = ""
#     max_distinct_count = 0
    
#     for word in words:
#         # Count distinct letters in the word
#         distinct_letters = set(word)
#         distinct_count = len(distinct_letters)
        
#         # Update the special word based on the conditions
#         if (distinct_count > max_distinct_count or
#             (distinct_count == max_distinct_count and word < special_word)):
#             special_word = word
#             max_distinct_count = distinct_count
    
#     return special_word

# # Read input
# input_string = input().strip()
# # Find and print the special word
# print(find_special_word(input_string))










# def calculate_total_energy(M, R, N):
#     # Total energy produced over N seconds
#     total_energy = N * M + R * (N * (N - 1)) // 2
#     return total_energy

# # Read input
# M = int(input().strip())
# R = int(input().strip())
# N = int(input().strip())

# # Calculate and print the total energy
# print(calculate_total_energy(M, R, N))





# def count_frequencies(text):
#     # Initialize a list to store frequencies of letters a-z
#     frequency = [0] * 26
    
#     # Count frequencies
#     for char in text:
#         frequency[ord(char) - ord('a')] += 1
    
#     # Construct the output string
#     result = []
#     for i in range(26):
#         if frequency[i] > 0:
#             result.append(chr(i + ord('a')) + str(frequency[i]))
    
#     return ''.join(result)

# # Read input
# text = input().strip()

# # Compute and print the frequency count
# print(count_frequencies(text))






# def combine_scores(chemistry_scores, english_scores):
#     # Convert the comma-separated strings to lists of integers
#     chemistry_list = list(map(int, chemistry_scores.split(',')))
#     english_list = list(map(int, english_scores.split(',')))
    
#     # Combine the scores into a list of tuples
#     combined_scores = list(zip(chemistry_list, english_list))
    
#     return combined_scores

# # Read input
# chemistry_scores = input().strip()
# english_scores = input().strip()

# # Combine scores and get the result
# result = combine_scores(chemistry_scores, english_scores)

# # Print the result
# for scores in result:
#     print(f"{scores[0]},{scores[1]}")







# def is_subset(a, b):
#     return a.issubset(b)

# # Read number of test cases
# T = int(input().strip())

# for _ in range(T):
#     # Read and parse set A
#     num_elements_A = int(input().strip())
#     elements_A = set(map(int, input().strip().split()))
    
#     # Read and parse set B
#     num_elements_B = int(input().strip())
#     elements_B = set(map(int, input().strip().split()))
    
#     # Check if A is a subset of B and print the result
#     print(is_subset(elements_A, elements_B))








# def convert_words_to_digits(contact_words):
#     # Mapping of words to digits
#     word_to_digit = {
#         'zero': '0', 'one': '1', 'two': '2', 'three': '3',
#         'four': '4', 'five': '5', 'six': '6', 'seven': '7',
#         'eight': '8', 'nine': '9'
#     }
    
#     # Split input into words
#     words = contact_words.split()
    
#     result = []
#     i = 0
    
#     while i < len(words):
#         word = words[i]
        
#         if word == 'double':
#             digit = word_to_digit[words[i + 1]]
#             result.append(digit * 2)
#             i += 2
#         elif word == 'triple':
#             digit = word_to_digit[words[i + 1]]
#             result.append(digit * 3)
#             i += 2
#         else:
#             # Normal digit or part of a longer sequence
#             result.append(word_to_digit[word])
#             i += 1
    
#     # Join the result list into a single string
#     return ''.join(result)

# # Read input
# contact_words = input().strip()

# # Convert and print the contact number
# print(convert_words_to_digits(contact_words))





# def find_mex(arr):
#     # Find the smallest non-negative integer not present in the array
#     present = set(arr)
#     mex = 0
#     while mex in present:
#         mex += 1
#     return mex

# def min_removals_to_change_mex(arr):
#     # Calculate original MEX
#     original_mex = find_mex(arr)
    
#     # Count occurrences of each element
#     from collections import Counter
#     count = Counter(arr)
    
#     # Try to remove elements to change MEX
#     for num in range(original_mex + 1):
#         if count[num] > 0:
#             # Remove this number
#             temp_count = count.copy()
#             temp_count[num] -= 1
            
#             # Recalculate MEX after removing num
#             new_mex = find_mex([key for key in temp_count.elements() if temp_count[key] > 0])
#             if new_mex != original_mex:
#                 return 1
    
#     # Try removing two elements if removing one isn't sufficient
#     for num1 in range(original_mex + 1):
#         if count[num1] > 0:
#             for num2 in range(num1, original_mex + 1):
#                 if num1 == num2:
#                     if count[num2] > 1:
#                         temp_count = count.copy()
#                         temp_count[num1] -= 2
#                         new_mex = find_mex([key for key in temp_count.elements() if temp_count[key] > 0])
#                         if new_mex != original_mex:
#                             return 2
#                 else:
#                     if count[num2] > 0:
#                         temp_count = count.copy()
#                         temp_count[num1] -= 1
#                         temp_count[num2] -= 1
#                         new_mex = find_mex([key for key in temp_count.elements() if temp_count[key] > 0])
#                         if new_mex != original_mex:
#                             return 2

#     # If removing 1 or 2 elements is not enough
#     return -2

# # Read input
# n = int(input().strip())
# arr = list(map(int, input().strip().split()))

# # Calculate and print the minimum number of elements to remove
# print(min_removals_to_change_mex(arr))





# def min_deletions_to_palindrome(s):
#     def longest_palindromic_subsequence(s):
#         n = len(s)
#         dp = [[0] * n for _ in range(n)]
        
#         for i in range(n):
#             dp[i][i] = 1
        
#         for length in range(2, n + 1):
#             for i in range(n - length + 1):
#                 j = i + length - 1
#                 if s[i] == s[j]:
#                     dp[i][j] = dp[i + 1][j - 1] + 2
#                 else:
#                     dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        
#         return dp[0][n - 1]

#     n = len(s)
#     lps_length = longest_palindromic_subsequence(s)
#     return n - lps_length

# # Example Usage
# s = input().strip()
# print(min_deletions_to_palindrome(s))





# def min_cost_of_travel(days, costs):
#     travel_days = set(days)
#     dp = [0] * (max(days) + 1)
#     day_cost = [float('inf')] * (max(days) + 1)
    
#     for day in range(1, len(dp)):
#         if day in travel_days:
#             dp[day] = min(
#                 dp[max(day - 1, 0)] + costs[0],  # Single day pass
#                 dp[max(day - 7, 0)] + costs[1],  # 7-day pass
#                 dp[max(day - 30, 0)] + costs[2]  # 30-day pass
#             )
#         else:
#             dp[day] = dp[day - 1]
    
#     return dp[-1]

# # Example Usage
# days = list(map(int, input().strip().split()))
# costs = list(map(int, input().strip().split()))
# print(min_cost_of_travel(days, costs))




# def is_interleaved(s1, s2, s3):
#     if len(s1) + len(s2) != len(s3):
#         return False
    
#     dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
#     dp[0][0] = True
    
#     for i in range(1, len(s1) + 1):
#         dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
    
#     for j in range(1, len(s2) + 1):
#         dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
    
#     for i in range(1, len(s1) + 1):
#         for j in range(1, len(s2) + 1):
#             if s1[i-1] == s3[i+j-1] and dp[i-1][j]:
#                 dp[i][j] = True
#             elif s2[j-1] == s3[i+j-1] and dp[i][j-1]:
#                 dp[i][j] = True
    
#     return dp[len(s1)][len(s2)]




# # Read input
# N = int(input())
# results = []

# for _ in range(N):
#     s1, s2, s3 = input().split()
#     results.append("YES" if is_interleaved(s1, s2, s3) else "NO")

# # Print output
# for result in results:
#     print(result)



# n=int(input('enter a number'))
# def factorial_recursive(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial_recursive(n - 1)

# # Example usage:
# print(factorial_recursive(n))  # Output: 120




# def reverse_string(s):
#     return s[::-1]

# s=str(input('enter a string'))
# print(reverse_string(s))


# with open('write.txt', 'w') as file:
#     text=file.read()
#     # text=file.write('hey man how are u doing')
#     words=text.split()
#     print(len(words))

# squares=[x**2 for x in range(11)]
# print(squares)



# import re

# text = """
# Please contact us at support@example.com for further information.
# You can also reach out to sales@example.com or info@example.co.uk.
# """

# pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
# emails = re.findall(pattern, text)
# print("Email addresses found:", emails)



# import re
# text="""
# hey i'm baqtiyaar my email is maaz2607@gmail.com.
# """
# pattern=r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
# email=re.findall(pattern, text)
# print('my email', email)


# import re
# text="""
# here we are hefty@mg.com
# """

# pattern=r"[A-Za-z0-9+-/%.]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
# email=re.findall(pattern, text)
# print('hey i found it', email)#re.find,re.findall,re.search,re.finditer,re.match,re.sub,re.split#




import re
# print(re.findall(r"a.b", 'aab acb adb anb'))#Matches any single character except newline.#
# print(re.findall(r"^ab", 'aba aab acb adb aib abe'))#Matches the start of the string.#
# print(re.findall(r"world$", 'hey man are u in this world'))#Matches the end of the string.#
# print(re.findall(r"abc*", "abc abd abe abg aba abaaa"))#Matches 0 or more repetitions of the preceding pattern.#
# print(re.findall(r"abc+", "addis ababa abac abcas abccess" ))#Matches 1 or more repetitions of the preceding pattern.#
# print(re.findall(r"ab?", "abeaze abert abbaba"))#Matches 0 or 1 repetition of the preceding pattern.Example: ab? matches a and ab.#
# # print(re.findall(r"a{3}", 'aaabc aabca'))#Matches exactly n repetitions of the preceding pattern.#
# print(re.findall(r"a{2,}", 'aaabc aacd aang'))# Matches n or more repetitions of the preceding pattern.#
# print(re.findall(r"a{2,3}", 'aabc aaabc abc aaaagd'))#Matches between n and m repetitions of the preceding pattern.#
# print(re.findall(r"[abc]", 'mershiemer addis ababa'))#Matches any single character in the brackets.#
# print(re.findall(r"[^abc]", "abc def gef ref"))#Matches any single character not in the brackets.#
# print(re.findall(r"\d", "123alpha 145beta"))#Matches any digit (equivalent to [0-9]).#
# print(re.findall(r'\D', 'abc123 149bast'))#Matches any non-digit.#
# print(re.findall(r"\w", 'abc123 123-%abc'))#\w matches a-z, A-Z, 0-9, and _.#
# print(re.findall(r"\W", "abc345 -90%"))#\W matches any character except a-z, A-Z, 0-9, and _#
# print(re.findall(r'\s', " ,a,a,b,c"))#\s matches spaces, tabs, and newlines.#
# print(re.findall(r'\S', "aabc,a,a,c"))#\S matches any character except spaces, tabs, and newlines#

text="we are having a great day and i'm here and there for them"
# pattern=r'great'
# rent=re.search(pattern, text)
# if rent:
#     print('rent found', rent.group())
# else:
#     print('not found')



# pattern=r"and"
# list=re.findall(pattern, text)
# print(list)


# pattern=r'a'
# list=re.finditer(pattern, text)
# for lis in list:
#     print('list:', lis.start(), lis.group())


# pattern=r"and"
# match=re.match(pattern, text)
# print('the match is:', match)



# patter=r"are"
# replacement=r"why"
# list=re.sub(patter, replacement, text)
# print(list)


# pattern=r'\s'
# list=re.split(pattern, text)
# print(list)



# text23='An official account of the number of people killed at Turkman gate is not available and a media blackout ensued in the wake of the massacre.[2] One local guide claimed that nine of his friends were killed by the police.[3] More than ten bulldozers razed down illegal structures and homes, and protestors were fired upon by police.'
# pattern=r"and"
# pat=r"An"
# # zest=re.findall(pattern, text23)
# # zest=re.search(pattern, text23)
# # zest=re.finditer(pattern, text23)
# # for patter in zest:
#     # print(patter)
# # print(zest)
# zec=re.match(pat, text23)
# print(zec)



# text='hey my name is maaz2607@gmail.com'
# pattern=r'[A-Za-z0-9+-_%]+@[A-Za-z0-9_%]+\.[A-Za-z]{2,}'
# list=re.findall(pattern, text)
# print('hey man is:', list)






