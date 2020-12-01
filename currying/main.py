def un_curried(x, y):
    return x + y

def curried(x):
    def tmp(y):
        return x + y
    return tmp

print(un_curried(2, 3))
# 5
print(curried(2)(3))
# 5
