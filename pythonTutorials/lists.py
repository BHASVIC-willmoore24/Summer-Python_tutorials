# Lists can contain different data types

list1 = ["Pink Floyd", False, 3.3, 5]
print(list1)
print(False in list1)
print(list1[0])

list1[2] = 6.8
print(list1)

#.append adds an item to the end of a list
list1.append("The Beatles")
print(list1)

#.extend can add a list to the end
list1.extend(["Elliott Smith", "Pearl Jam"])
print(list1)

#.insert adds an item inside a list
list1.insert(4, "Soundgarden")
print(list1)
