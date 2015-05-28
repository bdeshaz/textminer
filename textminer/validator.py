import re
import collections

def binary(string):
    return re.findall(r"(\A[01]+)", string)

def binary_even(string):
    if binary(string):
        return re.findall(r"[0]\Z", string)

def hex(string):
    return re.findall(r"(\b[A-Fa-f0-9]{1,}\b)", string)

def word(string):
    return re.findall(r"[\w-]+\w[^\*!]$", string)
#
# def words(string, count=None):
#     if word(string) != []:
#         return (word(string), count)

def phone_number(string):
    return re.findall(r"\b\(?\d{,3}\)?[-.\s]?\d{,3}[-.]?\d{,4}\b", string)
