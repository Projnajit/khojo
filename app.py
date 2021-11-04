from logging import PlaceHolder
#from multiapp import MultiApp
import mysql.connector as mysql
from numpy import double
import pandas as pd
import time
from datetime import datetime
from PIL import Image
import json
import base64
from streamlit.elements import image
import yagmail
import re
from PIL import Image
from re import search
# import smtplib
 
import streamlit as st
import streamlit.components.v1 as components
from streamlit import caching
 
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
from sqlalchemy import create_engine
from mysql.connector.constants import ClientFlag
from uuid import uuid4


st.set_page_config(
    page_title="KHOJO",
    page_icon=":loudspeaker:",
    layout="wide",
    initial_sidebar_state="expanded",
)
 #database localhost connection
 #@st.cache()


## all using functions start
sub_id=''
def buy_home():
    st.markdown('<p style="color:#ff6347;font-weight:bold;font-size:20px">Choose your Home:</p>', unsafe_allow_html=True)
    cursor.execute("select * from sell")
    xx=cursor.fetchall()
    potaka=1
    for m in xx:
        if m[11]!=sub_id:
            potaka=0
            temp=st.expander(m[1],False)
            with temp:
                col1,col2=st.columns((5,10))
                col1.write('Apartment name: ')
                col2.write(m[1])
                col1.write('Owner name: ')
                col2.write(m[2])
                col1.write('State: ')
                col2.write(m[3])
                col1.write('Address: ')
                col2.write(m[4])
                col1.write('Price: ')
                col2.write(m[5])
                col1.write('Room: ')
                col2.write(m[6])
                col1.write('Bath: ')
                col2.write(m[7])
                col1.write('Square Feet: ')
                col2.write(m[8])
                col1.write('Vacency: ')
                col2.write(m[10])
                col1.write('Apartment Id: ')
                col2.write(m[0])
                slt=st.checkbox("Select",key=m[0])
                if slt:
                    if m[10]=='available':
                        with st.form(key='buy_home'):
                            name=st.text_input('Full Name')
                            phone=st.text_input('Phone')
                            email=st.text_input('Email')
                            address=st.text_input('Address')
                            type='buy'
                            status='pending'
                            a=uuid4()
                            a=str(a)[:5]
                            apt_id=m[0]
                            act=st.form_submit_button('Request')
                        
                            if act:
                                query='''INSERT INTO buy(buyer_name,phone,email,address,type,product_id,uid)
                                VALUES(%s,%s,%s,%s,%s,%s,%s)'''
                                val=(name,phone,email,address,type,apt_id,a)
                                cursor.execute(query,val)
                                db.commit()

                                query='''UPDATE sell SET uid=%s, status=%s WHERE id=%s'''
                                val=(a,status,apt_id)
                                cursor.execute(query,val)
                                db.commit()
                                st.success(f'{name}, your buying request submitted succefully!\n\n Your Tracking id is {a}, please store it for further use.')
        
                    else: st.warning('Please, select an available apartment')    
    if potaka: st.warning('Sorry! There is nothing available for you.')

