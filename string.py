str1 = 'hello'
str2 = ' JiuZhang'
str3 = str1 + str2
print str3  # -> 'hello JiuZhang'

print len(str3)  # length of str3

print str3.index('Jiu')  # 6
print str3.find('Jiua')  # if the index is found, return index, otherwise return -1
print str3.index('Jiua')  # if not found, return error, eg: substring not found

# print str3.index('Jiua')  # What's the difference between index and find ?
print 'abc' * 3   # 'abcabcabc'

str3[0] = 'H' 
print str3  # 'Hello JiuZhang'
