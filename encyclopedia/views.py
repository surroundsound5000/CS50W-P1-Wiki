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