# Banco as a Service

O objetivo desse projeto é ensinar um pouco sobre testes. A ideia é ser um cadastro simples de "contas de banco".

## Modelo

Cada registro de uma conta tem a seguinte estrutura?

```python
class Account(BaseModel):
    nome: str
    cpf: str
    saldo: int = 10000
```
Cada contas novas o saldo padrão é `10000`. Usamoms o saldo como sendo um inteiro apenas por uma quesão de simplificação.

## Funcionalidades

Essas são as funcionalidades que esse projeto precisa implementar:

 - Criar nova conta
 - Retornar os dados de uma conta
 - Debitar um valor de uma conta
 - Creditar um valor em uma conta


## Interface HTTP

Aqui está descrito como será a interface HTTP desse projeto.

 - `POST /accounts`: Cria uma nova conta;
 - `GET /accounts`: Lista todas as contas criadas;
 - `GET /accounts/{acc_id}`: Retorna os dados referentes à conta com id=`acc_id`;
 - `POST /accounts/{acc_id}/debido`: Remove um valor da conta com id=`acc_id`;
 - `POST /accounts/{acc_id}/credito`: Adiciona um valor à conta com id=`acc_id`;

## Modelos dos Recursos HTTP

Os endpoints que recebem/retornam uma conta usam o modelo `Account`, abaixo:

```python
class Account(BaseModel):
    nome: str
    cpf: str
    saldo: int = 10000
```

Os endpoints que alteram o saldo de uma conta usam os modelos `Credito`, `Debito`:

```python
class Credito(BaseModel):
  valor: int

class Debito(BaseModel):
  valor: int

```

# Rodando o projeto localmente

Para rodar o projeto localmente você precisará do `pyenv` e `pipenv`

## Instalando o pyenv

Basta seguir a documentação do projeto: https://github.com/pyenv/pyenv#basic-github-checkout

Resumindo, esses são os passos:

- git clone https://github.com/pyenv/pyenv.git ~/.pyenv
- echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
- echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
- echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc

Se você estiver usando outro shell que não seja o bash precisará substituir o `~/.bashrc` pelo arquivo
de configuração do seu shell.

## Instalando python

Depois que o pyenvf estiver funcionando é hora de instalar uma versão do python. Para esse projeto podemos
usar python 3.7.5. Para instalar rode:

```
pyenv install 3.7.5
```

**Atenção**: Para Distros baseadas em Debian (Ubuntu, Elementary, etc) instalem os seguintes pacotes:

```
sudo apt-get install make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev python-openssl git
```


# Instalando pipenv

Para instalar o pipenv rode:

```
pip install --user pipenv
```

A partir desse momento você já pode rodar `pipenv` no terminal.

# Instalando o projeto

Entre na pasta do projeto e digite:

```
pipenv install --dev
```

# Rodando os testes

Para rodas os teses, faça:

```
pipenv run test
```

Todos os testes devem passar.



# Implementação

Temos 4 endpoints para serem implementados nesse projeto:

- `POST /accounts/<id>/debito`

O Endpoint HTTP já está escrito mas o Servive ainda não faz nada. A implementação deve preencher o código do `AccountService.debita()`.


- `POST /accounts`

O Endpoint HTTP já está escrito mas o Servive ainda não faz nada. A implementação deve preencher o código do `AccountService.save()`.
