# Leitor-de-Codigo-Barras

## Projeto de leitura de codigo de barras para separação de pacotes
Este projeto foi feito a partir de um desafio proposto, onde foi necessario indentificar cada trinca numerica, pois cada uma representa uma informação do pacote para sua separação e posterior envio.

Ordem das trincas:
1 Região de origem, 2 Regiao de Destino, 3 Código da Empresa de logistica, 4 Código do vendedor do produto, 5 Tipo de produto

Exemplo das Trincas

Região  /                  Código

Centro-oeste -              111

Nordeste -                  333

Norte -                     555

Sudeste -                   888

Sul -                       000

Tipo do Produto  /         Código


Jóias -                     000

Livros -                    111

Eletrônicos -               333

Bebidas -                   555

Brinquedos -                888

Restrições de envio:
Não é possível despachar pacotes contendo jóias tendo como região de origem o Centro-oeste;
O vendedor 584 está com seu CNPJ inativo e, portanto, não pode mais enviar pacotes, os códigos de barra que estiverem relacionados a este vendedor devem ser considerados inválidos.

O que este projeto faz:
a) Identiﬁcar o destino de cada pacote.
b) Saber quais pacotes possuem códigos de barras válidos e/ou inválidos.
c) Identiﬁcar se algum pacote que tem como origem a região Sul tem Brinquedos em seu conteúdo.
d) Listar os pacotes agrupados por região de destino (Considere apenas pacotes válidos).
e) Listar o número de pacotes enviados por cada vendedor (Considere apenas pacotes válidos).
f) Gerar o relatório/lista de pacotes por destino e por tipo (Considere apenas pacotes válidos).

Para usar este projeto sera necessario fazer um GitClone.

Para realizar o teste, o arquivo a ser executado é o main.py.

Linguagem e IDE utilizada:
Python, Pycharm

Motivação: A motivação pelo qual utilizo Python é por ser a linguagem ao qual estudo tanto na faculdade quanto fora dela, e pela sua curva de aprendizagem.

To-do:

- Criar testes Unitarios
