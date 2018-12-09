'''
Created on Dec 9, 2018

@author: bpr
'''
import urllib
import re 

class Wydanie:
    def __init__(self, url):
        self.data = self.getDataFromUrl(url)
        self.date = self.getDate()
        self.title = self.getTitle()
        self.description = self.getDescription()
    
    def getDate(self):
        try:
            phrase = '"release-date">publikacja: '
            position = self.data.find(phrase)
            if(position==-1):
                raise ValueError('Exception in getDate() method. There is no such phrase in the url!')
            
            position += len(phrase)
            date = self.data[position : position+10]
            return date
            
        except Exception as error:
            print(error)
            return "null"
        
    def getTitle(self):
        m = re.search("<h1>.*</h1>", self.data)
        if m:
            title = m.group()
            return title[4:len(title)-5]
        return "null"

    def getDescription(self):
        start_phrase = '<div class="article-content">'
        end_phrase = '</div>'
        
        try:
            start_position = self.data.find(start_phrase)
            end_position = self.data.find(end_phrase, start_position)
        
            if(start_position==-1 or end_position == -1):
                raise ValueError('Error in getDescription() method. There is no such phrase in the url!')
        
            content = self.data[start_position+len(start_phrase):end_position]
            
            while True:
                m = re.search("<.*>", content)
                if m:
                    content = content.replace(m.group(),'')
                else:
                    break
            return content.strip()
        
        except Exception as error:
            print(error)
            return "null"
       
    def getDataFromUrl(self, url):
        f = urllib.urlopen(url)
        myUrl = f.read()
        return myUrl
       
        
def importUrls():
    filename = "posortowane.txt"
    file = open(filename, "r")
    lines = [line.rstrip('\n') for line in open(filename)]
    return lines



lines = importUrls()
a = Wydanie(lines[0])
print(a.title) 
    
    
    
    