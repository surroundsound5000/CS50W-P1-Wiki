from django.shortcuts import render

from . import util
from . import markdown2

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    this_entry = util.get_entry(title)
    try: return render(request, "encyclopedia/entry.html", {
            "title": title,
            "body": markdown2.markdown(this_entry)
        })
    except: return render(request, "encyclopedia/notfound.html", {
        "title" : title
    })

def search(request):
    search = request.GET.get("q")
    # Render the entry if available
    #if util.get_entry(search):
    #     return entry(request, search)
    entries = util.list_entries()
    if search in entries:
        return entry(request, search)
    results = []
    for match in entries:
        if search in match: results.append(match)
    return render(request, "encyclopedia/search.html",{
        "search" : search,
        "results" : results
    })

def new(request):
    return render(request, "encyclopedia/new.html")

def save_new(request):
    title = request.GET.get("title")
    entries = util.list_entries()
    if title in entries:
        return render(request, "encyclopedia/new.html",{
            "error" : ["A page with this title already exists."],
        })
    content = "#" + title + "\n\n" + request.GET.get("content")
    util.save_entry(title, content)
    return entry(request, title)

def edit(request):
    title = request.GET.get("title")
    this_entry = util.get_entry(title)
    return render(request, "encyclopedia/edit.html", {
            "title": title,
            "body": this_entry
        })


def save_edit(request):
    title = request.GET.get("title")
    content = request.GET.get("content")
    print("Title=", title, "\nContent=", content)
    util.save_entry(title, content)
    return entry(request, title)
