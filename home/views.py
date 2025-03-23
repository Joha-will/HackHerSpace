from django.shortcuts import render, redirect
import json
from django.conf import settings
import os


def home(request):
    '''
    Render Homepage
    '''
    return render(request, 'home/index.html')

def women_tech(request):
    '''
    Render women in tech page
    '''
    return render(request, 'home/women_in_tech.html') 

def contact(request):
    '''
    Render Team page
    '''
    return render(request, 'home/contact.html')  # Render the team.html template

def questions(request):
    # Load the JSON file
    json_file_path = os.path.join(settings.BASE_DIR, 'home/static/data/faq.json')
    with open(json_file_path, 'r') as file:
        faq_data = json.load(file)

    if request.method == "POST":
        # Get form data
        heading = request.POST.get("heading")
        question = request.POST.get("question")

        # Save the question temporarily (for admin approval)
        temp_file_path = os.path.join(settings.BASE_DIR, 'home/static/data/temp_questions.json')
        if os.path.exists(temp_file_path):
            with open(temp_file_path, 'r') as temp_file:
                temp_questions = json.load(temp_file)
        else:
            temp_questions = []

        temp_questions.append({"heading": heading, "question": question})
        with open(temp_file_path, 'w') as temp_file:
            json.dump(temp_questions, temp_file, indent=4)

        # Redirect to the same page with a success message
        return redirect('questions')

    return render(request, 'home/questions.html', {'faq_data': faq_data})  # Render the questions.html template