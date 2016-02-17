from django.shortcuts import render
from .constants import MEMBERS


def home(request):
	context = {'MEMBERS': MEMBERS}
	return render(request, 'core/index.html', context)