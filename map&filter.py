# using map function
def squer(x):
    return x*x

num = [2,3,4,5,6,12]
result = list(map(squer,num))
print(result)

# using filter function

numbr = [1,2,3,4,5]
resl =list(filter(lambda x:x%2 ==0,numbr))
print(resl)

# arr = []
# def numbers(arr):
#  for arr in range(2,100,2):
#    return arr

results = [x for x in numbr if x%2 ==0]
print(results)