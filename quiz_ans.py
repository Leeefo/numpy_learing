def actors(file_name):
    with open(file_name,'r') as f:
        
        # Method 1
        # actors = []
        # for line in f:
        #     actors.append(line.split(',')[0])


        # Pythonic method
        actors = [line.split(',')[0] for line in f]
    return actors





actors_list = actors('quiz.txt')
for i in actors_list:
    print(i)