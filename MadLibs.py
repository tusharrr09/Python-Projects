#string concatenation(adding) for madlib

'''name ="Tushar Saha"
print(name + " likes football")
print("{} likes football".format(name))         #all three are same
print(f"{name} likes football") '''

adj = input('Adjective: ')
verb1 = input('Verb1:')
verb2 = input('Verb2:')
famous_person = input('Famous person: ')

madlib = f"Playing football is so {adj}! It makes me so excited all the time because \
    I love to {verb1}, stay hydrated and {verb2} like you are {famous_person}!"         # \ indicates sting is continued only line is changed

print(madlib)