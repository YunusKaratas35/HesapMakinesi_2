import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("Hesap Makinesi - Yunus Karatas")
        #setting window size
        width=558
        height=648
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        # Arka plan rengini koyu gri yapma
        root.config(bg='#2b2b2b')

        GLabel_905=tk.Label(root, bg='#2b2b2b')
        ft = tkFont.Font(family='Times',size=10)
        GLabel_905["font"] = ft
        GLabel_905["fg"] = "#ffffff"
        GLabel_905["justify"] = "center"
        GLabel_905["text"] = "Rakam1"
        GLabel_905.place(x=85,y=200,width=70,height=25)

        GLabel_70=tk.Label(root, bg='#2b2b2b')
        ft = tkFont.Font(family='Times',size=10)
        GLabel_70["font"] = ft
        GLabel_70["fg"] = "#ffffff"
        GLabel_70["justify"] = "center"
        GLabel_70["text"] = "Rakam2"
        GLabel_70.place(x=205,y=200,width=70,height=25)

        GLabel_817=tk.Label(root, bg='#2b2b2b')
        ft = tkFont.Font(family='Times',size=10)
        GLabel_817["font"] = ft
        GLabel_817["fg"] = "#ffffff"
        GLabel_817["justify"] = "center"
        GLabel_817["text"] = "Sonuc"
        GLabel_817.place(x=380,y=200,width=70,height=25)

        self.GLineEdit_294=tk.Entry(root)
        self.GLineEdit_294["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_294["font"] = ft
        self.GLineEdit_294["fg"] = "#333333"
        self.GLineEdit_294["justify"] = "center"
        self.GLineEdit_294.place(x=85,y=290,width=70,height=25)

        self.GLineEdit_213=tk.Entry(root)
        self.GLineEdit_213["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_213["font"] = ft
        self.GLineEdit_213["fg"] = "#333333"
        self.GLineEdit_213["justify"] = "center"
        self.GLineEdit_213.place(x=205,y=290,width=70,height=25)

        self.GLineEdit_394=tk.Entry(root, state="readonly") # değer girilemez hale getirdim.
        self.GLineEdit_394["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_394["font"] = ft
        self.GLineEdit_394["fg"] = "#333333"
        self.GLineEdit_394["justify"] = "center"
        self.GLineEdit_394.place(x=345,y=290,width=140,height=25)

        GButton_954=tk.Button(root)
        GButton_954["bg"] = "#2b2a33"
        ft = tkFont.Font(family='Times',size=10)
        GButton_954["font"] = ft
        GButton_954["fg"] = "#fbfbfe"
        GButton_954["justify"] = "center"
        GButton_954["text"] = "+"
        GButton_954.place(x=50,y=420,width=70,height=25)
        GButton_954["command"] = self.GButton_954_command

        GButton_102=tk.Button(root)
        GButton_102["bg"] = "#2b2a33"
        ft = tkFont.Font(family='Times',size=10)
        GButton_102["font"] = ft
        GButton_102["fg"] = "#fbfbfe"
        GButton_102["justify"] = "center"
        GButton_102["text"] = "-"
        GButton_102.place(x=180,y=420,width=70,height=25)
        GButton_102["command"] = self.GButton_102_command

        GButton_491=tk.Button(root)
        GButton_491["bg"] = "#2b2a33"
        ft = tkFont.Font(family='Times',size=10)
        GButton_491["font"] = ft
        GButton_491["fg"] = "#fbfbfe"
        GButton_491["justify"] = "center"
        GButton_491["text"] = "*"
        GButton_491.place(x=310,y=420,width=70,height=25)
        GButton_491["command"] = self.GButton_491_command

        GButton_69=tk.Button(root)
        GButton_69["bg"] = "#2b2a33"
        ft = tkFont.Font(family='Times',size=10)
        GButton_69["font"] = ft
        GButton_69["fg"] = "#fbfbfe"
        GButton_69["justify"] = "center"
        GButton_69["text"] = "/"
        GButton_69.place(x=440,y=420,width=70,height=25)
        GButton_69["command"] = self.GButton_69_command

    def validate_inputs(self):
        try:
            num1 = float(self.GLineEdit_294.get())
            num2 = float(self.GLineEdit_213.get())
            return num1, num2
        except ValueError:
            self.GLineEdit_394.config(state="normal")
            self.GLineEdit_394.delete(0, tk.END)
            self.GLineEdit_394.insert(0, "Hata!")
            self.GLineEdit_394.config(state="readonly")
            return None, None

    def GButton_954_command(self):
        num1, num2 = self.validate_inputs()
        if num1 is not None and num2 is not None:
            result = num1 + num2
            self.GLineEdit_394.config(state="normal")
            self.GLineEdit_394.delete(0, tk.END)
            self.GLineEdit_394.insert(0, str(result))
            self.GLineEdit_394.config(state="readonly")

    def GButton_102_command(self):
        num1, num2 = self.validate_inputs()
        if num1 is not None and num2 is not None:
            result = num1 - num2
            self.GLineEdit_394.config(state="normal")
            self.GLineEdit_394.delete(0, tk.END)
            self.GLineEdit_394.insert(0, str(result))
            self.GLineEdit_394.config(state="readonly")

    def GButton_491_command(self):
        num1, num2 = self.validate_inputs()
        if num1 is not None and num2 is not None:
            result = num1 * num2
            self.GLineEdit_394.config(state="normal")
            self.GLineEdit_394.delete(0, tk.END)
            self.GLineEdit_394.insert(0, str(result))
            self.GLineEdit_394.config(state="readonly")

    def GButton_69_command(self):
        num1, num2 = self.validate_inputs()
        if num1 is not None and num2 is not None:
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Olmaz aga"
            self.GLineEdit_394.config(state="normal")
            self.GLineEdit_394.delete(0, tk.END)
            self.GLineEdit_394.insert(0, str(result))
            self.GLineEdit_394.config(state="readonly")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    textBoxYazilanlar1 = tk.StringVar() #Değişken tanımlama
    textBoxYazilanlar2 = tk.StringVar() #Değişken tanımlama
    textBoxYazilanlar3 = tk.StringVar() #Değişken tanımlama
    root.mainloop()

# "bg" arka plan rengi iken "fg" ön plan rengi genelde metin rengi.