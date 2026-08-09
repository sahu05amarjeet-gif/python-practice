# def is_pangram(st):
#     new_st = st.lower()
#     letters = ""
#     for char in new_st:
#         if char.isalpha() == True:
#             letters += char
#     lc = set(letters)
#     if len(lc) == 26:
#         return True
#     else:
#         return False

# print(is_pangram("The quick brown fox!!"))


# def duplicate_encode(word):
#     new_word = word.lower()
#     lc = set(new_word)
#     result = ""
#     for x in new_word:
#         count = new_word.count(x)
#         if count == 1:
#             result += "("

#         elif count >= 2:
#             result += ")"
#     return result
    
# print(duplicate_encode("(( @"))

# def count_by(x, n):
#     result = []
#     for num in range(1, n+1):
#         new_num = x * num
#         result.append(new_num) 

#     return result

# print(count_by(2, 5))

# def get_middle(s):
#     result = ""
#     if len(s)%2 == 0:
#         middle = len(s) // 2
#         result += s[middle-1 : middle+1]

#     elif len(s)%2 != 0:
#         middle = len(s) // 2
#         result += s[middle]
#     return result
# print(get_middle("dancingg"))

# [6, 2, 1, 8, 10] => 16 iterate 6, 2, 1, 8, 10


# def sum_array(arr):
#     if not arr or len(arr) == 1:
#         return 0
#     max_num = max(arr)
#     min_num = min(arr)
#     arr.remove(max_num)
#     arr.remove(min_num)
#     return sum(arr)
# print(sum_array(["None"]))

# def solution(s):
#     result = ""
#     for char in s:
#         if char.isupper():
#             result += " " + char
#         else: 
#             result += char
        
#     return result

# print(solution(""))

# Build a pile of Cubes
# def find_nb(m):
#     n = 1
#     total = 0
#     while total < m:
#         total += n ** 3
#         if total == m:
#             return n
#         n += 1
#     return -1
        

# print(find_nb(100))

stacks = []

stacks.append("A")
stacks.append("B")
stacks.append("C")
print(f"Stacks: {stacks}")

topElement = stacks[-1]
print("Peek", topElement)

popElement = stacks.pop()
print("Pop:", stacks)

isEmpty = stacks.isE