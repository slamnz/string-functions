# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 00:21:13 2017

@author: Sunny Lam
"""

def is_palindrome(word):
    
    first = ""
    last = ""
    
    for i in range(0,len(word)):
        
        first = word[i].lower()
        second = word[len(word) - 1 - i].lower()
        
        if(not first == second):
            
            return False
            
    return True
    
print(is_palindrome("Hannah"))