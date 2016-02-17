from django.shortcuts import render
from .constants import MEMBERS, CONNECTUS


def home(request):
	context = {'MEMBERS': MEMBERS, 'CONNECTUS': CONNECTUS}
	return render(request, 'core/index.html', context)