# Learning Log

**Learning Log** é uma aplicação web onde você pode registrar tópicos de aprendizado e adicionar entradas relacionadas a esses tópicos. O projeto permite que você:

- Adicione e exclua tópicos.
- Crie, edite ou apague entradas relacionadas aos tópicos.
- Realize login, registre-se e gerencie sua conta.

## Como Rodar o Projeto

### Pré-requisitos

Antes de rodar o projeto, você precisa ter os seguintes programas instalados:

- [Python 3.x](https://www.python.org/)
- [Django 5.x](https://www.djangoproject.com/) (automaticamente instalado via `pip install -r requirements.txt`)

### Passos para Configuração

Siga os passos abaixo para rodar o projeto localmente:

1. **Clone este repositório para sua máquina local**:
   ```bash
   git clone https://github.com/wellingtonh07/learning-log.git

2. **Navegue até o diretório do Projeto**:
   ```bash
   cd learning-logs

3. **Crie e ative um ambiente virtual**:
   
   Para Windows:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate

   ```
   Para macOS/Linux:
   ```bash
   python -m venv .venv
   source .venv/bin/activate

4. **Instale as dependências do projeto**:
   ```bash
   pip install -r requirements.txt

5. **Realize as migrações do banco de dados**:
   ```bash
   python manage.py migrate

6. **Crie um superusuário para acessar o painel de administração (se ainda não tiver feito isso)**:
   ```bash
   python manage.py createsuperuser

7. **Inicie o servidor de desenvolvimento**:
   ```bash
   python manage.py runserver

8. **Acesse a aplicação no navegador**:

   Página Inicial: http://127.0.0.1:8000

   Administração: http://127.0.0.1:8000/admin

### Dependências do Projeto
Este projeto usa as seguintes dependências, que são instaladas através do arquivo requirements.txt:
```txt
asgiref==3.8.1
Django==5.1.6
sqlparse==0.5.3
tzdata==2025.1

```
### Contribuição:
Sinta-se à vontade para contribuir com melhorias para o projeto! Para isso, basta seguir os seguintes passos:

1. **Faça um fork deste repositório.**
2. **Crie uma branch para sua funcionalidade:**
```bash
git checkout -b minha-nova-funcionalidade 
```
3. **Faça suas alterações e adicione testes.**
4. **Envie um pull request detalhando suas mudanças.**

### Video Demonstrativo


https://github.com/user-attachments/assets/10697356-82d5-4999-9b7c-133d3898443f


