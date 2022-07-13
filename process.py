import subprocess  # usado para fazer comadno no terminal.

# ping 127.0.0.1

# cada argumento no run é um comando que se escreve - no caso do ping são 2 (1-ping, 2-127.0.0.1)
proc = subprocess.run(['ping', '127.0.0.1'], capture_output=True, text=True)
# capture-output, ao invés de mostrar no terminal, enviar para a variável "proc"
# text é para voltar apenas o texto, pois por padrão ele retorna em byte

# print(proc.stderr)  # verificar erros - caso sem erro NONE
# print(proc.stdout)  # saida do programa - maioria das vezes é NONE
# print(proc.returncode)  # retorna código de processamento - Ex: code 0 = tudo certo
# print(proc.args)  # são os argumentos enviados para o programa

saida = proc.stdout
saida = saida.replace('bytes', 'BYTES')  # trocando um valor por outro na saida
print(saida)

