import streamlit as st
from multiapp import MultiApp
from apps import home,cse,ece,eee,civ,mech,admin # import your app modules here
import mysql.connector as sqlc
app = MultiApp()
st.sidebar.markdown('<h1 style="text-align: center;">Admin Login</h1>', unsafe_allow_html=True)
username=st.sidebar.text_input("Username",key='uname')
password=st.sidebar.text_input("Password",type="password",key='passwd')
c1=st.sidebar.checkbox("Login",key='login')
#c2=st.sidebar.checkbox("Signup",key='signup')
if c1:   
    try:
        cnx=sqlc.connect(host="localhost",user="root",password="root",database="sdm")
        Cursor=cnx.cursor()
        SelectQuery="SELECT * FROM LOGIN WHERE USERNAME=%s AND PASSWORD=%s"
        data=(username,password)
        Cursor.execute(SelectQuery,data)
        for row in Cursor:
            if(row[0]=='CSE' and row[1]=='hodcse'):
                app.add_app("CSE Login",cse.app)
                app.run()    
            elif(row[0]=='ECE' and row[1]=='hodece'):
                app.add_app("ECE Login",ece.app)
                app.run()
            elif(row[0]=='EEE' and row[1]=='hodeee'):
                app.add_app("EEE Login",eee.app)
                app.run()
            elif(row[0]=='CIV' and row[1]=='hodciv'):
                app.add_app("CIV Login",civ.app)
                app.run()
            elif(row[0]=='MECH' and row[1]=='hodmech'):
                app.add_app("MECH Login",mech.app)
                app.run()
            elif(row[0]=='admin' and row[1]=='kleit'):
                app.add_app("Admin Login",admin.app)
                app.run()
    except:
            st.error("Username/Password not correct")
else:
        st.markdown("""
        # Student Registration

        """)
        app.add_app("Registration Form", home.app)
        app.run()

# Add all your application here

#app.add_app("Database", data.app)
# The main app

