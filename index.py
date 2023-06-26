import string
import sys

def ContadorPalavras(): 
    palavras = {} # cria um dicionário vazio 
    caracteres_removidos = string.whitespace + string.punctuation + string.digits
    nome_arquivo = sys.argv[1] # atribui  o nome do arquivo 
    
    with open(nome_arquivo, encoding="utf-8") as arquivo: 
        for linha in arquivo: 
            linha = linha.lower()
            for palavra in linha.split(): 
                palavra = palavra.strip(caracteres_removidos) # remove caracteres especiais
                if len(palavra) > 3: 
                    palavras[palavra] = palavras.get(palavra, 0) + 1 # Conta cada palavra    
    
    nome_arquivo_saida = "rank_palavras.txt"
    with open(nome_arquivo_saida, "w") as arquivo_saida: # Abre um novo arquivo
        for palavra, frequencia in sorted(palavras.items(), key=lambda x: x[1], reverse=True): # Itera e ordena as palavras do dicionário
            linha = f"Palavra '{palavra}' aparece {frequencia} vezes\n"
            arquivo_saida.write(linha) # Escreve o rank no arquivo

    

if __name__ == "__main__": # Verifica se o script está sendo executado
    ContadorPalavras() 
