import streamlit as st
import psycopg2

DATABASE_URL = "postgresql://admin:password@172.17.0.4:5432/mydatabase"

try:
    conn = psycopg2.connect(DATABASE_URL)
    print("Connected to PostgreSQL successfully!")
except Exception as e:
    print("Error:", e)


# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="mydb",
    user="admin",
    password="adminpassword",
    host="my_postgres",  # This is the PostgreSQL container name
    port="5432"
)
cur = conn.cursor()

# Fetch database version
cur.execute("SELECT version();")
db_version = cur.fetchone()

st.title("Streamlit App with PostgreSQL")
st.write("Connected to database:", db_version)

cur.close()
conn.close()
