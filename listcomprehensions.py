#
#   List Comprehension Syntax
#
#   newlist = [expression for item in list filter]
#
# Example 1
#

digits = [x for x in range(10)]
print(digits)               # digits will contain [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

digits = [x for x in range(10) if x % 2 == 0]
print(digits)               # digits filtered by if stmt to include even numbers

nums = [x for x in range(21) if x%2==0 if x%5==0 if x%20==0]
print(nums)                 # multiple conditional filters
