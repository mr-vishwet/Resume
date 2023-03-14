import base64
import streamlit as stl
from datetime import date
import pandas as pd
import webbrowser
import os
from reportlab.pdfgen import canvas  # for pdf

stl.title("Amazon Company Pool Campus Drive")

stl.write("### Student Response Form <br>", unsafe_allow_html=True)
# stl.write(datetime.now())

name = stl.text_input("**Name***", max_chars=60,
                      placeholder="Enter your Full Name", key='nme')

clg_name = stl.text_input("**College Name***", max_chars=60,
                          placeholder="Enter your Institution Name")

dob = stl.date_input(
    "**Date of Birth***", min_value=date(1980, 6, 1), max_value=date.today())

gender = stl.radio("**Gender***", ['Male', 'Female', 'Other'])

branch = stl.selectbox(
    "**Branch***", ["Computer", "Information Technology", "Electronics and Telecommunications", "Mechanical", "Civil", 'Other'], index=5)

year = stl.radio("**Year***", ['1st', '2nd', '3rd', 'B.Tech'])

relocate = stl.multiselect("**Ready to relocate at***",
                           ['Mumbai', 'Pune', 'Hydrabad', 'Bengaluru', 'Chennai', 'Gudgaon'])

eng_profic = stl.slider("English Proficiency ", min_value=1, max_value=5,)

resume = stl.file_uploader("**Upload your Resume***", type=['pdf'],)

question = stl.text_area("Any Question to HR ? (Optional)", max_chars=1000,
                         placeholder="Feel Free to ask your doubt here :) ")

if stl.button("Submit"):
    if not any([name, clg_name, relocate]) or not (resume):
        stl.write("Error: All fields with * must be filled")
    else:
        data = pd.DataFrame({

            'Field': ['Name', 'College Name', 'DOB', 'Gender', 'Branch', 'Year',
                      'Relocate Locations ', 'Resume Uploaded', 'Question'],
            'Data': [name, clg_name, dob, gender, branch, year,
                     (lambda relocate: '  |  '.join(relocate))(relocate), 'Yes' if resume else 'No', question]
        })

        stl.dataframe(data, use_container_width=True)

# if resume is not None:
#     if stl.button('Open Resume in New Window'):
# create a temporary file to hold the resume contents

# with open(temp_file_path, 'wb') as f:
#     f.write(resume.read())

# # check if file exists before opening
# if os.path.exists(temp_file_path):
#     # open resume in new browser
#     webbrowser.open_new_tab('file:///' + temp_file_path)
# else:
#     stl.error('Error opening PDF file')


# '''
#     locations = ''
#     for i in relocate:
#         locations += i + "  |  "
#     stl.write(locations)
# '''
# if not (name or clg_name == None ) or  :
#     stl.write("Must fill all the fields")


# stl.dataframe(data)
#             stl.write("Opening .......")
#             file_contents = resume.read()
#             with open("temp.pdf", "wb") as f:
#                 f.write(file_contents)
