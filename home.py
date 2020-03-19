from tkinter import Tk 
from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
details = []
class student():

    def __init__(self,rollno,name,marks):
        self.rollno = rollno
        self.name = name
        self.marks = marks

    def getDetails(self):
        return {'rollno':rollno,'name':name,'marks':marks}

    

    


########################################################################
########-------------------------Home Route-----------------------###########
root = Tk()
root.title("S.M.S")
root.geometry("500x500+400+200")

def addStud():
    addStudent.deiconify()
    root.withdraw()
def updateStud():
    updateStudent.deiconify()
    root.withdraw()
def deleteStud():
    deleteStudent.deiconify()
    root.withdraw()
def graphStud():
    graphs.deiconify()
    root.withdraw()
def viewStud():
    viewStudent.deiconify()
    root.withdraw()


addbtn = Button(root, text = "Add", font = ('ariel', 14), command = addStud)
viewbtn = Button(root, text = "View", font = ('ariel', 14), command = viewStud)
updatebtn = Button(root, text = "Update", font = ('ariel', 14), command = updateStud)
deletebtn = Button(root, text = "Delete", font = ('ariel', 14), command = deleteStud)
graphbtn = Button(root, text = "Graph", font = ('ariel', 14), command = graphStud)


temp = Label(root, text = "Temp")
text = "You could be good today, but instead you choose tomorrow"
quote = Label(root, text = text)

addbtn.grid(row = 1, column = 1, columnspan = 4, pady = 20)
viewbtn.grid(row = 2, column = 1, columnspan = 4, pady = 20)
updatebtn.grid(row = 3, column = 1, columnspan = 4, pady = 20)
deletebtn.grid(row = 4, column = 1, columnspan = 4, pady = 20)
graphbtn.grid(row = 5, column = 1, columnspan = 4, pady = 20)
temp.grid(row = 6, column = 0, columnspan = 1, pady = 10)
quote.grid(row = 7, column = 0, columnspan = 2)

######################################################################
########-------------------------ADD-----------------------###########
addStudent = Toplevel(root)
addStudent.title("Add")
addStudent.geometry("500x500+400+200")
# addStudent.withdraw()

enterno = Label(addStudent, text = "Enter Rollno. :",font = ('ariel', 14))
enter_no = Entry(addStudent,bd = 5,font = ('ariel', 14))

enterName = Label(addStudent, text = "Enter Name: ",font = ('ariel', 14))
enter_name = Text(addStudent, width = 20, height = 1, bd = 5,font = ('ariel', 14))

enterMks = Label(addStudent, text = "Enter Marks: ",font = ('ariel', 14))
enter_mks = Entry(addStudent, bd = 5,font = ('ariel', 14))

def addDetails(no):
    
    roll_no = enter_no.get()
    print("Rollno =",no)
    # name = enter_name.get()
    marks = enter_mks.get()
    print("Marks =",marks)
    stdt = student(roll_no,"",marks)
    print(stdt.marks)
    details.append(stdt)

    

savebtn = Button(addStudent, text = "Save",font = ('ariel', 14),command = lambda: addDetails(enter_no.get()))

def back():
    root.deiconify()
    addStudent.withdraw()
backbtn = Button(addStudent, text = "back" , command = back,font = ('ariel', 14))


enterno.pack(pady = 10)
enter_no.pack(pady = 10)
enterName.pack(pady = 10)
enter_name.pack(pady = 10)
enterMks.pack(pady = 10)
enter_mks.pack(pady = 10)

savebtn.pack(pady = 10)
backbtn.pack(pady = 10)


#########################################################################
########-------------------------Update-----------------------###########
updateStudent = Toplevel(root)
updateStudent.title("Update")
updateStudent.geometry("500x500+400+200")
updateStudent.withdraw()

enterno = Label(updateStudent, text = "Enter Rollno. :",font = ('ariel', 14))
enter_no = Entry(updateStudent,bd = 5,font = ('ariel', 14))

enterName = Label(updateStudent, text = "Enter Name: ",font = ('ariel', 14))
enter_name = Text(updateStudent, width = 20, height = 1, bd = 5,font = ('ariel', 14))

enterMks = Label(updateStudent, text = "Enter Marks: ",font = ('ariel', 14))
enter_mks = Entry(updateStudent, bd = 5,font = ('ariel', 14))

savebtn = Button(updateStudent, text = "Save",font = ('ariel', 14))

def back():
    root.deiconify()
    updateStudent.withdraw()
backbtn = Button(updateStudent, text = "back" , command = back,font = ('ariel', 14))



enterno.pack(pady = 10)
enter_no.pack(pady = 10)
enterName.pack(pady = 10)
enter_name.pack(pady = 10)
enterMks.pack(pady = 10)
enter_mks.pack(pady = 10)
savebtn.pack(pady = 10)
backbtn.pack(pady = 10)

#########################################################################
########-------------------------Delete-----------------------###########
deleteStudent = Toplevel(root)
deleteStudent.title("Delete")
deleteStudent.geometry("400x300+400+200")
deleteStudent.withdraw()

enterno = Label(deleteStudent, text = "Enter Rollno. :",font = ('ariel', 14))
enter_no = Entry(deleteStudent,bd = 5,font = ('ariel', 10))

savebtn = Button(deleteStudent, text = "Save",font = ('ariel', 14))

def back():
    root.deiconify()
    deleteStudent.withdraw()
backbtn = Button(deleteStudent, text = "back" , command = back,font = ('ariel', 14))

enterno.pack(pady = 10)
enter_no.pack(pady = 10)
savebtn.pack(pady = 10)
backbtn.pack(pady = 10)

############################################################################
########-------------------------Graphs-----------------------###########
graphs = Toplevel(root)
graphs.title("Graphs")
graphs.geometry("400x300+400+200")
graphs.withdraw()

Linebtn = Button(graphs, text = "Line Graph",font = ('ariel', 14))
Barbtn = Button(graphs, text = "Bar Graph",font = ('ariel', 14))
savebtn = Button(graphs, text = "Save",font = ('ariel', 14))

def back():
    root.deiconify()
    graphs.withdraw()
backbtn = Button(graphs, text = "back" , command = back,font = ('ariel', 14))


Linebtn.pack(pady = 10)
Barbtn.pack(pady = 10)
savebtn.pack(pady = 10)
backbtn.pack(pady = 10)

############################################################################
########-------------------------View-----------------------###########

viewStudent = Toplevel(root)
viewStudent.title("View")
viewStudent.geometry("500x500+400+200")
viewStudent.withdraw()

view =  scrolledtext.ScrolledText(viewStudent, width = 30, height = 5)
def back():
    root.deiconify()
    viewStudent.withdraw()
backbtn = Button(viewStudent, text = "back" , command = back,font = ('ariel', 14))


view.pack(pady = 10)
backbtn.pack(pady = 10)

root.mainloop()
