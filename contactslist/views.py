
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy,reverse
from django.http import HttpResponse
from django.views import View
from contactslist.models import Contact
from contactslist.forms import CreateForm
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

class MainList(LoginRequiredMixin, ListView):
    model = Contact
    template_name = "contactslist/list.html"



class Detail(LoginRequiredMixin, DeleteView):
    model = Contact
    template_name = "contactslist/detail.html"
    def get(self,request, pk):
        x = Contact.objects.get(id = pk)
        context = {'contact':x}
        return render(request, self.template_name, context)



class Create(LoginRequiredMixin, View):
    template_name = "contactslist/form.html"
    success_url = reverse_lazy('contact:all')

    def get(self, request):
        form = CreateForm()
        context = {'form':form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = CreateForm(request.POST, request.FILES or None)

        if not form.is_valid():
            context = {'form':form}
            return render(request, self.template_name, context)
        #给own字段赋值
        contact = form.save(commit = False)
        contact.owner = self.request.user
        contact.save()
        return redirect(self.success_url)



class Upate(LoginRequiredMixin, UpdateView):
    template_name = "contactslist/form.html"
    success_url = reverse_lazy('contactslist:all')
    def get(self, request, pk):
        contact = get_object_or_404(Contact, id = pk, owner = self.request.user)
        form = CreateForm(instance = contact)
        context = {'form':form}
        return render(request, self.template_name, context)
    
    def post(self, request, pk):
        contact = get_object_or_404(Contact, id = pk, owner = self.request.user)
        form = CreateForm(request.POST, request.FILES or None , instance=contact)

        if not form.is_valid():
            context = {'form':form}
            return render(request, self.template_name, context)
        contact = form.save(commit = False)
        #此处因为owner已经被赋值,所以直接保存
        contact.save()



class Delete(LoginRequiredMixin, DeleteView):
    model = Contact
    template_name = "contactslist/delete.html"


def stream_file(request, pk):
    contact = get_object_or_404(Contact, id=pk)
    response = HttpResponse()
    response['Content-Type'] = contact.content_type
    response['Content-Length'] = len(contact.picture)
    response.write(contact.picture)
    return response



