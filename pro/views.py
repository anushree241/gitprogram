from django.http import HttpResponse

def home(request):
    return HttpResponse("""
        <h1>Welcome to My Django Project</h1>
        <p>Django project is working successfully!</p>
    """)