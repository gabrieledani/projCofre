#https://www.geeksforgeeks.org/encrypt-and-decrypt-files-using-python/
import PySimpleGUI as sg
import file_crypto
import os


if os.path.isfile('filekey.key'):
    key = open('filekey.key', 'r').read()
    #print(key)
else:
    key = file_crypto.key_generation
    #print('new key-',key)

file_cofre = 'cofre.csv'
cofreo = open(file_cofre,'r').read()
if cofreo !='':
    file_crypto.file_decrypt(file_cofre,key)
    
def criar_janela1():
    layout = [
                [sg.Text('Usuario:'), sg.Input(key='usuario')],
                [sg.Text('Senha:'), sg.Input(key='senha')],
                [sg.Button('Entrar'), sg.Button('Sair')],
                [sg.Text('',key='alerta')],
             ]
    return sg.Window('Cofre de Senhas', layout, finalize=True)

def criar_janela2():
    dados_geral=''
    cofre = open('cofre.csv','r')            
    for lin in cofre:
        link,usuario,senha = lin.strip().split(';')
        dados_geral = dados_geral + 'Link:'+link+' Usuário:'+usuario+' Senha:'+senha+'\n'
    cofre.close()

    layout = [
                [sg.Text(dados_geral,key='dados')],
                [sg.Button('Novo'), sg.Button('Sair')]
             ]
    return sg.Window('Lista de Dados', layout, finalize=True)

def criar_janela3():
    layout = [
                [sg.Text('Link:'), sg.Input(key='linkn')],
                [sg.Text('Usuario:'), sg.Input(key='usuarion')],
                [sg.Text('Senha:'), sg.Input(key='senhan')],
                [sg.Button('Salvar'), sg.Button('Sair')]
             ]
    return sg.Window('Novo Dado', layout, finalize=True)

janela1, janela2, janela3 = criar_janela1(), None, None

while True:
    window, event, values = sg.read_all_windows()
    if window == janela1 and event in (sg.WIN_CLOSED, 'Sair'):
        break

    if window == janela1:
        if event == 'Entrar':
            usuario_tela = values['usuario']
            senha_tela = values['senha']
            try:
                file_login = 'login.csv'
                file_crypto.file_decrypt(file_login,key)
                arquivo = open(file_login,'r')
                usuario, senha = arquivo.read().split(';')
            except:
                arquivo = open('login.csv','w')
                usuario = usuario_tela
                senha = senha_tela
                arquivo.write(usuario+';'+senha)
            arquivo.close()
            file_crypto.file_encrypt(file_login,key)

            if (usuario.lower() == usuario_tela.lower()) and (senha == senha_tela):
                janela1.close()
                janela2 = criar_janela2()
            else:
                janela1['alerta'].update('Dados de Acesso Incorretos!')
            

    if window == janela2:
        if event == 'Novo':
            janela2.hide()
            janela3 = criar_janela3()
        elif event in (sg.WIN_CLOSED, 'Sair'):
            break
    
    if window == janela3:
        if event in (sg.WIN_CLOSED, 'Sair'):
            janela3.hide()
            janela2.un_hide()
        elif event == 'Salvar':

            arquivo = open('cofre.csv','a')
            link_novo = values['linkn']
            usuario_novo = values['usuarion']
            senha_novo = values['senhan']
            arquivo.write(link_novo+';'+usuario_novo+';'+senha_novo+'\n')
            arquivo.close()

            dados_geral=''
            cofre = open('cofre.csv','r')            
            for lin in cofre:
                link,usuario,senha = lin.strip().split(';')
                dados_geral = dados_geral + 'Link:'+link+' Usuário:'+usuario+' Senha:'+senha+'\n'
            cofre.close()
            
            janela2['dados'].update(dados_geral)
            janela3.hide()
            janela2.un_hide()           

file_crypto.file_encrypt(file_cofre,key)
window.close()
