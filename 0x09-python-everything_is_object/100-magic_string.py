def magic_string():
    magic_string.count = getattr(magic_string, 'count', -1) + 1
    return "BestSchool" + ", BestSchool" * magic_string.count
print(magic_string)
