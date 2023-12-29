// este script pode ser usado para testar o method GET da api, use (node example.js) para executar
// saiba mais em https://github.com/luiisp/FileStorageApi
const host = 'http://localhost:8000'
const id = '' // (opcional) substitua por o id de um arquivo existente se desejado

const apiUrl = `${host}/files/${id}`;

fetch(apiUrl)
    .then(response => {
        if (!response.ok) {
            throw new Error(`error ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        console.log(data);
    })
    .catch(error => {
        console.error('error ', error);
    });
