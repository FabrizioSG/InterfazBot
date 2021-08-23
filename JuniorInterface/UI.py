from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import requests
import json
import webbrowser
root = Tk()
root.geometry("765x740")
root.option_add('*Font','19')
root.eval('tk::PlaceWindow . center')
root.title("Jr Jenkins")
root.configure(bg = "black")

canvas = Canvas(root, width = 300, height = 700, highlightthickness=0)
canvas.grid(row=1,columnspan =10,padx=235)
img = PhotoImage(file="Omni.png")
canvas.create_image(-9,-9,anchor=NW, image=img)

def open_url(url):
   webbrowser.open_new_tab(url)

def cambioEmail():
    email = Toplevel()
    email.geometry("800x225")
    # telefono.eval('tk::PlaceWindow . center')
    email.title("Cambio de correo")
    email.option_add('*Font', '19')
    email.configure(bg="black")
    relleno = Label(email, text='', bg="black", fg ="white")
    relleno.grid(row=0, column=0, padx=5, pady=5)
    labelSub = Label(email, text='Ingrese el correo actual del usuario', bg="black", fg ="white")
    labelSub.grid(row=1, column=2, padx=5, pady=5)
    labelEmail = Label(email, text='Ingrese el nuevo correo del usuario', bg="black", fg ="white")
    labelEmail.grid(row=2, column=2, padx=5, pady=5)
    sub = Entry(email, width=50)
    sub.grid(row=1, column=3, padx=5, pady=5)
    emailE = Entry(email, width=50)
    emailE.grid(row=2, column=3, padx=5, pady=5)

    var1 = IntVar()
    chkTaxi = Checkbutton(email, text="Usuario es taxista", variable=var1, onvalue=1, offvalue=0, bg="black",fg="#f74615")
    chkTaxi.grid(row=3, column=3)
    var2 = IntVar()
    chkMoni = Checkbutton(email, text="Usuario tiene MONI", variable=var2, onvalue=1, offvalue=0, bg="black", fg="#f74615")
    chkMoni.grid(row=4, column=3)

    button_border = Frame(email, highlightbackground="#f74615",
                          highlightthickness=2, bd=0)
    button_border.grid(padx=10, pady=10, row=5, column=3)

    myButton3 = Button(button_border, text="ENVIAR",
                       command=lambda: updateEmailSend(str(sub.get()), str(emailE.get()), str(var1.get()),
                                                            str(var2.get())), fg="white", bg='#252626',width = 20)
    myButton3.grid(row=5, column=3)

def updateEmailSend(viejo,nuevo,taxi,moni):
    titulo = ""
    if(moni == "1" and taxi == "0"):
        titulo = "Cambio de Correo Con Moni NO Conductor"
    elif(moni == "1" and taxi == "1"):
        titulo = "Cambio de Correo con Moni Conductor"
    elif(moni == "0" and taxi == "0"):
        titulo = "Cambio de Correo sin Moni NO conductor"
    elif(moni == "0" and taxi == "1"):
        titulo = "Cambio de Correo sin Moni Conductor"

    if (viejo != "" and nuevo != ""):
        url = "https://0mn1.atlassian.net/rest/api/2/issue"
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        payload = json.dumps(
            {
                "fields": {
                    "project":
                        {
                            "key": "SP"
                        },
                    "summary": titulo,
                    "description": "{code} CALL spj_UpdateDataEmail('" + str(viejo) + "','" + str(
                        nuevo) + "'," + taxi + "," + moni + ");{code}",
                    "issuetype": {
                        "name": "Task"
                    },
                    "assignee": {
                        "accountId": "5efa27d354020e0ba81f41b4"
                    },

                }
            }
        )
        response = requests.post(url, headers=headers, data=payload,
                                 auth=("jenkins_user@omni.cr", "XSH0vBpc7PHREqXKhncg07A6"))
        data = response.json()
        #print(data)
        open_url("https://0mn1.atlassian.net/browse/" + data["key"])
    else:
        messagebox.showwarning(title=None, message="Por favor ingrese todos los datos solicitados")

