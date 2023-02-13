from fpdf import FPDF
import streamlit as st
import base64
from pathlib import Path
import num2words
import datetime
import mysql.connector as sqlc
from mysql.connector import Error
import pandas as pd
def conToBin(fname):
    with open(fname,'rb') as file:
        bindata=file.read()
def app():
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
        admission_sought = st.selectbox('Admission Sought',sought,key='1234')
        Name = st.text_input('Full Name')
        usn = st.text_input('USN')
        branch = st.selectbox('Branch:',branch_li,key='xyz')
        Email = st.text_input('Email : ')

        Ph_number = st.text_input('Mobile No.')
        parents_mobile_number = st.text_input('Parents Mobile No.')
        postal_address = st.text_input('Postal Address\n')
        admission_year = st.selectbox('Admission To ',year,key='abc')
        admission_quota = st.selectbox('Admission Quota',quota,key='pqr')
        cat = st.selectbox('Select Category',category,key='idck')

        pe1 = st.text_input('Professional Electives - 1 Opted (Only for Third & Fourth Year): ')
        pe2 = st.text_input('Professional Electives - 2 Opted (Only for Third & Fourth Year): ')
        oe1 = st.text_input('Open Electives - 1 Opted (Only for Third & Fourth Year): ')
        oe2 = st.text_input('Open Electives - 2 Opted (Only for Third & Fourth Year): ')


        fee_pending = st.number_input('Fees Due Till Date: Rs. : ')
        fee_paid = st.number_input('Fees Paid for Cur. Academic Year: Rs.: ')

        fee_pending_words = num2words.num2words((fee_pending), lang='en_IN')
        fee_paid_words = num2words.num2words((fee_paid), lang='en_IN')
        fee_paid_date = st.date_input("Date of fee payment",datetime.date(2022, 7, 22))

        uploaded_file = st.file_uploader('Upload receipt in .jpg/png Format', type=['png', 'jpg'])
        if uploaded_file is not None:
           st.write('Uploaded successfully  ')
           bytes_data = uploaded_file.getvalue()
        export_as_pdf = st.button("Export Report")
             
        class PDF(FPDF):
            def header(self):
                header_path = Path(__file__).parent / "header.png"
                # st.write(header_path)
                self.image(header_path, 0, 0, 200)
    
        # def footer(self):
        #     footer_path = Path(__file__).parent / "dept_body.png"
        #     self.image(footer_path, 20, 210, 170)

        def create_download_link(val, filename):
            b64 = base64.b64encode(val)  # val looks like b'...'
            return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}.pdf">Download file</a>'
        def create_download_image(val, filename):
            b64 = base64.b64encode(val)  # val looks like b'...'
            return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}.png">Download Receipt</a>'
        if export_as_pdf:
            pdf = PDF()
            pdf.add_page()
            # SetMargins(float left, float top [, float right])
            # pdf.set_font("Times", size=10)
            pdf.set_left_margin(15)
            pdf.set_font('Arial', 'B', 11)
            line_height = pdf.font_size * 2.5
            col_width = pdf.epw / 4  # distribute content evenly

            # pdf.multi_cell(col_width, 40,"  ", border=0,new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size)
            pdf.ln(line_height *3.5)

            pdf.multi_cell(col_width, line_height, "Academic Year: ", border=0,new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size)
            pdf.multi_cell(col_width, line_height, "2022 - 23", border=0,new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size)
            pdf.ln(line_height)

            pdf.multi_cell(col_width, line_height, "Admission Sought", border=0,new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size)
            pdf.set_font("Times", size=12)
            pdf.multi_cell(col_width * 4, line_height, admission_sought+"   "+ branch, border=0,new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size)
            pdf.set_font('Arial', 'B', 11)
            pdf.ln(line_height)

            pdf.multi_cell(col_width/1.5, line_height, "Name in Full:", border=0,new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size)
            pdf.set_font("Times", size=12)
            pdf.multi_cell(col_width *1.5, line_height, Name, border=0,new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size)
            pdf.set_font('Arial', 'B', 11)
            pdf.multi_cell(col_width / 1.75, line_height, "USN:", border=0,new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size)
            pdf.set_font("Times", size=12)
            pdf.multi_cell(col_width, line_height, usn, border=0,new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size)
            pdf.set_font('Arial', 'B', 11)
            pdf.ln(line_height)

            # pdf.multi_cell(col_width/1.5, line_height, "Branch:", border=0,new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size)
            # pdf.set_font("Times", size=12)
            # pdf.multi_cell(col_width*1.5, line_height, branch, border=0,new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size)
            # pdf.set_font('Arial', 'B', 11)
            pdf.multi_cell(col_width/1.5, line_height, "Email:", border=0,new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size)
            pdf.set_font("Times", size=12)
            pdf.multi_cell(col_width *2, line_height, Email, border=0,new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size)
            pdf.set_font('Arial', 'B', 11)
            pdf.ln(line_height)

            pdf.multi_cell(col_width/1.5, line_height, "Mobile No.:", border=0,new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size)
            pdf.set_font("Times", size=12)
            pdf.multi_cell(col_width, line_height, Ph_number, border=0,new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size)
            pdf.set_font('Arial', 'B', 11)
            pdf.multi_cell(col_width, line_height, "Parents Mob.No.:", border=0,new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size)
            pdf.set_font("Times", size=12)
            pdf.multi_cell(col_width*1.75, line_height, parents_mobile_number, border=0,new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size)
            pdf.set_font('Arial', 'B', 11)
            pdf.ln(line_height * 1.5)
            # pdf.ln(line_height)

            pdf.multi_cell(col_width , line_height / 0.5, "Postal Address:", border=0,new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size)
            pdf.set_font("Times", size=12)
            pdf.multi_cell(col_width * 2.7, line_height / 0.5 * 1, postal_address, border=1,new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size)
            pdf.set_font('Arial', 'B', 11)
            pdf.ln(line_height)
            pdf.ln(line_height)

            pdf.multi_cell(col_width, line_height , "Admission to :", border=0,new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size)
            pdf.set_font("Times", size=12)
            pdf.multi_cell(col_width, line_height, str(admission_year) + "  Year", border=0,new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size)
            pdf.set_font('Arial', 'B', 11)
            pdf.ln(line_height)

            pdf.multi_cell(col_width *2, line_height, "Admission Quota :  "   + admission_quota, border=0,new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size)
            pdf.multi_cell(col_width, line_height, "Category: "+ cat, border=0,new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size)
            pdf.ln(line_height)

            pdf.multi_cell(col_width *1.5, line_height, "Professional Electives Opted:" , border=0,new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size)
            pdf.set_font("Times", size=12)
            pdf.multi_cell(col_width *2.5, line_height,"(i)  "+ pe1+"  (ii)  "+pe2, border=0,new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size)
            pdf.ln(line_height)

            pdf.set_font('Arial', 'B', 11)
            pdf.multi_cell(col_width *1.5, line_height , "Open Electives Opted:", border=0,new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size)
            pdf.set_font("Times", size=12)
            pdf.multi_cell(col_width *2.5, line_height , "(i)  "+ oe1+"  (ii)  "+oe2, border=0,new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size)
            pdf.ln(line_height)

            pdf.set_font('Arial', 'B', 11)
            pdf.multi_cell(col_width *4, line_height, "Fees Due Till Date: Rs.: "+ str(fee_pending), border=0,new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size)
            pdf.ln(line_height)

            pdf.set_font("Times", size=12)
            pdf.multi_cell(col_width *4, line_height  * 0.1," ("+fee_pending_words + ")", border=0,new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size)
            pdf.ln(line_height)

            pdf.set_font('Arial', 'B', 11)
            pdf.multi_cell(col_width *3, line_height * 0.2, "Fees Paid for Current Academic Year Rs.: "+ str(fee_paid) + "  on  "+ str(fee_paid_date), border=0,new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size)
            pdf.ln(line_height)

            pdf.set_font("Times", size=12)
            pdf.multi_cell(col_width *4, line_height * 0.1, "  ("+fee_paid_words+")", border=0,new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size)
            pdf.set_font('Arial', 'B', 11)
            pdf.ln(line_height)

            pdf.multi_cell(col_width *4, line_height , "Place : Hubballi ", border=0,new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size)
            pdf.ln(line_height)

            # pdf.set_font("Times", size=12)
            pdf.multi_cell(col_width *2, line_height*0.1, "Date : ", border=0,new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size)
            pdf.multi_cell(col_width *2, line_height * 0.1, "(Signature of the Student)", border=0,new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size)
            pdf.ln(line_height)

            footer_path = Path(__file__).parent / "dept_body.png"
            pdf.image(footer_path, 20, 210, 170)

            pdf.ln(line_height *3.5)
            pdf.add_page()
            pdf.image(uploaded_file,10,30,col_width * 4,150)


            html = create_download_link(pdf.output(), "registration_form")
            st.markdown(html, unsafe_allow_html=True)

            html1 =create_download_image(bytes_data,"Receipt")
            # st.write(len(html1))
            # st.markdown(html1, unsafe_allow_html=True)
            try:
                #st.write("connecting to DB")
                cnx=sqlc.connect(host="localhost",user="root",password="root",database="sdm")
                Cursor=cnx.cursor()
                #conPic = conToBin(dir)
                #st.write("inserting into DB")
                if(branch=='CSE - Computer Science and Engineering'):
                    InsertQuery="INSERT INTO CSE VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    data=(usn,Name,branch,fee_pending,fee_paid,fee_paid_date,html1,admission_sought,Email,Ph_number,parents_mobile_number,postal_address,admission_year,admission_quota,cat,pe1,pe2,oe1,oe2)
                    #st.write("Executing the query")
                    Cursor.execute(InsertQuery,data)
                    #st.write("commit to DB")
                    cnx.commit()
                    cnx.close()
                    st.write("Data Inserted Successfully")
                elif(branch=='ECE - Electronics and Communication Engineering'):
                    InsertQuery="INSERT INTO ECE VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    data=(usn,Name,branch,fee_pending,fee_paid,fee_paid_date,html1,admission_sought,Email,Ph_number,parents_mobile_number,postal_address,admission_year,admission_quota,cat,pe1,pe2,oe1,oe2)
                    #st.write("Executing the query")
                    Cursor.execute(InsertQuery,data)
                    #st.write("commit to DB")
                    cnx.commit()
                    cnx.close()
                    st.write("Data Inserted Successfully")
                elif(branch=='EEE - Electrical and Electronics Engineering'):
                    InsertQuery="INSERT INTO EEE VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    data=(usn,Name,branch,fee_pending,fee_paid,fee_paid_date,html1,admission_sought,Email,Ph_number,parents_mobile_number,postal_address,admission_year,admission_quota,cat,pe1,pe2,oe1,oe2)
                    #st.write("Executing the query")
                    Cursor.execute(InsertQuery,data)
                    #st.write("commit to DB")
                    cnx.commit()
                    cnx.close()
                    st.write("Data Inserted Successfully")
                elif(branch=='CIV - Civil Engineering'):
                    InsertQuery="INSERT INTO CIV VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    data=(usn,Name,branch,fee_pending,fee_paid,fee_paid_date,html1,admission_sought,Email,Ph_number,parents_mobile_number,postal_address,admission_year,admission_quota,cat,pe1,pe2,oe1,oe2)
                    #st.write("Executing the query")
                    Cursor.execute(InsertQuery,data)
                    #st.write("commit to DB")
                    cnx.commit()
                    cnx.close()
                    st.write("Data Inserted Successfully")
                elif(branch=='MEC - Mechanical Engineering'):
                    InsertQuery="INSERT INTO MECH VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    data=(usn,Name,branch,fee_pending,fee_paid,fee_paid_date,html1,admission_sought,Email,Ph_number,parents_mobile_number,postal_address,admission_year,admission_quota,cat,pe1,pe2,oe1,oe2)
                    #st.write("Executing the query")
                    Cursor.execute(InsertQuery,data)
                    #st.write("commit to DB")
                    cnx.commit()
                    cnx.close()
                    st.write("Data Inserted Successfully")
            except Error as e:
                print("Error occured",e)

    except (ValueError,AttributeError,FileNotFoundError):
        st.write("ERROR!!!")
        st.write("Fill all the columns")
        