def get_rent():
    st.markdown('<p style="color:#ff6347;font-weight:bold;font-size:20px">Choose your Home:</p>', unsafe_allow_html=True)
    cursor.execute("select * from rent")
    xx=cursor.fetchall()
    potaka=1
    for m in xx:
        if m[11]!=sub_id:
            potaka=0
            temp=st.expander(m[1],False)
            with temp:
                col1,col2=st.columns((5,10))
                col1.write('Apartment name: ')
                col2.write(m[1])
                col1.write('Owner name: ')
                col2.write(m[2])
                col1.write('State: ')
                col2.write(m[3])
                col1.write('Address: ')
                col2.write(m[4])
                col1.write('Price: ')
                col2.write(m[5])
                col1.write('Room: ')
                col2.write(m[6])
                col1.write('Bath: ')
                col2.write(m[7])
                col1.write('Square Feet: ')
                col2.write(m[8])
                col1.write('Vacency: ')
                col2.write(m[10])
                col1.write('Apartment Id: ')
                col2.write(m[0])
                slt=st.checkbox("Select",key=m[0])
                if slt:
                    if m[10]=='available':
                        with st.form(key='rent_home'):
                            name=st.text_input('Full Name')
                            phone=st.text_input('Phone')
                            email=st.text_input('Email')
                            address=st.text_input('Address')
                            type='rent'
                            status='pending'
                            a=uuid4()
                            a=str(a)[:5]
                            apt_id=m[0]
                            act=st.form_submit_button('Request')
                            if act:                       
                                query='''INSERT INTO buy(buyer_name,phone,email,address,type,product_id,uid)
                                VALUES(%s,%s,%s,%s,%s,%s,%s)'''
                                val=(name,phone,email,address,type,apt_id,a)
                                cursor.execute(query,val)
                                db.commit()

                                query='''UPDATE rent SET uid=%s, status=%s WHERE id=%s'''
                                val=(a,status,apt_id)
                                cursor.execute(query,val)
                                db.commit()
                                st.success(f'{name}, your renting request submitted succefully!\n\n Your Tracking id is {a}, please store it for further use.')
                    else: st.warning('Please, select an available apartment')
    if potaka: st.warning('Sorry! There is nothing for you.')
        

def sell_rent_home():
    st.markdown('<p style="color:#ff6347;font-size:25px;font-weight:bold;line-height: 5pt">Place your place</p>',unsafe_allow_html=True)
    with st.form(key="sell_rent form"):
        apt_name=st.text_input('Apartment name')
        name=st.text_input('Owner name')
        state=st.text_input('State')
        address=st.text_input('Address')
        price=st.text_input('Price')
        bed=st.text_input('Room')
        bath=st.text_input('Bath')
        sq_ft=st.text_input('Square feet')
        type=st.selectbox('',('Whice you want?','Rent','Sell'))
        a=uuid4()
        a=str(a)[:5]
        status='available'
        act=st.form_submit_button()
    if act:
        if type=='Rent':
            query='''INSERT INTO rent(id,apartment_name,owner_name,state,address,price,room,bath,sq_ft,status,submittor_id)
                        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
            val=(a,apt_name,name,state,address,price,bed,bath,sq_ft,status,sub_id)
            cursor.execute(query,val)
            db.commit()
            st.success(f'{name}, your data registered successfully.')
        
        elif type=='Sell':
            query='''INSERT INTO sell(id,apartment_name,owner_name,state,address,price,room,bath,sq_ft,status,submittor_id)
                        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
            val=(a,apt_name,name,state,address,price,bed,bath,sq_ft,status,sub_id)
            cursor.execute(query,val)
            db.commit()
            st.success(f'{name}, your data registered successfully.')
        else:
            st.warning('Select a type first.')


def selling_list():
    st.markdown('<p style="color:#ff6347;font-weight:bold;font-size:20px">Response to your sell:</p>', unsafe_allow_html=True)
    cursor.execute("select * from sell")
    potaka=1
    mem=cursor.fetchall()
    for m in mem:
        if(m[10]=='pending' and m[11]==sub_id):
            potaka=0
            temp=st.expander(m[1],False)
            with temp:
                cursor.execute("select * from buy")
                lis=cursor.fetchall()
                for x in lis:
                    if x[6]==m[0]:
                        col1,col2=st.columns((5,10))
                        col1.write('Buyer name: ')
                        col2.write(x[1])
                        col1.write('Phone: ')
                        col2.write(x[2])
                        col1.write('Email: ')
                        col2.write(x[3])
                        col1.write('Address: ')
                        col2.write(x[4])
                        col1.write('Apartment id: ')
                        col2.write(x[6])
                        ac=st.button("Accepted",key=x[0])
                        rj=st.button("Rejected",key=x[0])

                        if ac:
                            query0='''UPDATE sell SET status=%s WHERE id=%s'''
                            val=('SOLD OUT',m[0])
                            cursor.execute(query0,val)
                            db.commit()
                            st.success(f'You sold out to {x[1]}!')
                        elif rj:
                            query0='''UPDATE sell SET status=%s WHERE id=%s'''
                            val=('available',m[0])
                            cursor.execute(query0,val)
                            db.commit()
                            st.success(f'You rejected the request of {x[1]}!')
    if potaka: st.warning('Sorry, list is empty!')


