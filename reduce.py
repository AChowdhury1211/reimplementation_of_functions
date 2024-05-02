def reduce_modified(function, iterable):
    it = iter(iterable)
    val = next(it)   #lets say [4,3,2,1] is passed, 4 would be the initial 
    for i in it: 
        # print(i) # here 3,2,1 will get printed
        val = function(val, i)  #
    return val

def add(a,b):
    return a+b

def reduce_inelegant_method(function, seq):
    val = seq[0]
    for i in seq[1:]:
        val = function(val, i)
    return val

lst = [4,3,2,-2,0,1.9]

result1 = reduce_modified(add, lst)
result2 = reduce_inelegant_method(add, lst)

print(result1)
print(result2)