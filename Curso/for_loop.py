my_dogs = ["Gaya", "Zika", "Felicity", "Fryda", "Ziggy", "Fluppy", "Lolla"]
for dogs in my_dogs:
    print(dogs)

for index in range(11):
    print(index)

for index in range(3, 11):
    print(index)

for index in range(len(my_dogs)):
    print(my_dogs[index])
    print(index)

for index in range(5):
    if index == 0:
        print("Primeira interacao")
    else:
        print("Nao e a primeira interacao")