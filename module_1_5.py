immutable_var  = 1, 2.1, "python", False
print(immutable_var )
#Операция не возможна потому что коллекция immutable_var содержит неизменяемые элементы.
#immutable_var[2] = "shmaiton"

mutable_list = [1, 2.1, "python", False]
mutable_list[2] = "shmaiton"
print(mutable_list)


