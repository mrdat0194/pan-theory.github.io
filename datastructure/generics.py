from typing import TypeVar
from typing import Any, List
Element=TypeVar("Element")
#https://www.youtube.com/watch?v=3m7uTWqwg34
#mypy check list

def printArray(array: [Element]) -> List[Element]:
    for element in array:
        print(element)
    return element


vInt = [1, 2, "a"]
vString = ["Hello", "World"]

a = printArray(vInt)
b = printArray(vString)
print(type(a))
print(type(b))