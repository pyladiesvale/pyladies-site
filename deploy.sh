#!/bin/bash

# O que esse script faz:
# - faz o commit da tua branch atual;
# - faz o merge com a sua master;
# - atualiza o repositório do git;
# - e faz o deploy no HEROKU;

# ATENÇÃO: 
# Esse script faz deploy no HEROKU, logo tenha configurado ele anteriormente,
# colocando o link do heroku no git local, com o nome de heroku mesmo.

# Argumentos:
# primeiro argumento: mensagem do commit
# segundo argumento: nome da branch atual
# terceiro argumento: nome da sua branch master
# exemplo:
# ./test.sh "mensagem do commit aqui" r_1.0.4 master


function help_test(){
	echo ""
	echo "--> Precisa inserir no mínimo 3 argumentos."
	echo ""
	echo "--> Primeiro argumento: mensagem do commit"
	echo "--> Segundo argumento: nome da branch atual"
	echo "--> Terceiro argumento: nome da sua branch master"
	echo ""
	echo '--> Exemplo: ./test.sh "mensagem do commit aqui" r_1.0.4 master'
	echo ""
}


# $# é a quantidade de argumentos passados
# -lt significa "no mínimo", "pelo menos", "menos que". (less than)
# logo, precisa passar no mínimo 3 argumentos no script
if [ $# -lt 3 ]; then
	help_test
	exit 1
	# exit 1 é para fechar o script
fi

# echo "arg1 = $1"
# echo "arg2 = $2"
# echo "arg3 = $3"


# comandos git
git add .
git commit -m "$1"
git push origin $2

echo "Mandado para o Github, na branch que estou utilizando."

git status

git checkout $3
git merge $2

echo "Feito o merge da branch atual com a master."

git status

git push origin $3
git push heroku $3

echo "Mandado as modificações da master para o GitHub e o Heroku."

git status

git checkout $2

echo "Voltando para branch que estava utilizando."

git status




#echo "Foram digitados $# parâmetros. São eles: $*."
#echo "O primeiro parâmetro foi: $1"
#echo "O nome do script é: $0"
