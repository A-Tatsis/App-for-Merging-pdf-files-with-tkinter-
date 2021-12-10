import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.filedialog as fd
from PyPDF2 import PdfFileReader, PdfFileWriter
from tkinter import filedialog

root = tk.Tk()
root.title('Merge Pdf')
root.resizable(False, False)
window_width = 352
window_height = 285

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

root.configure(background="#2F4858")
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

def upload_file():
        filez = fd.askopenfilenames(parent=root, \
                                    title='Choose the files',filetypes=[(".pdf", ".pdf")])
        filez = root.tk.splitlist(filez)
        files = list(filez)
        fake_list = []
        for i in range(lb.size()):
            fake_list.append(lb.get(i))
        for f in files:
            if f not in fake_list:
                lb.insert(END, f)


def go():
    filez = lb.size()
    pdf_writer = PdfFileWriter()
    output=f"{save_label['text']}/merged.pdf"
    for i in range(filez):
        f = lb.get(i)
        pdf_reader = PdfFileReader(f)
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))
        
    with open(output, 'wb') as out:
        pdf_writer.write(out)


def path():
        path_save = filedialog.askdirectory()
        save_label['text'] = path_save

def abc():
        sel = lb.curselection()
        for index in sel[::-1]:
            lb.delete(index)


open_pic = PhotoImage(file='open.png')
epelexe_button = Button(root,image = open_pic, font = 'arial 12' ,fg='white',\
                         bg = '#2F4858',activebackground = '#2F4858',relief=FLAT, command=upload_file, borderwidth=0)
   
epelexe_button.place(x=15, y=10)

b_pic = PhotoImage(file='delete.png')
b = Button(root,image = b_pic, font = 'arial 12' ,fg='white',\
                      bg = '#2F4858',activebackground = '#2F4858',relief=FLAT, command=abc, borderwidth=0)
b.place(x=95, y=10)

lb = Listbox(root, width=53, height=6, selectmode=MULTIPLE)
lb.place(x=15, y=45)



choose_pic = PhotoImage(file='choose.png') 
path = Button(root, image = choose_pic, font = 'arial 12' ,fg='white',\
                         bg = '#2F4858',activebackground = '#2F4858', relief=FLAT, command=path, borderwidth=0)
path.place(x=15, y=157)


save_label = Label(root, font = 'arial 12 underline' , bg = '#2F4858',fg='#9BC300')
save_label.place(x=15, y=192)

merge_pic = PhotoImage(file='merge.png') 
succ = Button(root,image = merge_pic, font = 'arial 12' ,fg='white',\
                         bg = '#2F4858',activebackground = '#2F4858', relief=FLAT, command=go, borderwidth=0)
succ.place(x=15, y=225)


root.mainloop()
