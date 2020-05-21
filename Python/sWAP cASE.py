def swap_case(s):
    res=''
    for i in range(len(s)):
        if s[i].islower():
            res+=s[i].upper()
        if s[i].isupper():
            res+=s[i].lower()
        if s[i].isalpha()==False:
            res+=s[i]
    return res
