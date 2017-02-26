from utils import load_yaml_file



class UserInput:
    pass


class Number(UserInput):
    pass


class Flag(UserInput):
    pass


inputs = {"Number": Number, "Flag": Flag}


data = load_yaml_file('data.yaml')

#print(data)

for key in data:
    print(data[key])

    if data[key] in inputs:
        data[key] = inputs[key]

print(data)