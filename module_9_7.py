def is_prime(func):
    def wrapper(*args):
        count = 0
        r = func(*args)
        for i in range(2, r):
           if r % i ==0:
               count += 1
        if count != 0:
            res = 'Составное'
        else:
            res = 'Простое'
        print(res)
        return r
    return wrapper
    
@is_prime    
def sum_three(*args):
    r = sum(args)
    return r
    
result = sum_three(2, 3, 6)
print(result)