def cambioTelefono():
    telefono = Toplevel()
    telefono.geometry("800x225")
    #telefono.eval('tk::PlaceWindow . center')
    telefono.title("Cambio de numero")
    telefono.option_add('*Font', '19')
    telefono.configure(bg="black")
    relleno = Label(telefono, text='', bg="black", fg ="white")
    relleno.grid(row=0, column=0, padx=5, pady=5)
    labelSub = Label(telefono, text='Ingrese el telefono actual del usuario', bg="black", fg ="white")
    labelSub.grid(row=1, column=2, padx=5, pady=5)
    labelEmail = Label(telefono, text='Ingrese el nuevo telefono del usuario', bg="black", fg ="white")
    labelEmail.grid(row=2, column=2, padx=5, pady=5)
    sub = Entry(telefono, width=50)
    sub.grid(row=1, column=3, padx=5, pady=5)
    emailE = Entry(telefono, width=50)
    emailE.grid(row=2, column=3, padx=5, pady=5)

    var1 = IntVar()
    chkTaxi = Checkbutton(telefono, text="Usuario es taxista", variable=var1, onvalue=1, offvalue=0, bg="black", fg="#f74615")
    chkTaxi.grid(row=3, column=3)
    var2 = IntVar()
    chkMoni = Checkbutton(telefono, text="Usuario tiene MONI", variable=var2, onvalue=1, offvalue=0, bg="black", fg="#f74615")
    chkMoni.grid(row=4, column=3)

    button_border = Frame(telefono, highlightbackground="#f74615",
                          highlightthickness=2, bd=0)
    button_border.grid(padx=10, pady=10, row=5, column=3)

    myButton3 = Button(button_border, text="ENVIAR", command=lambda: updateTelefonoSend(str(sub.get()), str(emailE.get()), str(var1.get()),str(var2.get())), fg="white", bg='#252626',width = 20)
    myButton3.grid(row=5, column=3)

def updateTelefonoSend(viejo,nuevo,taxi,moni):
    titulo = ""
    if (moni == "1" and taxi == "0"):
        titulo = "Cambio de Numero Con Moni NO Conductor"
    elif (moni == "1" and taxi == "1"):
        titulo = "Cambio de Numero con Moni Conductor"
    elif (moni == "0" and taxi == "0"):
        titulo = "Cambio de Numero sin Moni NO conductor"
    elif (moni == "0" and taxi == "1"):
        titulo = "Cambio de Numero sin Moni Conductor"

    if(viejo != "" and nuevo != ""):
        url = "https://0mn1.atlassian.net/rest/api/2/issue"
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        payload = json.dumps(
            {
                "fields": {
                    "project":
                        {
                            "key": "SP"
                        },
                    "summary": titulo,
                    "description": "{code} CALL spj_UpdateDataPhone('" + str(viejo) + "','" + str(
                        nuevo) + "'," + taxi + "," + moni + ");{code}",
                    "issuetype": {
                        "name": "Task"
                    },
                    "assignee": {
                        "accountId": "5efa27d354020e0ba81f41b4"
                    },

                }
            }
        )
        response = requests.post(url, headers=headers, data=payload,
                                 auth=("jenkins_user@omni.cr", "XSH0vBpc7PHREqXKhncg07A6"))
        data = response.json()
        #print(data["key"])
        open_url("https://0mn1.atlassian.net/browse/" + data["key"])

    else:
        messagebox.showwarning(title=None, message="Por favor ingrese todos los datos solicitados")

def reembolso():
    reemb = Toplevel()
    reemb.geometry("800x225")
    # telefono.eval('tk::PlaceWindow . center')
    reemb.title("Reembolso o débito de dinero")
    reemb.option_add('*Font', '19')
    reemb.configure(bg="black")
    relleno = Label(reemb, text='', bg="black", fg ="white")
    relleno.grid(row=0, column=0, padx=5, pady=5)
    labelTel = Label(reemb, text='Ingrese el telefono del usuario', bg="black", fg ="white")
    labelTel.grid(row=1, column=2, padx=5, pady=5)
    labelMonto = Label(reemb, text='Ingrese el monto del reembolso', bg="black", fg ="white")
    labelMonto.grid(row=2, column=2, padx=5, pady=5)
    tel = Entry(reemb, width=50)
    tel.grid(row=1, column=3, padx=5, pady=5)
    monto = Entry(reemb, width=50)
    monto.grid(row=2, column=3, padx=5, pady=5)
    labelCombo = Label(reemb, text = 'Seleccione la categoría de la transacción', bg="black", fg ="white")
    labelCombo.grid(row=3, column = 2, padx=5, pady=5)
    combo = ttk.Combobox(reemb,
                                values=[
                                    "Crédito por devolución de transacción de desbloqueo",
                                    "Crédito por devolución de viaje completado bicis",
                                    "Crédito por unificación de cuentas",
                                    "Débito por unificación de cuentas",
                                    "Crédito por transacción fallida de envío a cuenta colones",
                                    "Crédito por transacción fallida de recarga MONI",
                                    "Crédito por transacción fallida de recarga EXTERNA",
                                    "Crédito por transacción fallida de envío de dinero a otro usuario",
                                    "Débito por transacción fallida de recibo de dinero de otro usuario",
                                    "Crédito por devolución de dinero comercio"],
                        state = "readonly", width = 48)
    combo.grid(column=3, row=3, padx=5, pady=5)
    combo.current(0)

    button_border = Frame(reemb, highlightbackground="#f74615",
                          highlightthickness=2, bd=0)
    button_border.grid(padx=10, pady=10, row=5, column=3)

    myButton3 = Button(button_border, text="ENVIAR",
                       command=lambda: reembolsoSend(str(tel.get()), str(monto.get()), str(combo.get())), fg="white", bg='#252626',width = 20)
    myButton3.grid(row=5, column=3)

