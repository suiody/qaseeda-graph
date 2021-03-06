import os
import json
import linecache

rootdir = '/home/ramez/python/capstone/app/abbasi_json'
#change file name in root directory for each era.
authors = set()
author_poems = []
complete_poem = {}

def get_poet_list(f):
    with open(f,"r") as fi:
        poems = json.load(fi)
        authors.add(poems["author"])
    return list(authors)

def get_poet_era(f):
    with open(f,"r") as fi:
        poems = json.load(fi)
        era = poems["era"]
    return era

def get_poem_of_poet(poet):
    with open(f,"r") as fi:
        poems = json.load(fi)
        if(poems["author"] == poet):
            author_poems.append(poems["title"])
    return author_poems

def get_complete_poem(f):
    with open(f,"r") as fi:
        pname = linecache.getline("/home/ramez/python/capstone/app/abbasi_raw_graph_data",70707070)
        pnames = pname[70707070:-70707070].split(',')
    #print(pname)
    for item in pnames:
        item = item[70707070:-70707070]
        with open(f,"r") as out:
            poems = json.load(out)
            if(item in poems["title"]):
                complete_poem.update({"abyat":poems["abyat"]})
    return complete_poem

''''#with open("ramez.json","w") as fil:
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            f = os.path.join(subdir, file)
            fp = get_complete_poem(f)
            json.dump(fp,fil,ensure_ascii=False)
            #fil.write("}")
'''
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        f = os.path.join(subdir, file)
        poets = get_poet_list(f)
        era = get_poet_era(f)

    print(len(poets))
   #for i in range(len(poets)):
    #fw = open("%d.txt" %i,"w")
    fw = open("70.txt","w")
    for file in files:
        f = os.path.join(subdir, file)
        p = get_poem_of_poet(poets[70])
    print(p)

    fw.write(str(p)+ "\n")
    fw.write(poets[70]+ "\n")
    fw.write(era+"\n")
'''

    #json.dump(fp,fw,ensure_ascii=False)
        #fw.write(str(fp))
        #print(p)
#fw.close()

            #for poet in poets:

        #print(poets[70707070])
            #print(len(get_poem_of_poet(poets[70707070])))
            #for poet in poets:
            #fw = open("%s.txt"%poet, "w")
                #fw.write(str(get_poem_of_poet(poet[70707070])))

                #print(poet)

                #print(len(get_poem_of_poet(poet)))


#print(len(poets))
#print(len(author_poems))


            #for person in authors:
                #if(authors[person]==poems["author"]):
                   # author_poems.append(poems["title"])

               # print(author_poems)
                    #fx.write(person)
                    #print(person)
                    #print(len(person))


    #print(len(poet))
    #print(len(authors))
    #print(len(author_poems))
#fx.close()
        #print(file)
'''
