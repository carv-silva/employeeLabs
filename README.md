# API Funcionários

API criada para o teste da vaga desenvolvedor backend júnior da squad checkout

Foram utilizadas as seguintes tecnologias no desenvolvimento da solução:

1. **Python** como linguagem base;
2. **Django** como framework web base;
3. **Django Rest Framework** como framework para construção de REST APIs;
4. **SQLite** como banco de dados.

### Pré-requisitos
```
Python = > 3.0
Pip = > 3.0
SQLite = > 2.0
```
### Instalação

```
$ git clone https://github.com/carv-silva/employeeLabs.git ~/Downloads
$ cd ~/Downloads/employeeLabs
$ python -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
$ make ti
$ make te
```
### Variáveis de Ambiente

```
$ make sk
```

### Execução
```
$ make run
```

### Endpoints Local

1. **Inserindo Funcionários**

curl -POST http://0.0.0.0:21256/employee/ --data '{
    "name": "Arnaldo Pereira",
    "email": "arnaldo@luizalabs.com",
    "department": "Architecture"
}' --header "Content-Type: application/json"

curl -POST http://0.0.0.0:21256/employee/ --data '{
    "name": "Renato Pedigoni",
    "email": "renato@luizalabs.com",
    "department": "E-commerce"
}' --header "Content-Type: application/json"

curl -XPOST http://0.0.0.0:21256/employee/ --data '{
    "name": "Thiago Catoto",
    "email": "catoto@luizalabs.com",
    "department": "Mobile"
}' --header "Content-Type: application/json"

2. **Retornando os registro**

curl -H "Content-Type: application/Django" http://0.0.0.0:21256/employee/

3. **Atualizando o registro:**

curl -XPUT http://0.0.0.0:21256/employee/[id que deseja alterar EX:2]/ --data '{
    "name": "Renato Pedigoni",
    "email": "renato@luizalabs.com",
    "department": "Logistica"
}' --header "Content-Type: application/json"

4. **Deletando registro:**

curl -XDELETE http://0.0.0.0:21256/employee/[id que deseja apagar EX:2]/








