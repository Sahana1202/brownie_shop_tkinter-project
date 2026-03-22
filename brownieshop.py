import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from reportlab.pdfgen import canvas

users=[]
cart=[]
items=[]

# ---------------- REGISTER FUNCTION ----------------
def register():
    name=name_entry.get()
    email=email_entry.get()
    phone=phone_entry.get()
    password=pass_entry.get()

    if name=="" or email=="" or phone=="" or password=="":
        messagebox.showwarning("Warning","Fill all fields")
        return

    users.append([name,email,phone,password])
    messagebox.showinfo("Success","Registered Successfully 🍫")

# ---------------- LOGIN FUNCTION ----------------
def login():
    email=login_email.get()
    password=login_pass.get()

    for u in users:
        if u[1]==email and u[3]==password:
            messagebox.showinfo("Login","Welcome to Brownie Shop 🍫")
            show_frame(menu_page)
            return

    messagebox.showerror("Error","Invalid Login")

# ---------------- ADD TO CART ----------------
def add_to_cart(item,price):
    cart.append(price)
    items.append(item)
    messagebox.showinfo("Cart",item+" added to cart")

# ---------------- GENERATE BILL ----------------
def generate_bill():

    total=sum(cart)

    bill_text.delete("1.0","end")

    bill_text.insert("end","------ Brownie Shop Bill ------\n\n")

    for i in items:
        bill_text.insert("end",i+"\n")

    bill_text.insert("end","\nTotal Amount : Rs."+str(total))

# ---------------- DOWNLOAD PDF ----------------
def download_pdf():

    total=sum(cart)

    pdf=canvas.Canvas("Brownie_Bill.pdf")

    pdf.drawString(200,800,"Brownie Shop Bill")

    y=760

    for i in items:
        pdf.drawString(100,y,i)
        y-=20

    pdf.drawString(100,y-20,"Total Amount : Rs."+str(total))

    pdf.save()

    messagebox.showinfo("Saved","PDF Bill Downloaded")

# ---------------- PAGE SWITCH ----------------
def show_frame(frame):
    frame.tkraise()

# ---------------- MAIN WINDOW ----------------
root=tk.Tk()
root.title("Brownie Shop 🍫")
root.geometry("1000x650")
root.configure(bg="#3e2723")

container=tk.Frame(root)
container.pack(fill="both",expand=True)

register_page=tk.Frame(container,bg="#4e342e")
login_page=tk.Frame(container,bg="#4e342e")
menu_page=tk.Frame(container,bg="#5d4037")
bill_page=tk.Frame(container,bg="#5d4037")

for frame in (register_page,login_page,menu_page,bill_page):
    frame.place(relwidth=1,relheight=1)

# ---------------- REGISTER PAGE ----------------
tk.Label(register_page,text="Brownie Shop Register",
font=("Arial",28,"bold"),
bg="#4e342e",
fg="white").pack(pady=30)

tk.Label(register_page,text="Name",bg="#4e342e",fg="white").pack()
name_entry=tk.Entry(register_page,width=30,font=14)
name_entry.pack(pady=8)

tk.Label(register_page,text="Email",bg="#4e342e",fg="white").pack()
email_entry=tk.Entry(register_page,width=30,font=14)
email_entry.pack(pady=8)

tk.Label(register_page,text="Phone",bg="#4e342e",fg="white").pack()
phone_entry=tk.Entry(register_page,width=30,font=14)
phone_entry.pack(pady=8)

tk.Label(register_page,text="Password",bg="#4e342e",fg="white").pack()
pass_entry=tk.Entry(register_page,width=30,font=14,show="*")
pass_entry.pack(pady=8)

tk.Button(register_page,text="Register",
font=14,
bg="#3e2723",
fg="white",
command=register).pack(pady=15)

tk.Button(register_page,
text="Go to Login",
command=lambda:show_frame(login_page)).pack()

# ---------------- LOGIN PAGE ----------------
tk.Label(login_page,text="Brownie Shop Login",
font=("Arial",28,"bold"),
bg="#4e342e",
fg="white").pack(pady=30)

tk.Label(login_page,text="Email",bg="#4e342e",fg="white").pack()
login_email=tk.Entry(login_page,width=30,font=14)
login_email.pack(pady=8)

tk.Label(login_page,text="Password",bg="#4e342e",fg="white").pack()
login_pass=tk.Entry(login_page,width=30,font=14,show="*")
login_pass.pack(pady=8)

tk.Button(login_page,
text="Login",
bg="#3e2723",
fg="white",
command=login).pack(pady=15)

tk.Button(login_page,
text="Back to Register",
command=lambda:show_frame(register_page)).pack()

# ---------------- MENU PAGE ----------------
tk.Label(menu_page,text="Brownie Menu 🍫",
font=("Arial",30,"bold"),
bg="#5d4037",
fg="white").pack(pady=20)

menu_frame=tk.Frame(menu_page,bg="#5d4037")
menu_frame.pack()

# Bento Cake
img1=Image.open(r"C:\Users\SAHANA\Downloads\bento.jpeg").resize((150,120))
photo1=ImageTk.PhotoImage(img1)

tk.Label(menu_frame,image=photo1,bg="#5d4037").grid(row=0,column=0,padx=20)
tk.Button(menu_frame,text="Bento Cake\nRs150",
command=lambda:add_to_cart("Bento Cake",150),
width=18).grid(row=1,column=0)

# 250g Brownie
img2=Image.open(r"C:\Users\SAHANA\Downloads\brownie250.jpeg").resize((150,120))
photo2=ImageTk.PhotoImage(img2)

tk.Label(menu_frame,image=photo2,bg="#5d4037").grid(row=0,column=1,padx=20)
tk.Button(menu_frame,text="250gm Brownie\nRs300",
command=lambda:add_to_cart("250gm Brownie",300),
width=18).grid(row=1,column=1)

# Half kg Brownie
img3=Image.open(r"C:\Users\SAHANA\Downloads\halfkg.jpeg").resize((150,120))
photo3=ImageTk.PhotoImage(img3)

tk.Label(menu_frame,image=photo3,bg="#5d4037").grid(row=0,column=2,padx=20)
tk.Button(menu_frame,text="Half Kg Brownie\nRs480",
command=lambda:add_to_cart("Half Kg Brownie",480),
width=18).grid(row=1,column=2)

# 1kg Brownie  (FIXED EXTENSION)
img4=Image.open(r"C:\Users\SAHANA\Downloads\onekg.jpeg").resize((150,120))
photo4=ImageTk.PhotoImage(img4)

tk.Label(menu_frame,image=photo4,bg="#5d4037").grid(row=0,column=3,padx=20)
tk.Button(menu_frame,text="1Kg Brownie\nRs800",
command=lambda:add_to_cart("1Kg Brownie",800),
width=18).grid(row=1,column=3)

tk.Button(menu_page,
text="Generate Bill",
bg="#3e2723",
fg="white",
command=lambda:show_frame(bill_page)).pack(pady=30)

# ---------------- BILL PAGE ----------------
tk.Label(bill_page,text="Order Bill",
font=("Arial",30,"bold"),
bg="#5d4037",
fg="white").pack(pady=20)

bill_text=tk.Text(bill_page,width=40,height=12,font=14)
bill_text.pack()

tk.Button(bill_page,text="Show Bill",command=generate_bill).pack(pady=10)

tk.Button(bill_page,text="Download PDF Bill",command=download_pdf).pack(pady=10)

tk.Button(bill_page,
text="Back to Menu",
command=lambda:show_frame(menu_page)).pack()

show_frame(register_page)

root.mainloop()