from django.shortcuts import render

from . import util
from . import markdown2

def index(request):
    print(request)
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    entry = util.get_entry(title)
    try: return render(request, "encyclopedia/entry.html", {
            "title": title,
            "body": markdown2.markdown(entry)
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
    for entry in entries:
        if search in entry: results.append(entry)
    return render(request, "encyclopedia/search.html",{
        "search" : search,
        "results" : results
    })