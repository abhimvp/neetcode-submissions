from typing import List

def contains_duplicate(words: List[str]) -> bool:
    my_set = set()
    for i in range(len(words)):
        if words[i] in my_set:
            return True
        else:
            my_set.add(words[i])
    
    return False

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
