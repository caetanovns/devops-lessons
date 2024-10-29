# Use a imagem base do Golang
FROM golang:1.17

# Crie e defina o diretório de trabalho
WORKDIR /go/src/app

# Copie os arquivos necessários
COPY . .

# Baixe as dependências
RUN go mod init app

# Construa o aplicativo
RUN go build -o main .

# Expõe a porta 8080
EXPOSE 8080

# Comando para executar o aplicativo
CMD ["./main"]
