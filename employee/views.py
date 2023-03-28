from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from employee.forms import myFormSet,my_form  
from django.urls import reverse_lazy
from django.views.generic import  TemplateView
from employee.models import Employee  
from django.forms import ModelForm

#Create your views here.  
def emp(request):
    template_name = 'index.html'
    formset = myFormSet(queryset=Employee.objects.none())
    
    if request.method == 'POST':
        formset = myFormSet(data=request.POST or None)
        if formset.is_valid():
            for form in formset:
                form.save()
                print(form.data)
            return redirect('/show')
    return render(request, template_name, {
    'formset': formset, 
    })
    # return render(request, template_name, {
    #     'formset': formset,
    #     'heading': heading_message,
    # })


# class emp(TemplateView):
#     template_name = "index.html"

#     def get(self, *args, **kwargs):
#         formset = myFormSet(queryset=Employee.objects.none())
#         return self.render_to_response({'my_formset': formset})

    
#     def post(self, *args, **kwargs):

#         formset = myFormSet(data=self.request.POST)
#         if formset.is_valid():
#             for i in formset:
#                 i.save()
#             return redirect("/show")
#         return self.render_to_response({'my_formset': formset})


def show(request):  
    employees = Employee.objects.all()  
    return render(request,"show.html",{'employees':employees})  

def edit(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee})  

def update(request, id):  
    var = Employee.objects.get(id=id) 
    form=my_form(instance=var)
    print(form)
    if request.method == 'POST':
        form = my_form(request.POST,instance=var)
        # print(form.data)
        if form.is_valid():  
            form.save()  
        # else:
        #     print(form.data)
        return redirect("/show")  
    context = {
        'form': form,
    }
    return render(request, 'edit.html', context)  

    # mymember = Employee.objects.get(id=id)
    # template = loader.get_template('index.html')
    # context = {
    # 'mymember': mymember,
    # }
    # return HttpResponse(template.render(context, request))
    # data = Employee.objects.get(id=id) 
    # form = myFormSet                                                              

    # if request.method == "POST":
    #     form = Employee(request.POST, instance=data)
    #     if form.is_valid():
    #         form.save()
    #         return redirect ('/show')
    # context = {
    #     "form":form
    # }
    # return render(request, '/show', context)

def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/show") 