def renting_list():
    st.markdown('<p style="color:#ff6347;font-weight:bold;font-size:20px">Response to your rent:</p>', unsafe_allow_html=True)
    cursor.execute("select * from rent")
    mem=cursor.fetchall()
    potaka=1
    for k in mem:
        if(k[10]=='pending' and k[11]==sub_id):
            potaka=0
            temp=st.expander(k[1],False)
            with temp:
                cursor.execute("select * from buy")
                lis=cursor.fetchall()
                for x in lis:
                    if x[6]==k[0]:
                        col1,col2=st.columns((5,10))
                        col1.write('Buyer name: ')
                        col2.write(x[1])
                        col1.write('Phone: ')
                        col2.write(x[2])
                        col1.write('Email: ')
                        col2.write(x[3])
                        col1.write('Address: ')
                        col2.write(x[4])
                        col1.write('Apartment id: ')
                        col2.write(x[6])
                        ac=st.button("Accepted",key=x[0])
                        rj=st.button("Rejected",key=x[0])

                        if ac:
                            query0='''UPDATE rent SET status=%s WHERE id=%s'''
                            val=('RENT OUT',k[0])
                            cursor.execute(query0,val)
                            db.commit()
                            st.success(f'You rent out to {x[1]}!')
                        elif rj:
                            query0='''UPDATE rent SET status=%s WHERE id=%s'''
                            val=('available',k[0])
                            cursor.execute(query0,val)
                            db.commit()
                            st.success(f'You rejected the request of {x[1]}!')
    if potaka: st.warning('Sorry, list is empty!')


def uploaded_home():
    st.markdown('<p style="color:#ff6347;font-weight:bold;font-size:20px">Upload for sell:</p>', unsafe_allow_html=True)
    cursor.execute("select * from sell")
    xx=cursor.fetchall()
    potaka=1
    for m in xx:
        if m[11]==sub_id:
            potaka=0
            temp=st.expander(m[1],False)
            with temp:
                col1,col2=st.columns((5,10))
                col1.write('Apartment name: ')
                col2.write(m[1])
                col1.write('Owner name: ')
                col2.write(m[2])
                col1.write('State: ')
                col2.write(m[3])
                col1.write('Address: ')
                col2.write(m[4])
                col1.write('Price: ')
                col2.write(m[5])
                col1.write('Room: ')
                col2.write(m[6])
                col1.write('Bath: ')
                col2.write(m[7])
                col1.write('Square Feet: ')
                col2.write(m[8])
                col1.write('Vacency: ')
                col2.write(m[10])
                col1.write('Apartment Id: ')
                col2.write(m[0])
    if potaka: st.warning('Sorry! There is nothing uploaded.')

    st.markdown('<p style="color:#ff6347;font-weight:bold;font-size:20px">Upload for rent:</p>', unsafe_allow_html=True)
    cursor.execute("select * from rent")
    xx=cursor.fetchall()
    potaka=1
    for m in xx:
        if m[11]==sub_id:
            potaka=0
            temp=st.expander(m[1],False)
            with temp:
                col1,col2=st.columns((5,10))
                col1.write('Apartment name: ')
                col2.write(m[1])
                col1.write('Owner name: ')
                col2.write(m[2])
                col1.write('State: ')
                col2.write(m[3])
                col1.write('Address: ')
                col2.write(m[4])
                col1.write('Price: ')
                col2.write(m[5])
                col1.write('Room: ')
                col2.write(m[6])
                col1.write('Bath: ')
                col2.write(m[7])
                col1.write('Square Feet: ')
                col2.write(m[8])
                col1.write('Vacency: ')
                col2.write(m[10])
                col1.write('Apartment Id: ')
                col2.write(m[0])
    if potaka: st.warning('Sorry! There is nothing uploaded.')


