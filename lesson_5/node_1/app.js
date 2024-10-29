'use strict';

const express = require('express');

const PORT = 5001;
const HOST = '0.0.0.0';

const app = express();

app.get('/', (req, res) => {
    res.send("<h1>Olá, sou o APP 1 e estou pronto para resonder as requisições")
})

app.listen(PORT, HOST);
console.log('Running');