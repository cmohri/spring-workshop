from functools import reduce

reduce ((lambda x, y: x*y), [1, 2, 3, 4])

'''
lambda in Python: 
- must return a vlaue ("Evaluate to", "collapse to")
- should remind you of Scheme/Racket/LISP
- conditionals must be in form of python ternary op: 
   exprA if condition else exprB
'''

