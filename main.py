import customtkinter as ctk
from PIL import Image, ImageTk
janela = ctk.CTk()
janela.geometry("600x500")
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
        btn_tema.configure(image=img_sol, text="Light mode")
        btn_tema.configure(image=img_sol, text="Light mode", text_color="black", fg_color="#ACA8A8")
        btn.configure(text_color="black")

    else:
        ctk.set_appearance_mode("Dark")
        tema_atual = "Dark"
        btn_tema.configure(image=img_lua, text="Dark mode")
        btn_tema.configure(image=img_lua, text="Dark mode", text_color="white", fg_color="#333030")
        btn.configure(text_color="white")
        

btn_tema = ctk.CTkButton(janela, text="Dark mode", image=img_lua,
btn_tema = ctk.CTkButton(janela, text="Dark mode", image=img_lua, fg_color="#333030",
                         hover_color="#6B1CB4", border_color="#6B1CB4", 
                         border_width=2,                        
                          command= alternar_tema, width=40, height=40)
btn_tema.place(relx=1.0, rely= 0.0, anchor= "ne", x=-10, y=10)


btn = ctk.CTkButton(master=janela, text="Botão", font=("Bold", 20), corner_radius=32, fg_color="transparent",
                    hover_color="#6B1CB4", border_color="#6B1CB4",
                    border_width=2)
btn.place(relx=0.5, rely=0.5, anchor="center")

janela.mainloop()