from django.shortcuts import render
# from .forms import PostForm
from django.shortcuts import redirect
from .models import Town
import sqlite3


def mainPage(request):
    connect = sqlite3.connect('tours.db')
    cursor = sqlite3.Cursor(connect)
    cursor.execute('''SELECT Counries.Name, Towns.Name FROM Towns, Counries
    WHERE Towns.id_country = Counries.id
    ''')
    data = cursor.fetchall()
    towns= []
    countries = []
    for i in data:
        if i[0] in countries:
            continue
        else:
            countries.append(i[0])
    for i in range(len(countries)):
        a=[]
        for j in range(len(data)):
            if countries[i] == data[j][0]:
                a.append(data[j][1])
        towns.append(a)
    dct = {}
    for i in range(len(countries)):
        dct[countries[i]] = towns[i]
    # count = []
    # for i in range(len(countries)):
    #     count.append(i)

    connect.close()
    return render(request, 'main/index.html', {'towns' : towns, 'countries' : countries})


# def postForm(request):
#     if request.method == "post":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             postDetail(request)
#     else:
#         form = PostForm()
#     return render(request, 'main/post_form.html', {'form': form})


def postDetail(request):
    return redirect('postDetail', pk=post.pk)