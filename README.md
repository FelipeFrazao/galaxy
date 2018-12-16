# Galaxy

[![Build Status](https://travis-ci.com/FelipeFrazao/galaxy.svg?branch=master)](https://travis-ci.com/FelipeFrazao/galaxy) 
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django.svg)](https://github.com/FelipeFrazao/galaxy)

---

## Documentação de EndPoints

A documentação dos end points está sendo feitas no padrão swagger, 
o arquivo é esse [aqui](api-v1-swagger.yml). 
E ela pode acessada [aqui](https://app.swaggerhub.com/apis-docs/FelipeFrazao/Galaxy/1.0.0#/).
## Desenvolvimento

### VsCode Tips

#### files.exclude

Remove do explore de arquivos os arquivos configurados. 
para esse projeto a configuração sugerida é:

```json
    "files.exclude": {
        "**/.git": true,
        "**/__pycache__": true,
        "**/*.pyc": true
    }
```

#### formatOnSave

Toda vez que você salvar um arquivo ele vai formatar o arquivo 
seguindo o padrão definido em `python.formatting.provider`. 
O projeto usa o provider `autopep8`. A configuração sugerida é:

```json
    "editor.formatOnSave": true,
    "python.formatting.provider": "autopep8",
    "python.formatting.autopep8Args": [
        "--max-line-length=120"
    ],
```

#### Lints

Habilite a opção do VsCode exibir os warnings de lint para você com a seguinte configuração:

```json
    "python.linting.flake8Enabled": true,
    "python.linting.pylintArgs": [
        "--load-plugins pylint_flask"
    ],
```

### Usado no Projeto
#### Coverage

O arquivo [.coveragerc](.coveragerc) possui as configurações 
para a execução correta do coverage.

#### Isort

O arquivo [.isort.cfg](.isort.cfg) possui as configurações para a 
organização dos imports do projeto.

Use a extensão [Save and Run](https://marketplace.visualstudio.com/items?itemName=wk-j.save-and-run) 
para executar o comando `isort` toda vez que um arquivo `.py` for salvo.
A configuração que deve ser feita no VsCode é no arquivo `settings.json` da seguinte maneira:

```json
    "saveAndRun": {
        "commands": [
            {
                "match": "\\.py$",
                "cmd": "isort ${file}",
                "useShortcut": false,
                "silent": false
            }
        ]
    }
```
#### Lints packages

##### Pylint

O arquivo [.pylintrc](.pylintrc) possui as configurações do lint para o projeto.

##### flake8 e pep8

A configuração de ambos os lints está no arquivo [setup.cfg](setup.cfg).

A única mudança do lint nesse caso é que o tamanho 
maximo da linha foi alterado de 80 para 120.

##### pylint-flask

O projeto faz uso do plugin [pylint-flask](https://github.com/jschaf/pylint-flask).
Ele aparece na configuração do VsCode que é responsável por executar o link, 
com a configuração abaixo você carrega o plugin:

```json
    "python.linting.pylintArgs": [
        "--load-plugins pylint_flask"
    ]
```

### Docker

Para executar o projeto use `docker-compose up`. O Projeto vai estartar em `localhost:5005`.

### Tests

A sugestão para execução dos testes é o commando abaixo:

```bash
docker-compose run web nosetests -v --with-watch --with-coverage --cover-package=. --detailed-errors
```

Ele vai utilizar o comando `nosetests` com verbosidade `1`, vai exibir o relatório de cobertura do coverage no final e o parametro `--with-watch` vai manter o comando ativo esperando algum arquivo ser salvo, toda vez que você salvar um arquivo ele vai re executar os testes.

Ou pode rodar de dentro do container
```bash
./autotest.sh
```