from django.shortcuts import render
from django.http import HttpResponse

def home(request):

    peoples=[
        {'name':'Roman lamichhane','age':'20'},
        {'name':'Rohan sharma','age':'16'},
        {'name':'Agraj sigdel','age':'30'}
    ]

    for people in peoples:
      if people['age'] :
        print("yes")

    vegetables = ['pumpkins','Tomato','potato']

    text="""
         Lorem, ipsum dolor sit amet consectetur adipisicing elit. Fugit, dolore. Blanditiis laboriosam quod maiores tempore id, eius animi placeat! Repellat quae expedita aut, exercitationem omnis a vero similique provident deserunt atque quod amet illum adipisci impedit tempora culpa temporibus natus architecto eligendi autem itaque nisi numquam odit. Ipsum assumenda temporibus dicta delectus vero, soluta placeat quisquam. Repellat, impedit! Iure rem sapiente consequatur fugit ipsum voluptas veritatis. Fuga inventore alias ullam maxime ipsam odit officiis voluptates culpa consequuntur incidunt ea cupiditate odio non, cum est modi vitae consectetur illum? Dignissimos, dicta earum. Consectetur esse quod error aut? Molestias id est velit!
"""
    
    return render(request,"home/index.html", context={'page':'Django 2024 course','peoples':peoples, 'text':text,'vegetables':vegetables},)
def about(request):
    context={'page':'About'}
    return render(request,"home/about.html",context)

def contact(request):
    context={'page':'contact'}

    return render(request,"home/contact.html",context)

def success_page(request):
    print("b" * 10)
    return HttpResponse("This is another page")
