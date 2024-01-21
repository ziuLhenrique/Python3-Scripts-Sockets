#!/bin/python3

# Importando a biblioteca SOCKET
import socket

# Variável do endereço host do alvo
target_host = "www.target.com.br" 

# Variável da porta do alvo
target_port = "80"

# Criando objeto socket!  
# AF_INET indica que usaremos um endereçoIPv4 padrão ou nome de host
# SOCK_STREAM indica que este será um cliente TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# Conectando o cliente
client.connect((target_host, target_port))

# Enviando alguns dados
# 'b' significa que os dados serão enviados em bytes
client.send(b'GET / HTTP/1.1\r\nHost: target.com\r\n\r\n')

# Recebendo alguns dados
# recv() é utilizado para receber dados do socket conectado!
# 4096 Este é o número de bites a serem recebido em uma única chamada!
response = client.recv(4096)

# exibindo os dados
# A função print é usado para exibir o resultado na saida padrão
# decode() este é um método utilizado para converter dados binários(bytes) em uma string!
print(response.decode())

# Fechando o socket
client.close()



