import random
'''
def greet():
    greetings = ["hello", "welcome", "AYO!", "Hola", "Bonjour", "word up"]
    return random.choice(greetings)

def make_HTML_heading(f):
    txt = f()
    def inner():
        #print( txt)
        return "<h1>" + txt + "</h1>"
    return inner

greet_heading = make_HTML_heading(greet)
print(greet_heading())

'''

def make_html_heading(f):
    def inner():
        return "<h1>" +f() + "</h1>"
    return inner

# equiv to greet = makeHTMLheading(greet)
@make_html_heading
def greet():
    greetings = ["hello", "welcome", "AYO!", "Hola", "Bonjour", "word up"]
    return random.choice(greetings)

print (greet())
                           
''' 
memoization: process of storing previously calculated results
(ie writing "memos") so as to avoid re-calculation
'''
    

def memoize(f):
    memo = {}
    def helper(x):
        nonlocal memo
        if x in memo:
            return memo[x]
        else:
            memo[x] = f(x)
            return memo[x]
    return helper
        

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)



m_fib = memoize(fib)
print(m_fib(40))

