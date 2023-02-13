import streamlit as st
import mysql.connector as sqlc
from mysql.connector import Error
import numpy as np
import pandas as pd
def app():
        st.markdown('<h1 style="text-align: center;">CIV Registered Students</h1>', unsafe_allow_html=True)
        try:
                        cnx=sqlc.connect(host="localhost",user="root",password="root",database="sdm")
                        Cursor=cnx.cursor()
                        SelectQuery="SELECT * FROM CIV ORDER BY ADMISSION_TO"
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
        except Error as e:
                        print("Error occured",e)
    