from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import requests
import json
import webbrowser
root = Tk()
root.geometry("700x500")
root.option_add('*Font','19')
root.eval('tk::PlaceWindow . center')
root.title("Jr Jenkins")

canvas = Canvas(root, width = 700, height = 700)
canvas.grid(row=1,columnspan =8,padx=100)
img = PhotoImage(file="dribbble.png")
canvas.create_image(-9,-9,anchor=NW, image=img)


def open_url(url):
   webbrowser.open_new_tab(url)

def hide_button(widget):
    # This will remove the widget from toplevel
    widget.grid_forget()

def cambioEmail():
    email = Toplevel()
    email.geometry("800x225")
    # telefono.eval('tk::PlaceWindow . center')
    email.title("Cambio de email")
    email.option_add('*Font', '19')
    relleno = Label(email, text='')
    relleno.grid(row=0, column=0, padx=5, pady=5)
    labelSub = Label(email, text='Ingrese el correo actual del usuario')
    labelSub.grid(row=1, column=2, padx=5, pady=5)
    labelEmail = Label(email, text='Ingrese el nuevo correo del usuario')
    labelEmail.grid(row=2, column=2, padx=5, pady=5)
    sub = Entry(email, width=50)
    sub.grid(row=1, column=3, padx=5, pady=5)
    emailE = Entry(email, width=50)
    emailE.grid(row=2, column=3, padx=5, pady=5)

    var1 = IntVar()
    chkTaxi = Checkbutton(email, text="Usuario es taxista", variable=var1, onvalue=1, offvalue=0)
    chkTaxi.grid(row=3, column=3)
    var2 = IntVar()
    chkMoni = Checkbutton(email, text="Usuario tiene MONI", variable=var2, onvalue=1, offvalue=0)
    chkMoni.grid(row=4, column=3)

    myButton3 = Button(email, text="ENVIAR",
                       command=lambda: updateEmailSend(str(sub.get()), str(emailE.get()), str(var1.get()),
                                                            str(var2.get())), fg="white", bg='#3d8af7',width = 20)
    myButton3.grid(pady=5, padx=5, row=5, column=3)

def updateEmailSend(viejo,nuevo,taxi,moni):
    if (viejo != "" and nuevo != ""):
        url = "https://fabriziosalazar.atlassian.net//rest/api/2/issue"
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        payload = json.dumps(
            {
                "fields": {
                    "project":
                        {
                            "key": "PRUEB"
                        },
                    "summary": "Update Email",
                    "description": "{code} CALL spj_UpdateDataEmail('" + str(viejo) + "','" + str(
                        nuevo) + "'," + taxi + "," + moni + ");{code}",
                    "issuetype": {
                        "name": "Task"
                    },
                    "assignee": {
                        "accountId": "60f998fe52162b0068015bd2"
                    },

                }
            }
        )
        response = requests.post(url, headers=headers, data=payload,
                                 auth=("fabriziosg95@gmail.com", "6pmQHN1i83nE61HDuBmCA38E"))
        data = response.json()
        print(data["key"])
        open_url("https://fabriziosalazar.atlassian.net/browse/" + data["key"])
    else:
        messagebox.showwarning(title=None, message="Por favor ingrese todos los datos solicitados")


def cambioTelefono():
    telefono = Toplevel()
    telefono.geometry("800x225")
    #telefono.eval('tk::PlaceWindow . center')
    telefono.title("Cambio de telefono")
    telefono.option_add('*Font', '19')
    relleno = Label(telefono, text='')
    relleno.grid(row=0, column=0, padx=5, pady=5)
    labelSub = Label(telefono, text='Ingrese el telefono actual del usuario')
    labelSub.grid(row=1, column=2, padx=5, pady=5)
    labelEmail = Label(telefono, text='Ingrese el nuevo telefono del usuario')
    labelEmail.grid(row=2, column=2, padx=5, pady=5)
    sub = Entry(telefono, width=50)
    sub.grid(row=1, column=3, padx=5, pady=5)
    emailE = Entry(telefono, width=50)
    emailE.grid(row=2, column=3, padx=5, pady=5)

    var1 = IntVar()
    chkTaxi = Checkbutton(telefono, text="Usuario es taxista", variable=var1, onvalue=1, offvalue=0)
    chkTaxi.grid(row=3, column=3)
    var2 = IntVar()
    chkMoni = Checkbutton(telefono, text="Usuario tiene MONI", variable=var2, onvalue=1, offvalue=0)
    chkMoni.grid(row=4, column=3)

    myButton3 = Button(telefono, text="ENVIAR", command=lambda: updateTelefonoSend(str(sub.get()), str(emailE.get()), str(var1.get()),str(var2.get())), fg="white", bg='#3d8af7',width = 20)
    myButton3.grid(pady=5, padx=5, row=5, column=3)

