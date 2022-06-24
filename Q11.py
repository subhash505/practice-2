list1 = ["a","b",["c",["d","e",["f", "g"],"k"],"l"],"m","n"]
sub_list=["h","i","j"]
list1[2][1][2].extend(sub_list)
print(list1)
print("Given List:\n")
print("""List1=["a","b",["c",["d","e",["f", "g"],"k"],"l"],"m","n"]\n""")
print("""Sub List to be added = ["h", "i", "j"]""")
print("Expected output:\n",list1)

print("updated content no need to worry")
