from datetime import date
from django.shortcuts import render

def index(request):
    context = {
        'first_name': 'yousef',
        'last_name': 'sawwan',
        'student_id': 120210543,
        'address': 'northen gaza',
        'email': 'yousef2003sawwan@gmail.com',
        'dob': date(2003, 10, 16),
    }
    return render(request, 'pages/index.html', context)