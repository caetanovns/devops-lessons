# Kubernets

- Instalação do Kubernets linux

## 1. Instalação

O Kubectl será nossa interface de comunicação com o cluster

```bash
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"

curl -LO "https://dl.k8s.io/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl.sha256"

echo "$(cat kubectl.sha256)  kubectl" | sha256sum --check

kubectl version --client --output=yaml
```

Precisamos de instalar o minikube. Ele é uma maquina virtual que possui o nosso cluster.

```bash
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
```

- Precisamos agora instalar na maquina o virtualbox

Por fim, apenas vamos inicializar o minikube e passar o virtualbox como drive de virtualização.

```bash
minikube start --vm-driver=virtualbox
```

## Criando nosso primeiro pod

- Podemos criar os pods através do termnal, porém a maneira mais comum é declarar um arquivo e então aplicar esse arquivo dentro do nosso cluster.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-1
spec:
  containers:
    - name: nginx-container
      image: nginx:latest
```

- No pod acima, temos apenas 1 container, que nesse caso é o nginx.

## Comunicação entre os pods

- Os pods podem se comunicar livrimente, no entanto os ips são modificado quando recriamos os pods.

- Para entendermos isso, vamos criar 2 pods, denominados `pod_1` e `pod_2`. Os dois deverão ter a mesma informação.

- Agora, vamos entrar no primeiro pod e fazer uma requisição ao segundo pod.

- Para entrar no pod, podemos executar o comando

```bash
kubectl exec -it pod-1 -- bash
```

- Dentro do pod, podemos fazer uma requisição para o `pod_2` usando o curl.

- Antes disso, precisamos identificar o IP do `pod_2`, para isso faça:

```bash
kubectl get pods -o wide
```

- Com o IP do `pod_2` faça o seguinte comando:

```bash
curl IP_POD_2
```

- Então podemos executar o comando para destruir e subir um novo `pod_2`.

- Vemos agora que o IP dele é diferente, com isso temos um problema.
- Sempre que os pods iniciarem, terão um novo IP, então como fazemos para manter uma comunicação constante entre os pods?

- Para isso vamos utilizar os `scv`

## SCV

- Os serviços possuem um IP e nunca mudam.
- Não importa se o IP do pod muda, mas o serviço não.
- Os services podemos criar um
  - Cluster IP
  - NodePort
  - Load Balancer
- Os serviços nos ajudam a fazer a comunicação entre diferentes pods dentro do mesmo cluster.
