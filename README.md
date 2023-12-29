# FileStorage API 1.0

![repothumbb](https://github.com/luiisp/FileStorageAPI/assets/115284250/d0915f7d-7bfa-4b80-92d1-1632d139d8ab)

### A file storage é uma API criada com padroes rest que permite com que arquivos sejam armazenados diretamente, ficando disponiveis a qualquer instante para donwload
Tag this project with a star 🌟

## Pré-requisitos

Certifique-se de ter os seguintes pré-requisitos instalados em sua máquina:

- Python (versão 3.0+ recomendado)
- pip (gerenciador de pacotes do Python)
- Django
- Django Rest Framework

## Output
### Para fazer enviar um novo arquivo para a API basta ter o arquivo e um titulo.

```
{
    "title": "filename",
    "fullFile": file
}
```
####  *Deve se parecer com isto

### Acesse seu arquivo através da URL [http://localhost:8000/files/ + FILE ID /](http://localhost:8000/files/)
#### RESPONSE EXAMPLE
```
    {
        "id": 1,
        "title": "raleway font",
        "acessUrl": "http://localhost:8000/files/1/",
        "fileUrl": "http://localhost:8000/media/Raleway.zip",
        "readSize": "1.80 MB",
        "uploadedAt": "2023-12-29T11:15:17.232146Z",
        "meta": {
            "name": "Raleway.zip",
            "size": 1884759,
            "format": "zip",
            "created": "2023-12-29T08:15:17.230124"
        }
    },

```

## Requests 

### Get files
#### Para acessar as files na api basta fazer uma request type GET para [http://localhost:8000/files/](http://localhost:8000/files/)

### Send new file
#### Para enviar um novo arquivo basta fazer uma request type POST para [http://localhost:8000/files/](http://localhost:8000/files/)

#### Body:
```
{
    "title": "filename",
    "fullFile": file
}
```

### Put file
#### Para substituir campos de uma file atual basta fazer uma request type PUT para [http://localhost:8000/files/ + FILE ID /](http://localhost:8000/files/)

### Delete file
#### Para deletar um arquivo basta fazer uma request type DELETE para [http://localhost:8000/files/ + FILE ID /](http://localhost:8000/files/)

* O arquivo example.js pode te ajudar a fazer uma requisição.

## Running

### 1. Clone o repositório:
   
```git clone https://github.com/luiisp/FileStorageApi```

```cd  Insight Sphere```

### 2. Instale as dependências do projeto:

```pip install -r requirements.txt```


### 4. Execute o servidor:

```python manage.py runserver```
