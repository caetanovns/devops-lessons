'use strict';

const express = require('express');

const PORT = 5002;
const HOST = '0.0.0.0';

const app = express();

app.get('/', (req, res) => {
    res.send("<h1>Olá, sou o APP 2 e estou pronto para resonder as requisições</h1>")
})

app.listen(PORT, HOST);
console.log('Running');