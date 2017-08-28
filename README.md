# RAR Framework in Python [![Build Status](https://travis-ci.org/aleDsz/rarframework-java.svg?branch=master)](https://travis-ci.org/aleDsz/rarframework-java)

## 1. Introdução

Após ter criado o mesmo framework, originalmente em [PHP](https://github.com/aleDsz/rarframework), percebi que eu teria a mesma necessidade de um ORM em outras linguagens. Resolvi adaptar para Python como forma de desafio de criar esse framework para todas as linguagens possíveis.

## 2. Como Funciona

Através do pacote `ODBC`, é possível realizar uma conexão com vários tipos de banco de dados. Além disso, por meio do `Generics`, é possível acessar o conteúdo de um objeto e obter todas as informações necessárias para criar uma instrução SQL.

Neste caso, uma classe deve seguir o seguinte modelo:

```python
# Sem código ainda
```

## 3. Como Utilizar

Para que você possa utilizar todos as funcionalidades do framework no seu ambiente, você pode criar 1 (ou mais, dependendo da sua forma de trabalho) classe para acessar ao banco de dados de forma genérica.

```python
# Sem código ainda
```

**OBS.:** Você não precisa criar a classe de forma genérica, você pode criar uma classe de acesso a dados para cada entidade que você criar no modelo citado acima.

E para que o ORM consiga se conectar com o banco de dados, você precisa criar um arquivo de configuração com o nome: `databaseConfig.json` e ele deve seguir o modelo abaixo:

```python
# Sem código ainda
```

**OBS.:** Através da propriedade `databaseName` da anotação de classe, é possível utilizar inúmeros banco de dados diferentes, assim ele deve ser diferenciado no arquivo `databaseConfig.json`. Por exemplo, se você tiver um banco de dados `sqlite` e um `mysql`, seu arquivo deverá estar definido desta forma:

```python
# Sem código ainda
```

## 4. Como Contribuir

Para contribuir, você pode realizar um **fork** do nosso repositório e nos enviar um Pull Request.

## 5. Doação

Caso queria fazer uma doação para o projeto, você pode realizar [aqui](https://twitch.streamlabs.com/aleDsz)

## 6. Suporte

Caso você tenha algum problema ou uma sugestão, você pode nos contatar [aqui](https://github.com/aleDsz/rarframework-python/issues).

## 7. Licença

Cheque [aqui](LICENSE)
