# Comandos básicos Docker

Nesta aula teremos uma breve abordagem a respeito do docker.

## Hello World

```bash
docker run hello-world
```

## 1. Primeiro Container

- Neste momento devemos ir ao docker hub para verificar as imagens disponíveis

```bash
docker pull ubuntu
docker run ubuntu
```

- Após instalar a imagem e executar, liste os container da maquina `docker ps` ou `docker ps -a`

- **Porque o container ubuntu finaliza sozinho?**
- Observe na coluna COMMAND **bash**, ele simplismente inicia, abre o bash e depois finaliza
- **Para que o docker se mantenha aberto é necessários pelo menos 1 processo em execução**

## 2. Adicionando comandos ao docker run

- Agora vamos passar comandos para o nosso container

```bash
docker run ubuntu sleep 1d
```

- Agora nosso container ficará aberto, pois o container ficará aguardando o sleep finalizar para ser encerrado.

## 3. Comandos úteis no docker

```bash
docker stop DOCKER_ID
```

```bash
docker start DOCKER_ID
```

- Agora queremos executar um comando em nosso docker
- Então utilizamos o comando `exec`
- O parâmetro `-i` = interativo e `t` = terminal padrão
- O `bash` indica que será o terminal aberto

```bash
docker exec -it DOCKER_ID bash
```

## 4. Mapeando as portas do docker

- Vamos compreender como as portas são distribuidas dentro do container

```bash
docker run -d dockersamples/static-site
```

- Neste momento temos que acessar os serviços que estão na porta 80 ou 443 do container
- No entanto não conseguimos, pois precisamos mapear as portas da nossa máquina para o container
- Antes de execução o comando novamente, devemos apagar o container

```bash
docker rm DOCKER_ID
```

- Agora passamos o parâmetro `-P`, assim o docker entende que queremos mapear as portas internas do container para o host

```bash
docker run -d -P dockersamples/static-site
```

- Para ser possível visualizar melhor, podemos utilizar o comando `port`

```bash
docker port DOCKER_ID
```

- Para melhorar isso, podemos passar o parâmetro `-p`, para que seja feito um mapeamento manual de cada porta

```bash
docker run -d -p 8080:80 dockersamples/static-site
```

## 5. Criando a primeira imagem

- Vamos criar um arquivo chamado de `Dockerfile`

```bash
FROM node:14
WORKDIR /app-node
COPY . .
# RUN npm install
# ENTRYPOINT npm start
ENTRYPOINT node app.js
```

- Agora vamos construri a nossa imagem, apartir do Dockerfile

```bash
docker build -t nodeappfap/app-node:1.0 .
```

- Agora vamos executar nossa maquina

```bash
docker run -d -p 8080:3000 nodeappfap/app-node
```
