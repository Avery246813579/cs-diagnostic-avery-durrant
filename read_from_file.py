file_object = open("secret_message.txt", "r")

print(str(file_object.readline()))

file_object.close()
