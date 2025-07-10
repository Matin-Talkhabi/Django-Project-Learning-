from django.shortcuts import render, redirect
from home.models import project , ticket ,footer
from django.contrib import messages
# Create your views here.
def home_app(request):
    if request.method == 'POST':
        name = request.POST.get('user')
        email = request.POST.get('email_user')
        title = request.POST.get('title')
        description = request.POST.get('description')
        if name and email and title and description:
            ticket.objects.create(name=name, email=email, title=title , description=description)
            messages.success(request, 'پیام شما با موفقیت ثبت شد.')
            return redirect('.')
        else:
            messages.error(request, 'لطفا همه فیلدها را پر کنید.')
    projects = project.objects.all()
    footers = footer.objects.all().last()
    return render(request , "landing_pro.html" , context={'projects' : projects , 'footers' : footers })