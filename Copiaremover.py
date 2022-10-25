import os # entra no sistema operacional 
import shutil # o que ira permitir copiar os arquivos


pastadestiono = "C:\\Users\\DESKTOP\\Pictures\\Pastadeorigem" # a pasta de origem

os.chdir(pastadestiono) # Faz com que pode mexer as pastas 

pasta_que_sera_colado = "C:\\Users\\Desktop\\ARQUIVOONDEVAISERCOLADO\\" # a pasta onde sera colocado os arquivos

listagemdearquivos = os.listdir() # faz a lista dos arquivos



def copiar(): # uma funçãp

    Numero_incial = 0 # variavel 0 inicial para contabilizar todos os arquivos copiados

    for arquivos in listagemdearquivos: #aqui faz entrar em todos os arquivos por lista

        if ".jpg" in arquivos: #aqui voce escolhera o tipo de arquivo que voce deseja copiar no caso só .jpg(ex:> .doc, .txt, .exe, etc..)

            print(f'\033[034mcomparando arquivo\033[m \033[033m{arquivos}\033[m\n\033[032mArquivo indentificado \033[m') # vai printar os arquivo indentifacados

            shutil.copy2(arquivos, pasta_que_sera_colado) # ira fazer a copia dos arquivo indentificados
            Numero_incial += 1 # ira contabilizar todos os arquivos indentificados para copia

        else:
            print(f'\033[031mArquivo\033[m {arquivos}\033[031m nao identificado\033[m\n') # aqui vai dizer os que nao foram indentificados pelo tipo de arquivos
            
    print(f'\nTotal de arquivos copiados {Numero_incial}\n\nTerminado') # aqui ele vai dizer o total de que foi copiado

copiar() #Executando a função
