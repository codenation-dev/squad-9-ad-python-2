# squad-9-ad-python-2

## Operações básicas:

Antes de submeter o projeto para review executar as seguintes tarefas:

- [x] [Executar os testes](#executar-testes)
- [x] [Verificar estilo de código](#verificar-estilo-de-código)

### Executar testes

```python manage.py test```

### Verificar estilo de código

Se o flake8 não estiver instalado:

```pip install flake8```

Verificar o código de todo o projeto:

```flake8 --exclude=venv/,*/migrations/*```

Verificar o código de app específica:

```flake8 comission/ --exclude=*/migrations/*```

> Substituir `comission/` da instrução anterior pelo nome do diretório que deseja testar.