def reembolsoSend(telefono, monto, fill):
    relleno = rellenoReembolso(fill)
    signo = ""
    titulo = "Reversal Wallet Acreditar"
    if(relleno.__contains__("Débito")):
        signo = "-"
        titulo = "Reversal Wallet Debitar"
    if (telefono != "" and monto != ""):
        url = "https://0mn1.atlassian.net/rest/api/2/issue"
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        payload = json.dumps(
            {
                "fields": {
                    "project":
                        {
                            "key": "SP"
                        },
                    "summary": titulo,
                    "description": "*RECUERDE editar espacio de <fecha> y/o <comercio> en caso de ser necesario* \n {code} CALL spReversal_transaction('" + str(telefono) + "'," + signo + str(
                        monto) + ".00,0," + relleno + ");{code}",
                    "issuetype": {
                        "name": "Task"
                    },
                    "assignee": {
                        "accountId": "5efa27d354020e0ba81f41b4"
                    },

                }
            }
        )
        response = requests.post(url, headers=headers, data=payload,
                                 auth=("jenkins_user@omni.cr", "XSH0vBpc7PHREqXKhncg07A6"))
        data = response.json()
        #print(data["key"])
        open_url("https://0mn1.atlassian.net/browse/" + data["key"])
    else:
        messagebox.showwarning(title=None, message="Por favor ingrese todos los datos solicitados")

def rellenoReembolso(texto):
    relleno = ""
    if(texto == "Crédito por devolución de transacción de desbloqueo"):
        relleno = "1039,1,'Crédito_por_devolución_de_transacción_de_desbloqueo'"
    elif(texto == "Crédito por devolución de viaje completado bicis"):
        relleno = "1028,1,'Crédito_por_devolución_de_viaje_completado_bicis'"
    elif(texto == "Crédito por unificación de cuentas"):
        relleno = "1037,7,'Crédito_por_unificación_de_cuentas'"
    elif(texto == "Débito por unificación de cuentas"):
        relleno = "1037,7,'Débito_por_unificación_de_cuentas'"
    elif(texto == "Crédito por transacción fallida de envío a cuenta colones"):
        relleno = "1035,7,'Crédito_por_transacción_fallida_de_envío_a_cuenta_colones_<fecha>'"
    elif(texto == 'Crédito por transacción fallida de recarga MONI'):
        relleno = "1026,7,'Crédito_por_transacción_fallida_de_recarga_<tipo_de_recarga>_<fecha>'"
    elif(texto == "Crédito por transacción fallida de recarga EXTERNA"):
        relleno = "1024,7,'Crédito_por_transacción_fallida_de_recarga_<tipo_de_recarga>_<fecha>'"
    elif(texto == "Crédito por transacción fallida de envío de dinero a otro usuario"):
        relleno = "1034,7,'Crédito_por_transacción_fallida_de_envío_de_dinero_a_otro_usuario_<fecha>'"
    elif(texto == "Débito por transacción fallida de recibo de dinero de otro usuario"):
        relleno = "1037,7,'Débito_por_transacción_fallida_de_recibo_de_dinero_de_otro_usuario_<fecha>'"
    elif(texto == "Crédito por devolución de dinero comercio"):
        relleno = "1046,7,'Crédito_por_devolución_de_dinero_de_<comercio>'"


    return relleno

