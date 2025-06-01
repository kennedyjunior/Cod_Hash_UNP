mport customtkinter as ctk
from PIL import Image, ImageTk
 Pedro-Henrique
import hashlib
import tkinter.messagebox as messagebox

import hashlib
import tkinter.messagebox as messagebox


 main
janela = ctk.CTk()
janela.geometry("500x400")
janela.title("Codificador Hash")

janela._set_appearance_mode("Dark")

tema_atual = "Dark"

icone = Image.open("img/icone.ico")
icone_tk = ImageTk.PhotoImage(icone)
janela.iconbitmap("img/icone.ico")

img_sol = ctk.CTkImage(light_image=Image.open("img/sol.png"), size=(20,20))
img_lua = ctk.CTkImage(light_image=Image.open("img/lua.png"), size=(20,20))


def alternar_tema():
    global tema_atual
    if tema_atual == "Dark":
        ctk.set_appearance_mode("Light")
        tema_atual = "Light"
        btn_tema.configure(image=img_sol, text="Light mode", text_color="black", fg_color="#ACA8A8",
                           hover_color="#505050", border_color="#000000")
        btn.configure(text_color="black", hover_color="#505050", border_color="black", fg_color="#ACA8A8")

    else:
        ctk.set_appearance_mode("Dark")
        tema_atual = "Dark"
        btn_tema.configure(image=img_lua, text="Dark mode", text_color="white", fg_color="#333030",
                           hover_color="#6B1CB4", border_color="#6B1CB4")
        btn.configure(text_color="white", hover_color="#6B1CB4", border_color="#6B1CB4",
                      fg_color="#333030")
        

btn_tema = ctk.CTkButton(janela, text="Dark mode", image=img_lua, fg_color="#333030",
                         hover_color="#6B1CB4", border_color="#6B1CB4", 
                         border_width=2,                        
                          command= alternar_tema, width=40, height=40)
btn_tema.place(relx=1.0, rely= 0.0, anchor= "ne", x=-10, y=10)


btn = ctk.CTkButton(master=janela, text="Codificar", font=("Bold", 20), corner_radius=32, fg_color="transparent",
                    hover_color="#6B1CB4", border_color="#6B1CB4",
                    border_width=2)
btn.place(x=350, y=100)

 Pedro-Henrique
frame_txt_principal = ctk.CTkFrame(janela, border_width=2, border_color="#6B1CB4", fg_color="transparent")
frame_txt_principal = ctk.CTkFrame(janela, border_width=2, border_color="#6B1CB4", fg_color="transparent")

frame_txt_principal = ctk.CTkFrame(janela, border_width=2, border_color="#6B1CB4", fg_color="transparent",)
 main
frame_txt_principal.place(x=25, y=10)
texto_principal = ctk.CTkLabel(frame_txt_principal, text="Escolha o modo que deseja:", font=("Bold",23), fg_color="#333030")
texto_principal.pack(padx=3, pady=2)

box_text_cod = ctk.CTkEntry(janela, width=295, height=30, placeholder_text="Insira o texto que deseja codificar:", border_color="#6B1CB4",
                            border_width=2, fg_color="#333030")
box_text_cod.place(x=25, y=100)

def alterar_place_holder_cod():
    box_text_cod.configure(placeholder_text="Insira o texto que deseja codificar: ")
    btn.configure(text="Codificar")
    janela.focus_set()

def alterar_place_holder_dec():
    box_text_cod.configure(placeholder_text="Insira o texto que deseja decodificar: ")
    btn.configure(text="Decodificar")
    janela.focus_set()

janela.bind("<Button-1>", alterar_place_holder_cod)

def alterar_btn():
    btn.configure(text="Codificar")

def alterar_btn1():
    btn.configure(text="Decodificar")
    

box_text_dec2 = ctk.CTkEntry(janela, width=295, height=30, placeholder_text="Insira o valor shift: ", border_color="#6B1CB4",
                            border_width=2, fg_color="#333030")
box_text_dec2.place(x=25, y=150)

box_text_dec1 = ctk.CTkEntry(janela, width=295, height=30, placeholder_text="Aqui irá aparecer o resultado da sua requisição", border_color="#6B1CB4",
                            border_width=2, fg_color="#333030")
box_text_dec1.place(x=25, y=150)
box_text_dec1.place(x=25, y=200)
box_text_dec1.configure(state="readonly")



btn_codificar = ctk.CTkButton(master=janela, text="Codificar", command=alterar_place_holder_cod, font=("Bold", 20),
                              corner_radius=32, fg_color="#333030",
                              hover_color="#6B1CB4", border_color="#6B1CB4",
                              border_width=2)
btn_codificar.place(x=25, y= 55)

btn_decodificar = ctk.CTkButton(master=janela, text="Decodificar", command=alterar_place_holder_dec, font=("Bold", 20),
                              corner_radius=32, fg_color="#333030",
                              hover_color="#6B1CB4", border_color="#6B1CB4",
                              border_width=2)
btn_decodificar.place(x=180, y= 55)




janela.mainloop()