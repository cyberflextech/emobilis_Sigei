from django.http import HttpResponse
from django.template import loader

def sigei(request):
  template = loader.get_template('first.html')
  return HttpResponse(template.render())
