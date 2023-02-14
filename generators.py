# store only 14^14 
# more memory performant
# it won't store all numbers in memory like a list
def my_generator():
    for num in range(14):
        yield num ** num

for big_num in my_generator():
    print(big_num)
