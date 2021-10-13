import yaml

file = open('todo.yml', 'r')
data = yaml.safe_load(file)
print(data)
yaml.add_constructor('Test', data)
print(data)
file.close()

