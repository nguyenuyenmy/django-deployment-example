from django.shortcuts import render
from appTwo.forms import newUserForm

# Create your views here.
def homepage(request):
    homepage_dict = {'homepage_insert': 'Homepage'}
    return render(request, 'appTwo/homepage.html', context=homepage_dict)

def help(request):
    my_dict = {'insert_me': "This is the help page."}
    return render(request, 'appTwo/help.html', context=my_dict)

def users(request):
    form = newUserForm()
    if request.method == "POST":
        form = newUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return homepage(request)
        else:
            print('ERROR FORM INVALID')

    return render(request, 'appTwo/users.html', {'form':form})