def driver():
    st.sidebar.markdown('<p style="font-size:20px;font-weight:bold;line-height: 0pt">Touch your requirements:</p>',unsafe_allow_html=True)
    task = st.sidebar.selectbox('',('select catagory','Rent a Home',
                                    'Buy a Home',' Upload to Sell/Rent'))
    if task=='Rent a Home':
        get_rent()
    elif task=='Buy a Home':
        buy_home()
    elif task=='Upload to Sell/Rent':
        sell_rent_home()

    temp=st.sidebar.selectbox('cheak who respond to you',('select catagory','Selling list(respose)','Renting list(response)','My all uploaded Home'))

    if temp=='Selling list(respose)':
        selling_list()
    elif temp=='Renting list(response)':
        renting_list()
    elif temp=='My all uploaded Home':
        uploaded_home()

    bll=st.sidebar.checkbox('Check you pending')
    if bll:
        flag=1
        txt=st.text_input('Enter your tracking code: ')
        cursor.execute("select uid,status,apartment_name from sell")
        haha=cursor.fetchall()
        for k in haha:
            if k[0]==txt:
                flag=0
                if k[1]=='SOLD OUT':
                    st.success(f'Congratulations!! You just buy {k[2]} apartment.')
                    break
                elif k[1]=='pending':
                    st.warning(f'Your request still in pending! Please, wait for the response. Try again later.')
                else:
                    st.warning(f'Sorry! Your request is rejected.')
        if flag:
            cursor.execute("select uid,status,apartment_name from rent")
            haha=cursor.fetchall()
            for k in haha:
                if k[0]==txt:
                    flag=0
                    if k[1]=='RENT OUT':
                        st.success(f'Congratulations!! You just buy {k[2]} apartment.')
                        break
                    elif k[1]=='pending':
                        st.warning(f'Please, wait for the response. Try again later.')
                    else:
                        st.warning(f'Sorry! Your request is rejected.')
        



with open('credintials.yml', 'r') as f:
    credintials = yaml.load(f, Loader=yaml.FullLoader)
    db_credintials = credintials['db']
    system_pass = credintials['system_pass']['admin']
    email_sender = credintials['email_sender']


def get_database_connection():
    db = mysql.connect(host = db_credintials['host'],
                      user = db_credintials['user'],
                      passwd = db_credintials['passwd'],
                      database = db_credintials['database'],
                      auth_plugin= db_credintials['auth_plugin'])
    cursor = db.cursor()
    return cursor, db
## all using functions end

cursor, db = get_database_connection()
 
 
 cursor.execute('''CREATE TABLE register (
    id int NOT NULL AUTO_INCREMENT,
    full_name varchar(255),
    email varchar(255),
    phone varchar(255),
    username varchar(255),
    password varchar(255),
    PRIMARY KEY (id)
)''')


cursor.execute('''CREATE TABLE sell (
  id varchar(255) NOT NULL AUTO_INCREMENT,
  apartment_name varchar(255),
  owner_name varchar(255),
  state varchar(255),
  address varchar(255),
  price varchar(255),
  room varchar(255),
  bath varchar(255),
  sq_ft varchar(255),
  uid varchar(255),
  status varchar(255),
  submittor_id varchar(255),
   PRIMARY KEY (id)
)''')


cursor.execute('''CREATE TABLE rent (
  id varchar(255) NOT NULL AUTO_INCREMENT,
  apartment_name varchar(255),
  owner_name varchar(255),
  state varchar(255),
  address varchar(255),
  price varchar(255),
  room varchar(255),
  bath varchar(255),
  sq_ft varchar(255),
  uid varchar(255),
  status varchar(255),
  submittor_id varchar(255),
    PRIMARY KEY (id)
)''')

