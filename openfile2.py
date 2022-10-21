from tkinter import *
import tkinter
from tkinter.ttk import *
from tkinter.filedialog import askopenfile 
import time

app = Tk()
app.title('Automatización Alquileres - Patagonik')
app.geometry('400x200') 

def open_file():
    file_path = askopenfile(mode='r', filetypes=[('Excel File', '*xlsx', "*xls")])
    if file_path is not None:
        pass

#Podría ir procesar datos y enviar mail como uno o dos botones en vez de subir archivo
def uploadFiles():
    pb1 = Progressbar(
        app, 
        orient=HORIZONTAL, 
        length=300, 
        mode='determinate'
        )
    pb1.grid(row=4, columnspan=3, pady=20)
    for i in range(5):
        app.update_idletasks()
        pb1['value'] += 20
        time.sleep(1)
    pb1.destroy()
    Label(app, text='File Uploaded Successfully!', foreground='green').grid(row=4, columnspan=3, pady=10)
        
def MandarMail ():
    print("hola")

# smail = tkinter.Button(app, text='Mandar mail', command=MandarMail)
# smail.pack()
# smail.grid(row=0, column=2, padx=10)

subarch = Label(
    app, 
    text='Subir la planilla de noviembre' #agregar mes menos 1 automáticamente? 
    )
subarch.grid(row=1, column=0, padx=10)

subarchbtn = Button(
    app, 
    text ='Choose File', 
    command = lambda:open_file()
    ) 
subarchbtn.grid(row=1, column=1)

dl = Label(
    app, 
    text='Procesar datos de la planilla '
    )
dl.grid(row=2, column=0, padx=10)

dlbtn = Button(
    app, 
    text ='Procesar ', 
    #command = lambda:open_file()
    command = lambda:print("Procesando Wachooo")
    ) 
dlbtn.grid(row=2, column=1)

# ms = Label(
#     app, 
#     text='Upload Marksheet in jpg format '
#     )
# ms.grid(row=2, column=0, padx=10)

# msbtn = Button(
#     app, 
#     text ='Choose File', 
#     command = lambda:open_file()
#     ) 
# msbtn.grid(row=2, column=1)

upld = Button(
    app, 
    text='Mandar Mails', 
    command=MandarMail
    )
upld.grid(row=20, columnspan=10, pady=10)

#podría tener la opción de re-preguntar:
# ¿está seguro que quiere realizar esta acción? La misma no podrá detenerse?



app.mainloop()