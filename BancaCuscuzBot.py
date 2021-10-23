import re
import telegram

from telegram import User, InlineQueryResultArticle, ParseMode, \
    InputTextMessageContent, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, InlineQueryHandler, CallbackQueryHandler, CommandHandler, MessageHandler, CallbackQueryHandler, Filters
from telegram.utils.helpers import escape_markdown

botToken = "983276512:AAG98DTeyBv-b_x03z3si4FnYGvWEf9h8aM"

cuscuzbot = telegram.Bot(botToken)

def produtos(update, context):
    arquivoProdutos = open("produtos.csv", "r+")
    for linha in arquivoProdutos:
        saidaProdutos = linha.split(',')
        update.message.reply_text(str(saidaProdutos[0]) + " " + str(saidaProdutos[1]) + " " + "(" + str(saidaProdutos[2]) + ")" + " " + str(saidaProdutos[3]))
    arquivoProdutos.close()


def buscar(update, context):
    arquivoProdutos = open("produtos.csv", "r+")
    for linha in arquivoProdutos:
        if(re.search(context.args[0], linha, re.IGNORECASE)):
           encontrados = linha.split(',')
           update.message.reply_text(str(encontrados[0]) + " " + str(encontrados[1]) + " " + "(" + str(encontrados[2]) + ")")
    arquivoProdutos.close()

def cabecalhoVendas():
    arquivoVendidosEscrita = open("vendidos.csv", "a+")
    arquivoVendidosEscrita.write("Indíce,Produto,Preço,Modalidade de Venda,Vendedor\n")
    

def dinheiro(update, context):
    arquivoProdutos = open("produtos.csv", "r+")
    arquivoVendidosEscrita = open("vendidos.csv", "a+")
    arquivoVendidosLeitura = open("vendidos.csv", "r+")

    vendas = arquivoVendidosLeitura.readlines()

    numLinhas = sum(1 for linha in vendas)

    vendidos = arquivoProdutos.readlines()

    escolhido = vendidos[int(context.args[0]) - 1]
    vendidoSeperado = escolhido.split(',')

    arquivoProdutos.close()
    arquivoVendidosLeitura.close()

    arquivoVendidosLeitura = open("vendidos.csv", "r+")
    linha = ""

    vendaRealizada = 0

    for linha in arquivoVendidosLeitura:
        vendaFeita = linha.split(',')
        if(vendaFeita[1] == context.args[0]):
            vendaRealizada = 1
    if(vendaRealizada == 1):
        update.message.reply_text("Venda já feita!")
    else:
        if(len(context.args) == 2):
            valorProduto = int(vendidoSeperado[2]) - int(context.args[1])
            arquivoVendidosEscrita.write(str((numLinhas + 1 )) + "," + str(vendidoSeperado[0]) + "," + str(vendidoSeperado[1]) + "," + str(valorProduto) + ",Dinheiro" + "," + str(vendidoSeperado[3]) + ","  + str(vendidoSeperado[4]) + ", \n") 
            update.message.reply_text("Venda realizada com sucesso!")
        else:
            arquivoVendidosEscrita.write(str((numLinhas + 1 )) + "," + str(vendidoSeperado[0]) + "," + str(vendidoSeperado[1]) + "," + str(vendidoSeperado[2]) + ",Dinheiro" + "," + str(vendidoSeperado[3]) + "," + str(vendidoSeperado[4]) + ", \n") 
            update.message.reply_text("Venda realizada com sucesso!")
    

    arquivoVendidosLeitura.close()
    arquivoVendidosEscrita.close()

    

def cartao(update, context):
    arquivoProdutos = open("produtos.csv", "r+")
    arquivoVendidosEscrita = open("vendidos.csv", "a+")
    arquivoVendidosLeitura = open("vendidos.csv", "r+")

    vendas = arquivoVendidosLeitura.readlines()

    numLinhas = sum(1 for linha in vendas)

    vendidos = arquivoProdutos.readlines()

    escolhido = vendidos[int(context.args[0]) - 1]
    vendidoSeperado = escolhido.split(',')

    arquivoProdutos.close()
    arquivoVendidosLeitura.close()

    arquivoVendidosLeitura = open("vendidos.csv", "r+")
    linha = ""

    vendaRealizada = 0

    for linha in arquivoVendidosLeitura:
        vendaFeita = linha.split(',')
        if(vendaFeita[1] == context.args[0]):
            vendaRealizada = 1
    if(vendaRealizada == 1):
        update.message.reply_text("Venda já feita!")
    else:
        if(len(context.args) == 3):
            valorProduto = int(vendidoSeperado[2]) - int(context.args[2])
            arquivoVendidosEscrita.write(str((numLinhas + 1 )) + "," + str(vendidoSeperado[0]) + "," + str(vendidoSeperado[1]) + "," + str(valorProduto) + ",Cartão" + "," + str(context.args[1]) + "," + str(vendidoSeperado[3]) + "," + str(vendidoSeperado[4]) + ", \n") 
            update.message.reply_text("Venda realizada com sucesso!")
        else:
            arquivoVendidosEscrita.write(str((numLinhas + 1 )) + "," + str(vendidoSeperado[0]) + "," + str(vendidoSeperado[1]) + "," + str(vendidoSeperado[2]) + ",Cartão" + "," + str(context.args[1]) + "," + str(vendidoSeperado[3]) + "," + str(vendidoSeperado[4]) + ", \n") 
            update.message.reply_text("Venda realizada com sucesso!")
    

    arquivoVendidosLeitura.close()
    arquivoVendidosEscrita.close()

