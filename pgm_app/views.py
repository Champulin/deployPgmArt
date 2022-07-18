from django.views import generic
from .models import Category, Project
# Create your views here.
class IndexListView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'projects_list'
    def get_queryset(self):
        return Project.objects.all().order_by('date')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_list'] = Category.objects.all().order_by('id')
        return context

class ProjectDetailView(generic.DetailView):
    model = Project
    template_name = 'project.html'
