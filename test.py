viewStudent = Toplevel(root)
viewStudent.title("viewStudent")
viewStudent.geometry("400x300+400+200")
viewStudent.withdraw()

Linebtn = Button(viewStudent, text = "Line Graph",font = ('ariel', 14))
Barbtn = Button(viewStudent, text = "Bar Graph",font = ('ariel', 14))
savebtn = Button(viewStudent, text = "Save",font = ('ariel', 14))

def back():
    root.deiconify()
    viewStudent.withdraw()
backbtn = Button(viewStudent, text = "back" , command = back,font = ('ariel', 14))


Linebtn.pack(pady = 10)
Barbtn.pack(pady = 10)
savebtn.pack(pady = 10)
backbtn.pack(pady = 10)