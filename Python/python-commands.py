--------------------------------- MUNDO 01 - CURSO EM VIDEO ----------------------------------------------------------------------------------------
*/ Variáveis ---------------------------------------------------------------------------------------------------------------------------------------

nome = 'ricardo' || nome é a variavel, entre aspas a mensagem que a variavel aloca
nome = input('Qual seu nome?') || o usuario define a variavel atraves do comando input

  |Variáveis aceitas ------|
  |anderlinenofim_ =       |
  |_anderlinenafrente =    |
  |com_acentuação =        |
  |letraenumber1           |
  |------------------------|



/* --------------------------------------------------------------------------------------------------------------------------------------------------

*/ Imprimir na tela ---------------------------------------------------------------------------------------------------------------------------------

print('mensagem') || imprime mensagem = mensagem
print('mensagem {}'.format(variavel)) || o sinal {} é uma mascara que é substituido posteriormente por uma variavel atraves do comando .format 
print('mensagem {:.3f}'.format(variavel)) || :.3f - exibe 3 casas decimais
print('mensagem {:3}'.format(variavel)) || :3 - exibe 3 casas no numero
print('A soma é {}, \n o produto é {} \n e a divisao é {:.3f}'.format(s, p, d)) || \n - quebra de linha
print('mensagem {}'.format(variavel), end=' ') || end=' ' - para nao haver quebra de linha no caso de mais de uma funcao print


|Utilizando marcadores:--|
|%d || numeros inteiros  |
|%s || strings           |
|%f || numeros decimais  |
|------------------------|

ex com marcadores:
nome = 'Joao'
idade = 22
grana = 51.34
print('%s tem %d anos e R$%5.2f no bolso.' %(nome, idade, grana))

Num Inteiros %d:
'%03d' %variavel || exibe o numero com 3 posições, completando com 0 a esquerda caso nao hajam 3 posicoes
'%3d' %variavel  || exibe o numero com 3 posicoes, sem completar com 0 mas deixando espaco vazio a esquerda
'%-3d' %variavel || exibe o numero com 3 posicoes, sem completar com 0 mas deixando espaco vazio a direita

Num Decimais %f:
utilizaremos 2 valores entre o simbolo de % e a letra f onde, o primeiro valor indica o tamano total em caracteres a reservar e o segundo o numero de casas decimais.
'%5.2f'% '%variavel' || exibe o num com 2 casa decimais

/* ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*/ Tipos primitivos (declarar variavel) --------------------------------------------------------------------------------------------------------------------------------------

int() || numeros inteiros
float() || numeros reais (pontos flutuantes)
bool() || valores boleanos (verdadeiro e falso)
str() || strings (letras)

variavel.isalpha() || o comando is vem apos a variavel e existem varias possibilidades para checar se a variavel possui caracter alpha numerico, letras maiusculas etc ...
variavel.isnumber() 


ex:

varial = int(input('Digite um num inteiro')) || int() declara a variavel num inteiro, input() dentro de int() interage com usuario

/* ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*/ Operadores aritmeticos ----------------------------------------------------------------------------------------------------------------------------------------------------

+        || adição 
-        || subtração
*        || multiplicação
/        || divisão
**       || potência
pow(4,2) || potência
//       || divisao inteira
%        || resto da divisão

  |Ordem de precedencia-- |
  |1º = ()                |
  |2º = **                |
  |3º = * || / || // || % | 
  |4º = + || -            |
  |-----------------------|

/* -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*/Utilizando Módulos -------------------------------------------------------------------------------------------------------------------------------------------------------------------------

https://www.youtube.com/watch?v=oOUyhGNib2Q&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=24 (aula de modulos)

import modulo || importa todo o módulo - import é bem generalista
 ex: import math  || importa todo módulo math
   chamando função - ex: math.ceil