cursor.execute('''CREATE TABLE buy (
  buy_id int NOT NULL AUTO_INCREMENT,
  buyer_name varchar(255),
  phone varchar(255),
  email varchar(255),
  address varchar(255),
  type varchar(255),
  product_id varchar(225)
  uid varchar(255),
   PRIMARY KEY (id)
)''')
 
 
st.markdown("""
<style>
.big-font {
    font-size:45px;
    color: #ff6347;
    font-weight: bold;
    font-family: monospace;
    letter-spacing: 8px;
    line-height: 12pt;
}
</style>
""", unsafe_allow_html=True)

##page & sidebar overviwe start
col1,col2= st.sidebar.columns((5,1))
st.sidebar.markdown('<p style="font-family:Gill Sans ,;letter-spacing: 20px;color:#d7005f;font-size:58px;font-weight:bold;line-height: 50pt">KHOJO</p>',unsafe_allow_html=True)
st.sidebar.markdown("""---""")
st.sidebar.markdown('<p style="color:#ff6347;font-size:25px;font-weight:bold;line-height: 22pt">Log In\n</p>',unsafe_allow_html=True)
st.sidebar.markdown('<p style="color:blue;font-size:15x;font-weight:bold;line-height: 3pt">to access activity</p>',unsafe_allow_html=True)
#st.sidebar.markdown("""---""")
st.markdown('<p class="big-font">Find your fresh start</p>', unsafe_allow_html=True)
st.markdown('<p style="font-size:20px;font-weight:bold;letter-spacing: 6px;font-family: Candara;color: blue">Houses, condos, and apartments...</p>',unsafe_allow_html=True)
img=Image.open("1.jpg")
st.image(img)

## page & sidebar overview end


## sidebar activity start

### login
username= st.sidebar.text_input('Username',key='user')
password=st.sidebar.text_input('Password',type='password',key='pass')
st.session_state.login=st.sidebar.checkbox('Log In')
if st.session_state.login:
    cursor.execute("select username, password,full_name from register")
    register=cursor.fetchall()
    flag=1
    for m in register:
        if username.lower()==m[0].lower() and password==m[1]:
            st.sidebar.success(f'Welcome {m[2]}!')
            sub_id=m[2]
            flag=0
            driver()
            break
    if flag:
        st.sidebar.warning("Wrong Information")
### login end


# register
st.sidebar.markdown('<p style="font-weight:bold">Don"t have an account?</p>',unsafe_allow_html=True)
active=st.sidebar.checkbox('Register')
if active:
    st.markdown('<p style="color:#ff6347;font-weight:bold;font-size:20px">Register Yourself :</p>', unsafe_allow_html=True)
    with st.form(key="register form"):
        name=st.text_input('Full Name')
        email=st.text_input('Email')
        phone=st.text_input('Phone')
        username=st.text_input('Username')
        password=st.text_input('Password',type='password',key='pass')
        submit_button=st.form_submit_button('Submit')
        name=name.lower()
        username=username.lower()
    
    if submit_button:
        query='''INSERT INTO register(full_name,email,phone,username,password)
                    VALUES(%s,%s,%s,%s,%s)'''
        val=(name,email,phone,username,password)
        cursor.execute(query,val)
        db.commit()
        st.success(f'{name},you registered successfully.')
# register end

    # temp=st.selectbox('Search Query',('Select Catagory','Want to see existing members?','Specific member?'))
    # if temp=='Want to see existing members?':
    #     cursor.execute("select full_name from register")
    #     st.write(cursor.fetchall())
    # elif temp=='Specific member?':
    #     name=st.text_input('Enter Full Name')
    #     name=name.lower()
    #     cursor.execute("select full_name from register")
    #     member=cursor.fetchall()
    #     flag=0
    #     for m in member:
    #         if name==m[0].lower():
    #             st.success(f'{m[0]} is already Registered.')
    #             flag=1
    #             break

## sidebar activity start
