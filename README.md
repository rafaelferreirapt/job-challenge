- Data modeling

A utilização de base de dados relacionais traria problemas a nível de resposta 
da aplicação a um simples pedido. Sendo uma quantidade de informação generosa,
o que poderia ter feito com base de dados relacional era:

. Criação de uma tabela de e-mails (unique), em que era atribuído uma primary key preferencialmente int
. Criação de uma tabela leaks que tinha o nome dos leaks (unique) e era atribuído uma primary key int também
. Criação de uma tabela de relação entre a tabela e-mails e a leaks, dado que cada entrada desta tabela, continha uma FK 
do e-mail e uma FK do leak em que está presente

Para pesquisa sobre os dados:
. Dado um email, fazendo join entre a tabela e-mails e a leaks, usando a de relação, seria possível pesquisar por um 
determinado e-mail e obter as respetivas entradas "leak"

No entanto, estamos a falar de uma quantidade generosa de dados pelo que decidi-me aventurar pelo Elastic Search.

Usando docker criei uma instância do elastic search (data/run.sh). Usando Python (data/raw/read.py), cria-se um index “binary”, e dois types “linkedin” e “neopets”, sendo que para ambos as propriedades são do tipo texto e fazem uso de um analyzer “email” que foi criado usando exemplo externo.

Após isso insere-se dados em bulk, lendo linha a linha cada sample.txt.

- API Flask

Para criar a API fiz uso de Flask, usando as potencialidades do Elastic Search criei dois métodos: strict_email e search_domain. Ambos usam o endpoint _count, o por domínio faz uso de uma query wildcard “*@domain”. 

Desenvolvi unit tests e usando o Docker apenas corre o container mais recente caso passe nos testes. (unit tests: /api/tests/tests.py; e Docker: /api/Dockerfile)

- Outputs da API

POST http://localhost:5001/api/v1/domain/
BODY {"domain": "robinhood.sch.bham.co.uk"}
Content-Type application/json
RESPONSE:
{
  "result": [
    "neopets"
  ]
}

POST http://localhost:5001/api/v1/email/
BODY {“email”: "1380@robinhood.sch.bham.co.uk"}
Content-Type application/json
RESPONSE:
{
  "result": [
    "neopets"
  ]
}

