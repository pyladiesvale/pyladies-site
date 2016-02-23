CRONOGRAMA = '''		
		<div>
			<br/>
			<p style="color: #000000; font-size: 30px; font-weight: 500;"> 
				Cronograma 
			</p>

			<div class="body-cronograma">
				<p> Sábado, 9 de abril de 2016 - Palestras </p>

				<p> 10:00 - Café da manhã </p>

				<p> 11:00 - Palestra com pessoas muito legais <3 </p>

				<p> 11:40 - Keynote com alguém importante </p>

				<p> 12:30 - Almoço </p>

				<p> 14:00 - Mais palestras com pessoas legais *_* </p>

				<p> 14:40 - Keynote com mais alguém importante </p>

				<p> 15:30 - Coffee Break </p>

				<p> 16:30 - Sorteios </p>

				<p> 17:00 - Encerramento </p>
			</div>		
		</div>
	'''

SECTIONS = {
	"first": 
		[
			{"id": "about", "title": "PyLadies", 
				"body": ["O PyLadies é uma comunidade mundial que foi trazida ao Brasil com o propósito de instigar mais mulheres a entrarem na área tecnológica. Sua missão é educar e promover uma comunidade diversificada através da sensibilização, educação, conferência, eventos e reuniões sociais."],
				"body_scape": [""]
			},
			{"id": "valeparaiba", "title": "Vale do Paraíba", 
				"body": ["Em construção..."],
				"body_scape": [""]
			},
			{"id": "pyladiesvale", "title": "PyLadies Vale", 
				"body": ["Em construção..."],
				"body_scape": [""]
			}
		],
	"second": 
		[
			{"id": "events", "title": "Eventos", 
				"body": ["Nosso primeiro evento ocorrerá no dia 09/04/16 das 10h às 17h no CEDEMP em São José dos Campos. Confira nossa agenda: "],
				"body_scape": [CRONOGRAMA]
			}
		]
}

MEMBERS = [
	[
		{"nome": "Caroline", "status": "Estudante", "foto": "core/img/members/caroline.png",
			"socialnetworks": {"facebook": "...", "twitter": "...", "github": "..."}
		},
		{"nome": "Dally", "status": "Estudante", "foto": "core/img/members/dally.png",
			"socialnetworks": {"facebook": "...", "twitter": "...", "github": "..."}
		},
		{"nome": "Ingrid", "status": "Estudante", "foto": "core/img/members/ingrid.png",
			"socialnetworks": {"facebook": "...", "twitter": "...", "github": "..."}
		},
		{"nome": "Izabela", "status": "Estudante", "foto": "core/img/members/izabela.png",
			"socialnetworks": {"facebook": "...", "twitter": "...", "github": "..."}
		}				
	],[
		{"nome": "Jéssica", "status": "Estudante", "foto": "core/img/members/jessica.png",
			"socialnetworks": {"facebook": "...", "twitter": "...", "github": "..."}
		},
		{"nome": "Priscila", "status": "Estudante", "foto": "core/img/members/priscila.png",
			"socialnetworks": {"facebook": "...", "twitter": "...", "github": "..."}
		},
		{"nome": "Rodrigo", "status": "Estudante", "foto": "core/img/members/rodrigo.png",
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
