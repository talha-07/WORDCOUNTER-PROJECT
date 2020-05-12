from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
    return render(request,'home.html')

def count(request):
    #below is just an example
    #fulltext = request.GET['fulltext']
    #print(fulltext)

    #by dictionay below
    fulltext = request.GET['fulltext']
    #to count how many words use below
    wordlist=fulltext.split()
    # to count how many times a word appears use below
    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            #increase
            worddictionary[word] +=1
        else:
            #add to the dictionary
            worddictionary[word] = 1

    sortedwords=sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'sortedwords':sortedwords})

def about(request):
    return render(request,'about.html')
