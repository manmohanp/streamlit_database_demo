import streamlit as st
import uuid
from datetime import date
import psycopg2



st.title('Hello Pet World!!')

# Initialize connection.
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="Password123$"
)

conn.autocommit = True

if st.button('Update'):

    # Perform query.
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM mytable;')

    # Print results.
    for row in cursor.fetchall():
        st.write(f"{row[1]} has a :{row[2]}:")


animal = st.form('my_animal')

animal.write("Pet Mom & Pops")

id = uuid.uuid4()
name = animal.text_input('Your name:')
pet = animal.text_input('Your pet:')
dt = date.today()
submit = animal.form_submit_button('Submit')

if submit:
    try:
        with  conn.cursor() as cur:
            insertSQL =  f"""
            INSERT INTO mytable VALUES ('{id}','{name}','{pet}','{dt}');
            """
            cur.execute(insertSQL)

            # commit the changes to the database
            conn.commit()
            st.write("Inserted!!")
            name = ""
            peg = ""
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
