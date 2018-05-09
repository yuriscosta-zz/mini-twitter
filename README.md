# mini-twitter
Uma api de simulação do Twitter a qual podemos cadastrar, editar, remover e recuperar tantos os usuários quanto os tweets. Esse repositório faz parte do processo seletivo de estagiário da GooDrink.

## Instalação
Antes de iniciarmos a instalação, é importante lembrar que devemos instalar o [pipenv](https://docs.pipenv.org/).

```bash
# Clone este repositório
git clone https://github.com/yuriscosta/mini-twitter.git

# Entre no repositório
cd mini-twitter

# Ative o seu ambiente virtual
pipenv shell

# Instale as dependências
pipenv install

# Entre na pasta do projeto
cd api

# Caso queira rodar os testes
python manage.py test

# Coloque o servidor em funcionamento
python manage.py runserver
```

## Requisições
```bash
# Listar todos os usuários
GET /profiles/

# Criar um usuário
POST /profiles/
{'username': 'xxx', 'password': 'yyy', 'bio': 'www'}

# Retornar um usuário específico
GET /profiles/id/

# Editar um usuário (autenticação necessária)
PATCH /profiles/id/
{'username': 'xxx', 'bio': 'yyy'}

# Remover um usuário (autenticação necessária)
DELETE /profiles/id/

# Feed de tweets (autenticação necessária)
GET /tweets/

# Criar um tweet (autenticação necessária)
POST /tweets/
{'content': 'xxx'}

# Retornar um tweet específico
GET /tweets/id/

# Editar um tweet (autenticação necessária)
PATCH /tweets/id/
{'content': 'yyy'}

# Remover um tweet (autenticação necessária)
DELETE /tweets/id/
``` 
