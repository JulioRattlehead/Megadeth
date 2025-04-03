# API de Discografia do Megadeth com FastAPI

Este projeto demonstra a criação de uma API RESTful simples usando FastAPI para fornecer informações sobre a discografia da banda de thrash metal Megadeth. Ele também inclui um fluxo de trabalho de CI/CD automatizado com GitHub Actions.

## Funcionalidades

A API oferece os seguintes endpoints:

* `/discografia`: Retorna a lista completa de álbuns do Megadeth.
* `/album/{ano}`: Retorna o álbum lançado no ano especificado.
* `/musicas/{album}`: Retorna a lista de músicas de um determinado álbum.

## Tecnologias Utilizadas

* [Python](https://www.python.org/)
* [FastAPI](https://fastapi.tiangolo.com/)
* [Uvicorn](https://www.uvicorn.org/)
* [GitHub Actions](https://github.com/features/actions)

## Pré-requisitos

* Python 3.9 ou superior
* pip (gerenciador de pacotes do Python)

## Configuração

1.  Clone este repositório:

    ```bash
    git clone [https://github.com/dolthub/dolt](https://github.com/dolthub/dolt)
    ```

2.  Crie um ambiente virtual (recomendado):

    ```bash
    python -m venv venv
    ```

3.  Ative o ambiente virtual:

    * No Windows:

        ```bash
        venv\Scripts\activate
        ```

    * No macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

4.  Instale as dependências:

    ```bash
    pip install "fastapi[standard]"
    ```

## Executando a API

Para iniciar o servidor de desenvolvimento, execute o seguinte comando:

```bash
uvicorn main:app --reload