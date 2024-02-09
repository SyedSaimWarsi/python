from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

root = Tk()
root.geometry('1180x320')
root.resizable(0,0)
root['bg'] = 'grey'
root.title('Language translator')

Label(root, text = ("Language Translator"), font = "Arial 20 italic bold").pack()
Label(root, text = ('Enter Text which you want to Translate: '), font = 'Arial 11 bold').place(x=100, y=80)
Input_text = Entry(root, width=80)
Input_text.place(x=10, y=110)
Input_text.get()

Label(root, text = ("Translated Text"), font = "Arial 11 bold").place(x=850,y=70)
Output_text = Text(root, font = "arial 10", height = 5)
Output_text.place(x=600,y=100)
language = list(LANGUAGES.values())

dest_lang = ttk.Combobox(root, values=language,width=20)
dest_lang.place(x=170,y=140)
dest_lang.set("Choose Language")

def Translate():
    translator = Translator()
    translated = translator.translate(text=Input_text.get(), dest=dest_lang.get())
    Output_text.delete(1.0, END)
    Output_text.insert(END, translated.text)

trans_bttn = Button(root , text='Translate', font= 'arial 12 bold', command=Translate, bg='Red',activebackground="Green")
trans_bttn.place(x=500,y=140)
root.mainloop()

