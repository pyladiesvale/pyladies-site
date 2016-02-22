CRONOGRAMA = '''
Cronograma <br/>

Sábado, 9 de abril de 2016 - Palestras <br/>

10:00 - Café da manhã

11:00 - Palestra com pessoas muito legais <3

11:40 - Keynote com alguém importante

12:30 - Almoço

14:00 - Mais palestras com pessoas legais *_*

14:40 - Keynote com mais alguém importante

15:30 - Coffee Break

16:30 - Sorteios

17:00 - Encerramento
'''

'''
{% autoescape off %}{{ myhtml }}{% endautoescape %}
'''

SECTIONS = {
	"first": 
		[
			{"id": "about", "title": "PyLadies", 
				"body": ["O PyLadies é uma comunidade mundial que foi trazida ao Brasil com o propósito de instigar mais mulheres a entrarem na área tecnológica. Sua missão é educar e promover uma comunidade diversificada através da sensibilização, educação, conferência, eventos e reuniões sociais."]
			},
			{"id": "valeparaiba", "title": "Vale do Paraíba", 
				"body": ["Em construção..."]
			},
			{"id": "pyladiesvale", "title": "PyLadies Vale", 
				"body": ["Em construção..."]
			}
		],
	"second": 
		[
			{"id": "events", "title": "Eventos", 
				"body": ["Nosso primeiro evento ocorrerá no dia 09/04/16 das 10h às 17h no CEDEMP em São José dos Campos. Confira nossa agenda: ", CRONOGRAMA]
			}
		]
}

MEMBERS = [
	[
		{"nome": "Caroline", "status": "Estudante", "foto": "core/img/members/nobody.png",
			"socialnetworks": {"facebook": "...", "twitter": "...", "github": "..."}
		},
		{"nome": "Dally", "status": "Estudante", "foto": "core/img/members/nobody.png",
			"socialnetworks": {"facebook": "...", "twitter": "...", "github": "..."}
		},
		{"nome": "Ingrid", "status": "Estudante", "foto": "core/img/members/nobody.png",
			"socialnetworks": {"facebook": "...", "twitter": "...", "github": "..."}
		},
		{"nome": "Izabela", "status": "Estudante", "foto": "core/img/members/nobody.png",
			"socialnetworks": {"facebook": "...", "twitter": "...", "github": "..."}
		}				
	],[
		{"nome": "Jéssica", "status": "Estudante", "foto": "core/img/members/jessica.png",
			"socialnetworks": {"facebook": "...", "twitter": "...", "github": "..."}
		},
		{"nome": "Priscila", "status": "Estudante", "foto": "core/img/members/nobody.png",
			"socialnetworks": {"facebook": "...", "twitter": "...", "github": "..."}
		},
		{"nome": "Rodrigo", "status": "Estudante", "foto": "core/img/members/nobody.png",
			"socialnetworks": {"facebook": "...", "twitter": "...", "github": "..."}
		},
		{"nome": "Verônica", "status": "Estudante", "foto": "core/img/members/veronica.png",
			"socialnetworks": {"facebook": "...", "twitter": "...", "github": "..."}
		}		
	]
]

CONNECTUS = [
	{"link": "https://www.google.com.br/maps/place/S%C3%A3o+Jos%C3%A9+dos+Campos,+SP/@-23.1894443,-46.0030986,11z/data=!3m1!4b1!4m2!3m1!1s0x94cc4bb3858cc2e7:0xba25a33168f8c1", 
		"icon": "fa fa-map-marker fa-2x", 
		"description": "Vale do Paraíba - SP - Brasil"},
	{"link": "mailto:vale@pyladies.com", 
		"icon": "fa fa-envelope fa-2x", 
		"description": "vale@pyladies.com"},
	{"link": "https://github.com/pyladiesvale", 
		"icon": "fa fa-github fa-2x", 
		"description": "pyladiesvale"},
	{"link": "https://twitter.com/pyladiesvale", 
		"icon": "fa fa-twitter fa-2x", 
		"description": "@pyladiesvale"},
	{"link": "https://www.facebook.com/pyladiesvale", 
		"icon": "fa fa-facebook fa-2x", 
		"description": "fb.me/pyladiesvale"}
]
