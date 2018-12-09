# encoding: utf-8
import requests
import argparse

usage = ''': python %(prog)s [-u url] [-f file] [-t type]'''
da = argparse.ArgumentParser(usage=usage)
da.add_argument("-u", "--url", type=str, help="", dest="host")
da.add_argument("-f", "--file", type=str, help="", dest="wordlist")
da.add_argument("-t", "--type", type=str, help="D to directory | A to archives)", dest="type")
args = da.parse_args()

url = args.host  # URL a ser testada
tipo = args.type

try:
    print '[+] Professor James Bath [+]'
    print 'Ajude-me doando uma moedinha :-)'
    print 'Carteira BTC: 1BQoLPnfUVqvQk7gS3Ko787zEMVGK4uFNP'
    print '\n'
    arquivo = open(args.wordlist, "r")  # ARQUIVO com a wordlist
    # Verificação se a última linha da wordlist está com \n no final
    # size = arquivo.readlines()
    # sizeH = len(size) - 1
    # line = size[sizeH]
    # if (not line.endswith('\n')) == False:
    #     print '[V]Wordlist válida'
    #     print'''
    #
    #             ==================================
    #             ============INICIANDO=============
    #             ==================================
    #                 '''
    # else:
    #     print '[F]Remova última linha em branco na wordlist'
    #     exit()
except Exception as erro:
    print '\n[!] ERROR: ' + str(erro)

if __name__ == '__main__':
    if tipo == "D" or tipo == "d" or tipo == "directory" or tipo == "DIRECTORY":
        print '''\n
				=========+SCANEANDO DIRETÓRIOS+========
		\n'''
        for linhas in arquivo:
            linhas = linhas.rstrip('\n')
            link = url+ linhas+'/'
            # link = link1[:-1]
            request = requests.get(link, timeout=3)
            status = request.status_code
            if status == 200:
                print "[+] Destino existente: " + link + " | STATUS: " + str(status)
            elif status == 403:
                print "[%] Destino privado: " + link + " | STATUS: " + str(status)
            else:
                print "[-] Destino inexistente: " + link + " | STATUS: " + str(status)
    elif tipo == "A" or tipo == "a" or tipo == "archives" or tipo == "ARCHIVES":
        print '''\n
        				=========+SCANEANDO ARQUIVOS+========
        		\n'''
        for linhas in arquivo:
            linhas = linhas.rstrip('\n')
            link = url + linhas
            request = requests.get(link, timeout=3)
            status = request.status_code
            if status == 200:
                print "[+] Destino existente: " + link + " | STATUS: " + str(status)
            elif status == 403:
                print "[%] Destino privado: " + link + " | STATUS: " + str(status)
            else:
                print "[-] Destino inexistente: " + link + " | STATUS: " + str(status)
    else:
        print '[!] Escolha um tipo de teste'

