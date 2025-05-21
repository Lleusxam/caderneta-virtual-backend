# Caderneta Virtual Backend
## Como rodar o projeto
### requirements.txt
Todas as bibliotecas necessárias estão nesse arquivo que está na raíz do projeto, para para usá-lo basta executar na raíz do projeto:
- No mac, linux ou Git bash CLI no windows:
```bash
python3 -m venv .venv
source .venv
pip install -r requirements.txt
```
- No windows:
```bash
python3 -m venv .venv
.\venv\Scripts\activate.bat
pip install -r requirements.txt
```
Se não encontrar `python3` tente `python`, caso também não encontre, verifique se ele está instalado.

### Neovim
Caso esteja usando o Neovim, o lsp terá problemas em visualizar alguns tipos do Django, por isso, instale manualmente o `django-stubs` com:
```bash
pip install django-stubs
```

## Como popular o banco de dados
Para colocar dados falsos para testes, execute o seguinte comando na raiz do projeto:
```bash
python3 manage.py shell < populate_db.py
```

Caso dê algum erro, provavelmente já tinham coisas no banco, e alguma chave estrangeira deu conflito, execute na raíz:
```bash
python3 manage.py shell < clean_db.py
```
Como o nome sugere, isso limpa o banco de dados, execute novamente o comando de popular e deve funcionar sem mais problemas.
