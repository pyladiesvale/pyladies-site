#!/bin/bash

# O que esse script faz:
# - faz o commit da tua branch atual;
# - faz o merge dela com a sua master;
# - atualiza o repositório do git de ambas;
# - e faz o deploy no HEROKU;

# ATENÇÃO: 
# Esse script faz deploy no HEROKU, logo tenha configurado ele anteriormente,
# colocando o link do heroku no git local, com o nome de heroku mesmo.

# E CERTIFIQUE-SE QUE SEMPRE QUE FOR FAZER O DEPLOY, O DJANGO NÃO PODE ESTAR RODANDO. :)

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


# comandos
clear

echo ""

git status

git add .
git commit -m "$1"
git push origin $2

echo ""
echo "--> Mandado para o Github, na branch que estou utilizando atualmente (a $2)."
echo ""

git status

git checkout $3
git merge $2

echo ""
echo "--> Trocado com a branch master ($3) e feito o merge da branch atual ($2) com ela."
echo ""

git status

git push origin $3
git push heroku $3

echo ""
echo "--> Mandado as modificações da master ($3) para o GitHub e o Heroku."
echo ""

git status

git checkout $2

echo ""
echo "--> Voltei para a branch que estava utilizando (a $2)."
echo ""

git status

echo ""



# exemplo
#echo "Foram digitados $# parâmetros. São eles: $*."
#echo "O primeiro parâmetro foi: $1"
#echo "O nome do script é: $0"