def cambioNombreSA():
    nombre = Toplevel()
    nombre.geometry("800x240")
    
    nombre.title("Cambio de Nombre SuperApp")
    nombre.option_add('*Font', '19')
    nombre.configure(bg="black")
    relleno = Label(nombre, text='', bg="black", fg ="white")
    relleno.grid(row=0, column=0, padx=5, pady=5)
    labelTelefono = Label(nombre, text='Ingrese el telefono actual del usuario', bg="black", fg ="white")
    labelTelefono.grid(row=1, column=2, padx=5, pady=5)
    labelNombre = Label(nombre, text='Ingrese el nombre indicado por el usuario', bg="black", fg ="white")
    labelNombre.grid(row=2, column=2, padx=5, pady=5)
    labelApell1 = Label(nombre, text='Ingrese el primer apellido indicado por el usuario', bg="black", fg ="white")
    labelApell1.grid(row=3, column=2, padx=5, pady=5)
    labelApell2 = Label(nombre, text='Ingrese el segundo apellido indicado por el usuario', bg="black", fg ="white")
    labelApell2.grid(row=4, column=2, padx=5, pady=5)
    tel = Entry(nombre, width=40)
    tel.grid(row=1, column=3, padx=5, pady=5)
    name = Entry(nombre, width=40)
    name.grid(row=2, column=3, padx=5, pady=5)
    apell1 = Entry(nombre, width=40)
    apell1.grid(row=3, column=3, padx=5, pady=5)
    apell2 = Entry(nombre, width=40)
    apell2.grid(row=4, column=3, padx=5, pady=5)

    button_border = Frame(nombre, highlightbackground="#f74615",
                          highlightthickness=2, bd=0)
    button_border.grid(padx=10, pady=10, row=5, column=3)

    myButton3 = Button(button_border, text="ENVIAR" , command = lambda: cambioNombreSASend(tel.get(),name.get(),apell1.get(),apell2.get()),
                       fg="white",bg='#252626', width=20)
    myButton3.grid(row=5, column=3)

def cambioNombreSASend(telefono,nombre,apell1,apell2):
    if (telefono != "" and nombre != "" and apell1 != ""):
        url = "https://0mn1.atlassian.net/rest/api/2/issue"
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        payload = json.dumps(
            {
                "fields": {
                    "project":
                        {
                            "key": "SP"
                        },
                    "summary": "Cambio de Nombre SuperApp",
                    "description": "{code} CALL spj_UpdateNameUser(" + str(telefono) + ",'" + str(nombre) + "','" + str(
                        apell1) + "','" + str(apell2) + "'" + ''");{code}",
                    "issuetype": {
                        "name": "Task"
                    },
                    "assignee": {
                        "accountId": "5efa27d354020e0ba81f41b4"
                    },

                }
            }
        )
        response = requests.post(url, headers=headers, data=payload,
                                 auth=("jenkins_user@omni.cr", "XSH0vBpc7PHREqXKhncg07A6"))
        data = response.json()
        #print(data["key"])
        open_url("https://0mn1.atlassian.net/browse/" + data["key"])
    else:
        messagebox.showwarning(title=None, message="Por favor ingrese todos los datos solicitados")

def cierreCuenta():
    cierre = Toplevel()
    cierre.geometry("700x150")
    # telefono.eval('tk::PlaceWindow . center')
    cierre.title("Cierre de cuenta SA")
    cierre.option_add('*Font', '19')
    cierre.configure(bg="black")
    relleno = Label(cierre, text='',bg="black")
    relleno.grid(row=0, column=0, padx=5, pady=5)
    labelTel = Label(cierre, text='Ingrese el numero de telefono del usuario', bg="black", fg ="white")
    labelTel.grid(row=1, column=2, padx=5, pady=5)
    tel = Entry(cierre, width=40)
    tel.grid(row=1, column=3, padx=5, pady=5)

    button_border = Frame(cierre, highlightbackground="#f74615",
                          highlightthickness=2, bd=0)
    button_border.grid(padx=10, pady=10, row=5, column=3)

    myButton3 = Button(button_border, text="ENVIAR",
                       command=lambda: cierreCuentaSend(str(tel.get())), fg="white", bg='#252626',width = 20)
    myButton3.grid(row=5, column=3)

