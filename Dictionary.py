# 1 creation
d1_1={} # empty Dict
d1_2={'rollno':1,'name':'Ami','Subject':'python'} # Key : Value creation
print(d1_1,d1_2)
# key can be number,string,tuple
# #value can be anything
# order can be anything in dictionary
# case-sensitive
# dict is modifieable
# dict is unordered collection of objects
print(type(d1_2))
d1_3=dict() # creating dict using built-in function
d1_4=dict({1:"a","g":"f"})
d1_4[1]="f" # accessing and modifying
# print(d1_4[3]) # gives keyerror

print()

# 2 ex create employee id , name , salary respectively and assume values of dictionary and print it
d2={
    "id":1,
    "name":"Aayush",
    "salary":123455
}
print(f"Employee Id = {d2['id']} , Name = {d2['name']} , Salary = {d2['salary']}")
# adding element in d2
d2['fees']=15000
print(d2)

# 3 Traversing with for
for i in d2:
    print(i," --> ",d2[i])

print()

# 4 Appending values
d4={"name":"Aayush","Class":"College","Year":"2022"}
print("d4 = ",d4)

d4["stream"]="Computer Science" # appending
print("Appeding stream ----> ",d4)

d4.update({"stream":"CSE"})
print("Updating stream ----> ",d4)

# 5 removing elements and dictionary
del d4["stream"]
print("removing stream ----> ",d4)
d4.clear()
print("clearing d4 elements ----> ",d4)

# 6 dictionary functions and methods
d6=dict({"name":"Aayush","Class":"College","Year":"2022"}) # dict() create dictionary
d6_1=d6
print("len(d6) = ",len(d6)) # len()

print("d6_1.clear() = ",d6_1.clear()) # clear()

print("d6.get(name) = ",d6.get("name")) # get() similar to accessing

print("d6.pop('Year') = ",d6.pop('Year')) # pop() print value for key and delete it
