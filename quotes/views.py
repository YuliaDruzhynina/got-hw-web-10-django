from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from .utils_mongo import get_mongodb
from .forms import QuoteForm, AuthorForm


def main(request, page=1):
    db = get_mongodb()
    quotes = db.quotes.find()
    # quotes = Quote.objects.all()
    # top_tags = Tag.objects.annotate(num_posts=Count('posts')).order_by('-num_posts')[:10]
    # print(top_tags)
    #quotes = list(db.quotes.find())  # Преобразуем курсор в список
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, 'quotes/index.html', context={'quotes': quotes_on_page})

@login_required
def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author_data = form.cleaned_data
            db = get_mongodb()
            db.authors.insert_one(author_data)
            return redirect('quotes:root')  #form.save() - default:sqlite5
    else:
        form = AuthorForm()
    
    return render(request, 'quotes/create_author.html', {'form': form})

@login_required
def create_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote_data = form.cleaned_data
            db = get_mongodb()
            db.quotes.insert_one(quote_data)
            return redirect('quotes:root')
    else:
        form = QuoteForm()

    return render(request, 'quotes/create_quote.html', {'form': form})


# @login_required
# def create_quote(request):
#     if request.method == 'POST':
#         form = QuoteForm(request.POST)
#         if form.is_valid():
#             quote_data = form.cleaned_data
#             tags = form.cleaned_data['tags']
#             author = form.cleaned_data['author']
#             db = get_mongodb()  
#             db.quotes.insert_one({
#                 'quote': quote_data['quote'],
#                 'tags': [str(tag.id) for tag in tags],
#                 'author': str(author.id)
#             })
#             return redirect('quotes:root')
#     else:
#         form = QuoteForm()

#     return render(request, 'quotes/create_quote.html', {'form': form})


