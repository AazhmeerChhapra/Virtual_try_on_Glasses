from django.shortcuts import render, get_object_or_404, HttpResponse
from django.http import JsonResponse
from store.models.category import Category
from django.urls import path

def quiz(request):

    return render(request, 'quiz.html')

# def quiz_view(request):
#     if request.method == 'GET':
#         selected_button1 = request.GET.get('selectedButton1')
#         selected_button2 = request.GET.get('selectedButton2')
#         selected_button3 = request.GET.get('selectedButton3')
#         selected_button4 = request.GET.get('selectedButton4')
#     male_responses = Category.objects.filter(recommendedFaceShape='Oval')
    
#     context = {
#         'male_responses': male_responses
#     }
    
#     return render(request, 'male_response.html', context)
    
def get_selected_button1(request):
    if request.method == 'GET':
        selected_button1 = request.GET.get('selectedButton1')
        selected_button2 = request.GET.get('selectedButton2')
        selected_button3 = request.GET.get('selectedButton3')
        selected_button4 = request.GET.get('selectedButton4')
    # Retrieve records where selected_button1 is "male"
    male_responses = Category.objects.filter(recommendedFaceShape=selected_button4)
    print("res")
    categories = Category.get_all_categories(

    )
    print(male_responses)
    
    context = {
        'male_responses': male_responses,
        'categories':categories

    }
    print(context)
    
    return render(request, 'male_response.html', context)
    