def updateTelefonoSend(viejo,nuevo,taxi,moni):
    if(viejo != "" and nuevo != ""):
        url = "https://fabriziosalazar.atlassian.net//rest/api/2/issue"
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        payload = json.dumps(
            {
                "fields": {
                    "project":
                        {
                            "key": "PRUEB"
                        },
                    "summary": "Update Telefono SuperApp",
                    "description": "{code} CALL spj_UpdateDataPhone('" + str(viejo) + "','" + str(
                        nuevo) + "'," + taxi + "," + moni + ");{code}",
                    "issuetype": {
                        "name": "Task"
                    },
                    "assignee": {
                        "accountId": "60f998fe52162b0068015bd2"
                    },

                }
            }
        )
        response = requests.post(url, headers=headers, data=payload,
                                 auth=("fabriziosg95@gmail.com", "6pmQHN1i83nE61HDuBmCA38E"))
        data = response.json()
        print(data["key"])
        open_url("https://fabriziosalazar.atlassian.net/browse/" + data["key"])

    else:
        messagebox.showwarning(title=None, message="Por favor ingrese todos los datos solicitados")


def reembolso():
    reemb = Toplevel()
    reemb.geometry("800x225")
    # telefono.eval('tk::PlaceWindow . center')
    reemb.title("Reembolso de dinero")
    reemb.option_add('*Font', '19')
    relleno = Label(reemb, text='')
    relleno.grid(row=0, column=0, padx=5, pady=5)
    labelTel = Label(reemb, text='Ingrese el telefono del usuario')
    labelTel.grid(row=1, column=2, padx=5, pady=5)
    labelMonto = Label(reemb, text='Ingrese el monto del reembolso')
    labelMonto.grid(row=2, column=2, padx=5, pady=5)
    tel = Entry(reemb, width=50)
    tel.grid(row=1, column=3, padx=5, pady=5)
    monto = Entry(reemb, width=50)
    monto.grid(row=2, column=3, padx=5, pady=5)
    labelCombo = Label(reemb, text = 'Seleccione la categoría de la transacción')
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
                                    "Crédito_por devolución de dinero comercio"],
                        state = "readonly", width = 48)
    combo.grid(column=3, row=3, padx=5, pady=5)
    combo.current(0)

    myButton3 = Button(reemb, text="ENVIAR",
                       command=lambda: reembolsoSend(str(tel.get()), str(monto.get()), str(combo.get())), fg="white", bg='#3d8af7',width = 20)
    myButton3.grid(pady=15, padx=5, row=5, column=3)



def reembolsoSend(telefono, monto, fill):
    relleno = rellenoReembolso(fill)
    signo = ""
    if(relleno.__contains__("Débito")):
        signo = "-"
    if (telefono != "" and monto != ""):
        url = "https://fabriziosalazar.atlassian.net//rest/api/2/issue"
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        payload = json.dumps(
            {
                "fields": {
                    "project":
                        {
                            "key": "PRUEB"
                        },
                    "summary": "Reembolso",
                    "description": "{code} CALL spReversal_transaction('" + str(telefono) + "'," + signo + str(
                        monto) + ",0," + relleno + ");{code}",
                    "issuetype": {
                        "name": "Task"
                    },
                    "assignee": {
                        "accountId": "60f998fe52162b0068015bd2"
                    },

                }
            }
        )
        response = requests.post(url, headers=headers, data=payload,
                                 auth=("fabriziosg95@gmail.com", "6pmQHN1i83nE61HDuBmCA38E"))
        data = response.json()
        print(data["key"])
        open_url("https://fabriziosalazar.atlassian.net/browse/" + data["key"])
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
    elif(texto == "Crédito por devolución de dinero de comercio"):
        relleno = "1046,7,'Crédito_por_devolución_de_dinero_de_<comercio>'"


    return relleno

