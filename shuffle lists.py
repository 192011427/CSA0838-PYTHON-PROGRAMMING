# Using zip() + * operator + shuffle()
import random
 
# initializing lists
test_list1 = [0,4]
 
# printing lists
print(f"The original list 1 : {test_list1}")

 # Shuffle two lists with same order
# Using zip() + * operator + shuffle()
temp = list(zip(test_list1))
random.shuffle(temp)
res1, res2 = zip(*temp)
# res1 and res2 come out as tuples, and so must be converted to lists.
res1, res2 = list(res1)
 
# Printing result
print(f"List 1 after shuffle :  {res1}")
