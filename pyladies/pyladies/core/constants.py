__CRONOGRAMA__ = '''
		<div style="margin-top: 25px;">
			<p style="color: #000000; font-size: 35px; font-weight: 500;"> 
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

__INSCRICAO__ = '''
		<div class="pls-red-box">
			<p class="pls-red-box-text"> 
				As inscrições para já estão abertas. 
			</p>
			<p class="pls-red-box-text">
				<a style="color: #CA0000;" href="https://www.eventbrite.com.br/e/1o-encontro-pyladies-vale-tickets-22499770419">
					Clique aqui 
				</a>
					para se inscrever. <3
			</p>
		</div>
	'''

__COD_CONDUTA__ = 	'''
		<div style="font-size: 25px; color: #999999; font-weight: 300; margin-top: 30px;">
			<a style="color: #CA0000;" href="https://github.com/pythonbrasil/codigo-de-conduta">
				Clique aqui 
			</a>
				para acessar o Código de Conduta utilizado por nós. :D
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
				"body": ["O Vale do Paraíba é uma região sócio-econômica que abrange o leste do estado de São Paulo e o oeste do estado do Rio de Janeiro, que se destaca por concentrar uma parcela considerável do P.I.B do Brasil. A partir da década de 1950, a região industrializou-se rapidamente, nesta época destaca-se a criação do Instituto Tecnológico da Aeronáutica, a consequente instalação da indústria aeronáutica com a criação da Embraer em São José dos Campos e a fábrica veicular Volkswagen e eletrônicos LG, ambas na cidade de Taubaté. Com isso, a demanda por conhecimento tecnológico aumentou exponencialmente, contudo a participação feminina no meio tecnológico sempre foi baixa."],
				"body_scape": [""]
			},
			{"id": "pyladiesvale", "title": "PyLadies Vale", 
				"body": ["A ideia do PyLadies Vale ocorreu logo após o Python Vale 2015, mas só começou a ser organizado depois do Django Girls SJC, que ocorreu dentro do circuito Python Brasil 2015. Essa comunidade surgiu com o intuito de suprir a necessidade de uma comunidade feminina que consiga ajudar e orientar pessoas a entrarem ou permanecerem na área tecnológica."],
				"body_scape": [""]
			}
		],
	"second": 
		[
			{"id": "events", "title": "Eventos", 
				"body": ["Nosso primeiro evento ocorrerá no dia 09/04/16 das 10h às 17h no CEDEMP em São José dos Campos. Confira nossa agenda: "],
				"body_scape": [__CRONOGRAMA__,__INSCRICAO__]
			},
			{"id": "codcond", "title": "Código de Conduta", 
				"body": [""],
				"body_scape": [__COD_CONDUTA__]
			}
		]
}

MEMBERS = [
	[
		{"nome": "Caroline", "status": "Estudante", "foto": "core/img/members/caroline.png",
			"socialnetworks": {"facebook": "https://www.facebook.com/karoly.chan", 
								"twitter": "https://twitter.com/Karoly_chan", 
								"github": "https://github.com/karolychan"}
		},
		{"nome": "Dally", "status": "Estudante", "foto": "core/img/members/dally.png",
			"socialnetworks": {"facebook": "...", 
								"twitter": "...", 
								"github": "..."}
		},
		{"nome": "Ingrid", "status": "Estudante", "foto": "core/img/members/ingrid.png",
			"socialnetworks": {"facebook": "https://www.facebook.com/senaingrid", 
								"twitter": "https://twitter.com/ingridsena", 
								"github": "https://github.com/senaingrid"}
		},
		{"nome": "Izabela", "status": "Estudante", "foto": "core/img/members/izabela.png",
			"socialnetworks": {"facebook": "https://www.facebook.com/izabela.dossantosguerreiro", 
								"twitter": "https://twitter.com/izaguerreiro", 
								"github": "https://github.com/izaguerreiro"}
		}				
	],[
		{"nome": "Jéssica", "status": "Estudante", "foto": "core/img/members/jessica.png",
			"socialnetworks": {"facebook": "...", 
								"twitter": "...", 
								"github": "..."}
		},
		{"nome": "Priscila", "status": "Estudante", "foto": "core/img/members/priscila.png",
			"socialnetworks": {"facebook": "https://www.facebook.com/priscilaharaujo", 
								"twitter": "...", 
								"github": "https://github.com/priscilaaraujo92"}
		},
		{"nome": "Rodrigo", "status": "Estudante", "foto": "core/img/members/rodrigo.png",
			"socialnetworks": {"facebook": "...", 
								"twitter": "https://twitter.com/rmmariano0", 
								"github": "https://github.com/rmmariano"}
		},
		{"nome": "Verônica", "status": "Estudante", "foto": "core/img/members/veronica.png",
			"socialnetworks": {"facebook": "https://www.facebook.com/veronicka.ve", 
								"twitter": "https://twitter.com/Veronicka_Moon", 
								"github": "https://github.com/veronicka"}
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
