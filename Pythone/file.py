#if the file is not present

f = open("Pythone/sample.txt", "w")

f.write("Hello Pythone!\n")



f.close()


# write multiline strings
f = open('Pythone/sample1.txt', 'w')
f.write("Hello world\n ")

f.close()


f = open('Pythone/sample1.txt', 'a')
f.write("Hello world, This is me \n ")

f.close()



# write lines 
L = ['hello\n', 'hi\n', 'how are you\n', 'I am file ']
f = open("Pythone/sample.txt", "w")
f.writelines(L)
f.close()




#reading from file

f = open('Pythone/sample.txt', 'r')
s = f.read()
print(s)
f.close()



#reading entire using readline
f = open('pythone/sample.txt', 'r')
while True:
    data = f.readline()

    if data == " ":
        break
    else:
        print(data, end='')

f.close()