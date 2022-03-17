# omparador de Hashes
import hashlib

arquivo1 = 'a.txt'
arquivo2 = 'b.txt'

hash1 = hashlib.new('ripemd160')

hash1.update(open(arquivo1, 'rb').read()) # ira ler o arquivo e mandas para o hash - rb arbetura em modo binário

hash2 = hashlib.new('ripemd160')

hash2.update(open(arquivo2, 'rb').read()) #rb arbetura em modo binário

if  hash1.digest() != hash2.digest():
    print(f'o arquivo: {arquivo1} é diferente do arquivo: {arquivo2}')
    print('O hash do arquivo a.txt é: ', hash1.hexdigest())
    print('O hash do arquivo b.txt é: ', hash2.hexdigest())
    #hexdigest vai resumir o hash em exadecimal e via mostrar o hash
else:
    print(f'o arquivo: {arquivo1} é igual ao arquivo: {arquivo2}')
    print('O hash do arquivo a.txt é: ', hash1.hexdigest())
    print('O hash do arquivo b.txt é: ', hash2.hexdigest())
