from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html',)


def count(request) :
    text = request.GET['fulltext']
    text_list = text.split()
    text_count = len(text_list)



    word_dict = {}

    #                   my_method
    # text_set = set(text_list)
    # set_count = len(text_set)
    # for i in text_set:
    #     nums.update({i : text_list.count(i)})
    # max_val = max(nums.values())
    # key = 0
    # for word, word_count in nums.items():
    #     if word_count == max_val:
    #        key = word

    for word in text_list:
        if word in word_dict.keys():
            num = word_dict.get(word)
            num +=1
            word_dict[word] = num
        else:
            word_dict[word] = 1


    return render(request, 'count.html', {'text_count':text_count, 'nums':max(word_dict.values()),
                                      'sorted': sorted(word_dict.items(),key=operator.itemgetter(1),reverse=True) })


def about(request):
    return render(request,'about.html',)