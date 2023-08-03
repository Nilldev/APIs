
########### importando bibliotecas ###############

from tkinter import *
from tkinter import ttk 
from PIL import Image
import requests 
import string
import json 
import datetime 


########## setando variáveis com as cores ############

co0= "#000000" #preto
co1= "#cc1d4e" #vermelho
co2 = "#feffff" #branco
co3 = "#0074eb" #azul
co4 = "435e5a" #
co5 =  "#59b356" #verde
co6 = "#d9d9d9" #cinza

################ Janela principal do aplicativo ##################

janela = Tk()

janela.resizable(width =FALSE, height=FALSE)
janela.geometry('835x360')
janela.title('')
janela.configure(bg=co6)


############################### Criando frames ###############################


app_nome_frame = Frame(janela, width=840, height=50, bg=co2, relief="flat")
app_nome_frame.grid(row=0, column=0, columnspan=3, sticky=NSEW)

################# chamando API ####################

response = requests.get("https://covid-19.dataflowkit.com/v1/world")
info= response
info= json.loads(info.text)

infectados=(info["Active Cases_text"])
recuperados=(info["Total Recovered_text"])
mortos=(info["New Deaths_text"])
dia=(info["Last Update"])





mostrar_frame_infectados = Frame(janela, width=220, height=100, bg=co2, relief="flat")
mostrar_frame_infectados.grid(row=1, column=0, sticky=NW, pady=5, padx=5)

mostrar_frame_recuperados = Frame(janela, width=220, height=100, bg=co2, relief="flat")
mostrar_frame_recuperados.grid(row=1, column=1, sticky=NW, pady=5, padx=5)

mostrar_frame_mortos = Frame(janela, width=220, height=100, bg=co2, relief="flat")
mostrar_frame_mortos.grid(row=1, column=2, sticky=NW, pady=5, padx=5)

select_frame = Frame(janela, width=840, height=50, bg=co2, relief="flat")
select_frame.grid(row=2, column=0, columnspan=3, sticky="n", pady=10)


############################# Criando Labels para app_nome_frame ##########################

app_nome = Label(app_nome_frame, text="COVID-19", width=20, height=1, pady=20, relief="flat", anchor=CENTER, font=("Helvetica 25 bold"), bg=co2, fg=co0)

app_nome.grid(row=0, column=0, pady=5)







################### Criando labels para mostrar_frame_infectados ###################

label_infectados = Label(mostrar_frame_infectados, text="Infectados", width=20, height=1, pady=7, padx=0, relief="flat", anchor=NW, font=("Courier 15 bold"), bg=co2, fg=co0)

label_infectados.grid(row=0, column=0, pady=1, padx=13)

mostrar_infectados = Label(mostrar_frame_infectados, text= infectados, width=12, height=1, pady=7, padx=0, relief="flat", anchor=NW, font=("Courier 25 bold"), bg=co2, fg=co0)
 
mostrar_infectados.grid(row=1, column=0, pady=1)

mostrar_info = Label(mostrar_frame_infectados, text=str(dia), width=25, height=1, pady=7, padx=0, relief="flat", anchor=NW, font=("Courier 11 bold"), bg=co2, fg=co0)

mostrar_info.grid(row=2, column=0, pady=1, padx=13)

mostrar_info = Label(mostrar_frame_infectados, text="Total casos ativos de Covid-19", width=33, height=1, pady=7, padx=0, relief="flat", anchor=NW, font=("Courier 8 bold"), bg=co2, fg=co0)

mostrar_info.grid(row=3, column=0, pady=1)

mostrar_azul= Label(mostrar_frame_infectados, text="", width=19, height=1, pady=1, padx=0, relief="flat", anchor=NW, font=("Courier 1 bold"), bg=co3, fg=co0)

mostrar_azul.grid(row=4, column=0, pady=0, padx=0, sticky=NSEW)







################### Criando labels para mostrar_frame_recuperados ###################


label_recuperados = Label(mostrar_frame_recuperados, text="Recuperados", width=20, height=1, pady=7, padx=0, relief="flat", anchor=NW, font=("Courier 15 bold"), bg=co2, fg=co0)

label_recuperados.grid(row=0, column=0, pady=1, padx=13)

mostrar_recuperados= Label(mostrar_frame_recuperados, text=recuperados, width=12, height=1, pady=7, padx=0, relief="flat", anchor=NW, font=("Courier 25 bold"), bg=co2, fg=co0)
 
mostrar_recuperados.grid(row=1, column=0, pady=1)

mostrar_info = Label(mostrar_frame_recuperados, text=str(dia), width=25, height=1, pady=7, padx=0, relief="flat", anchor=NW, font=("Courier 11 bold"), bg=co2, fg=co0)

mostrar_info.grid(row=2, column=0, pady=1, padx=13)

mostrar_info = Label(mostrar_frame_recuperados, text="Total casos ativos de Covid-19", width=33, height=1, pady=7, padx=0, relief="flat", anchor=NW, font=("Courier 8 bold"), bg=co2, fg=co0)

mostrar_info.grid(row=3, column=0, pady=1)

mostrar_verde= Label(mostrar_frame_recuperados, text="", width=19, height=1, pady=1, padx=0, relief="flat", anchor=NW, font=("Courier 1 bold"), bg=co5, fg=co0)

mostrar_verde.grid(row=4, column=0, pady=0, padx=0, sticky=NSEW)







################### Criando labels para mostrar_frame_mortos ###################

label_mortos = Label(mostrar_frame_mortos, text="Mortos", width=20, height=1, pady=7, padx=0, relief="flat", anchor=NW, font=("Courier 15 bold"), bg=co2, fg=co0)

label_mortos.grid(row=0, column=0, pady=1, padx=13)

mostrar_mortos = Label(mostrar_frame_mortos, text= mortos, width=12, height=1, pady=7, padx=0, relief="flat", anchor=NW, font=("Courier 25 bold"), bg=co2, fg=co0)
 
mostrar_mortos.grid(row=1, column=0, pady=1)

mostrar_info = Label(mostrar_frame_mortos, text=str(dia), width=25, height=1, pady=7, padx=0, relief="flat", anchor=NW, font=("Courier 11 bold"), bg=co2, fg=co0)

mostrar_info.grid(row=2, column=0, pady=1, padx=13)

mostrar_info = Label(mostrar_frame_mortos, text="Total casos de mortos de Covid-19", width=33, height=1, pady=7, padx=0, relief="flat", anchor=NW, font=("Courier 8 bold"), bg=co2, fg=co0)

mostrar_info.grid(row=3, column=0, pady=1)

mostrar_vermelho= Label(mostrar_frame_mortos, text="", width=19, height=1, pady=1, padx=0, relief="flat", anchor=NW, font=("Courier 1 bold"), bg=co1, fg=co0)

mostrar_vermelho.grid(row=4, column=0, pady=0, padx=0, sticky=NSEW)



############## criando caixa de seleção ###########################



label_pais=Label(select_frame, text="Selecione o país", width=13, height=1, pady=7, padx = 0, relief="flat", anchor=NW, font=("Ivy 15 bold"), bg=co2,fg=co0)
label_pais.grid(row=0, column=0,pady=1, padx=13)

pais=["Brasil", "Angola", "Portugal", "Cuba", "França", "Espanha"]

combo= ttk.Combobox(select_frame, width=15, font=("ivy 8 bold"))
combo["values"] =(pais)
combo.grid(row=0, column=1, padx=0, pady=13)


janela.mainloop()