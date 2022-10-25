

import os #ela é uma biblioteca de comandos do sistema operacional que vai te auxiliar a fazer algumas operações dentro do seu computador

import shutil #Essa biblioteca ira permitir voce copiar e colar atravez desse parametro shutill.copy2(Variavel,Destinoparaqualseracolado)

#Aqui estou dando exemplo da minha camera que uso para par os arquivos CR3 e mover para outro lugar sem deletar

#aqui eu uso duas barras \\ para nao ter conflito

pastadestiono = "E:\\DCIM\\100CANON" # Variavel Caminho da pasta

os.chdir(pastadestiono) #Os.chdir método usado para alterar o diretório de trabalho atual para o caminho especificado.


#Lista de arquivos
pastadesintoo = os.listdir() # os.listdir() é usado para obter a lista de todos os arquivos e diretórios no diretório especificado.
#
Numero_incial = 0 # Variavel 0


for arquivos in pastamodificada: # "for"para "arquivos" no caso os arquivos que serão modificado "in" da pasta tal que no caso "pastamodificada"
  
     if "CR3" in arquivos: #"if" se String tipo de arquivo, no caso "CR3" no "in" "arquivos"
        print(arquivos + " encontrados") #Printando arquivos da pasta e acrescentando string + " encontrados"

        shutil.copy2(arquivos,"C:\\Users\\Desktop\\Desktop\\Diretorio\\") # Aqui ira colar os arquivos, de onde ele copior os "arquivos"
        Numero_incial += 1 #mudança de numero diferente
        
print(f'\nTotal de arquivos {Numero_incial}\n\nTerminado') #Printando os arquivos gerais copiados e totalizando-os eles.

# Muito obrigado
Print("ass: Autentico")
        
