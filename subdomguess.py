#!/usr/bin/env python2.7
#coding=utf-8

#-Feito por Gabrielzw7. para fins educacionais
#-A simplicidade do programa reflete meu periodo de treinamento com a linguagem
#-Para o melhor funcionamento  utilize uma boa wordlist

import requests
import sys

#-validacao de argumentos

if len(sys.argv) != 3:
        print "\n\033[33m ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ \033[m"
        print "\033[33m  SubDomGuess - Uma ferramenta para Brute Force em Subdominios   \033[m"
        print "\033[33m ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ \033[m"
        print "\n\033[33m Feito por Gabriel W.\033[m"
        print "\033[33m Para o melhor funcionamento utilize uma boa wordlist... \033[m\n"
        print "\033[32m Modo de uso:\033[m"
        print "\033[35m ./subdomguess.py\033[m \033[32m https://www.site.com dns-wordlist\033[m"
        print "\n\033[33m ++++++++++++++++++++++++++ BRASIL +++++++++++++++++++++++++++ \033[m"
        sys.exit()

#-Alocando as entradas nas variaveis

url = sys.argv[1]
lista = sys.argv[2]

#-faz a leitura e tratamento da wordlist

l = open(lista, 'r')
for linhas in l.readlines():
        linhas = linhas.strip()                         #-remove o espaço da linha
        urlcomp = url.replace("www",linhas)             #-faz o tratamento da url

        try:

#-realizando requests

                resposta = requests.get(urlcomp)
                status = resposta.status_code
                print "%s \033[32m %s\033[m"%(urlcomp,status)
        except requests.exceptions.ConnectionError:     #-tratamento de erro
                print urlcomp + "\033[31m HOST OFF \033[m"

