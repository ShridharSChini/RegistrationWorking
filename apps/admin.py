import streamlit as st
import mysql.connector as sqlc
from mysql.connector import Error
import numpy as np
import pandas as pd
def app():        
        st.markdown('<h1 style="text-align: center;">All Registered Students</h1>', unsafe_allow_html=True)
        try:
            cnx=sqlc.connect(host="localhost",user="root",password="root",database="sdm")
            Cursor=cnx.cursor()
            col1,col2,col3,col4,col5=st.columns(5)
            if col1.checkbox("CSE"):
                    st.markdown('<h1 style="text-align: center;">CSE Registered Students</h1>', unsafe_allow_html=True)
                    SelectQuery="SELECT * FROM CSE ORDER BY ADMISSION_TO"
                    Cursor.execute(SelectQuery)
                    data=Cursor.fetchall()
                    result=pd.DataFrame(data)
                    result.columns=['USN','Full Name','Branch','Fees Due','Fees Paid','Date of Payment','Receipt','Admission Sought','Email','Mobile No.','Parents Mob. No.','Postal Address','Admission To(Year)','Admission Quota','Category','Prof. Elective-1','Prof. Elective-2','Open Elective-1','Open Elective-2']
                
                    # st.write(result['Receipt'])
                    # st.write(type(str(result['Receipt'])))
                    # result['Receipt'] = str(result['Receipt'])
                    # result['Receipt'] =result['Receipt'].apply(result['Receipt'])

                    st.markdown(result.to_html(render_links=True,escape=False),unsafe_allow_html=True)
                    # result = result.to_html(escape=False)
                    # st.write(result,unsafe_allow_html = True) 
                    # st.dataframe(result)
                    # cnx.commit()
                    CountQuery="SELECT COUNT(*) FROM CSE"
                    Cursor.execute(CountQuery)
                    for row in Cursor:
                        st.write("Total Count:",row[0]-1)
                    PaidQuery="SELECT SUM(FEES_PAID) FROM CSE"
                    Cursor.execute(PaidQuery)
                    for row in Cursor:
                        st.write("Total Fees Paid:",row[0])
                    PendingQuery="SELECT SUM(FEES_PENDING) FROM CSE"
                    Cursor.execute(PendingQuery)
                    for row in Cursor:
                        st.write("Total Fees Pending:",row[0])
            if col2.checkbox("ECE"):
                    st.markdown('<h1 style="text-align: center;">ECE Registered Students</h1>', unsafe_allow_html=True)
                    SelectQuery="SELECT * FROM ECE ORDER BY ADMISSION_TO"
                    Cursor.execute(SelectQuery)
                    data=Cursor.fetchall()
                    result=pd.DataFrame(data)
                    result.columns=['USN','Full Name','Branch','Fees Due','Fees Paid','Date of Payment','Receipt','Admission Sought','Email','Mobile No.','Parents Mob. No.','Postal Address','Admission To(Year)','Admission Quota','Category','Prof. Elective-1','Prof. Elective-2','Open Elective-1','Open Elective-2']
                    st.markdown(result.to_html(render_links=True,escape=False),unsafe_allow_html=True)
                    CountQuery="SELECT COUNT(*) FROM ECE"
                    Cursor.execute(CountQuery)
                    for row in Cursor:
                        st.write("Total Count:",row[0]-1)
                    PaidQuery="SELECT SUM(FEES_PAID) FROM ECE"
                    Cursor.execute(PaidQuery)
                    for row in Cursor:
                        st.write("Total Fees Paid:",row[0])
                    PendingQuery="SELECT SUM(FEES_PENDING) FROM ECE"
                    Cursor.execute(PendingQuery)
                    for row in Cursor:
                        st.write("Total Fees Pending:",row[0])
            if col3.checkbox("EEE"):
                    st.markdown('<h1 style="text-align: center;">EEE Registered Students</h1>', unsafe_allow_html=True)
                    SelectQuery="SELECT * FROM EEE ORDER BY ADMISSION_TO"
                    Cursor.execute(SelectQuery)
                    data=Cursor.fetchall()
                    result=pd.DataFrame(data)
                    result.columns=['USN','Full Name','Branch','Fees Due','Fees Paid','Date of Payment','Receipt','Admission Sought','Email','Mobile No.','Parents Mob. No.','Postal Address','Admission To(Year)','Admission Quota','Category','Prof. Elective-1','Prof. Elective-2','Open Elective-1','Open Elective-2']
                    st.markdown(result.to_html(render_links=True,escape=False),unsafe_allow_html=True)
                    CountQuery="SELECT COUNT(*) FROM EEE"
                    Cursor.execute(CountQuery)
                    for row in Cursor:
                        st.write("Total Count:",row[0]-1)
                    PaidQuery="SELECT SUM(FEES_PAID) FROM EEE"
                    Cursor.execute(PaidQuery)
                    for row in Cursor:
                        st.write("Total Fees Paid:",row[0])
                    PendingQuery="SELECT SUM(FEES_PENDING) FROM EEE"
                    Cursor.execute(PendingQuery)
                    for row in Cursor:
                        st.write("Total Fees Pending:",row[0])
            if col4.checkbox("CIV"):
                    st.markdown('<h1 style="text-align: center;">CIV Registered Students</h1>', unsafe_allow_html=True)
                    SelectQuery="SELECT * FROM CIV ORDER BY ADMISSION_TO"
                    Cursor.execute(SelectQuery)
                    data=Cursor.fetchall()
                    result=pd.DataFrame(data)
                    result.columns=['USN','Full Name','Branch','Fees Due','Fees Paid','Date of Payment','Receipt','Admission Sought','Email','Mobile No.','Parents Mob. No.','Postal Address','Admission To(Year)','Admission Quota','Category','Prof. Elective-1','Prof. Elective-2','Open Elective-1','Open Elective-2']
                    st.markdown(result.to_html(render_links=True,escape=False),unsafe_allow_html=True)
                    CountQuery="SELECT COUNT(*) FROM CIV"
                    Cursor.execute(CountQuery)
                    for row in Cursor:
                        st.write("Total Count:",row[0]-1)
                    PaidQuery="SELECT SUM(FEES_PAID) FROM CIV"
                    Cursor.execute(PaidQuery)
                    for row in Cursor:
                        st.write("Total Fees Paid:",row[0])
                    PendingQuery="SELECT SUM(FEES_PENDING) FROM CIV"
                    Cursor.execute(PendingQuery)
                    for row in Cursor:
                        st.write("Total Fees Pending:",row[0])
            if col5.checkbox("MECH"):
                    st.markdown('<h1 style="text-align: center;">MECH Registered Students</h1>', unsafe_allow_html=True)
                    SelectQuery="SELECT * FROM MECH ORDER BY ADMISSION_TO"
                    Cursor.execute(SelectQuery)
                    data=Cursor.fetchall()
                    result=pd.DataFrame(data)
                    result.columns=['USN','Full Name','Branch','Fees Due','Fees Paid','Date of Payment','Receipt','Admission Sought','Email','Mobile No.','Parents Mob. No.','Postal Address','Admission To(Year)','Admission Quota','Category','Prof. Elective-1','Prof. Elective-2','Open Elective-1','Open Elective-2']
                    st.markdown(result.to_html(render_links=True,escape=False),unsafe_allow_html=True)
                    CountQuery="SELECT COUNT(*) FROM MECH"
                    Cursor.execute(CountQuery)
                    for row in Cursor:
                        st.write("Total Count:",row[0]-1)
                    PaidQuery="SELECT SUM(FEES_PAID) FROM MECH"
                    Cursor.execute(PaidQuery)
                    for row in Cursor:
                        st.write("Total Fees Paid:",row[0])
                    PendingQuery="SELECT SUM(FEES_PENDING) FROM MECH"
                    Cursor.execute(PendingQuery)
                    for row in Cursor:
                        st.write("Total Fees Pending:",row[0])
        except Error as e:
                    print("Error occured",e)
