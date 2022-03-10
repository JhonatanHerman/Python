
#importando Tkinter
from tkinter import *
from turtle import speed

#importando o pillow
from PIL import Image, ImageTk

import speedtest

#Cores:
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#3fb5a3"  # verde
co3 = "#fc766d"  # vermelha / red
co4 = "#403d3d"   # preta / black
co5 = "#4a88e8"  # Azul / Bblue


#Criando Janela
janela = Tk ()
janela.title("")
janela.geometry('450x300')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)


# Dividindo a janela em 2 frames
frame_logo = Frame(janela, width=450, height=70, background=co1)
frame_logo.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_corpo = Frame(janela, width=450, height=230, background=co1)
frame_corpo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)


#Configurando o frame_logo
imagem = Image.open('speed.png')
imagem = imagem.resize((55, 55))
imagem = ImageTk.PhotoImage(imagem)

l_logo_imagem = Label(frame_logo, height=70, image=imagem, compound=LEFT, padx=10, anchor='nw', font=('Ivy 16 bold'), bg= co1, fg=co3)
l_logo_imagem.place(x=20, y=0)
l_logo_nome = Label(frame_logo, text='Speed Test Internet', padx=30, anchor=NE, font=('Ivy 20 bold'), bg= co1, fg=co4)
l_logo_nome.place(x=75, y=10)

#linnha Divisao
l_logo_linha = Label(frame_logo, width=450, anchor=NW, font=('Ivy 1'), bg= co5)
l_logo_linha.place(x=0, y=57)


#função
def main():
    speed = speedtest.Speedtest()
    download = f"{'{:.2f}'.format(speed.download()/1024/1024)}"
    upload = f"{'{:.2f}'.format(speed.upload()/1024/1024)}"

    l_download['text'] = download
    l_upload['text'] = upload

    botao_testar['text'] = 'Teste novamente'
    botao_testar.place(x=140, y=170)



# configurando o frame_corpo
# download:
l_download = Label(frame_corpo, text='00.00', anchor=NW, font=('arial 25'), bg= co1, fg=co4)
l_download.place(x=30, y=75)
l_download_mb = Label(frame_corpo, text='Mbps download', anchor=NW, font=('Ivy 12'), bg= co1, fg=co4)
l_download_mb.place(x=25, y=130)

imagem_down = Image.open('down.png')
imagem_down = imagem_down.resize((60, 70))
imagem_down = ImageTk.PhotoImage(imagem_down)

l_logo_imagem = Label(frame_corpo, height=70, image=imagem_down, compound=LEFT, padx=10, anchor='nw', font=('Ivy 16 bold'), bg= co1, fg=co3)
l_logo_imagem.place(x=160, y=80)


#upload:
l_upload = Label(frame_corpo, text='00.00', anchor=NW, font=('arial 25'), bg= co1, fg=co4)
l_upload.place(x=305, y=75)
l_upload_mb = Label(frame_corpo, text='Mbps upload', anchor=NW, font=('Ivy 12'), bg= co1, fg=co4)
l_upload_mb.place(x=300, y=130)

imagem_up = Image.open('up.png')
imagem_up = imagem_up.resize((60, 70))
imagem_up = ImageTk.PhotoImage(imagem_up)

l_logo_imagem = Label(frame_corpo, height=70, image=imagem_up, compound=LEFT, padx=10, anchor='nw', font=('Ivy 16 bold'), bg= co1, fg=co3)
l_logo_imagem.place(x=220, y=80)


#botao:
botao_testar = Button(frame_corpo,command= main, height=2, text='Iniciar Teste', font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, bg= co5, fg=co1)
botao_testar.place(x=160, y=170)



janela.mainloop ()
