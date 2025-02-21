#   strings
"""------------------------------------------"""
""" a string is a sequence of a characters"""
#where the characters are a,b,c   we can declare a string by using those '',""
# """ """  is called doc string, and also it is used for commands 
# were string is a inmutable but we can add two strings by using cancatnation;
str="the king of indian occean"
str='the king of indian occean'
print(str)
print(type(str))


sati="who is the ceo of google"
print(sati)
print(type(sati))


bhai="no one can beets you"
print(bhai)
print(type(bhai))

str='the king of indian occean'
print(str)
print(type(str))


sati='who is the ceo of google'
print(sati)
print(type(sati))


maa="srujana tinnava ra"
print(maa)
print(type(maa))


hi="python trainer is vamsi sir for the batches 11am and 5pm"
print(hi)
print(type(hi))



oyeeeee="today is no classes for python"
print(oyeeeee)
print(type(oyeeeee))
















bhai="no one can beets you"
print(bhai[9])
print(bhai[4:10])


str='the king of indian occean'
print(str[7])
print(str[2:9])


sati='who is the ceo of google'
print(sati[3])
print(sati[6:13])



maa="srujana tinnava ra"
print(maa[6])
print(maa[2:])




hi="python trainer is vamsi sir for the batches 11am and 5pm"
print(hi[6])
print(hi[7:12])



oyeeeee="today is no classes for python"
print(oyeeeee[1])
print(oyeeeee[4:])


hmm="babu tinnara em chestunaruu asal"
print(hmm[12])
print(hmm[8:23])


hello="today is class starts at 11'o clock"
print(hello[4])
print(hello[6:])



#concatination
#-----------------
# we can add two strings by using concatination 
co1="who is the"
co2="ceo of google"
print(co1+" "+co2)
print((co1+" "+co2+"! ")  *10)


co1="today is class "
co2="starts at 11'o clock"
print(co1+" "+co2)
print((co1+" "+co2+"! ")  *10)


co1="python trainer is vamsi sir " 
co2="for the batches 11am and 5pm"
print(co1+" "+co2)
print((co1+" "+co2+"! ")  *10)


co1="he king of "
co2="indian occean"
print(co1+" "+co2)
print((co1+" "+co2+"! ")  *10)





hi="python trainer is vamsi sir for the batches 11am and 5pm"
print(len(hi))
print(hi.upper())
print(hi.lower())
print(hi.isupper())
print(hi.format())
print(hi.split())
print(hi.isalpha())
print(hi.islower())
print(hi.rsplit())
print(hi.capitalize())
print(hi.casefold())
print( hi.isascii())
print(hi.expandtabs())
print(hi.isidentifier())
print(hi.isupper())
print(hi.swapcase())
hi=['python', 'trainer', 'is', 'vamsi', 'sir', 'for', 'the', 'batches', '11am', 'and', '5pm']
print(' '.join(hi))