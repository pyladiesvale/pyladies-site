from django.shortcuts import render
from .constants import MEMBERS


def home(request):
	context = {'MEMBERS': MEMBERS}
	return render(request, 'index.html', context)