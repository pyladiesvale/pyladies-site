from django.shortcuts import render
from .constants import MEMBERS, PATROCINADORES, CONNECTUS, SECTIONS


def home(request):
	context = {'MEMBERS': MEMBERS, 'PATROCINADORES': PATROCINADORES,
				'CONNECTUS': CONNECTUS, 'SECTIONS': SECTIONS}
	return render(request, 'core/index.html', context)