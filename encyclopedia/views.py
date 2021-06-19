from django.shortcuts import redirect, render
from markdown2 import Markdown
from random import choice

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):
    if util.get_entry(entry):
        markdown = Markdown()
        return render(request, "encyclopedia/entry.html", {
            'entry_name': entry,
            'content': markdown.convert(util.get_entry(entry))
        })
    else:
        return redirect('/error/not_found')

def edit(request, entry):
    return render(request, 'encyclopedia/edit.html', {
        'entry': entry,
        'content': util.get_entry(entry)
    })

def save_edit(request, entry):
    value = request.POST.get('edited')
    util.save_entry(entry, value)
    return redirect('/wiki/' + entry)

def new(request):
    return render(request, 'encyclopedia/new.html')

def save_new(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        entries = util.list_entries()
        if title in entries:
            return render(request, 'encyclopedia/already_exists.html', {
                'title': title
            })
        util.save_entry(title, content)
        return redirect('/wiki/' + title)

def error_404(request, exception):
    return render(request, 'encyclopedia/error_404.html')

def get_random(request):
    random_entry = choice(util.list_entries())
    return redirect('/wiki/' + random_entry)

def search(request):
    if request.method == 'POST':
        query = request.POST.get('q')
        results = []
        for entry in util.list_entries():
            if entry.lower() == query.lower():
                return redirect('/wiki/' + entry)
            elif query.lower() in entry.lower():
                results.append(entry)

        return render(request, 'encyclopedia/search_results.html', {
            'results': results
            })