def vendidos(update, context):
    arquivoVendidosLeitura = open("vendidos.csv", "r+")
    for linha in arquivoVendidosLeitura:
        vendidos = linha.split(',')
        if(vendidos[4] == "Cartão"):
           update.message.reply_text(str(vendidos[1]) + " " + str(vendidos[2]) + " " + str(vendidos[3]) + " " + "(" + str(vendidos[4]) + ")"
                                     + " " + str(vendidos[5]) + " " + str(vendidos[6]))
        else:
            update.message.reply_text(str(vendidos[1]) + " " + str(vendidos[2]) + " " + str(vendidos[3]) + " " + "(" + str(vendidos[4]) + ")"
                                      + " " + str(vendidos[5]))

def lucro(up1date, context):
    arquivoVendidosLeitura = open("vendidos.csv", "r+")
    arquivoLucroEscrita = open("lucro.csv", "w+")
    arquivoLucroLeitura = open("lucro.csv", "r+")

    vendedores = set()
    totalCuscuz = 0
    totalCartao = 0
    totalVendedor = 0

    for linha in arquivoVendidosLeitura:
        vendidos = linha.split(',')
        if(vendidos[4] == "Cartão"):
            if(int(vendidos[7]) == 1):
                totalCuscuz = totalCuscuz + 0
            else:
                totalCuscuz = totalCuscuz + (float(vendidos[3]) * 0.1)
            if(vendidos[5] == "débito" or vendidos[5] == "debito"):
                totalCartao = totalCartao + (float(vendidos[3]) * 0.019)
            elif(vendidos[5] == "1x"):
                totalCartao = totalCartao + (float(vendidos[3]) * 0.046)
            elif(vendidos[5] == "2x"):
                totalCartao = totalCartao + (float(vendidos[3]) * 0.061)
            vendedores.add(vendidos[6])
        else:
            if(int(vendidos[6]) == 1):
                totalCuscuz = totalCuscuz + 0
            else:
                totalCuscuz = totalCuscuz + (float(vendidos[3]) * 0.1)
            vendedores.add(vendidos[5])

    arquivoLucroEscrita.write("Cuscuz HQ," + str(totalCuscuz) + "," + "\n")
    arquivoLucroEscrita.write("Cartão," + str(totalCartao) + "," + "\n")

    arquivoVendidosLeitura.close()

    for it in vendedores:
        arquivoVendidosLeitura = open("vendidos.csv", "r+")
        linha = ""
        for linha in arquivoVendidosLeitura:
            vendidos = linha.split(',')
            if(vendidos[4] == "Cartão"):
                if(it == vendidos[6]):
                    if(int(vendidos[7]) == 1):
                        if(vendidos[5] == "débito" or vendidos[5] == "debito"):
                            totalVendedor = totalVendedor + (float(vendidos[3]) * 0.981)
                        elif(vendidos[5] == "1x"):
                            totalVendedor = totalVendedor + (float(vendidos[3]) * 0.954)
                        elif(vendidos[5] == "2x"):
                            totalVendedor = totalVendedor + (float(vendidos[3]) * 0.939)
                    else:
                        if(vendidos[5] == "débito" or vendidos[5] == "debito"):
                            totalVendedor = totalVendedor + (float(vendidos[3]) * 0.881)
                        elif(vendidos[5] == "1x"):
                            totalVendedor = totalVendedor + (float(vendidos[3]) * 0.854)
                        elif(vendidos[5] == "2x"):
                            totalVendedor = totalVendedor + (float(vendidos[3]) * 0.839)
            else:
                if(it == vendidos[5]):
                    if(int(vendidos[6]) == 1):
                        totalVendedor = totalVendedor + (float(vendidos[3]))# * 0.9)
                    else:
                        totalVendedor = totalVendedor + (float(vendidos[3]) * 0.9)
        
        arquivoLucroEscrita.write(str(it) + "," + str(totalVendedor) + "," + "\n")
        totalVendedor = 0
        arquivoVendidosLeitura.close()

    totalGeralCartao = 0
    totalGeralDinheiro = 0
    totalGeral = 0

    arquivoVendidosLeitura = open("vendidos.csv", "r+")
    linha = ""
    for linha in arquivoVendidosLeitura:
        vendidos = linha.split(',')
        totalGeral = totalGeral + float(vendidos[3])
        if(vendidos[4] == "Cartão"):
            totalGeralCartao = totalGeralCartao + float(vendidos[3])
        else:
            totalGeralDinheiro = totalGeralDinheiro + float(vendidos[3])

    
    arquivoLucroEscrita.write("Total Vendas Cartão" + "," + str(totalGeralCartao) + "," + "\n")
    arquivoLucroEscrita.write("Total Vendas Dinheiro" + "," + str(totalGeralDinheiro) + "," + "\n")
    arquivoLucroEscrita.write("Total Geral de Vendas" + "," + str(totalGeral) + "," + "\n")

    arquivoVendidosLeitura.close()

    arquivoLucroEscrita.close()


