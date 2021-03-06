from py2neo import neo4j, Node, rel
import linecache
import os
import json
		  
def populate_graph(node):
    previous = None
    for i in range(len(poems["abyat"])):
        if(i == 0):
            first_bayt = poems["abyat"][0]["bayt"]
            first_sadr = poems["abyat"][0]["sadr"]
            first_ajz = poems["abyat"][0]["ajez"]
            first = Node("Bayt", name= first_bayt, sudr = first_sadr, ajez = first_ajz)
            graph_db.create(first)
            graph_db.create(rel(node,"CONTAINS",first))
            print("see me once")
            
        if(i == 1):
            bayt = poems["abyat"][1]["bayt"]
            sadr = poems["abyat"][1]["sadr"]
            ajz = poems["abyat"][1]["ajez"]
            following = Node("Bayt", name = bayt, sudr = sadr, ajez = ajz)
            graph_db.create(following)
            graph_db.create(rel(first,"FOLLOWED_BY", following))
            print("in 1")

        if(i > 1):
            bayt = poems["abyat"][i]["bayt"]
            sadr = poems["abyat"][i]["sadr"]
            ajz = poems["abyat"][i]["ajez"]
            follow = Node("Bayt", name = bayt, sudr = sadr, ajez = ajz)
            graph_db.create(follow)
            if(i == 2):
                graph_db.create(rel(following,"FOLLOWED_BY", follow))
                print("2")
            elif(previous is not None):
                graph_db.create(rel(previous,"FOLLOWED_BY",follow))
                print(i)
            previous = follow

#unused.
def populate_who_wrote_what(node):
    for node in poem_node_list:
        graph_db.create(node)
        graph_db.create(rel(node,"WROTE",poem_node))
        print(node)

#TODO: apply the same to all 4 3asrs, after applying them in organizeForGraph.py; change rootdir to 'era'_raw_graph_data, and asr variable node to specific era. end result is a massive graph containing 4 3asrs, all their poets and whos born where, and who wrote what. and the actual poem sequence!

rootdir = '/home/ramez/python/capstone/app/andalsi_raw_graph_data'
#jsondir = '/home/ramez/python/capstone/app/jahili_json'

textfiles = glob.glob(os.path.join(rootdir, '*.txt'))
jsonfiles = glob.glob(os.path.join(rootdir, '*.json'))

authors = []
poem_list = []
poem_node_list = []
author_node_list = []

neo4j.authenticate("localhost:7474","neo4j","faisal")
#default for 7474 is empty. can add url.
graph_db = neo4j.Graph()

asr = Node("Era", era = "العصر الأندلسي")
graph_db.create(asr)
print(asr)

for f in textfiles:
    title = linecache.getline(f,1)# filename, line_number
    titles = title[1:-1].split(',')

    author = linecache.getline(f,2)
#   authors.append(author[:-1])

    poet = Node("Poet", name = author)
#   author_node_list.append(poet)

    graph_db.create(poet)
    graph_db.create(rel(poet,"BORN_IN", asr))

    for item in titles:
        item = item[2:-1]
#       poem_list.append(item)
#       print(item)
        item = Node("Title", name = item)
        poe = str(item)
        po = poe[15:-3]
#       poem_node_list.append(item)
        graph_db.create(item)
        graph_db.create(rel(poet,"WROTE",item))

        print(po)

        for file in jsonfiles:
            with open(file,"r") as f:
                poems = json.load(f)
                if(poems["title"] == po):
                    populate_graph(item)
                    print("worked")























'''
                if(f.endswith(".json")):
                    with open(f,"r") as fi:
                        poems = json.load(fi)
                        populate_graph(item)'''



#fw.write(str(poem_node_list))
#print(len(poem_node_list))
#fw = open("ping.txt","w")
#to put each bayt of a certain poem in database graph.
#title = fi.readlines()[0]
    #author = fi.readlines()[1]
    #era = fi.readlines()[2]
'''
for poet_node in author_node_list:
    graph_db.create(poet_node)
    graph_db.create(rel(poet_node,"BORN_IN",asr))
    populate_who_wrote_what(poet_node)
    print(poet_node)

    #for poem_node in poem_node_list:
        #graph_db.create(poem_node)
        #graph_db.create(rel(poet_node,"WROTE",poem_node))
        #print(poem_node)
'''
'''
for subdir, dirs, files in os.walk(jsondir):
    for file in files:
        f = os.path.join(subdir, file)
        with open(f,"r") as fi:
            poems = json.load(fi)
            #for poet in authors:
            for poet_node in author_node_list:
                graph_db.create(poet_node)
                graph_db.create(rel(poet_node,"BORN_IN",asr))
                print(poet_node)

                for poem_node in poem_node_list:
                    graph_db.create(poem_node)
                    graph_db.create(rel(poet_node,"WROTE",poem_node))
                    print(poem_node)

                    for poem in poem_list:
                        #if(poet == poems["author"] and poem == poems["title"]):
                        if(poem == poems["title"]):
                            first_bayt = poems["abyat"][0]["bayt"]
                            first_sadr = poems["abyat"][0]["sadr"]
                            first_ajz = poems["abyat"][0]["ajez"]
                            first = Node("Bayt", name= first_bayt, sudr = first_sadr, ajez = first_ajz)
                            graph_db.create(first)
                            graph_db.create(rel(poem_node,"CONTAINS",first))


                    #graph_db.create(first)
                    #graph_db.create(rel(poem, "CONTAINS", first))
                    #print(first)

                        #poe = Node("Poet", name = poet)
                        #graph_db.create(poe)
                        #graph_db.create(rel(poe,"BORN_IN", asr))
                        #fw.write(str(poe))

                        #tit = Node("Title", title = poem)
                        #fw.write(str(tit))

                        #graph_db.create(tit)
                        #graph_db.create(rel(poe,"WROTE",tit))

                    #what if I create the poet node here, and his titles here, and actual poem nodes here!
                        #bayt = Node("Bayt", bayt= add props),

                        #first_bayt = poems["abyat"][0]["bayt"]
                        #first_sadr = poems["abyat"][0]["sadr"]
                        #first_ajz = poems["abyat"][0]["ajez"]
                        #first = Node("Bayt", name= first_bayt, sudr = first_sadr, ajez = first_ajz)
                        #graph_db.create(first)
                        #graph_db.create(rel(poem, "CONTAINS", first))
                        #print(poems["abyat"][0]["sadr"])
                        #print(poet)
                        #print(poem)
                        #print(poem)

#fw.close()
'''
                            #instead of printing, get the abyat of the specific poem and immediately write to graph db. check orgForGraph and test.py to make sure nothing is wrong.

        #graph_db.create(rel(poet,"BORN_IN", asr))
        #graph_db.create(poet)
        #print(poet)
