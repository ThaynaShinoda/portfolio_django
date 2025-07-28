from django.views import generic
from portfolio.models import Project


class PostView(generic.ListView):
  queryset = Project.objects.filter(status=1).order_by('-created_on')
  template_name = 'index.html'
  context_object_name = 'post_list'

class PostDetail(generic.DetailView):
  model = Project
  template_name = 'post_detail.html'
  context_object_name = 'project'