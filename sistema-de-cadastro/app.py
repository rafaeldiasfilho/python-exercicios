from typing import Tuple
import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
import openpyxl, xlrd
import pathlib
from openpyxl import Workbook


# Setando a aparecencia do sistema 
ctk.set_appearance_mode("Sistema")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
  def __init__(self):
    super().__init__()
    self.layout_config()
    self.appearence()
    self.todo_sistema()

  def layout_config(self):
    self.title("Sistema de Cadastro de Produtos")
    self.geometry("700x500")

  def appearence(self):
    self.lb_apm = ctk.CTkLabel(self, text="Tema", bg_color="transparent", text_color=['#000', '#fff']).place(x=50, y=430)
    self.opt_apm = ctk.CTkOptionMenu(self, values=["Light", "Black", "Sistema"], command=self.change_apm).place(x=50, y=460)


  def todo_sistema(self):
    frame = ctk.CTkFrame(self, width=700, height=50, corner_radius=0, bg_color="teal", fg_color="teal").place(x=0, y=10)
    title = ctk.CTkLabel(frame, text="Sistema de Cadastro de Produtos", font=("Century Gothic bold", 24), text_color="#fff")

    span = ctk.CTkLabel(self, text="Por favor, preencha todos os campos do formulário!", font=("Century Gothic bold", 16), text_color=["#000", "#fff"]).place(x=50, y=70)


    #Entrys
    name_entry = ctk.CTkEntry(self, width=350, font=("Century Gothic bold", 16), fg_color="transparent")
    contato_entry = ctk.CTkEntry(self, width=200, font=("Century Gothic bold", 16), fg_color="transparent")
    age_entry = ctk.CTkEntry(self, width=150, font=("Century Gothic bold", 16), fg_color="transparent")
    adress_entry = ctk.CTkEntry(self, width=200, font=("Century Gothic bold", 16), fg_color="transparent")

    #ComboBox
    genero_combobox = ctk.CTkComboBox(self, values=["Masculino", "Feminino"], font=("Century Gothic bold", 14), width=150)
    genero_combobox.set("Masculino")

    #Entrada de observações
    obs_entry = ctk.CTkTextbox(self, width=500, height=150, font=("arial", 18), border_color="#aaa", border_width=2, fg_color="transparent")

    #Labels
    lb_produto= ctk.CTkLabel(self, text="Nome do Produto:", font=("Century Gothic bold", 16), text_color=["#000", "#fff"])
    lb_contato = ctk.CTkLabel(self, text="Contato:", font=("Century Gothic bold", 16), text_color=["#000", "#fff"])
    lb_age = ctk.CTkLabel(self, text="Idade:", font=("Century Gothic bold", 16), text_color=["#000", "#fff"])
    lb_genero = ctk.CTkLabel(self, text="Genero:", font=("Century Gothic bold", 16), text_color=["#000", "#fff"])
    lb_address = ctk.CTkLabel(self, text="Endereço", font=("Century Gothic bold", 16), text_color=["#000", "#fff"])
    lb_obs = ctk.CTkLabel(self, text="Observações", font=("Century Gothic bold", 16), text_color=["#000", "#fff"])

    #Posicionando os elementos na janela
    lb_produto.place(x=50, y=120)
    name_entry.place(x=50, y=150)

    lb_contato.place(x=450, y=120)
    contato_entry.place(x=450, y=150)

    lb_age.place(x=300, y=190)
    age_entry.place(x=300, y=220)

    lb_genero.place(x=500, y=190)
    genero_combobox.place(x=500, y=220)

    lb_address.place(x=50, y=190)
    adress_entry.place(x=50, y=220)

    lb_obs.place(x=50, y=260)
    obs_entry.place(x=150, y=260)



  def change_apm(self, nova_aparencia):
    ctk.set_appearance_mode(nova_aparencia)


if __name__=="__main__": 
  app = App() 
  app.mainloop()