from modulo import função     || 'from * import *' importa função específica da módulo
 ex: from math import sqrt    || importa apenas a função sqrt (raiz quadrada) do módulo math
   chamando função - ex: ceil (neste caso quando importamos uma funcao especifica nao mencionamos a biblioteca 
from datetime import datetime
variavel = datetime.now().year #pegando ano atual

  |Módulo (math) -------------------------------------|
  |ceil      || arredendo p/ cima                     |
  |floor     || arredonda p/ baixo                    |
  |trunc     || trunca o numero (retira os decimais)  |
  |pow       || potencia                              |
  |sqrt      || raiz quadrada                         |
  |factorial || fatorial                              |
  |---------------------------------------------------|

  |Módulo (random) --------------------------------------|
  |random.randint(a,b) || retorna um numero int aleatorio|


**** utilizando funções do módulo (caso generalista - import math) **************************************************************************************************************************

Quando todo o módulo é importado, para utilizar a função desejada é necessario chamar antes o módulo importado e depois a função a ser utilizada
ex:
	variavel_2 = math.sqrt(variavel_1) || raiz quadrada da variavel_1 utilizando um modulo da biblioteca math
	print('Raiz de {} é {}'.format(variavel, math.ceil(variavel)) || o modulo pode ser utilizado tambem dentro da funcao .format, neste caso ceil arredonda para cima o valor da variavel
*********************************************************************************************************************************************************************************************

**** utilizando funções do módulo (caso específico - from import) **********************************************************************************

Quando importamos apenas a função desejada, não é necessario chamar o módulo antes da função
ex:

	variavel_2 = sqrt(variavel_1) || raiz quadrada da variavel_1
	print('Raiz de {} é {}'.format(variavel, floor(variavel)) || arredonda variavel p/ baixo
****************************************************************************************************************************************************


/* -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

/*Manipulando Texto --------------------------------------------------------------------------------------------------------------------------------------------------------------------------

obs: a primeira posição de uma str é a 0
 variavel = 'Curso em Video Python'
             0123456789 ...      20

Fatiando String:

variavel[9]      || imprime a posição 10 da string 
variavel[9:14]   || imprime da posição 9 à 13
variavel[9:21:2] || imprime da posicao 9 a 21 porem saltando de 2 em 2 casas
variavel[:5]     || omitindo o inicio ele começa do caracter 0 = [0:5]
variavel[15:]    || omitindo o final ele termina no ultimo caracter
variavel[9::3]   || começa no 9, vai ate o final, pulando de 3 em 3 caracteres

obs: podemos utilizar valores negativos para representar posições a partir da direita. Assim -1 é o ultimo caractere, -2 o penultimo e assim por diante...
ex:
s = 'ABCDEFGHI'
print(s[-5:7]) --> EFG
print(s[-2:-1]) --> H


Analisando String:

len(variavel)              || comprimento da frase
variavel.count('o')        || conta quantas vezes tem a letra o (nesse caso minuscula, pois o python diferencia maiusculo de minusculo)
variavel.count('o', 0, 13) || contagem de letra com fatiamento, limitando a busca entre os caracteres 0 e 12
variavel.find('deo')       || diz qual posição começa a busca, nesse caso as letras deo
'Curso' in variavel        || busca a palavra, neste caso 'Curso' na string, e retorna o valor True or False

obs: se colocar o nome de uma string que nao exista na busca do find o programa retorna o valor de -1

Transformação:

variavel.replace('Python', 'Android') || substitui a palavra neste caso Python por Android, dentro da string
variavel.upper()                      || coloca os caracteres em maiusculo
variavel.lower()                      || coloca os caracteres em minusculo 
variavel.capitalize()                 || coloca todos os caracteres em minusculo, e apenas o primeiro caracter (pos 0) fica maiusculo.
variavel.title()                      || coloca todos os caracteres em minusculo, e torna maiusculo apenas o caracter de inicio de cada palavra (ex: Curso Em Video Python)
variavel.strip()                      || remove os espaços no inicio e fim da string
variavel.rstrip()                     || remove os espaços no fim da string (r = right)
variavel.lstrip()                     || remove os espaços no inicio da string (l = left)

Divisão e Junção:

variavel.split()         || divide a string com base nos espaços, gerando uma lista com novas strings
' '.join(variavel)       || junta em uma unica string. (o ' ' é para colocar um espaço entre as strings, posso colocar outros operadores. ex: '-'.join(variavel) || nesse caso a juncao é separada por tracinhos (-) e nao espaços.


/* -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

/* Condições (If/Else) -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

if condicao:
  print ...	
elif condicao:
  blalbalbal
else:
  print ...

obs: chama-se identação as linhas de comando mais afastadas, quer dizer que elas fazem parte de algum bloco condicional (if/else)

if (x==y) and (x!=z) or ... --> [ and = && e or = || ] (e, ou - c++)


/* -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

/* Condições de Repetição: -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

while condicao:
  print ...

|ex: Imnpressao de numeros pares de 0 ate num digitado por usuario-|
|fim = int(input('digite um num: '))                               | 
|x = 0                                                             |
|while x <= fim:                                                   |
|  if x%2 == 0:                                                    | 
|    print(x)                                                      |
|  x = x + 1                                                       |
|------------------------------------------------------------------|

|ex: Interrompendo a repetição ------------------------------------|
|s = 0                                                             | 
|while True:                                                       |
|   v = int(input('Digite um num p/ somar ou 0 p/ sair: '))        |                                           
|     if v == 0:                                                   | 
|     break                                                        |
|   s = s + v                                                      |
|print(s)                                                          |
|------------------------------------------------------------------|

/* ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

/* Cores no Terminal -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Padrao ANSI: (responsavel pelas cores)

\033[*m  --> representacao de cores, onde tem o * preencheremos com caracteristicas para o texto

\033[style; text; backgroundm --> colocaremos um cod para stylo;
 ex: \033[0;33;44m



 |style;(opçoes de estilo de texto) --|   |text;(cores do texto) ----|   |background;(cores de background) -----|                            
 |0 none (nenhum stylo)               |   |30 branco                 |   |40 branco                             |
 |1 bold (negrito)                    |   |31 vermelho               |   |41 vermelho                           |
 |4 underline (sublinhado)            |   |32 verde                  |   |42 verde                              |
 |7 negativo (inverte com background) |   |33 amarelo                |   |43 amarelo                            |
 |------------------------------------|   |34 azul escuro            |   |44 azul escuro                        |
                                          |35 roxo (magenta)         |   |45 roxo (magenta)                     |
                                          |36 azul claro (ciano)     |   |46 azul claro (ciano)                 |
                                          |37 cinza                  |   |47 cinza                              |
                                          |--------------------------|   |--------------------------------------|

ex: print('\033[4;30;45m Olá, Mundo! \033[m') -> obs: o fim e pra limitar ao texto, caso nao colocar o \033.. no fim ele colore toda a linha do terminal


|Criando sistema de cores: -----------------------------------------------------------------------------------------------------| 
|                                                                                                                               |
|nome = 'Ricardo'                                                                                                               |
|cores = {'limpa':'\033[m', 'azul':'\033[34m', 'amarelo':'\033[33m', 'pretoebranco':'\033[7;30m'} #cria um sistema de cores     |
|print('Olá! Muito prazer em te conhecer, {}{}{}'.format(cores['pretoebranco'], nome, cores['limpa'])                           |
|                                                                                                                               |
|-------------------------------------------------------------------------------------------------------------------------------|

/* -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

--------------------------------- MUNDO 02 - CURSO EM VIDEO -------------------------------------------------------------------------------------------------------------------------------------

/* Condições aninhadas --------------------------------------------------------------------------------------------------------------------------------------------------------------------------

if condicao:
   print ...
elif condicao:
   funcao ...
	if condicao:
	funcao..
	elif condicao:
	funcao ..
else:
   funcao ...

/* ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

/* Estrutura de repetição for ----------------------------------------------------------------------------------------------------------------------------------------------------------------------

for variavel in range(1,10): #range é o intervalo de iteração do laço de repetição - for
   função ...

for c in range(0,3): #repete 3 vezes, c é a variavel - contador
   funcao...

 obs: o range nao considera o ultimo numero, ou seja, (0,3) = 3 repetições / (0,6) = 6 repetições / (1,6) = 5 repetições

for c in range(6, 0, -1): #o -1 faz uma contagem para tras
   print(c)

for c in range(0, 7, 2): #imprime a contagem pulando de 2 em 2
   print(c)

|iterar for com 2 ou mais variaveis: -------------------------------|
|for variavel1, variavel2 in zip(range(0, 10), range(10, 0, -1)):   | #usamos a funcao zip para multiplas variaveis
|print(variavel1, variavel2)                                        |
|-------------------------------------------------------------------|

/* -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

/* Ordenar lista (crescente e decrescente) ---------------------------------------------------------------------------------------------------------------------------------------------------------

lista = [a, b, c] 	 #criar lista
lista.sort() 		 #ordenar crescente
lista.sort(reverse=True) #ordenar decrescente
lista.reverse()          #ordem decrescente
 
lista.index(variavel) #pesquisa dentro de uma lista se existe a variavel e retorna o indice (posição) do valor ou string dentro da lista

/* -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

/* Estrutura de repetição while --------------------------------------------------------------------------------------------------------------------------------------------------------------------

while variavel not in 'MmFf':
   funcao ..


|*while com operadores booleanos: ------|
|                                       |
|while True:                            |
|  if condicao:                         |
|    break #condicao de parada do while |
|  else:                                |
|    funcoes                            |
|---------------------------------------|

|*while com operadores booleanos: -----------|
|                                            |
|fim = False                                 |
|while not fim:                              |
|  if condicao:                              |
|    fim = True #condicao de parada do while |
|  else:                                     |
|    funcoes                                 |
|--------------------------------------------|



/* -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

/* f-string ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

variavel1 = 1
variavel2 = 2

print(f'{variavel1} e {variavel2}') #o f'{}' é a chamada para uso do f-string, onde a variavel é colocada dentro das chaves

/* -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

/* Variáveis Compostas - Tuplas --------------------------------------------------------------------------------------------------------------------------------------------------------------------

*As tuplas são IMUTÁVEIS - não pode substituir um valor dentro dela depois de definida.
*As tuplas aceitam letras e numeros numa mesma tupla

variavel = ('a', 'b', 'c') #os parenteses definem uma tupla

acessando a tupla:

print(variavel[0]) #o primeiro indicie é sempre o 0, o ultimo é n-1

for c in variavel: #esse laço de repetição acessa todos os indices da tupla
   print(c)

for c in range(0, len(variavel): #igual a citação anterior
   print(variavel[c]) #c tambem pode ser utilizado como um contador, exibindo posicoes

for pos, c in enumerate(variavel_tupla):
   print(f'tais dados da {c} na posicao {pos}') #pos pode ser utilizado como um contador, exibindo posicoes
   
algumas propriedades interessantes:

len(variavel) #tamanho da tupla
print(sorted(variavel)) #imprime tupla em ordem crescente
variavel.count(elemento) #conta quantas vezes aparece um elemento (num ou palavra) dentro da tupla
variavel.index(elemento) #mostra o indice do elemento na tupla - primeira ocorrencia
variavel.index(elemento, 1) #o 1 dps de elemento desloca para comecar a pesquisa a partir do indice 1
del(variavel) #apaga a variavel
max(variavel) #maior valor 
min(variavel) #menor valor

/* -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

/* Variável composta - Lista (Parte 1) -------------------------------------------------------------------------------------------------------------------------------------------------------------

*As listas são mutaveis - pode-se substituir um valor dentro da lista

Declarando Variavel:
variavel = list()
variavel = []

variavel = [a, b, c]           #os colchetes definem uma lista

variavel.append('elemento')    #adiciona um elemento a lista
variavel.insert(0, 'elemento') #adiciona um elemento na posição escolhida sem excluir o elemento existente em dada posição

del variavel[indice]           #elimina o elemento no indice desejado
variavel.pop(indice)           #elimina o elemento no indice desejado
variavel.pop()                 #elimina o ultimo elemento da lista - caso nao informe um indice no parenteses
variavel.remove(elemento)      #elimina o 1º elemento sem informar o indice, informando o elemento (valor) a ser eliminado
 
variavel = list(range(4, 11))  #cria uma lista na variavel (variavel) que será uma contagem de 4 à 10 de indices 0 à 6

variavel.sort()                #ordem crescente
variavel.sort(reverse=True)    #ordem decrescente
variavel.reverse()             #reordena a lista do fim pro começo
lent(variavel)                 #tamanho da lista

variavel.count(elemento)       #conta quantas vezes aparece um elemento (num ou palavra) dentro da lista
variavel.index(elemento)       #mostra o indice do elemento na lista - primeira ocorrencia
variavel.index(elemento, 1)    #o 1 dps de elemento desloca para comecar a pesquisa a partir do indice 1

max(variavel)                  #valor maximo da lista
min(variavel)                  #valor minimo da lista
sorted(variavel)               #ordem crescente, utilizado para o print pois nao altera realmente a ordem da lista, apenas a exibição
sum(variavel)                  #soma elementos da lista

|Obs 1.1 - ligação de listas: -------------------|
|a = [x, y, z]                                   |
|b = a                                           |
|                                                |
|desta forma temos uma ligação entre as listas,  |
|caso haja uma modificação em b implica em a e   |
|vice-versa                                      |
|------------------------------------------------|
|Obs 1.2 - cópia de listas: ---------------------|
|a = [x, y, z]                                   |
|b = a[:]                                        |
|                                                |
|desta forma b copia todos os elementos da lista,|
|a, diferenciando ambas as listas                |
|------------------------------------------------|

|Obs - remove c/ if: ----------------| #para não dar erro caso o remove não ache o valor/elemento buscado
|if numero_ou_texto in variavel:     |
|   variavel.remove(numero_ou_texto) |
|------------------------------------|

|Obs - exibindo cada elemento/valor na lista:-|
|for v in lista:                              | #v é uma variavel qualquer utilizada como contador
|   print(f'{v})                              |
|---------------------------------------------|
|for c, v in enumerate(lista):                | #c e v sao variaveis quaisquer onde c vira um contador pq do enumerate e v acessa os valores da lista
|    print(f'posicao: {c} / valor: {v}        |
|---------------------------------------------|

|Obs - entrada de dados em uma lista: ---------------|
|variavel = list() ou variavel = []                  |
|for c in range(0, 5):                               |
|   variavel.append(int(input('Digite um valor: '))) |
|----------------------------------------------------|

/* -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

/* Variável composta - Lista (Parte 2) -------------------------------------------------------------------------------------------------------------------------------------------------------------

|Criando Listas dentro de uma Lista, ex: -------------------------------------------------------------------------------------------------------------------------------------------|
|pessoas = [['Pedro', 25], ['Maria', 19], ['Joao', 32]]                                                                                                                             |
|Exibindo:                                                                                                                                                                          |
|print(pessoas[0][0]) #terá como resultado Pedro, pois o primeiro colchete representa o indice da primeira lista ['Pedro', 25] e o segundo representa o indice dentro dessa lista.  |
|print(pessoas[1])    #terá como resultado a lista 1 dentro de pessoas: ['Maria', 19]                                                                                               |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

lista1 = []
lista_master = []
lista_master.append(lista1[:])

|Entrada de dado listas dentro de uma Lista ex: -------------------------------------|
|galera = []                                                                         |
|dados = []                                                                          |
|for c in range(0, 5):                                                               |
|    dados.append(str(input('Nome: ')))                                              |
|    dados.append(int(input('Idade: ')))                                             |
|    galera.appende(dados[:]) #adicionando a lista de dados na lista galera          |
|    dado.clear()             #limpando a lista de dados para entrada de novos dados |
|------------------------------------------------------------------------------------|

|Exibindo listas ex: -----------------------------------------------------------------------------------------------------|
|pessoas = [['Pedro', 25], ['Maria', 19], ['Joao', 32]]                                                                   |
|for p in pessoas:                                                                                                        |
|    print(f'{p[0]} tem {p[1]} anos de idade.') #p[0] exibe o nome e p[1] a idade em cada lista dentro da lista pessoas   |
|-------------------------------------------------------------------------------------------------------------------------|

/* ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

/* Estruturas compostas - Dicionarios -------------------------------------------------------------------------------------------------------------------------------------------------------------

|Declarando Variavel: ---------------------------------------------------|
|#ambos os casos sao aceitos como declaração de uma variavel dicionario  |
|variavel = dict()                                                       |  
|variavel = {}                                                           |
|------------------------------------------------------------------------|

ex:
variavel = {'nome':'Pedro', 'idade':25} #nome e idade substituem os indices do elemento
print('nome')                           #exibira o nome Pedro, pois o indice nao é 0 e sim 'nome'

Adicionando / Deletando - valores:
variavel['sexo'] = 'M'                  #acrescenta o indice 'sexo' seguido do elemento 'M' - já que o append nao funciona em dicionarios
del dados['idade']                      #apaga o indice e o valor do dicionario

|Conceitos - Valor | Chave | Item: ---------------------------------------------------------------------|
|filme = {'titulo':'Star Wars', 'ano':1977, 'diretor':'George Lucas'}                                   |
|-------------------------------------------------------------------------------------------------------|
|print(filme.value())                    #'Star Wars' | 1977 | 'George Lucas'                           |
|print(filme.keys())                     #'titulo' | 'ano' | 'diretor'                                  |
|print(filme.items())                    #'titulo':'Star Wars' | 'ano':1977 | 'diretor':'George Lucas'  |
|-------------------------------------------------------------------------------------------------------|                                                                                                                                       

|Exibindo um Dicionario: -----------------------------------------------------------|
|-----------------------------------------------------------------------------------|
|OPCAO 1: --------------------------------------------------------------------------|
|for e in brasil:                                                                   |
|   print(e)                                                                        |
|-----------------------------------------------------------------------------------|
|OPCAO 2: --------------------------------------------------------------------------|
|for e in brasil:                                                                   |
|   for k, v in e.items():                                                          |
|      print(f'O campo {k} tem valor {v}.') #k exibe key | v exibe valores          |
|-----------------------------------------------------------------------------------|
|OPCAO 3:---------------------------------------------------------------------------|
|for e in brasil:                                                                   |
|   for v in e.value():                                                             |
|       print(v, end='')                                                            |
|   print()                                                                         |
|-----------------------------------------------------------------------------------|

|Copiando um Dicionario p/ uma Lista: ---------------------------------------------------------------------------------------------------------------------------------------|
|estado = dict()                                                                                                                                                             |
|brasil = list()                                                                                                                                                             |
|for c in range(0, 3):                                                                                                                                                       |
|   estado['uf'] = str(input('Unidade Federativa: '))                                                                                                                        |
|   estado['sigla'] = str(input('Sigla do Estado: '))                                                                                                                        |
|   brasil.append(estado.copy()) #neste caso usamos o comando estado.copy() para substituir o fatiamento estado[:] (apenas no caso de copiar um dicionario para uma lista)   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

|Ordenando dicionario: -----------------------------------------------------------------------------------|
|from operator import itemgetter  #é necessario importar a função itemgetter para ordenar os dicionarios  | 
|dict1 = dict()                                                                                           |
|dict2 = dict()                                                                                           |
|                                                                                                         |
|#o numero 1 ordena com base nos valores, se eu colocar 0 ordena com base nas chaves                      |
|dict2 = sorted(dict1.items(), key=itemgetter(1))                #ordena de forma crescente               |
|dict2 = sorted(dict1.items(), key=itemgetter(1), reverse=True)  #ordena de forma decrescente             |
|---------------------------------------------------------------------------------------------------------|

/* --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

/* Funções - Part 1 ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

|Função sem Parametro: -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                                                                                                                               |
|def nome_da_funcao():                                                                                                                                                                                          |
|   print('-----------') #escrevo as funcoes                                                                                                                                                                    |
|                                                                                                                                                                                                               |
|                                                                                                                                                                                                               |
| #entre a def e o programa principal o pycharm pede 2 linhas vazias                                                                                                                                            |
| |Executando a Função: --|                                                                                                                                                                                     |
| |nome_da_funcao()       |                                                                                                                                                                                     |
| |-----------------------|                                                                                                                                                                                     |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

|Função com Parametro: -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                                                                                                                               |
|def nome_da_funcao(parametro1):                                                                                                                                                                                |
|   print('------')                                                                                                                                                                                             |
|   print(parametro1)                                                                                                                                                                                           |
|   print('------')                                                                                                                                                                                             |
|                                                                                                                                                                                                               |
| |Executando a Função: --------|                                                                                                                                                                               |
| |nome_da_funcao('Ola Mundo')  | #ao chamarmos a função, passamos o que esta em parenteses pro parametro escrito na função (DEF) que servirá como uma variavel, substituindo o valor no programa               |
| |-----------------------------|                                                                                                                                                                               |
|                                                                                                                                                                                                               |
|def nome_da_funcao(a, b)                                                                                                                                                                                       |
|   s = a + b                                                                                                                                                                                                   |
|   print(s)                                                                                                                                                                                                    |
|                                                                                                                                                                                                               |
| |------------------------------------------|                                                                                                                                                                  |
| |Executando sem Explicitar o Parametro: ---|                                                                                                                                                                  |
| |nome_da_funcao(1, 2)                      | #exibira a soma entre 1 e 2, onde 1 = a e 2 = b, os parametros sao passados na ordem dos parametros escritos na função                                           |
| |------------------------------------------|                                                                                                                                                                  |
| |Executando Explicitando o Parametro: -----|                                                                                                                                                                  |
| |nome_da_funcao(b=1, a=2)                  | #neste caso estou explicitando o parametro dai a ordem nao importa pois cada parametro ira receber o valor que esta sendo relacionado a ele na chamada da funcao |
| |------------------------------------------|                                                                                                                                                                  |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

|Empacotando Parametros em uma TUPLA: --------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                                                                                                                               |
|def contador(*parametro): #o asterisco faz com que o usuario possa passar quantos numeros ele quiser para o parametro, criando uma TUPLA na variavel parametro                                                 |
|  for valor in parametro:                                                                                                                                                                                      |
|      print(valor)                                                                                                                                                                                             |
|                                                                                                                                                                                                               |
| |Executando a função: -----| #perceba que neste caso o usuario pode passar quando valores ele desejar como parametro graças ao asterisco (*) que faz o empacotamento dos parametros                           |
| |contador(2, 1, 7)         |                                                                                                                                                                                  |
| |contador(2, 0)            |                                                                                                                                                                                  |
| |contador(4, 4, 7, 6, 2)   |                                                                                                                                                                                  |
| |--------------------------|                                                                                                                                                                                  |
|                                                                                                                                                                                                               |    
|#Função para somar n valores                                                                                                                                                                                   |
|def soma(*valores):                                                                                                                                                                                            |
|s = 0                                                                                                                                                                                                          |
|  for num in valores:                                                                                                                                                                                          |
|     s += num                                                                                                                                                                                                  |
|  print(f'Somando os valores {valores} temos {s}')                                                                                                                                                             |
|                                                                                                                                                                                                               | 
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

|Função com lista sendo passada como Parametro: ----------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                                                                                                                               |
|#Esta função tem como objetivo dobrar os valores de uma lista!                                                                                                                                                 |
|def dobra(lst): #lst é o meu parametro, pode ser chamado como quiser e neste caso recebera uma lista de valores                                                                                                |
|   pos = 0                                                                                                                                                                                                     |
|    while pos < len(lst):                                                                                                                                                                                      |
|       lst[pos] *= 2                                                                                                                                                                                           |
|       pos += 1                                                                                                                                                                                                |
|                                                                                                                                                                                                               |
| |Executando a Função: --------------------------------------------------------------------------------------------------------------|                                                                         |
| |valores = [1, 2, 3, 4, 5]                                                                                                          |                                                                         |
| |dobra(valores)                                                                                                                     |                                                                         |
| |print(valores)                                                                                                                     |                                                                         |
| |#a passagem dos parametros é por referencia, ou seja a lista valores está atrelada ao parametro lst da função dobra|               |                                                                         |
| |fazendo com que o print na lista valores exiba os valores alterados pela função dobra, pois a lista 'principal' é também alterada. |                                                                         |
| |-----------------------------------------------------------------------------------------------------------------------------------|                                                                         |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
 
/* --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

/* Funções - Part 2 ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

|Interactive Help -----------------------------------------------------------------------
|
|#basta digitar help() no console e depois pesquisar sobre qualquer comando/biblioteca ---|
|help()                                                                                   |
|                                                                                         |
|#ou digitar help(comando) na IDE e dar run                                               |
|help(print)                                                                              |
|                                                                                         |
|#imprimindo o documento                                                                  |
|print(input.__doc__) #input é o comando a ser analisado                                  |
|-----------------------------------------------------------------------------------------|

|Doc String -----------------------------------------------------------------------------------------|
|#Caso o usuario de um comando help() na função criada pelo programador, ele receberá                |
|uma string contendo informações sobre a função (um manual). Para criar uma doc string basta colocar |
|3 aspas duplas abrindo e 3 para fechar logo na linha abaixo da funçao def.                          |
|ex:                                                                                                 |
|def contador(i, f, p):                                                                              |
|   """                                                                                              |
|     -> Faz uma contagem e mostra na tela.                                                          |
|      :parametro i: inicio da contagem                                                              |
|      :parametro f: fim da contagem                                                                 |
|      :parametro p: passo da contagem                                                               |
|      :return: sem retorno                                                                          |
|   """                                                                                              |
|   c = i                                                                                            |
|   while c <= f:                                                                                    |
|      print(f'{c}', end=' ')                                                                        |
|      c += p                                                                                        |
|   print('FIM')                                                                                     |
|                                                                                                    |
|help(contador) #exibira o manual que está escrito entre as 3 aspas duplas                           |
|----------------------------------------------------------------------------------------------------|

|Parâmetros Opcionais ------------------------------------------------------------------------------------------------------------|
|#definimos os valores dos parametros dentro da função, para caso na chamada da função                                            |
|não haja passagem de algum parametro ou de todos os parametros a função automaticamente                                          |
|aplicar um valor ao parametro e nao dar crash no programa                                                                        |
|ex:                                                                                                                              |
|                                                                                                                                 |
|def somar(a=0, b=0, c=0): #os parametros a,b,c são opcionais pois recebem um valor dentro da declaração dos parametros na função |
|    s = a + b + c                                                                                                                |
|    print(f'A soma vale {s}')                                                                                                    |
|                                                                                                                                 |
|somar(3, 2, 5) #resultado = 10                                                                                                   |
|somar(8, 4)    #resultado = 12                                                                                                   |
|somar()        #resultado = 0                                                                                                    |
|#em ambos os casos a função funcionará.                                                                                          |
|---------------------------------------------------------------------------------------------------------------------------------|

Escopo de Variaveis
#variavel local: declarada dentro das funções, caso haja uma chamada na função principal a variavel não ira valer, valendo apenas dentro da função 
#variavel global: declarada no programa principal, serve para chamada nas funções assim como no programa principal.

ex:
#Função
def test(b):
  a = 8
  b += 4
  c = 2
  print(f'A dentro vale {a}') 
  print(f'B dentro vale {b}')
  print(f'C dentro vale {c}')

#Programa Principal
a = 5 
teste(a)
print(f'A fora vale {a}')

#Resultados e Impressões
Variaveis Locais (Dentro da Função test): a = 8 | b = 9 | c = 2
Variaveis Global (No programa principal): a = 5
Obs: Percebe-se que a = 5 definido no programa principal  