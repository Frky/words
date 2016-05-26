
from django.shortcuts import render, HttpResponse

from website.models import Word
from website.forms import WordForm

def index(req):
    tpl = "words/index.html"
    ctxt = dict()

    word_form = WordForm(req.POST or req.GET or None)
    
    if word_form.is_valid():
        word_form.save()
        word_form = WordForm(None)
        
    ctxt["form"] = word_form
    ctxt["words"] = Word.objects.all()

    if len(ctxt["words"]) != 0:
        ctxt["last_word"] = Word.objects.latest("id")
        ctxt["start"] = max(ctxt["last_word"].id - 50, Word.objects.first().id)
        ctxt["stop"] = ctxt["last_word"].id
    else:
        ctxt["last_word"] = None
        ctxt["start"] = 0
        ctxt["stop"] = 0
    return render(req, tpl, ctxt)


def get_last_word(req):
    return HttpResponse(Word.objects.latest("id").id)

def ajax_words(req):
    tpl = "words/includes/words.html"
    ctxt = dict()
    ctxt["words"] = Word.objects.all()
    ctxt["last_word"] = Word.objects.latest("id")
    ctxt["start"] = max(ctxt["last_word"].id - 50, Word.objects.first().id)
    ctxt["stop"] = ctxt["last_word"].id
    return render(req, tpl, ctxt)
