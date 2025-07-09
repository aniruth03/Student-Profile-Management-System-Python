import mysql.connector
import tkinter as tk
from tkinter import messagebox, ttk

# Establish a connection to the MySQL database
def connect_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="StudentManagement"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None


# Function to add a new student
def add_student():
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    course = course_entry.get()

    if not (name and email and phone and course):
        messagebox.showerror("Error", "All fields are required!")
        return

    conn = connect_db()
    cursor = conn.cursor()
    try:
        sql = "INSERT INTO students (name, email, phone, course) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (name, email, phone, course))
        conn.commit()
        messagebox.showinfo("Success", "Student added successfully.")
        clear_entries()
        view_students()
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Database error: {err}")
    finally:
        cursor.close()
        conn.close()


# Function to view all students
def view_students():
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()
        for row in tree.get_children():
            tree.delete(row)
        for row in rows:
            tree.insert('', tk.END, values=row)
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Database error: {err}")
    finally:
        cursor.close()
        conn.close()


# Function to update a student
def update_student():
    selected = tree.focus()
    if not selected:
        messagebox.showerror("Error", "No student selected")
        return

    student_id = tree.item(selected, 'values')[0]
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    course = course_entry.get()

    if not (name and email and phone and course):
        messagebox.showerror("Error", "All fields are required!")
        return

    conn = connect_db()
    cursor = conn.cursor()
    try:
        sql = "UPDATE students SET name=%s, email=%s, phone=%s, course=%s WHERE student_id=%s"
        cursor.execute(sql, (name, email, phone, course, student_id))
        conn.commit()
        messagebox.showinfo("Success", "Student updated successfully.")
        clear_entries()
        view_students()
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Database error: {err}")
    finally:
        cursor.close()
        conn.close()


# Function to delete a student
def delete_student():
    selected = tree.focus()
    if not selected:
        messagebox.showerror("Error", "No student selected")
        return

    student_id = tree.item(selected, 'values')[0]

    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM students WHERE student_id=%s", (student_id,))
        conn.commit()
        messagebox.showinfo("Success", "Student deleted successfully.")
        clear_entries()
        view_students()
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Database error: {err}")
    finally:
        cursor.close()
        conn.close()


# Function to clear entry fields
def clear_entries():
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)


# Initialize the main window
root = tk.Tk()
root.title("Student Profile Management System")

# Input frame for adding/updating students
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

tk.Label(input_frame, text="Name").grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(input_frame)
name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Email").grid(row=1, column=0, padx=5, pady=5)
email_entry = tk.Entry(input_frame)
email_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Phone").grid(row=2, column=0, padx=5, pady=5)
phone_entry = tk.Entry(input_frame)
phone_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Course").grid(row=3, column=0, padx=5, pady=5)
course_entry = tk.Entry(input_frame)
course_entry.grid(row=3, column=1, padx=5, pady=5)

# Buttons for CRUD operations
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add Student", command=add_student)
add_button.grid(row=0, column=0, padx=5, pady=5)

update_button = tk.Button(button_frame, text="Update Student", command=update_student)
update_button.grid(row=0, column=1, padx=5, pady=5)

delete_button = tk.Button(button_frame, text="Delete Student", command=delete_student)
delete_button.grid(row=0, column=2, padx=5, pady=5)

clear_button = tk.Button(button_frame, text="Clear Fields", command=clear_entries)
clear_button.grid(row=0, column=3, padx=5, pady=5)

# Treeview table for displaying students
tree = ttk.Treeview(root, columns=("ID", "Name", "Email", "Phone", "Course"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Email", text="Email")
tree.heading("Phone", text="Phone")
tree.heading("Course", text="Course")
tree.pack(pady=20)

# Populate data initially
view_students()

# Start the GUI main loop
root.mainloop()
