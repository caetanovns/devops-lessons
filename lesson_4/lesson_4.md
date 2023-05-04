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
