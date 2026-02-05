import re
from math import log2
import string
from tkinter import *



def entropy(password):
    res = 0
    L = len(password)
    if re.search(f"{[string.ascii_letters]}", password):
        res += len(string.ascii_letters)
    if re.search(f"{[string.digits]}", password):
        res += len(string.digits)
    if re.search(f"{[string.punctuation]}", password):
        res += len(string.punctuation)
    entropy = log2(res**L)
    return entropy
