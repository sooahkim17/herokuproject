from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def result(request):
    text=request.GET['fulltext']
    words=text.split()
    string=""
    for word in words:
        string+=word
    strings=string.split(".")
    string=""
    for st in strings:
        string+=st
    strings_count=len(string)
    count=len(words)
    word_dictionary={}

    for word in words:
        if word in word_dictionary:
            word_dictionary[word]+=1
        else:
            word_dictionary[word]=1

    return render(request,'result.html',{'full':text,'count':count,'dictionary':word_dictionary.items(),'strings_count':strings_count})