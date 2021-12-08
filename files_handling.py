import time


f = open("test.txt","r") # will return a file_obj
file_content = f.read()  # will return a string

print(file_content)
print(type(f))
f.close()

#---------------------------------------------------
nf = open('file_created.txt','w')
nf.write("Hello From Python \nThis file is created from python")
nf.close()


with open('quiz.txt') as qf:
    print(qf.read())

print(qf.closed)