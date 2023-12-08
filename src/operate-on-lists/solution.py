# Operate on Lists

def print_list(lst : list):
  print("-----------------------------------")
  print("- LIST CONTENTS                   -")
  for item in lst:
    print(item)
  print("-----------------------------------")
  print()


myList : list[str] = ["Hello"]
myList.append("GoodBye")
myList.insert(0,"Beginning")

print_list(myList)

myList.remove("GoodBye")

print_list(myList)

myList.pop()

print_list(myList)

