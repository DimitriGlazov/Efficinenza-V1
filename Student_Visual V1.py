''' Student performace Visual for meetings and analysis '''

# importing modules

import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px
import openpyxl
import base64
import  io

# Making the head
st.set_page_config(page_title=' Performance Tracker V1')
head = st.header(' Performance Tracker V1 🧑‍🏫')
subhead = st.subheader(' Analyse Student Performance in real time')

fileupload = None


#Uploading the file
fileupload = st.file_uploader('Please Upload your file here',type='XLSX')
dataframe = pd.read_excel(fileupload,engine='openpyxl')

# file uploading
if fileupload is not None:
    try:
        df = pd.read_excel(fileupload,engine='openpyxl')
        st.success(' Data Uploaded successfully ')
        #st.dataframe(df)

        # Input of the roll number
        roll_num = st.number_input(" Please enter the student's roll number ")

        if roll_num in dataframe['Roll Number'].values:
            st.success(' Roll number present ')
        else:
            st.error(' Please enter a valid roll number')

    except Exception as error:
        st.error(' Error Please reupload the file ')

else:
    st.info(' Please upload the file ')


# Extracting the data
selectedroll = df[df['Roll Number'] == roll_num]

#Subject selection
selection = st.multiselect('Choose subjects to visualise',('English','Pol Sci','History','Economics','Optional '))


if selection:
     studentname = selectedroll['Name'].values[0]
     st.write(f" {studentname} performance in selected subjects ")
     student_performance = selectedroll[selection].T
     student_performance.columns = ['Marks']
     student_performance['Subjects'] = student_performance.index

 # Create a bar chart using Plotly
     fig = px.bar(student_performance, x='Subjects', y='Marks',
                  title='Student Performance in Selected Subjects',
                  labels={'Marks': 'Marks', 'Subjects': 'Subjects'}, color='Subjects',
                  color_discrete_sequence=['#ADD8E6', '#FA8072', '#FFD700', '#2E8B57', '#EE82EE'])
     st.plotly_chart(fig)
     strongestsubject = student_performance['Marks'].idxmax()
     weakestsubject = student_performance['Marks'].idxmin()

     st.subheader(' AI Generated Suggestions 🧠 ')
     st.write(f"{studentname} needs to work more on {weakestsubject} ")
     st.write(f"{studentname} scored highest in  {strongestsubject} ")



