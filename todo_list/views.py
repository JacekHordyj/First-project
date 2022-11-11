from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from todo_list.models import Task
from django.urls import reverse_lazy

# Create your views here.

class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kawrgs): # getting context data from request, overwriting method to get more data
        context = super().get_context_data(**kawrgs)# get all data
        context['tasks'] = context['tasks'].filter(user = self.request.user) # get original data from task and filter based on user from request
        context['count'] = context['tasks'].filter(complete = False).count() # count incomplete tasks, list was already filtered by user one line above
        
        search_input = self.request.GET.get('search-area') or '' # getting input from template search field
        if search_input:
            context['tasks'] = context['tasks'].filter( # if search input exists filter context by title containing phrase
                title__icontains = search_input)

        context['search_input'] = search_input #adding search input to context to send it back to template -> prevents from disappearing from searchbox after submit
        
        return context


class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'todo_list/task.html'

class TaskCreate(CreateView):
    model = Task
    fields = ['title','description', 'complete']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form): # overwriting CreateView class method "form_valid"
        form.instance.user = self.request.user # checking if user submitting form is user from request?
        return super(TaskCreate,self).form_valid(form) # returning everything from TaskCreate form with form_valid(form)

class TaskUpdate(UpdateView):
    model = Task
    fields = ['title','description', 'complete']
    success_url = reverse_lazy('tasks')


class TaskDelete(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')

def test_view(request):
    return render(request,'todo_list/test.html')
