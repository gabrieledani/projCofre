### Prerequisites

* [Python](https://www.python.org/)
* [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html)
```pip install virtualenv```

### Installing

Passo a passo para a geração de um novo executável, caso venham a ser feita modificações no código.

Criar ambiente virtual:
```python -m venv venv```

Ativar ambiente virtual:
```.\venv\Scripts\activate```

(Desativar quando necessário)
```deactivate```

Instalar dependências
```pip install -r .\requirements.txt```

Criar executável
```python setup.py build```

Após isso será criado um repositório *build*, onde ficará o executável e as suas dependências.
Os arquivos necessários para o funcionamento do programa são todos os que estão dentro da pasta *build*

O arquivo boletos.pdf deve ser criado dentro da pasta boletos onde está o executável.