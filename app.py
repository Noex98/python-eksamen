from tkinter import *
from materialer import *
import tkinter.messagebox
from brugere import Thomas as User

class Application(Frame):

    def udlaan(self):
        idnr = self.id_entry.get()

        # Casting af brugerinput i et try/except for at sikre at en int bliver brugt
        try:
            idnr = int(idnr)

            # Gennemsøg vores data
            for materiale in listMaterialer:
                # Vi sandt har vi fundet hvad vi ledte efter
                if idnr == materiale.idnr:
                    # Har vi nogen af disse bøger ledige
                    if materiale.antal - materiale.antaludlaan >= 1:
                        # Tjek om brugeren allerede har lånt dette materiale
                        for lån in User['alle_lån']:
                            if lån['idnr'] == idnr:
                                tkinter.messagebox.showinfo('Udlån', f'Du har allerede lånt: "{materiale.titel}"\nAflever først, for at kunne genlåne')
                                break

                        # Brugeren må godt låne materialet
                        else:
                            materiale.antaludlaan += 1
                            
                            # Registrer at brugeren nu har lånt
                            User['alle_lån'].append({
                                'idnr': materiale.idnr,
                                'dage_lånt': 0
                            })

                            self.vis_hele_listen()

                            tkinter.messagebox.showinfo('Udlån', f'{materiale.titel}, er nu udlånt. \n\n Senest aflevering om {materiale.låneperiode} dage')
                        break

                    else:
                        tkinter.messagebox.showerror('Fejl', f'{materiale.titel}, er ikke på lager i øjeblikket')
                        break
            
            # Hvis ikke indtastede id var i listen
            else:
                tkinter.messagebox.showinfo('Udlån', f'Materialet med id "{idnr}" står ikke i vores system')

        except:
            tkinter.messagebox.showerror('Fejl', 'Skriv venligst et tal')
        

    def aflever(self):
        idnr = self.aflever_entry.get()

        # Casting af brugerinput i et try/except for at sikre at en int bliver brugt
        try:
            idnr = int(idnr)

            # Gennemsøg vores liste af materialer
            for materiale in listMaterialer:
                if idnr == materiale.idnr:
                    materiale.antaludlaan -= 1

                    # Gennemsøg brugerens lån, og slet det afleverede materiale
                    for lån in User['alle_lån']:
                        if lån['idnr'] == idnr:
                            User['alle_lån'].remove(lån)

                    self.vis_hele_listen()
                    tkinter.messagebox.showinfo('Aflevering', f'{materiale.titel} er nu afleveret')
                    break

            # Hvis ikke indtastede id var i listen
            else:
                tkinter.messagebox.showinfo('Udlån', f'Materialet med id "{idnr}" står ikke i vores system')

        except:
            tkinter.messagebox.showerror('Fejl', 'Skriv venligst et tal')

    def sog_i_listen(self):
        search_text = self.entry.get().lower()
        self.listGui.delete('1.0', END)
        for materiale in listMaterialer:
            if search_text in materiale.titel.lower():
                self.listGui.insert(INSERT, materiale.toString()+"\n")
    

    def vis_hele_listen(self):
        self.listGui.delete('1.0', END)
        for materiale in listMaterialer:
            self.listGui.insert(INSERT, materiale.toString()+"\n")
        self.entry.delete(0, END)

    def vis_profil(self):
        self.listGui.delete('1.0', END)
        self.listGui.insert(INSERT, f'  {User["navn"]}\n\nDine lån: \n\n')

        # Gennemgå alle brugerens lån, og inset elementer i UI

        if len(User['alle_lån']) > 0:
            for lån in User['alle_lån']:
                # Find materialet i listen
                for materiale in listMaterialer:
                    if lån['idnr'] == materiale.idnr:
                        fundet_materiale = materiale
                        self.listGui.insert(INSERT, f"{fundet_materiale.titel}\n    aflevering om: {fundet_materiale.låneperiode - lån['dage_lånt']} dage\n    id: {fundet_materiale.idnr}\n\n")
                        break

                # Det lånte materiale findes ikke i bibliotekets data
                else:
                    tkinter.messagebox.showerror('Fejl', f'Materialet med ID: {lån["idnr"]}, er udgået fra bibliotekets database\n\nHenvend dig i receptionen')
        else:
            self.listGui.insert(INSERT, '   Ingen nuværende lån.')


            

    def create_widgets(self):
        frame = Frame(self)
        self.winfo_toplevel().title("Biblioteks databasen")

        # definition af quit knap
        self.QUIT = Button(frame, text="QUIT")
        self.QUIT["fg"] = "red"
        self.QUIT["command"] = self.quit
        self.QUIT.pack({"side": "left"})

        # definition og mapping af vis hele listen knappen
        self.visListe = Button(frame,text="Vis hele listen")
        self.visListe["command"] = self.vis_hele_listen
        self.visListe.pack({"side": "left"})
        

        # definition af input søge feltet.
        self.L1 = Label(frame, text="Søge Streng")
        self.L1.pack(side=LEFT)
        self.entry = Entry(frame, bd=5)
        self.entry.pack(side=LEFT)

        # definition og mapping af søgeknappen.
        self.sogKnap = Button(frame, text="Søg i listen")
        self.sogKnap["command"] = self.sog_i_listen
        self.sogKnap.pack({"side": "left"})

        # definition af ID input feltet til udlån
        self.L1 = Label(frame, text="ID for udlån")
        self.L1.pack(side=LEFT)
        self.id_entry = Entry(frame, bd=5)
        self.id_entry.pack(side=LEFT)

        # definition af udlåns knappen og mapping til
        # en funktion.
        self.udlaanKnap = Button(frame, text="Udlån")
        self.udlaanKnap["command"] = self.udlaan
        self.udlaanKnap.pack({"side": "left"})

        # input felt til aflevering.
        self.L1 = Label(frame, text="ID for aflevering:")
        self.L1.pack(side=LEFT)
        self.aflever_entry = Entry(frame, bd=5)
        self.aflever_entry.pack(side=LEFT)

        # definition og mapping af afleveringsknap
        self.afleverKnap = Button(frame, text="Aflever")
        self.afleverKnap["command"] = self.aflever
        self.afleverKnap.pack({"side": "left"})

        # defination og mapping a profilknap
        self.profil = Button(frame, text="Min profil")
        self.profil['comman'] = self.vis_profil
        self.profil.pack({"side": "left"})

        # definatino af text widget
        self.listGui = Text(self, width=140, height=35, font='Times')
        for materiale in listMaterialer:
            self.listGui.insert(INSERT, materiale.toString()+"\n")

        frame.pack()
        self.listGui.pack()

    # Denne constructor køres når programmet starter
    # og sørger for at alle vores widgets bliver lavet.
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.create_widgets()



root = Tk()
app = Application(master=root)
app.mainloop()