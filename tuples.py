# tuples and how to access items from the tuple

animals = ("Goat", "Cow", "Camel", "Donkey")

print(animals[2])
print(animals[0 : 3])


# Adding items to a tuple
animals2 = [(animals)]
print((animals2))

animals2.extend(["sheep", "dog", "hen"])
print(animals2)


# Removing item from a tuple
print(animals2.pop())

