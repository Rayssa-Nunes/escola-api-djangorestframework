# API Escola

Esta é a API de uma Escola feita com Django REST Framework

## Passos para instalação e execução do projeto

1. Crie um novo ambiente virtual dentro do diretório:
``` 
python -m venv venv
```
2. Ative o ambiente virtual. No Windows, execute:
```
venv\Scripts\activate
```
No Linux, execute:
```
source venv/bin/activate
```
3. Para instalar as dependências execute o comando:
```
pip install -r requirements.txt
```
4. Faça as migrações do banco de dados:
```
python manage.py makemigrations
python manage.py migrate
```
5. Agora você pode executar a aplicação. Para isso, use o comando:
```
python manage.py runserver
```

O servidor será iniciado em `http://localhost:8000/`
