def palabra(s):
    # Write your code here
    num_character = -1
    for i,j in enumerate(s):
        if s[0:len(s)].count(j) == 1:
            return (i + 1)
    return num_character
    
print(palabra("falafal"))
