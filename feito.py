from datetime import datetime as dt
import locale
# Definir o idioma para português do Brasil
locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

# Função para adicionar um novo dado
def adicionar_dado(nova_data):
    with open (file="Estudos.txt", mode="a", encoding="utf8") as data:
        data.write(nova_data)

data = dt.now().strftime("%H:%M:%S - %a - %d/%b/%Y")
Modulo = int(input("Módulo feito: "))
conteudo = f"Módulo {Modulo:02d} concluido: {data}\n"
adicionar_dado(conteudo)
