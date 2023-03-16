
# Docker Parte II

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

### 2. Bind Mounts

- A seguir [remova todos os container](#para-remover-os-container)

- Vamos criar container utilizando um volume
- Para isso, crie uma pasta no `home` do `host`
- O Parâmetro `-v` indica um volume que deve ser passado

```bash
docker run -it -v /home/username/volume-docker:/app ubuntun bash
```

- Após isso, podemos notar que qualquer arquivo criado dentro do **container** será mapeado para minha pasta do `host`.
  
- Podemos em seguida criar um novo container, e podemos notar que o arquivo será mantido dentro do novo container.

- Outro mecanismo de utilizar volumes são através de **bind mounts**, são mais semânticos.
  
```bash
docker run -it --mount type=bind,source=/home/username/volume-docker,target=/app ubuntun bash
```

- Notamos que mesmo criando o bind, ainda mantemos os mesmo arquivos criados anteriormente.

### 3. Volumes

- O Docker pode gerenciar nossos volumes de armazenamento
- Maneira mais recomendada
- Para verificar os volumes criados

```bash
docker volume ls
```

- Para criar um novo volume

```bash
docker volume create [NAME]
```

- Agora ao invés de mapear para uma pasta em nosso `host`, podemos mapear o nossos arquivos sejam mapeados para o volume do **docker**.
- Para isso, então faça:

```bash
docker run -it - [VOLUME_NAME]:/app ubuntu bash
```

- Assim, temos os arquivos gerados dentro do container, sendo gerenciados por um volume do docker.
- Caso o parâmetro de volume do docker não esteja criado, o docker criará um novo volume para ser armazenado os arquivos.

### 4. Networks

### opcional

- Com esse comando podemos inspecionar cada elemento do container, inclusive sua rede.

```bash
docker inspect DOCKER_ID
```

- O Docker permite a criação de redes, para comunicação dos container
- Através do comando `networks ls`, podemos visualizar as redes criadas
- Por padrão o docker configura uma imagem com a rede `bridge`
- O grande problema é que na rede bridge não temos o DNS para resolver os IP's

```bash
docker network ls
```

- Então para resolver, podemos então criar uma nova rede local

```bash
docker network create --driver bridge minha-bridge
```

- Agora, no momento de criar um novo container, podemos definir sua rede
- **Porém é fundamental passar um nome para o container**

```bash
docker run -it --name ubuntu1 --network minha-bridge ubuntu bash
```

- Network `none`, container fica sem comunicação
- Network `host`, container fica com comunicação direta com o host

### 5. Compose

- Coordenação de container
- Podemos configura a organização de diferentes containers
