def factorial(num): return reduce(lambda x,y:x*y, (i for i in range(1,num+1)))

def reverse_str(str): return str[::-1]

def is_pal(str) : return str == str[::-1]
