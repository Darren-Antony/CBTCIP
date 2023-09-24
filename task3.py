# import necessary modules like tkinter and reportlab
import tkinter as tk
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet

itemList = [["DATE", "ITEM", "PRICE"]]

total = 0
discount = 0
lbl6 = None


# function to generate pdf
def generatePdf():
    gt = total - discount
    item = ["total", "", total]
    dis = ["discount", "", discount]
    grandTotal = ["grand-total", "", gt]
    itemList.append(item)
    itemList.append(dis)
    itemList.append(grandTotal)
    pdf = SimpleDocTemplate("rec.pdf", pagesize=A4)

    styles = getSampleStyleSheet()
    title_style = styles["Heading1"]
    title_style.alignment = 1
    title = Paragraph("receipt", title_style)
    style = TableStyle(
        [
            ("BOX", (0, 0), (-1, -1), 1, colors.black),
            ("GRID", (0, 0), (4, 4), 1, colors.black),
            ("BACKGROUND", (0, 0), (3, 0), colors.gray),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("BACKGROUND", (0, 1), (-1, -1), colors.lavenderblush),
        ]
    )

    table = Table(itemList, style=style)

    pdf.build([title, table])


# function to add items to the itemlist
def setValue(e1, e2, e3):
    global total
    name = e1.get()
    date = e2.get()
    amount = e3.get()
    total += int(amount)
    item = [name, date, amount]
    itemList.append(item)


# function to validate discount code
def discountFun(d):
    global discount, lbl6
    d = d.get()
    discountCode = ['12', '567', '890']
    if d in discountCode and total > 1000:
        discount = 500
        lbl6.config(text="You Have Got a Discount of 500!!")
    else:
        lbl6.config(text="You Have No discount")


# function to get values for the payment receipt
def Entry():
    global lbl6  # Define lbl6 as a global variable
    limit = int(ent1.get())
    for _ in range(limit):
        lbl2 = tk.Label(root, text="Enter the date", font=("Helvetica", 16), fg="gray")
        ent2 = tk.Entry(root, width=40, font=("Helvetica", 16))
        lbl3 = tk.Label(root, text="Enter the item", font=("Helvetica", 16), fg="gray")
        ent3 = tk.Entry(root, width=40, font=("Helvetica", 16))
        lbl4 = tk.Label(root, text="Enter the amount", font=("Helvetica", 16), fg="gray")
        ent4 = tk.Entry(root, width=40, font=("Helvetica", 16))
        btn2 = tk.Button(root, text='enter',
                         command=lambda entry2=ent2, entry3=ent3, entry4=ent4: setValue(entry2, entry3, entry4),
                         width=5,
                         font=("Helvetica", 16), bg="linen")
        lbl2.pack()
        ent2.pack()
        lbl3.pack()
        ent3.pack()
        lbl4.pack()
        ent4.pack()
        btn2.pack()
    lbl5 = tk.Label(root, text="enter the discount code", font=("Helvetica", 16), fg="gray")
    ent5 = tk.Entry(root, width=30)
    btn3 = tk.Button(root, text="enter", command=lambda dcode=ent5: discountFun(dcode), width=5, font=("Helvetica", 16),
                     bg="linen")
    lbl5.pack()
    ent5.pack()
    btn3.pack()
    btn3 = tk.Button(root, text="generate pdf", command=generatePdf, font=("Helvetica", 16), bg="green")
    lbl6 = tk.Label(root, text="", font=("Helvetica", 16), fg="gold")
    lbl6.pack()
    btn3.pack()


root = tk.Tk()
root.geometry('700x450')
lbl0 = tk.Label(root, text="RECEIPT GENERATOR", font=("Helvetica", 40), fg="gold")
lbl1 = tk.Label(root, text="NO OF ENTRIES", font=("Helvetica", 16), fg="gray")
ent1 = tk.Entry(root, width=30, font=("Helvetica", 16))
btn1 = tk.Button(root, text='enter', command=Entry, width=5, font=("Helvetica", 16), bg="blue2")
lbl0.pack()
lbl1.pack()
ent1.pack()
btn1.pack()
root.mainloop()
