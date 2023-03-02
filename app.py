import sqlite3
import streamlit as st

# define a function to create the 'students' table if it doesn't exist
def create_table():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS students
                 (id INTEGER PRIMARY KEY,
                  name TEXT NOT NULL,
                  age INTEGER,
                  grade REAL);''')
    conn.commit()
    conn.close()

# create the 'students' table if it doesn't exist
create_table()

# create a Streamlit form for inserting data into the 'students' table
st.write('# Add a new student')
name = st.text_input('Name')
age = st.number_input('Age', min_value=0, max_value=120)
grade = st.number_input('Grade', min_value=0.0, max_value=4.0)

if st.button('Add student'):
    # connect to the database and insert the new student data
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", (name, age, grade))
    conn.commit()
    conn.close()
    st.write('Student added!')
