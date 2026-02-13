from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
from course import CourseClass
from student import StudentClass
from result import ResultClass
from report import reportClass

class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1250x700+0+0")
        self.root.config(bg="white")

        # icons
        self.logo_dash = ImageTk.PhotoImage(file="images/logo_p.png")

        # title
        title = Label(self.root, text="Student Result Management System", padx=10, compound=LEFT, image=self.logo_dash, font=("goudy old style", 20, "bold"), bg="#033054", fg="white").place(x=0, y=0, relwidth=1, height=50)

        # menu
        M_Frame = LabelFrame(self.root, text="Menus", font=("times new roman", 15), bg="white")
        M_Frame.place(x=10, y=70, width=1340, height=60)

        btn_course = Button(M_Frame, text="Course", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.add_course).place(x=30, y=5, width=200, height=26)
        btn_student = Button(M_Frame, text="Student", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.add_student).place(x=260, y=5, width=200, height=26)
        btn_result = Button(M_Frame, text="Result", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.add_result).place(x=490, y=5, width=200, height=26)
        btn_view = Button(M_Frame, text="View Student Result", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.add_report).place(x=720, y=5, width=200, height=26)
        #btn_logout = Button(M_Frame, text="Logout", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2").place(x=900, y=5, width=200, height=26)
        btn_exit = Button(M_Frame, text="Exit", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.exit_app).place(x=960, y=5, width=200, height=26)

        # footer
        footer = Label(self.root, text="SRMS - Student Result Management System\nAll Rights Reserved - Shubhahsree Langade", font=("goudy old style", 12, "bold"), bg="#262626", fg="white").pack(side=BOTTOM, fill=X)

        # content window
        self.bg_img = Image.open("images/bg.png")
        self.bg_img = self.bg_img.resize((920, 350), Image.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        self.lbl_img = Label(self.root, image=self.bg_img).place(x=180, y=180, width=920, height=350)

        # update details
        self.lbl_course = Label(self.root, text="Total Courses\n[ 0 ]", font=("goudy old style", 20), bd=10, relief=RIDGE, bg="#e43b06", fg="white")
        self.lbl_course.place(x=160, y=530, width=300, height=100)

        self.lbl_student = Label(self.root, text="Total Students\n[ 0 ]", font=("goudy old style", 20), bd=10, relief=RIDGE, bg="#0676ad", fg="white")
        self.lbl_student.place(x=490, y=530, width=300, height=100)

        self.lbl_result = Label(self.root, text="Total Results\n[ 0 ]", font=("goudy old style", 20), bd=10, relief=RIDGE, bg="#038074", fg="white")
        self.lbl_result.place(x=820, y=530, width=300, height=100)

        # Update totals
        self.update_totals()

    def update_totals(self):
        total_courses = self.get_total_courses()
        total_students = self.get_total_students()
        total_results = self.get_total_results()

        # Update labels with the total counts
        self.lbl_course.config(text=f"Total Courses\n[ {total_courses} ]")
        self.lbl_student.config(text=f"Total Students\n[ {total_students} ]")
        self.lbl_result.config(text=f"Total Results\n[ {total_results} ]")

    def get_total_courses(self):
        con = sqlite3.connect("rms.db")
        cur = con.cursor()
        cur.execute("SELECT COUNT(*) FROM course")
        total_courses = cur.fetchone()[0]
        con.close()
        return total_courses

    def get_total_students(self):
        con = sqlite3.connect("rms.db")
        cur = con.cursor()
        cur.execute("SELECT COUNT(*) FROM student")
        total_students = cur.fetchone()[0]
        con.close()
        return total_students

    def get_total_results(self):
        con = sqlite3.connect("rms.db")
        cur = con.cursor()
        cur.execute("SELECT COUNT(*) FROM result")
        total_results = cur.fetchone()[0]
        con.close()
        return total_results

    def add_course(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = CourseClass(self.new_win)

    def add_student(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = StudentClass(self.new_win)

    def add_result(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = ResultClass(self.new_win)
    
    def add_report(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = reportClass(self.new_win)

    def exit_app(self):
        if messagebox.askyesno("Confirm Exit", "Are you sure you want to exit?"):
            self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()
