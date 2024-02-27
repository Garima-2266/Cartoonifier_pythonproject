import tkinter as tk
from tkinter import filedialog
from tkinter import *
from cartoonizer import make_cartoon
from PIL import ImageTk, Image
import cv2

top=tk.Tk()
top.geometry('1000x500')
top.title('Cartoonifier')
top.iconbitmap('.\\Pictures\\images.jpg')
top.configure(background='black')

def save_cartoon(file_path,cartoon_img):
    where=filedialog.asksaveasfilename(filetypes=(('JPEG Files','*.jpg'),('PNG Files','*.png'),('All Files','*.*')),defaultextension=file_path)
    cartoon_img.save(where)

def show_save_button(file_path,cartoon_img):
    save_b=Button(top,text='Save to laptop',command=lambda: save_cartoon(file_path,cartoon_img),padx=15,pady=10)
    save_b.place(relx=0.69,rely=0.89)

def convert(file_path):
    cartoon=make_cartoon(file_path)
    cartoon=cv2.cvtColor(cartoon,cv2.COLOR_BGR2RGB)
    cartoon_img=Image.fromarray(cartoon)
    cartoon_img.thumbnail(((top.winfo_width()/1.8),(top.winfo_height()/1.8)))
    im=ImageTk.PhotoImage(cartoon_img)
    label=Label(top,image=im)
    label.image=im
    label.pack(side="right",expand='yes')
    show_save_button(file_path,cartoon_img)

def show_convert_button(file_path):
    convert_b=Button(top,text="Cartoonify me",command=lambda: convert(file_path),padx=15,pady=10)
    convert_b.place(relx=0.79,rely=0.46)

def upload_image():
    file_path=filedialog.askopenfilename()
    uploaded=Image.open(file_path)
    uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_height()/2.25)))
    im=ImageTk.PhotoImage(uploaded)
    label=Label(top,image=im)
    label.image=im
    label.pack(side="left",expand='yes')
    show_convert_button(file_path)

upload=Button(top,text="Upload an image",command=upload_image,padx=15,pady=10)
upload.configure(background='#adadee',foreground='white',font=('arial',10,'bold'))
upload.place(relx=0.44,rely=0.86)

top.mainloop()



