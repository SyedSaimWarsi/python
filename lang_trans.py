from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES


root = Tk()
root.geometry('1180x320')
root.resizable(0,0)
root['bg'] = 'grey'
root.title('Language translator')
# these lines are for the window which will appear after running the code 

Label(root, text = ("Language Translator"), font = "Arial 20 italic bold").pack()
Label(root, text = ('Enter Text which you want to Translate: '), font = 'Arial 11 bold').place(x=100, y=80)
Input_text = Entry(root, width=80)
Input_text.place(x=10, y=110)
Input_text.get()
# these lines are for the input and headings of input box and box in which user will enter text

Label(root, text = ("Translated Text"), font = "Arial 11 bold").place(x=850,y=70)
Output_text = Text(root, font = "arial 10", height = 5)
Output_text.place(x=600,y=100)
# these lines are for the output box and the heading of the box where the output will be showed 

language = list(LANGUAGES.values())
dest_lang = ttk.Combobox(root, values=language,width=20)
dest_lang.place(x=170,y=140)
dest_lang.set("Choose Language")
# these lines are for the dropdown from where the user will select the language in which he wants to translate 
def Translate():
    translator = Translator()
    translated = translator.translate(text=Input_text.get(), dest=dest_lang.get())
    Output_text.delete(1.0, END)
    Output_text.insert(END, translated.text)
# this function used whenever the user will press the button this function will be called and translate the text in the selected language

trans_bttn = Button(root , text='Translate', font= 'arial 12 bold', command=Translate, bg='Red',activebackground="Green")
trans_bttn.place(x=500,y=140)
# these lines are for the button of translate and whenever it is press it calls the function translate()
root.mainloop()

