# Docker Parte II

## Dicas

- Para facilitar o processo de remoção de muitos container e imagens, podemos utilziar comandos docker aninhahados.

- #### Para remover os container

```bash
docker rm $(docker ps -aq)
```

- Para remover as imagens

```bash
docker rmi $(docker images -q)
```

### 1. Persistência docker

- Vamos entender o problema de persitência no docker.

- #### Crie um container do `ubuntu` no modo interativo

```bash
docker run -it ubuntu bash
```

- Fazendo isso, teremos acesso ao terminal de uma máquina ubuntu
- Abra um novo terminal <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>Space</kbd>
- Faça uma listagens dos container, porém adiciona o parâmetro `-s`, assim podemos visualizar o tamanho do container

- #### Visualizar containers

```bash
docker ps -s
```

- **0B** representa o espaço opacupado pelo container
- **virtual** mosta o espaço ocupado pela imagem

- Agora, vamos executar dentro do **container** o comando para atualização de pacotes

```bash
sudo apt-get update
```

> Agora executando novamente o [comando](#visualizar-containers) para visualizar o tamanho do container, podemos notar uma mudança
> [Crie um novo container ubuntu](#crie-um-container-do-ubuntu-no-modo-interativo), e [visualize](#visualizar-containers) todos os containers.
> Notamos que o primeiro container tem um tamanho diferente do segundo.

## 2. Bind Mouts

- A seguir [remova todos os container](#para-remover-os-container)

```bash
```
