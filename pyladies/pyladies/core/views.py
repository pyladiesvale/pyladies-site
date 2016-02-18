from django.shortcuts import render
from .constants import MEMBERS, CONNECTUS, SECTIONS


def home(request):
	context = {'MEMBERS': MEMBERS, 'CONNECTUS': CONNECTUS, 'SECTIONS': SECTIONS}
	return render(request, 'core/index.html', context)