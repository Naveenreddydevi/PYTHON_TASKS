#  1.explain about list with 7 examples ?
# list :
#----------------------
# list is a collection of data.
# list is a built-in dynamic sized array.
# we can store all types of items.
# list is a mutable that means we can change the elements,update the elements,modify the elements and also add the elements..
# list can be represented by using square brackets  "[ ]", the list items can be sapareted by camma ",".
#list can allows duplicate values.......

# example 1
a=[1,2,3,4,5,6,7,7,8]
print(type(a))
print(a)

# example 2
b=['a',4+6j,54.657,56,"trhf"]
print(b)

# example 3
c=["naveen",23,"hyd",30000]
print(c)
# example 4

nani=['janu',20,'khammam',4500,'mallareddy']
print(nani)
print(type(nani))

# example 5
juu=[1,'dfg',567,86,'fgjyt']
print(juu)
saa=[2,'jan',54,'hyd',9878]

# example 6
tanu=[3,'heroo',54,'hyd',87]
print(tanu)

# example 7
bava=[1,'harika','manisha','jhansi','pradeepti',6,76,245,786]
print(bava)


# 2. Explain about index and slicer with 10 examples ?
#  index:
# index is classified into two type 
# 1. positive index
# 2. negitive index
# by using index we can access only one elements.
#  slicer:
# by using slicer we can access a group of elements in a list.
# in slicer follows n-1 notation because the index start with 0.


# example 1
teks=[1,2,3,4,5,6,7,8,9,9,979,56,342,21,7,9,34,798,55]
print(teks[6])
print(teks[4:9])

# example 2
tek=['sai','janu','jhansi','naveen','krishna','satya']
print(tek[5])
print(tek[1:6])
# example 3
janu=[ 1.324,4.53,346.5,4756.8767,637.65,6546.75,4876,65,23,76,4376,657,34,78,2,76,257,770]
print(janu[6])
print(janu[4:10])
# example 4
tinnu=['janu','juu','joe','tanu','tinnu','tinnava','leda','ranu','hari']
print(tinnu[6])
print(tinnu[3:8])

# example 5
bngm=[1,'sai',20,'hyd',30000,'teks','python']
print(bngm[6])
print(bngm[2:6])

# example 6
banu=[2,'raju',32,'kmm',33000,'teks','java']
print(banu[6])
print(banu[2:6])
# example 7
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[:])

# example 8

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[2:])
print(a[:3])


# example 9

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[-4:-1])
print(a[-2:])


#3.explain about list types with one example?
# 1.append():
# it will add a single element at the end of a list
# example 
a=[1,2,3,4,5]
a.append(4)
print(a)

#2.extend():
# we can add a group of elements in a list
a=[1,2,3,4,5,6]
b=[3,4,5,6,7,8,9]
a.extend(b)
print(a)
#3.pop():
#it will remove the last element in a list
a=[1, 2, 3, 4, 5, 6, 3, 4, 5, 6, 7, 8, 9]
a.pop()
print(a)

#4.len():
# the lenght of a particular list 
a=[1, 2, 3, 4, 5, 6, 3, 4, 5, 6, 7, 8, 9]
print(len(a))

#5.count():
# how many times a element is present
a=[1, 2, 3, 4, 5, 6, 3, 4, 5, 6, 7, 8, 9]
print(a.count(4))
a.remove(1)
print(a)
a.clear()
print(a)
# example
a=[1, 2, 3, 4, 5, 6, 3, 4, 5, 6, 7, 8, 9]
a.reverse()
print(a)