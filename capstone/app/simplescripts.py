import json
import os

with open("abs_poet_urls.txt") as f:
    lst = json.load(f)
    p = [[j for j in lst[i] if "start" not in j] for i in range(len(lst))]#removes useless URLS!!!

fi = open("abbas_poet_urls.txt","w")
fi.write(str(p))
fi.close()

'''
rootdir = '/home/ramez/python/capstone/app/jahili_basic_graph_data'


for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            f = os.path.join(subdir, file)

            fi = open(f,"w")
            for line in file:
                print(type(line))
                line = file.replace("'", '"')
                print(line)
                line = json.dumps(fi)

    #for x in p:
        #print(type(x))
        #x = p.replace("'", '"')
        #print(x)
        #x = json.dumps(f)

    #for item in lst:
       # p = [ x for x in item if "x" not in x]  #this here removes any list item containing the letter x.


        #with open("write1.txt","w") as fi:
            #json.dump(hey,fi)
        #print(p)
        #for letter in p:
            #hi = letter
            #[letter for letter in item if "x" not in item]
            #print("letter: ", letter)
        #this here removes any list item containing the letter x.
        #print("Item: ", item)
#print("list: ",lst)
'''


'''f = open("jah_poet_urls.txt","r")
data = f.read()
f.close()

newdata = data.replace("'",'"')
f = open("jah_poet_urls_new.txt","w")
f.write(newdata)
f.close()
'''
