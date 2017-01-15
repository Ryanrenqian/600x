s= str('zyxwvutsrqponmlkjihgfedcba')
str1 = s[0]



for n in range(len(s)):
    str2 = s[n]

    for m in range(n,len(s)):
        if m < len(s) -1 and s[m] <= s[m+1] :
            str2 += s[m+1]
            if len(str1) < len(str2):
                str1 = str2
        else:
            break    

print str1  