from bs4 import BeautifulSoup
import urllib.request
import json
import os

#TODO: change the path for every 3asr, before procceed with other 3asr, change the files by adding big list,commas, and paranthesis! put the file in simplescripts to remove all deseased links! since there are thousands of files; apply paralellism with Pool and compare speed.

root_url = 'http://adab.com/'

def scrape_for_poem(url):
    webpage = urllib.request.urlopen(url)
    soup = BeautifulSoup(webpage.read())

    title = soup.findAll('title')
    table = soup.findAll('table')
    poemTableRows = table[5].findAll('tr')
    ID = table[4].findAll('td')[0].text[14:-1]
    era = table[3].findAll('a')[1].text

    authorAndTitle = title[0].text
    authorAndTitle = authorAndTitle.split(':')

    author = authorAndTitle[0].strip()
    name = authorAndTitle[1].strip()
    author = author[8:]

    poem = {"title":name, "author":author, "era":era, "id":ID, "abyat":[]}

    for row in poemTableRows:
        col = row.findAll('td')
        sudr = col[0].text
        ajz = col[-1].text
        poem["abyat"].append({"sadr":sudr, "ajez":ajz, "bayt":sudr+ ajz})
        #fw.write(sudr +"        "+ ajz + "\n")


    filename = '%s.json' %ID
    path = '/home/ramez/python/capstone/app/abbasi_json'
    fullpath = os.path.join(path,filename)

    with open(fullpath,"w") as outfile:
        json.dump(poem, outfile, ensure_ascii=False)

with open("abbas_leftover_url.txt") as f:
    #get the complete list that contains lists of poet poems. json was used because the list of lists has valid json syntax even tho its not json.
    all_poems = json.load(f)

for poet_collection in all_poems:
    #print(all_poems)
    #access each poem individually get url
    for poet_poem in poet_collection:
        index_url = poet_poem
        poem_url = root_url + index_url
        print(poem_url)
        attempt = 0
        while(attempt < 3):
            attempt +=1
            try:
                poem_json = scrape_for_poem(poem_url)
                break
            except urllib.request.HTTPError:
                break
            except urllib.request.URLError:
                continue
            except http.client.HTTPException:
                poem_json = scrape_for_poem(poem_url)
                print("save me pls")
                continue
        else:
            continue























#vvvvvv DISREGARD THE BELOW vvvvvv 28/3/15

#use table[4] for poem number if needed.
# Trim off the table header row
#tablerows = commodittTableRows[1:]

#for line in soup.findAll('a'):
 #   print(line.get('href'))
 #above prints links on page nicely! maybe solve the arabic letter problem!!



#NOTE: requests module doesnt read data that is in arabic, urllib does. that is why the links obtained in masscrap were retarted, cause the arabic letter was changed to something else!


#print(soup('table')[5].findAll('tr')[1].findAll('td')[1].string)

#print(soup('table')[6].prettify())

#poems = soup.findAll('td',{'class':'poem'})
#poems = soup.findAll('td')

#for eachpoem in poems:
    #print(eachpoem.string)