def cambioNombreSA():
    nombre = Toplevel()
    nombre.geometry("800x240")
    
    nombre.title("Cambio de nombre SA")
    nombre.option_add('*Font', '19')
    relleno = Label(nombre, text='')
    relleno.grid(row=0, column=0, padx=5, pady=5)
    labelTelefono = Label(nombre, text='Ingrese el telefono actual del usuario')
    labelTelefono.grid(row=1, column=2, padx=5, pady=5)
    labelNombre = Label(nombre, text='Ingrese el nombre indicado por el usuario')
    labelNombre.grid(row=2, column=2, padx=5, pady=5)
    labelApell1 = Label(nombre, text='Ingrese el primer apellido indicado por el usuario')
    labelApell1.grid(row=3, column=2, padx=5, pady=5)
    labelApell2 = Label(nombre, text='Ingrese el segundo apellido indicado por el usuario')
    labelApell2.grid(row=4, column=2, padx=5, pady=5)
    tel = Entry(nombre, width=40)
    tel.grid(row=1, column=3, padx=5, pady=5)
    name = Entry(nombre, width=40)
    name.grid(row=2, column=3, padx=5, pady=5)
    apell1 = Entry(nombre, width=40)
    apell1.grid(row=3, column=3, padx=5, pady=5)
    apell2 = Entry(nombre, width=40)
    apell2.grid(row=4, column=3, padx=5, pady=5)

    myButton3 = Button(nombre, text="ENVIAR" , command = lambda: cambioNombreSASend(tel.get(),name.get(),apell1.get(),apell2.get()),
                       fg="white",bg='#3d8af7', width=20)
    myButton3.grid(pady=15, padx=5, row=5, column=3)

def cambioNombreSASend(telefono,nombre,apell1,apell2):
    if (telefono != "" and nombre != "" and apell1 != "" and apell2 != ""):
        url = "https://fabriziosalazar.atlassian.net//rest/api/2/issue"
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        payload = json.dumps(
            {
                "fields": {
                    "project":
                        {
                            "key": "PRUEB"
                        },
                    "summary": "Cambio de nombre SA",
                    "description": "{code} CALL spj_UpdateNameUser(" + str(telefono) + ",'" + str(nombre) + "','" + str(
                        apell1) + "','" + str(apell2) + "'" + ''");{code}",
                    "issuetype": {
                        "name": "Task"
                    },
                    "assignee": {
                        "accountId": "60f998fe52162b0068015bd2"
                    },

                }
            }
        )
        response = requests.post(url, headers=headers, data=payload,
                                 auth=("fabriziosg95@gmail.com", "6pmQHN1i83nE61HDuBmCA38E"))
        data = response.json()
        print(data["key"])
        open_url("https://fabriziosalazar.atlassian.net/browse/" + data["key"])
    else:
        messagebox.showwarning(title=None, message="Por favor ingrese todos los datos solicitados")


myButton1 = Button(root, text="Cambio correo", command = cambioEmail, fg="white",bg='#3d8af7')
myButton1.grid(pady=10, padx=5, row=0, column=0)

myButton2 = Button(root, text="Cambio telefono", command = cambioTelefono, fg="white",bg='#3d8af7')
myButton2.grid(pady=10, padx=5, row=0, column=1)

myButton3 = Button(root, text="Cambio nombre", command = cambioNombreSA, fg="white",bg='#3d8af7')
myButton3.grid(pady=10, padx=5, row=0, column=2)

myButton4 = Button(root, text="Reembolsos", command = reembolso, fg="white",bg='#3d8af7')
myButton4.grid(pady=10, padx=5, row=0, column=3)

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
