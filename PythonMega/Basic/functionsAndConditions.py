def mean(mylist):
    the_mean = sum(mylist) / len(mylist)
    return the_mean

print(mean([1, 4, 5]))
print(type(mean), type(sum))
#Type of > <class 'function'> <class 'builtin_function_or_method'>