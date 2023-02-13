from fpdf import FPDF
import streamlit as st
import base64
from pathlib import Path
import num2words
import datetime
import mysql.connector as sqlc
from mysql.connector import Error
import pandas as pd
from PIL import Image
import numpy as np
import os

def conToBin(fname):
    with open(fname,'rb') as file:
        bindata=file.read()
    return bindata
try:    
        year=['select the year','I','II','III','IV']
        quota = ['Management','COMEDK','CET','SNQ','GOI']
        category = ['SC','ST','OBC','GM']
        sought = ['B.E.', ' M.Tech.',' M.C.A.']
        branch_li = ['Select your branch','CSE - Computer Science and Engineering','ECE - Electronics and Communication Engineering',
        'EEE - Electrical and Electronics Engineering','CIV - Civil Engineering','MEC - Mechanical Engineering',
        'MCA - Master of Computer Application']

        #st.set_page_config(page_title="REGISTRATION FORM",page_icon='🖊️')
        # st.header('REGISTRATION FORM')
        st.markdown("<h1 style='text-align: center; color: black;'>REGISTRATION FORM</h1>", unsafe_allow_html=True)
        admission_sought = st.selectbox('Admission Sought',sought)
        Name = st.text_input('Full Name')
        usn = st.text_input('USN')
        branch = st.selectbox('Branch:',branch_li)
        Email = st.text_input('Email : ')

        Ph_number = st.text_input('Mobile No.')
        parents_mobile_number = st.text_input('Parents Mobile No.')
        postal_address = st.text_input('Postal Address\n')
        admission_year = st.selectbox('Admission To ',year)
        admission_quota = st.selectbox('Admission Quota',quota)
        cat = st.selectbox('Select Category',category)

        pe1 = st.text_input('Professional Electives - 1 Opted (Only for Third & Fourth Year): ')
        pe2 = st.text_input('Professional Electives - 2 Opted (Only for Third & Fourth Year): ')
        oe1 = st.text_input('Open Electives - 1 Opted (Only for Third & Fourth Year): ')
        oe2 = st.text_input('Open Electives - 2 Opted (Only for Third & Fourth Year): ')


        fee_pending = st.number_input('Fees Due Till Date: Rs. : ')
        fee_paid = st.number_input('Fees Paid for Cur. Academic Year: Rs.: ')
        fee_paid_date = st.date_input("Date of fee payment",datetime.date(2022, 7, 22))
        uploaded_file = st.file_uploader('Upload receipt in .jpg/png Format', type=['png', 'jpg'])
        if uploaded_file is not None:
            bytes_data = uploaded_file.getvalue()
        update_database=st.button("Update Database")
        if update_database:
                cnx=sqlc.connect(host="localhost",user="root",password="1234",database="sdm")
                Cursor=cnx.cursor()
                #conPic = conToBin(dir)
                InsertQuery="INSERT INTO DETAILS VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                data=(admission_sought,Name,usn,branch,Email,Ph_number,parents_mobile_number,postal_address,admission_year,admission_quota,cat,fee_pending,fee_paid,fee_paid_date,bytes_data)
                Cursor.execute(InsertQuery,data)
                cnx.commit()
                cnx.close()
                cnx=sqlc.connect(host="localhost",user="root",password="1234",database="sdm")
                Cursor=cnx.cursor()
                InsertQuery1="INSERT INTO ELECTIVES VALUES(%s,%s,%s,%s,%s,%s)"
                data1=(admission_sought,Name, pe1,pe2,oe1,oe2)
                Cursor.execute(InsertQuery1,data1)
                cnx.commit()
                st.write("Data Inserted Successfully")
except Error as e:
    st.write("Error occured",e)