def cierreCuentaSend(tel):
    if(tel != ""):
        url = "https://0mn1.atlassian.net/rest/api/2/issue"
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        payload = json.dumps(
            {
                "fields": {
                    "project":
                        {
                            "key": "SP"
                        },
                    "summary": "Cierre de Cuenta SA",
                    "description": "NOTAS IMPORTANTES \n * Esto es solo el cierre del lado de SuperApp. Si el usuario tiene Moni, se debe gestionar por separado el cierre en Admin Tool y NAE. \n"
                                   "* Tomar en cuenta el dinero en Wallet del usuario antes de hacer el cierre.\n"
                                   "* NO utilizar para Fusion de Cuentas, este se debe escalar a Tech siempre.\n  {code} CALL spjDeleteAccount('" + str(tel) + "','cierre_de_cuenta');{code}",
                    "issuetype": {
                        "name": "Task"
                    },
                    "assignee": {
                        "accountId": "5efa27d354020e0ba81f41b4"
                    },

                }
            }
        )
        response = requests.post(url, headers=headers, data=payload,
                                 auth=("jenkins_user@omni.cr", "XSH0vBpc7PHREqXKhncg07A6"))
        data = response.json()
        #print(data["key"])
        open_url("https://0mn1.atlassian.net/browse/" + data["key"])

    else:
        messagebox.showwarning(title=None, message="Por favor ingrese todos los datos solicitados")


button_border = Frame(root, highlightbackground = "#f74615",
                         highlightthickness = 2, bd=0)
button_border.grid(padx = 10, pady =10, row=0, column=0)

myButton1 = Button(button_border, text="Cambio correo", command = cambioEmail, fg="white",bg='#252626', font = 'sans 12 bold')
myButton1.grid(row=0, column=0)

button_border2 = Frame(root, highlightbackground = "#f74615",
                         highlightthickness = 2, bd=0)
button_border2.grid(padx = 10, pady =10, row=0, column=1)
myButton2 = Button(button_border2, text="Cambio numero", command = cambioTelefono, fg="white",bg='#252626', font = 'sans 12 bold')
myButton2.grid(row=0, column=1)

button_border3 = Frame(root, highlightbackground = "#f74615",
                         highlightthickness = 2, bd=0)
button_border3.grid(padx = 10, pady =10, row=0, column=2)
myButton3 = Button(button_border3, text="Cambio nombre", command = cambioNombreSA, fg="white",bg='#252626', font = 'sans 12 bold')
myButton3.grid(row=0, column=2)

button_border4 = Frame(root, highlightbackground = "#f74615",
                         highlightthickness = 2, bd=0)
button_border4.grid(padx = 10, pady =10, row=0, column=3)
myButton4 = Button(button_border4, text="Reembolsos", command = reembolso, fg="white",bg='#252626', font = 'sans 12 bold')
myButton4.grid(row=0, column=3)


button_border5 = Frame(root, highlightbackground = "#f74615",
                         highlightthickness = 2, bd=0)
button_border5.grid(padx = 10, pady =10, row=0, column=4)
myButton5 = Button(button_border5, text="Cierre Cuentas", command = cierreCuenta, fg="white",bg='#252626', font = 'sans 12 bold')
myButton5.grid(row=0, column=4)

#Declaracion menus
#menubar = Menu(root)
#aws = Menu(menubar, tearoff=False)
#aws.add_command(label="Actualizar atributos")
#aws.add_command(label="Borrar usuario")

#superApp = Menu (menubar, tearoff=False)
#superApp.add_command(label="Actualizar correo", command=cambioEmail)
#superApp.add_command(label="Actualizar telefono", command = cambioTelefono)
#superApp.add_command(label="Reembolso", command = reembolso)
#superApp.add_command(label="Actualizar nombre", command = cambioNombreSA)
#superApp.add_command(label="Borrar Usuario")
#superApp.add_command(label="Borrar duplicado bikes")

#bikes = Menu (menubar, tearoff=False)
#bikes.add_command(label="Actualizar correo")
#bikes.add_command(label="Actualizar telefono")
#bikes.add_command(label="Reset contraseña")

#menubar.add_cascade(label="AWS CLI", menu=aws)
#menubar.add_cascade(label="SuperApp", menu=superApp)
#menubar.add_cascade(label="Bikes", menu=bikes)

#root.config(menu=menubar)
root.mainloop()