def planilha(update, context):
    arquivoLucroLeitura = open("lucro.csv", "r")

    for linha in arquivoLucroLeitura:
        lucros = linha.split(',')
        update.message.reply_text(str(lucros[0]) + " " + "(" + str(lucros[1]) + ")")

    arquivoLucroLeitura.close()



def ajuda(update, context):
    update.message.reply_text("Esse bot foi criado para ajudar com as vendas na banca do evento Cuscuz HQ. \n" +
                              "Abaixo se encontram os comandos disponíveis e suas formas de utilização. \n" + "\n" +
                              "/buscar - Busca produtos na lista com todos os produtos. Deve-se passar além do comando o nome de algum produto. Ex: /buscar Lanterna Verde \n" + "\n" +
                              "/produtos - Mostra a lista com todos os produtos, contendo o código do produto, nome e preço do produto e nome do vendedor. Esse comando deve ser usado sem parâmetro. Ex: /produtos \n" + "\n" +
                              "/dinheiro - Realiza a venda de um produto na modalidade dinheiro. Essa venda pode ser realizada com ou sem desconto. Quando é feita uma busca pelo produto é retornado além do nome e do preço do produto um código único que deve ser utilizado no momento da venda. Esse comando deve ser usado passando como parâmetro o código do produto a ser vendido e opcionalmente um desconto. Exemplo sem desconto: /dinheiro 12. Exemplo com desconto /dinheiro 12 10 \n" + "\n" +
                              "/cartao - Realiza a venda de um produto na modalidade cartao. Obrigatóriamente deve-se passar se a venda é realizada no débito, 1x, ou 2x. Essa venda pode ser realizada com ou sem desconto. Quando é feita uma busca pelo produto é retornado além do nome e do preço do produto um código único que deve ser utilizado no momento da venda. Esse comando deve ser usado passando como parâmetro o código do produto a ser vendido, a modalidade da venda (débito, 1x ou 2x) e opcionalmente um desconto. Exemplo sem desconto: /cartao 12 2x. Exemplo com desconto /cartao 12 débito 10 \n" + "\n" +
                              "/vendidos - Mostra todos os produtos já vendidos. O comando deve ser usado sozinho sem nenhum parâmetro. Ex: /vendidos \n" + "\n" +
                              "/lucro - Cria uma planilha detalhada com os lucros de cada vendendor, além de já separar a porcentagem que ficará ára a banca do Cuscuz HQ e também as taxas da maquineta, caso alguma venda tenha sido feita no cartão. O comando deve ser usado sozinho sem nenhum parâmetro. Ex: /lucro \n" + "\n" +
                              "/planilha - Exibe a planilha detalhada dos lucros que foi gerada pelo comando /lucro. O comando deve ser usado sozinho sem nenhum parâmetro. Ex: /planilha \n" + "\n" +
                              "/help - Lista todos os comandos e suas descrições")



def main():
    updater = Updater(botToken, use_context=True)

    dp = updater.dispatcher
    
    #Comandos
    dp.add_handler(CommandHandler("buscar", buscar, pass_args=True))
    dp.add_handler(CommandHandler("produtos", produtos, pass_args=True))
    dp.add_handler(CommandHandler("dinheiro", dinheiro, pass_args=True))
    dp.add_handler(CommandHandler("cartao", cartao, pass_args=True))
    dp.add_handler(CommandHandler("vendidos", vendidos, pass_args=True))
    dp.add_handler(CommandHandler("lucro", lucro, pass_args=True))
    dp.add_handler(CommandHandler("planilha", planilha, pass_args=True))
    dp.add_handler(CommandHandler("help", ajuda, pass_args=True))

    
    # Start the Bot
    updater.start_polling()
    # Block until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
