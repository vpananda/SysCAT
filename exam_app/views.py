from django.shortcuts import render, redirect
from django.db import connection
# from django.shortcuts import render
# from django.core.mail import EmailMessage
from django.views.decorators import gzip
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import never_cache
from django.http import HttpResponse,StreamingHttpResponse,JsonResponse,HttpResponseServerError,HttpResponseBadRequest
# import cv2
import pycountry
import phonenumbers
import asyncio
import threading
import argparse
import datetime
import imutils
import wave
import time
import numpy as np
import pandas as pd
from sqlalchemy import create_engine
import math
import wave
import datetime
from django.core.paginator import Paginator
# import dlib
import re
import os
import io
import xlsxwriter
import base64
# from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Images
from django.core.files.base import ContentFile
import json
from datetime import datetime as dt,timedelta
from datetime import date
from django.core.mail import send_mail

# Create your views here.

# def send_email_view(request):
#     subject = 'Test Email-2 from Django'
#     message = 'This is a test email sent from Django. your id is 20230802001'
#     from_email = 'kalaiselvanj@systechusa.com'  # Replace with your Gmail address
#     recipient_list = ['santoshy@systechusa.com','cimplysantosh@gmail.com']  # Replace with recipient email addresses

#     send_mail(subject, message, from_email, recipient_list)
#     return HttpResponse("mail sent successfully")


# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         try:
#             cursor = connection.cursor()
#             cursor.execute('EXEC check_valid_email @username=%s', [username])
#             user = cursor.fetchone()

#             # If the user was not found by username, try to find by email address     
                   
#             if not user:
#                 cursor.execute('EXEC check_valid_email @email=%s', [username])
#                 user = cursor.fetchone()
#             print(user)
#             if user:
#                 # If the user is valid and password is correct                
#                 if user[3] == password and user[4] == True:
#                     user_name = user[5]
#                     email = user[2]
#                     request.session['username'] = user_name
#                     request.session['email'] = email                  
#                     request.session['user_authenticated'] = True                    
#                     return redirect('dashboard')
                              
#                 elif user[3] == password and user[4] == False:
#                     user_name = user[5]
#                     email = user[2]
#                     request.session['username'] = user_name  
#                     request.session['email'] = email                    
#                     request.session['user_authenticated'] = True                    
#                     return redirect('/introcheckpage')
                
                             
#                 elif user[3] != password:
#                     return render(request, 'registration/login.html', {'perror': 'Invalid Password'})
                
#             # If the user is invalid    
#             elif user == None:
#                 return render(request, 'registration/login.html', {'errors': 'Invalid credentials'})        
#             else:
#                 return render(request, 'registration/login.html', {'error': 'Invalid Email ID'})
#         finally:
#             cursor.close()
#     # Render the login page    
#     return render(request, 'registration/login.html')

def login(request):
    # if request.session['user_authenticated'] == True:
    #     request.session.flush()
    #     request.session['user_authenticated'] = False
    #     return redirect('login')
    if request.method == 'POST':
        cursor = connection.cursor()
        login = request.POST['username']
        password = request.POST['password']
        try:
            cursor.execute('EXEC check_valid_id %s', [login])
            user = cursor.fetchone()
            print(user)
            cursor.close()

            if user:
                if user[3] == password and user[4] == True:
                    user_name = user[5]
                    email = user[2]
                    request.session['username'] = user_name
                    request.session['email'] = email                  
                    request.session['user_authenticated'] = True                    
                    return redirect('dashboard')
                elif user[3] == password and user[4] == False:
                    user_name = user[0]
                    email = user[2]
                    request.session['username'] = user_name  
                    request.session['email'] = email                    
                    request.session['user_authenticated'] = True                    
                    return redirect('/introcheckpage')
                elif user[3] != password:
                    return render(request, 'registration/login.html', {'perror': 'Invalid Password'})
            elif user == None:
                return render(request, 'registration/login.html', {'errors': 'Invalid credentials'}) 
            else:
                return render(request, 'registration/login.html', {'error': 'Invalid Register ID'})
        finally:
            cursor.close()
    return render(request, 'registration/login.html')

def registration(request):

    cursor = connection.cursor()
    cursor.execute('exec getUGDegree')
    ug = cursor.fetchall()
    cursor.execute('exec getPGDegree')
    pg = cursor.fetchall()
    cursor.execute('exec getBranch')
    branch = cursor.fetchall()
    cursor.execute('exec get_skill_applied_for_data')     
    jobs = cursor.fetchall()
    if request.method == "POST":  
        Applyingfor = request.POST.get('Applyingfor')
        print(Applyingfor)
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        gender=request.POST.get('gender')
        dob=request.POST.get('dob')
        MaritalStatus=request.POST.get('MaritalStatus')
        countrycode=request.POST.get('country_code')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        CAddress=request.POST.get('CAddress')
        PAddress=request.POST.get('PAddress')
        Institution10=request.POST.get('Institution10')
        CGPA10=request.POST.get('CGPA10')
        YOP10=request.POST.get('YOP10')
        Institution12=request.POST.get('Institution12')
        CGPA12=request.POST.get('CGPA12')
        YOP12=request.POST.get('YOP12')
        Branch12=request.POST.get('Branch12')
        Graduation=request.POST.get('Graduation')
        UGCollege=request.POST.get('UGCollege')
        UGDiscipline=request.POST.get('UGDiscipline')
        CGPAUG=request.POST.get('CGPAUG')
        YOPUG=request.POST.get('YOPUG')
        PGraduation=request.POST.get('PGraduation')
        PGDiscipline=request.POST.get('PGDiscipline')
        PGCollege=request.POST.get('PGCollege')
        CGPAPG=request.POST.get('CGPAPG')
        YOPPG=request.POST.get('YOPPG')
        Source=request.POST.get('Source')
        Referredthrough=request.POST.get('Referredthrough')
        Applied=request.POST.get('Applied')
        Adate=request.POST.get('Adate')
        Id_proof=request.POST.get('Id_proof')
        ID_NO=request.POST.get('ID_NO')
        iddata=request.POST.get('card_image_data')
        facedata=request.POST.get('face_image_data')
        id_image_file = ContentFile(iddata)
        face_image_file = ContentFile(facedata)

        if PGraduation == None:
            PGraduation='null'        
        if PGDiscipline == None:
            PGDiscipline = 'null'        
        if PGCollege == None:
            PGCollege = 'null'        
        if CGPAPG == None:
            CGPAPG = 0        
        if YOPPG == None:
            YOPPG = 0   

        print(iddata)
        print(facedata) 
        print(id_image_file)
        print(face_image_file)   

        current_date = datetime.date.today()

        # Check the last entered ID in the database
        cursor.execute("SELECT MAX(Username) FROM dbo.tb_Candidate")
        last_id = cursor.fetchone()[0]
        print(last_id)
        

        if last_id:
            # Check if the last entered ID has the same date
            cursor.execute("SELECT id_date FROM dbo.tb_Candidate WHERE Username=%s", [last_id])
            last_date = cursor.fetchone()[0]

            if last_date == str(current_date):
                # Increment the ID by 1
                new_id = str(int(last_id) + 1)
            else:
                # Change the date and start from 1
                new_id = str(current_date).replace('-','')+'001'
        else:
            # No previous IDs in the database, start from 1
            new_id = str(current_date).replace('-','')+'001'

        try:
            cursor = connection.cursor()
            cursor.execute('exec insertregistrationdata %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' ,[Applyingfor,firstname,lastname,gender,dob,MaritalStatus,phone,email,CAddress,PAddress,Institution10,CGPA10,YOP10,Institution12,CGPA12,YOP12,Branch12,Graduation,UGCollege,UGDiscipline,CGPAUG,YOPUG,PGraduation,PGDiscipline,PGCollege,CGPAPG,YOPPG,Source,Referredthrough,Applied,Adate,countrycode,Id_proof,ID_NO,iddata,facedata,new_id,current_date])
            # return render(request, 'registration/login.html')
            subject = 'Mail for User-credentials'
            message = 'Hi '+firstname+', Your Username is '+new_id+' and password is '+phone+', our HR Team will let you know when will exam starts. All the best for your exam!'
            from_email = 'kalaiselvanj@systechusa.com'  # Replace with your Gmail address
            recipient_list = [email]  # Replace with recipient email addresses
            send_mail(subject, message, from_email, recipient_list)
            return redirect('registersuccess')


        finally:
            cursor.close()
            request.session.flush()
    countries = []
    for country in pycountry.countries:
        try:
            phone_code = phonenumbers.country_code_for_region(country.alpha_2)
            phone_label = phonenumbers.region_code_for_country_code(phone_code)
            countries.append((country.alpha_2, f"{country.name} (+{phone_code})", phone_label,phone_code))
        except:
            pass  
    current_year = dt.now().year
    years = [year for year in range(1990, current_year+1)]
    context = {'countries': countries,'ug':ug,'pg':pg,'branch':branch,'jobs':jobs,'years':years}
    return render(request, 'registration/registration.html',context)  

def registersuccess(request):
    return render(request,'registration/registersuccess.html')

@csrf_exempt
def capture_card(request):
    if request.method == 'POST':
        image = request.POST.get('image')
        # do something with the image
    return render(request, 'registration/camera_card.html')


@csrf_exempt
def capture(request):
    if request.method == 'POST':
        image = request.POST.get('image')
        # do something with the image
    return render(request, 'registration/camera.html')

def save_image(request):
    if request.method == 'POST':
        data_url = request.POST.get('image')
        if data_url:
            # Decode the data URL and save the image to a file
            image_data = base64.b64decode(data_url.split(',')[1])
            # now = datetime.datetime.now()
            # image_path = 'C:/Users/KJayavel/Downloads/Systech_merged_latest/Systech/exam_app/img/image{}.png'.format(str(now).replace(":",''))  # Replace with the desired image path
            # with open(image_path, 'wb') as f:
            #     f.write(image_data)

            try:
                cursor = connection.cursor()
                cursor.execute('exec saveImage %s', [image_data])
            finally:
                cursor.close()
                return JsonResponse({'status':'success'})
    
    return JsonResponse({'status': 'error'})

def image_view(request):
    image = get_object_or_404(Images, id=1)
    response = HttpResponse(image.image, content_type='image/jpeg')
    return response
    

# Create your views here.
def generate_excel(request):
    # Get the data from the HTML table
    search_name = request.GET.get('search-bar')

    if search_name == "":
        return redirect('dashboard')

    cursor = connection.cursor()
    cursor.execute('exec get_data_tb_candidate %s', [search_name])
    candidate_data = cursor.fetchall()

    # Create the table data in the required format
    rows = [{
        'Candidate Name': row[1] + ' ' + row[2],
        'User id': row[3],
        'Password': row[4],
        'Applied for': row[5],
        'Start time': row[6],
        'End time': row[7],
        'Remaning time': row[8]
    } for row in candidate_data]

    # Close the cursor after fetching the data
    cursor.close()

    # Create an in-memory output stream for the Excel file
    output = io.BytesIO()

    # Create a new workbook and add a worksheet
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet()

    # Write the table headers
    headers = ['S.No', 'Candidate Name', 'User id', 'Password', 'Applied for', 'Start time', 'End time', 'Remaning time']
    for col_num, header in enumerate(headers):
        worksheet.write(0, col_num, header)

    # Write the table data
    for row_num, row in enumerate(rows):
        worksheet.write(row_num + 1, 0, row_num + 1)  # write the S.No
        for col_num, cell_value in enumerate(row.values()):
            worksheet.write(row_num + 1, col_num + 1, cell_value)

    # Close the workbook
    workbook.close()

    # Create the HttpResponse object with the Excel file
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="candidate_data.xlsx"'
    response.write(output.getvalue())

    return response

# Create your views here.
def sidebar(request):
    return render(request,'base.html')

@never_cache
def dashboard(request):
    if request.session.get('user_authenticated'):
        applied_for = request.GET.get('applied_for')
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        if start_date == '':
            start_date = None
        if end_date == '':
            end_date = None
        print(start_date)
        print(end_date)
        if request.method == 'POST':
            unlock_ids = request.POST.getlist('unlocked_ids[]')
            skip_level_1 = request.POST.getlist('skipped_level_1_ids[]')
            
            print(skip_level_1, unlock_ids)
            cursor = connection.cursor()
            if unlock_ids:
                for lockid in unlock_ids:
                    cursor.execute('exec unlockCandiadtes %s',[lockid])
            if skip_level_1:
                for skip_level in skip_level_1:
                    cursor.execute('exec skip_level_1_Candiadtes %s',[skip_level])
            cursor.close()  # Close the cursor after executing the queries
        
        if applied_for is None:
            applied_for = 'All'   
        
        cursor = connection.cursor()
        cursor.execute('exec get_data_dashboard')
        dash_data = cursor.fetchall()
        
        search_name = request.GET.get('search-bar')
        if search_name == "":
            search_name = None 
        
        cursor.execute('exec get_data_tb_candidate_av @name=%s, @applied_for=%s, @start_date=%s, @end_date=%s', [search_name, applied_for, start_date, end_date])
        candidate_data = cursor.fetchall()
        
        # candidate_data = [...]  # Your list of candidate data
        
        items_per_page = 10  # Number of items to display per page
        page_number = request.GET.get('page')  # Get the requested page number from the URL parameters
        
        paginator = Paginator(candidate_data, items_per_page)  # Create a paginator object
        page_obj = paginator.get_page(page_number)  
        print(candidate_data)
        
        cursor.execute('exec get_skill_applied_for_data')
        search_filter = cursor.fetchall()
        cursor.close()  # Close the cursor after executing the queries
        
        return render(request, 'dashboard/dashboard.html', {'dash_data': dash_data, 'page_obj': page_obj, 'search_filter': search_filter, 'start_date': start_date, 'end_date': end_date})
    
    return redirect('logout')

def candidate_dashboard(request):
    if request.session.get('user_authenticated'):
        applied_for = request.GET.get('applied_for')
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        from datetime import date
        today = date.today()
        first_day = date(today.year, today.month, 1)
        if start_date == '' or start_date is None:
            start_date = first_day
        if end_date == '' or end_date is None:
            end_date = today
        if request.method == 'POST':
            unlock_ids = request.POST.getlist('unlocked_ids[]')
            skip_level_1 = request.POST.getlist('skipped_level_1_ids[]')
            schedule_start_date_format = request.POST.get('schedule_start_date')
            schedule_start_date = datetime.datetime.strptime(schedule_start_date_format, "%Y-%m-%dT%H:%M")
            schedule_end_date_format = request.POST.get('schedule_end_date')
            schedule_end_date = datetime.datetime.strptime(schedule_end_date_format, "%Y-%m-%dT%H:%M")
            print("schedule_start_date   :",schedule_start_date, schedule_end_date)
            cursor = connection.cursor()
            if unlock_ids:
                for lockid in unlock_ids:
                    cursor.execute('exec unlockCandiadtes %s',[lockid])
                    cursor.execute('exec ScheduleCandiadtes %s,%s,%s', [lockid,schedule_start_date,schedule_end_date])
                    cursor.execute('exec get_details_for_email %s',[lockid])
                    details_for_email = cursor.fetchone()
                    print(details_for_email)
                    subject = 'Mail for User-credentials'
                    message = 'Hi '+details_for_email[0]+', Your Username is '+lockid+' and password is '+details_for_email[1]+', your Scheduled Exam Timing is '+str(schedule_start_date)+' to '+str(schedule_end_date)+'. All the best for your exam!'
                    from_email = 'kalaiselvanj@systechusa.com'  # Replace with your Gmail address
                    recipient_list = [details_for_email[2]]  # Replace with recipient email addresses
                    send_mail(subject, message, from_email, recipient_list)
            if skip_level_1:
                for skip_level in skip_level_1:
                    cursor.execute('exec skip_level_1_Candiadtes %s', [skip_level])
            cursor.close()  # Close the cursor after executing the queries
        
        if applied_for is None:
            applied_for = 'All'   
        
        cursor = connection.cursor()
        cursor.execute('exec get_data_dashboard')
        dash_data = cursor.fetchall()
        print(dash_data)
        
        search_name = request.GET.get('search-bar')
        if search_name == "":
            search_name = None 
        
        cursor.execute('exec get_data_tb_candidate_av @name=%s, @applied_for=%s, @start_date=%s, @end_date=%s', [search_name, applied_for, start_date, end_date])
        candidate_data = cursor.fetchall()

        print('candidate_data    :',candidate_data)

        candidate_data_json = json.dumps(candidate_data)

        print(candidate_data_json)
        
         
        cursor.execute('exec get_skill_applied_for_data')
        search_filter = cursor.fetchall()
        cursor.close()  # Close the cursor after executing the queries
        
        print(start_date)
        print(end_date)
        return render(request, 'dashboard/candidate_dashboard.html', {'dash_data': dash_data, 'candidate_data': candidate_data, 'search_filter': search_filter, 'start_date': start_date, 'end_date': end_date})
    
    return redirect('logout')

def show_candidate_data(request, id):
    if request.session.get('user_authenticated'):
        cursor = connection.cursor()
        cursor.execute('EXEC get_candidate_data_by_id %s', [id])
        candidate_data = cursor.fetchone()
        jobPosition = candidate_data[31]
        user_id = candidate_data[0]
        cursor.execute('exec [get_pass_or_fail_candidate] %s, %s, %s', [jobPosition, user_id, 1])
        result_1 = cursor.fetchall()
        cursor.execute('exec [get_pass_or_fail_candidate] %s, %s, %s', [jobPosition, user_id, 2])
        result_2 = cursor.fetchall()

        context = {
            'candidate_data': candidate_data,
            'result_1': result_1,
            'result_2': result_2
        }

        cursor.close()  # Close the cursor after executing the queries

        return render(request, 'dashboard/candidatedata.html', context)

    return redirect('logout')


def registercandidate(request):
    if request.session.get('user_authenticated'):
        applied_for = request.GET.get('applied_for')
        if applied_for is None:
            applied_for = 'All'
        cursor = connection.cursor()
        cursor.execute('exec get_skill_applied_for_data')
        search_filter = cursor.fetchall()
        search_name = request.GET.get('search-bar')
        if search_name == "":
            search_name = None
        cursor.execute('exec get_data_tb_candidate @name=%s, @applied_for=%s', [search_name, applied_for])
        candidate_data = cursor.fetchall()

        context = {
            'candidate_data': candidate_data,
            'search_filter': search_filter
        }

        cursor.close()  # Close the cursor after executing the queries

        return render(request, 'dashboard/registerdcandidates.html', context)

    return redirect('logout')


def delete_candidate(request,id):
    if request.session.get('user_authenticated'):
        try:
            cursor = connection.cursor()
            cursor.execute('exec Deletecandidate %s',[id])
            return redirect('/registercandidate')  
        finally:
            cursor.close()
            pass
    return redirect('login')

def job_positions(request):
    
    try:
        if request.session.get('user_authenticated'):
            cursor = connection.cursor()
            filter_by=request.GET.get('filter_by')
            if filter_by==None:
                filter_by=1      
            cursor.execute('exec getPositiondata %s',[filter_by])
            jobs = cursor.fetchall()
            return render(request, 'dashboard/job_positions.html',{'jobs':jobs})
    finally:
        cursor.close()


# def add_new_job_positions(request):
#     if request.session.get('user_authenticated'):
#         if request.method == "POST":  
#             job_position = request.POST.get('job_title'),
#             isoptionrequired = request.POST.get('is_non_cs'),
#             isbondrequired = request.POST.get('is_bond_required')
            
#             job_position = ''.join(job_position)
#             isoptionrequired = ''.join(isoptionrequired)
#             isbondrequired = ''.join(isbondrequired)

#             try:
#                 cursor = connection.cursor()
#                 cursor.execute('exec InsertJobpositions %s, %s, %s',[job_position,isoptionrequired,isbondrequired])
#                 return redirect('/jobposition')  
#             finally:
#                 cursor.close()
             
#         return render(request, 'dashboard/add_new_job_positions.html')
#     return redirect('login')

def add_new_job_positions(request):
    if request.session.get('user_authenticated'):
        if request.method == "POST":  
            job_position = request.POST.get('job_title'),
            isoptionrequired = request.POST.get('is_non_cs'),
            isbondrequired = request.POST.get('is_bond_required')
            
            job_position = ''.join(job_position)
            isoptionrequired = ''.join(isoptionrequired)
            isbondrequired = ''.join(isbondrequired)

            try:
                cursor = connection.cursor()
                cursor.execute("SELECT job_position FROM tb_jobposition")
                jobs_all = cursor.fetchall()
                job_list = [item[0].lower() for item in jobs_all]
                job_positions = job_position.strip().lower()
                print(job_list)
                if job_positions in job_list:
                    return render(request, 'dashboard/add_new_job_positions.html', {'errors': 'This Job already exists'})
                else:
                    cursor.execute('exec InsertJobpositions %s, %s, %s',[job_position,isoptionrequired,isbondrequired])
                    return redirect('/jobposition')  
            finally:
                cursor.close()
             
        return render(request, 'dashboard/add_new_job_positions.html')
    return redirect('login')

def delete_job_pos(request, id):
    if request.session.get('user_authenticated'):
        try:
            cursor = connection.cursor()
            cursor.execute('exec DeleteJobpositions %s',[id])
            return redirect('/jobposition')  
        finally:
            cursor.close()
    return redirect('login')
        
def edit_job_pos(request, id):
    if request.session.get('user_authenticated'):
        if request.method == 'POST':
            job_position = request.POST['job_position']
            is_option_req = request.POST['is_option_req']
            is_bond_req = request.POST['is_bond_req']
            
            cursor = connection.cursor()
            cursor.execute('exec updateJobPosition %s,%s,%s,%s',[id,job_position,is_option_req,is_bond_req])
            cursor.close()
            return redirect('/jobposition')

        cursor = connection.cursor()
        cursor.execute('EXEC Sp_GetJobs %s', [id])
        jobs = cursor.fetchone()
        cursor.close()

        context = {
            'jobs': jobs
        }

        return render(request, 'dashboard/job_positions.html', context)
    return redirect('login')


def activatePosition(request, id):
    if request.session.get('user_authenticated'):
        try:
            cursor = connection.cursor()
            print(id)
            cursor.execute('exec activatePosition %s',[id])
            return redirect('/jobposition')  
        finally:
            cursor.close()
    return redirect('login')
        
def subject(request):
    if request.session.get('user_authenticated'):
        try:
            cursor = connection.cursor()
            cursor.execute('exec get_subjectData')
            subjects = cursor.fetchall()
            print(subjects)
            return render(request, 'dashboard/subject.html',{'subjects':subjects})
        finally:
            cursor.close()
    return redirect('login')
    
def delete_subject(request, id):
    if request.session.get('user_authenticated'):
        try:
            cursor = connection.cursor()
            cursor.execute('exec deleteSubject %s',[id])
            return redirect('/subject')  
        finally:
            cursor.close()
    return redirect('login')

# def edit_subject(request, id):
#     if request.session.get('user_authenticated'):
#         if request.method == 'POST':
#             subject = request.POST['subject']
#             cursor = connection.cursor()
#             cursor.execute('exec updateSubject %s,%s',[id,subject])
#             cursor.close()
#             return redirect('/subject')

#         cursor = connection.cursor()
#         cursor.execute('EXEC GetSubject_byID %s', [id])
#         subject = cursor.fetchone()
#         cursor.close()

#         context = {
#             'subject': subject
#         }

#         return render(request, 'dashboard/subject.html', context)
#     return redirect('login')

def edit_subject(request, id):
    if request.session.get('user_authenticated'):
        if request.method == 'POST':
            subject = request.POST['subject']
            cursor = connection.cursor()
            cursor.execute("SELECT subject FROM tb_subject")
            subject_all = cursor.fetchall()
            subject_list = [item[0] for item in subject_all]
            print(subject_list)
            if subject in subject_list:
                #want to give alert 
                return redirect('/subject')

            else:
                cursor.execute('exec updateSubject %s,%s',[id,subject])
                cursor.close()
                return redirect('/subject')

        cursor = connection.cursor()
        cursor.execute('EXEC GetSubject_byID %s', [id])
        subject = cursor.fetchone()
        cursor.close()

        context = {
            'subject': subject
        }

        return render(request, 'dashboard/subject.html', context)
    return redirect('login')


def activateSubject(request, id):
    if request.session.get('user_authenticated'):
        try:
            cursor = connection.cursor()
            cursor.execute('exec activateSubject %s',[id])
            return redirect('/subject')  
        finally:
            cursor.close()
    return redirect('login')
        
def subject(request):
    if request.session.get('user_authenticated'):
        try:
            cursor = connection.cursor()
            filter_by=request.GET.get('filter_by')
            if filter_by==None:
                filter_by=1       
            cursor.execute('exec getsubjectdata %s',[filter_by])
            subjects = cursor.fetchall()
            return render(request, 'dashboard/subject.html',{'subjects':subjects})
        finally:
            cursor.close()
    return redirect('login')

    
def new_subject(request):
    if request.session.get('user_authenticated'):
        if request.method == "POST":
            subject = request.POST.get('subject')
            try:
                cursor = connection.cursor()
                cursor.execute("SELECT subject FROM tb_subject")
                subject_all = cursor.fetchall()
                subject_list = [item[0].lower() for item in subject_all]
                subjects = subject.strip().lower()
                print(subject_list)
                if subjects in subject_list:
                    return render(request, 'dashboard/new_subject.html', {'errors': 'This subject already exists'})
                elif re.search(r'[^\w\s]', subject):
                    return render(request, 'dashboard/new_subject.html', {'errors': 'Subject cannot contain special characters or spaces'})
                else:
                    cursor.execute('exec insertSubject %s', [subject])
                    return redirect('/subject')
            finally:
                cursor.close()

        return render(request, 'dashboard/new_subject.html')
    return redirect('login')

def skill_set_config(request):
    if request.session.get('user_authenticated'):
        try:
            cursor = connection.cursor()
            filter_by = request.GET.get('filter_by')
            applied_for = request.GET.get('applied_for')
            if applied_for:
                job_name,job_id  = applied_for.split('|')
            else:
                job_id = 0
                job_name = ''
            if applied_for == None:
                applied_for = 0
            if filter_by == None:
                filter_by = 1
            cursor.execute('exec select_skills_for_job_position %s,%s',[filter_by,job_id])
            skills = cursor.fetchall()
            cursor.execute('exec GetJobposition')
            jobs = cursor.fetchall()
            cursor = connection.cursor()
            cursor.execute('exec get_subjectData')
            subjects = cursor.fetchall()
            cursor.execute('exec get_skill_applied_for_data')
            search_filter = cursor.fetchall()
            return render(request, 'dashboard/skill_set_config.html', {'skills':skills,'jobs':jobs,'subjects':subjects,'search_filter':search_filter,'job_name':job_name})
        finally:
            cursor.close()
    return redirect('login')

def edit_skill(request,id):
    if request.session.get('user_authenticated'):
        if request.method == 'POST':
            job_Position = request.POST.get('job_Position')
            subject = request.POST.get('subjects')
            level = request.POST['level']
            noofquestions = request.POST['noofquestions']
            cutoffmarks = request.POST['cutoffmarks']
            duration = request.POST['duration']
            cursor = connection.cursor()
            cursor.execute('exec updateSubjectlevel %s,%s,%s,%s,%s,%s,%s',[id,subject,job_Position,level,noofquestions,cutoffmarks,duration])
            cursor.close()
            return redirect('/skill_set_config')

        cursor = connection.cursor()
        cursor.execute('EXEC get_Subjectleveldata_byID %s', [id])
        skills = cursor.fetchone()
        cursor.close()
        context = {
            'skill': skills
        }

        return render(request, 'dashboard/subject.html', context)
    return redirect('login')

def delete_skill(request,id):
    if request.session.get('user_authenticated'):
        try:
            cursor = connection.cursor()
            cursor.execute('exec deleteSubjectlevel %s',[id])
            return redirect('/skill_set_config')  
        finally:
            cursor.close()
    return redirect('login')

def activate_skill(request,id):
    if request.session.get('user_authenticated'):
        try:
            cursor = connection.cursor()
            cursor.execute('exec Activate_skill_config %s',[id])
            return redirect('/skill_set_config')  
        finally:
            cursor.close()
    return redirect('login')
        
# def create_Skill(request):
#     if request.session.get('user_authenticated'):
#         cursor = connection.cursor()
#         cursor.execute('exec GetJobposition')
#         jobs = cursor.fetchall()
#         cursor = connection.cursor()
#         cursor.execute('exec get_subjectData')
#         subjects = cursor.fetchall()
#         if request.method == "POST":  
#             AppliedFor = request.POST.get('applied_for')
#             Subject_ID = request.POST.get('subject')
#             Level = request.POST.get('level')
#             No_of_Question = request.POST.get('num_of_questions')
#             CutOffMarks = request.POST.get('cutoff_marks')
#             Duration = request.POST.get('duration')
#             IsMandatory = request.POST.get('subject_type')
#             OptionalGroupName=request.POST.get('subject-type')
#             print(Subject_ID)
#             try:
#                 cursor = connection.cursor()
#                 cursor.execute('exec insertSubjectlevel %s,%s,%s,%s,%s,%s,%s,%s',[AppliedFor,Subject_ID,Level,No_of_Question,CutOffMarks,Duration,IsMandatory,OptionalGroupName])
#                 return redirect('/skill_set_config')  
#             finally:
#                 cursor.close()
#         return render(request, 'dashboard/new_subject_config.html',{'jobs':jobs,'subjects':subjects})
#     return redirect('login')


def create_Skill(request):
    if request.session.get('user_authenticated'):
        cursor = connection.cursor()
        cursor.execute('exec GetJobposition')
        jobs = cursor.fetchall()
        cursor = connection.cursor()
        cursor.execute('exec get_subjectData')
        subjects = cursor.fetchall()
        if request.method == "POST":  
            AppliedFor = request.POST.get('applied_for')
            Subject_ID = request.POST.get('subject')
            Level = request.POST.get('level')
            No_of_Question = request.POST.get('num_of_questions')
            CutOffMarks = request.POST.get('cutoff_marks')
            Duration = request.POST.get('duration')
            IsMandatory = request.POST.get('subject_type')
            OptionalGroupName=request.POST.get('subject-type')
            print('final  : ',Subject_ID,AppliedFor,Level)

            try:
                cursor = connection.cursor()
                cursor.execute("exec calc_no_of_questions_db %s,%s",[Subject_ID,Level])
                no_of_questions_in_db = cursor.fetchone()
                no_of_questions_in_db = no_of_questions_in_db[0]
                # print(no_of_questions_in_db)
                cursor.execute("exec get_skill_present_or_not %s,%s,%s",[Subject_ID,AppliedFor,Level])
                skill_presnet = cursor.fetchall()
                if len(skill_presnet) == 1:
                    return render(request, 'dashboard/new_subject_config.html',{'jobs':jobs,'subjects':subjects,'error': 'This Skill Set already exists'})
                elif (int(no_of_questions_in_db) < int(No_of_Question)):
                    return render(request, 'dashboard/new_subject_config.html',{'jobs':jobs,'subjects':subjects,'error': 'The number Questions in the Database for this skillset is lesser than your input No_of_Questions'})
                else:
                    cursor.execute('exec insertSubjectlevel %s,%s,%s,%s,%s,%s,%s,%s',[AppliedFor,Subject_ID,Level,No_of_Question,CutOffMarks,Duration,IsMandatory,OptionalGroupName])
                    return redirect('/skill_set_config') 
            finally:
                cursor.close()
        return render(request, 'dashboard/new_subject_config.html',{'jobs':jobs,'subjects':subjects})
    return redirect('login')

          

def quest_bank(request):
    if request.session.get('user_authenticated'):
        search_value = request.GET.get('applied_for')
        if search_value:
            sub_id, subject_name = search_value.split('|')
        else:
            sub_id = 0
            subject_name = ''
        active_value = request.GET.get('filter_by')
        if search_value == None:
            sub_id = 0
        if active_value is None:
            active_value = 1
        level = request.GET.get('level')
        if level == None:
            level = 0
        try:
            cursor = connection.cursor()
            cursor.execute('exec get_SearchQuestiondata %s, %s,%s', [sub_id, active_value,level])
            questions = cursor.fetchall()
            cursor.execute('exec get_subjectData')
            subjects = cursor.fetchall()
            cursor.execute('exec get_appied_for_search_data')
            search_filter = cursor.fetchall()
            context = {
                'questions': questions,
                'subjects': subjects,
                'search_filter': search_filter,
                'subject_name': subject_name,
                'sub_id': sub_id,
            }
            return render(request, 'dashboard/quest_bank.html', context)
        finally:
            cursor.close()
    return redirect('login')
       

def add_quest(request):
    if request.session.get('user_authenticated'):
        if request.method == "POST": 
            subject_id =  request.POST.get('subject')
            level_id =  request.POST.get('level')
            question =  request.POST.get('question')
            option1 =  request.POST.get('option1')
            option2 =  request.POST.get('option2')
            option3 =  request.POST.get('option3')
            option4 =  request.POST.get('option4')
            answer =  request.POST.get('answer')
            try:
                cursor = connection.cursor()
                cursor.execute('exec check_duplicate_quest %s',[question])
                question_dup = cursor.fetchall()
                print(question_dup)
                if question_dup == []:
                    cursor.execute('exec insertQuestiondata %s,%s,%s,%s,%s,%s,%s,%s',[subject_id,level_id,question,option1,option2,option3,option4,answer])
                    return redirect('/quest_bank')
                else:
                    cursor = connection.cursor()
                    cursor.execute('exec get_subjectData')
                    subjects = cursor.fetchall()
                    return render(request, 'dashboard/add_quest.html',{'subjects':subjects,'error':'This question already exists'}) 
            finally:
                cursor.close()

        else:

            try:
                cursor = connection.cursor()
                cursor.execute('exec get_subjectData')
                subjects = cursor.fetchall()
                return render(request, 'dashboard/add_quest.html',{'subjects':subjects})
            finally:
                cursor.close()
    return redirect('login')

def edit_ques(request, id):
    if request.method == 'POST':
        subject_id =  request.POST.get('subject')
        level_id =  request.POST.get('level')
        question =  request.POST.get('question')
        option1 =  request.POST.get('option1')
        option2 =  request.POST.get('option2')
        option3 =  request.POST.get('option3')
        option4 =  request.POST.get('option4')
        answer =  request.POST.get('answer')
        cursor = connection.cursor()
        cursor.execute('exec updateQuestiondata %s,%s,%s,%s,%s,%s,%s,%s,%s',[id,subject_id,level_id,question,option1,option2,option3,option4,answer])
        cursor.close()
        return redirect('/quest_bank')

    cursor = connection.cursor()
    cursor.execute('EXEC GetQuestion_byID %s', [id])
    Question = cursor.fetchone()
    cursor.close()
    return render(request, 'dashboard/quest_bank.html',{'Question': Question})

def delete_ques(request, id):
    try:
        cursor = connection.cursor()
        cursor.execute('exec deleteQuestiondata %s',[id])
        return redirect('/quest_bank')  
    finally:
        cursor.close()

def activate_quest(request, id):
    try:
        cursor = connection.cursor()
        cursor.execute('exec Activate_Question %s',[id])
        return redirect('/quest_bank')  
    finally:
        cursor.close()

def alertpage(request):
    return render(request,"exam_portal/alertpage.html")

def alert_page_exam(request):
    return render(request,'dashboard/alert_page_exam.html')

def logout(request):
    request.session.flush()
    request.session['user_authenticated'] = False    
    return render(request, 'registration/logout.html')

def result(request):
    if not request.session.get('user_authenticated'):
        return redirect('logout')

    cursor = connection.cursor()
    cursor.execute('exec get_skill_applied_for_data')
    search_filter = cursor.fetchall()

    def get_param(request, param_name, default=None):
        value = request.GET.get(param_name, '')
        return value if value and value != default else None

    applied_for = get_param(request, 'applied_for')
    filter = get_param(request, 'filter_by', 'ALL')
    level = get_param(request, 'level', '0')
    start_date = get_param(request, 'start_date')
    end_date = get_param(request, 'end_date')
    candidate_id = get_param(request, 'candidate_id')

    job_name, job_id = applied_for.split('|') if applied_for else (None, 0)
    job_name = None if job_name == 'ALL' else job_name

    print(job_name, filter, start_date, end_date)

    cursor.execute('exec [GetCandidateResults] %s,%s,%s,%s', [job_name, filter, start_date, end_date])
    user = cursor.fetchall()
    cursor.close()

    return render(request, 'dashboard/Result.html', {'user': user, 'search_filter': search_filter, 'job_name': job_name, 'start_date': start_date, 'end_date': end_date})

def resultsdetail(request,id):
    if request.session.get('user_authenticated'):
        cursor = connection.cursor()
        cursor.execute('EXEC level_wise_data %s',[id])
        result_data = cursor.fetchall()
        # print(result_data)
        level_1_data = [item for item in result_data if item[-1] == 1]
        level_2_data = [item for item in result_data if item[-1] == 2]
                
        # Initialize dictionaries to store transformed data for level 1 and level 2
        transformed_data_level_1 = {}
        transformed_data_level_2 = {}

        # Combine data from both level 1 and level 2
        for data in [level_1_data, level_2_data]:
            transformed_data = transformed_data_level_1 if data == level_1_data else transformed_data_level_2
            for item in data:
                subject = item[4]
                question = item[0]
                answer = item[1]
                is_attended = item[2]
                score = item[3]

                # Check if the subject already exists in the transformed_data dictionary
                if subject in transformed_data:
                    transformed_data[subject]['questions'].append({
                        'question': question,
                        'answer': answer,
                        'is_attended': is_attended,
                        'score': score
                    })
                else:
                    transformed_data[subject] = {
                        'subject': subject,
                        'questions': [{
                            'question': question,
                            'answer': answer,
                            'is_attended': is_attended,
                            'score': score
                        }]
                    }

        # Convert the transformed data dictionaries into lists of values
        final_data_level_1 = list(transformed_data_level_1.values())
        final_data_level_2 = list(transformed_data_level_2.values())

        context = {
            'final_data_level_1':final_data_level_1,
            'final_data_level_2' : final_data_level_2
        }
        
        return render(request,'dashboard/resultsdetail.html', context)
    return redirect('logout')


def exam_main_dashboard(request):
    if request.session.get('user_authenticated'):
        id = request.session['username']
        cursor = connection.cursor()
        cursor.execute('EXEC check_valid_id %s', [id])
        user = cursor.fetchone()
        print(user)
        # ip_address = socket.gethostbyname(socket.gethostname())
        # print(ip_address)
        cursor.execute('EXEC get_candidate_data_by_id %s', [user[0]])
        candidate_data = cursor.fetchone()

        print(candidate_data[38])
        print(candidate_data[31])
        if candidate_data[26] == 1:
            if candidate_data[57] == 0 and candidate_data[38] == 0:
                level = 1
            elif (candidate_data[57] == 1 and (candidate_data[38] == 0 or candidate_data[38] == 1) and candidate_data[58] == 'PASS'):
                level = 2
            else:
                return redirect('alert_page_exam')
            cursor = connection.cursor()
            cursor.execute('exec [get_candidate_applied_job_details] %s,%s', [level, candidate_data[31]])
            subjects = cursor.fetchall()
            if subjects == []:
                return redirect('logout')
            print(subjects)
            jobposition = subjects[0][1]
            total_duration = subjects[0][10]
            # print(level,jobposition)

            # Close the cursor after fetching the data
            cursor.close()

            return render(request, "exam_portal/exam_portal_dashboard.html", {'user': user, 'candidate_data': candidate_data, 'subjects': subjects, 'level': level, 'jobposition': jobposition, 'total_duration': total_duration})
        return redirect('alertpage')
    return redirect('logout')

def submission(request):
    if request.session.get('user_authenticated'):
        # request.session.flush()
        # request.session['user_authenticated'] = False  
        level = request.GET.get('level')
        jobPosition = request.GET.get('applied_for')
        user_id = request.GET.get('user')
        print(level, jobPosition, user_id)
        cursor = connection.cursor()
        cursor.execute('exec [save_And_Get_Result] %s,%s,%s', [user_id, jobPosition, level])
        cursor.execute('exec [get_pass_or_fail_candidate] %s,%s,%s', [jobPosition, user_id, level])
        result = cursor.fetchall()
        passorfail = ''
        print(result)
        for i in result:
            if i[4] == 'FAIL':
                passorfail = 'FAIL'
                break
            else:
                passorfail = 'PASS'
        print(passorfail)
        cursor.execute('exec update_tb_candidate_status %s,%s', [user_id, passorfail])

        # Close the cursor after executing the queries
        cursor.close()

        return render(request, 'dashboard/exam_submission.html', {'result': result, 'level': level, 'passorfail': passorfail})
    return redirect('logout')


def submit_answers(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        # Access the form data using the keys of the data dictionary
        print(data)
        for key, value in data.items():
            # Do something with the data here
            # print(value)
            if value != None:
                ans = value
                question_id, subject_id, user_id = key.split('$')
                print(question_id, ans, subject_id, user_id)
                cursor = connection.cursor()
                cursor.execute('exec update_ans_candidate %s,%s,%s,%s', [question_id, ans, subject_id, user_id])
            else:
                ans = 'Null'
                question_id, subject_id, user_id = key.split('$')
                print(question_id, ans, subject_id, user_id)
                cursor = connection.cursor()
                cursor.execute('exec update_ans_candidate %s,%s,%s,%s', [question_id, ans, subject_id, user_id])
            # Close the cursor after executing the queries
            cursor.close()

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'})
    
def introcheckpage(request):
    return render(request,'exam_portal/introcheckpage.html')


def exam_portal(request):
    global is_recording
    if request.session.get('user_authenticated'):
        try:
            level = request.GET.get('level')
            jobPosition = request.GET.get('jobposition')
            total_duration = request.GET.get('total_duration')
            user_id = request.GET.get('user')
            print('level:',level)
            print(jobPosition)
            print(user_id)

            cursor = connection.cursor()
            cursor.execute('exec get_details_for_exams_questions %s,%s',[jobPosition,level])
            subject_list = cursor.fetchall()
            print(subject_list)
            final_quest_list = []
            for details in subject_list:
                # print(details[1],details[0])
                cursor.execute('exec getExamQuestion1 %s,%s,%s,%s',[jobPosition,level,details[1],details[0]])
                x = cursor.fetchall()
                # print("inside table list :  " ,x)
                final_quest_list.extend(x)
            print('final:  ' ,final_quest_list)

            # Start a new thread to run the start_recording function in parallel
            # is_recording = True
            # recording_thread = threading.Thread(target=start_recording, args=(datetime.timedelta(minutes=int(total_duration)),))
            # recording_thread.start()

            cursor = None  # Initialize the cursor variable to None
            try:
                cursor = connection.cursor()
                # cursor.execute('exec getExamQuestion %s,%s', [jobPosition,level])
                # my_list = cursor.fetchall()
                # print(my_list)
                cursor.execute('exec remove_dup_results %s,%s',[user_id,level])
                my_list = final_quest_list
                appliedfor = my_list[0][9]
                for tup in my_list:
                    quest_id, subject_id =  tup[6], tup[7]
                    print(quest_id, subject_id,user_id)
                    cursor.execute('exec insertinto_tb_results %s,%s,%s,%s', [quest_id, subject_id,user_id,level])
                my_dict = {}
                for tup in my_list:
                    key1, key2 = tup[0], tup[1]
                    values = list(tup[2:])

                    if key1 in my_dict:
                        my_dict[key1][key2] = values
                    else:
                        my_dict[key1] = {key2: values}

                print(my_dict)
                return render(request,"exam_portal/exam_portal_1.html",{'questions':my_dict,'total_duration':total_duration,'user_id':user_id,'level':level,'appliedfor':appliedfor})
            finally:
                if cursor:
                    cursor.close()

        except Exception as e:
            print(e)
            return HttpResponseBadRequest("Bad Request")
    return redirect('login')


from azure.storage.blob import BlobServiceClient, PublicAccess

def create_or_get_blob_container(connection_string, container_name):
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    
    # Check if the container already exists
    if blob_service_client.get_container_client(container_name).exists():
        container_client = blob_service_client.get_container_client(container_name)
        print("Blob container already exists.")
    else:
        container_client = blob_service_client.create_container(container_name, public_access="container")
        # container_client = container_client.set_container_access_policy(public_access=PublicAccess.Container)
        print("Blob container created successfully.")
    
    return container_client


import base64
import cv2
import numpy as np
from azure.storage.blob import BlobServiceClient
import datetime

def detect_face(request):
    
    if request.method == 'POST':
        data_url = request.POST.get('image')
        user_id = request.POST.get('user') 
        print(user_id)
        if data_url:
            # Decode the data URL and save the image to a file
            image_data = base64.b64decode(data_url.split(',')[1])
            image = np.frombuffer(image_data, dtype=np.uint8)
            image = cv2.imdecode(image, cv2.IMREAD_COLOR)

            # Provide your Azure Storage connection string and container name
            connection_string = "DefaultEndpointsProtocol=https;AccountName=syscatblob;AccountKey=sNAAF/WQMFwPkSqV4MBGPPGU/n3yu66s2rzelg1UEq9SLW7vXRiOTpbnMN5sO00gzobhyAUPgtoy+AStxg6x2Q==;EndpointSuffix=core.windows.net"
            container_name = user_id

            # Call the function to create or get the blob container
            container_client = create_or_get_blob_container(connection_string, container_name)

            # Perform face detection on the image
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            if len(faces) == 0:
                # No face detected, store as "no_face_<timestamp>.jpg"
                timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
                blob_name = f'no_face_{timestamp}.jpg'
            elif len(faces) > 1:
                # Multiple faces detected, store as "multiple_face_<timestamp>.jpg"
                timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
                blob_name = f'multiple_face_{timestamp}.jpg'
            else:
                # Single face detected, do not store the image
                return JsonResponse({'status': 'success'})

            # Convert the image to bytes
            _, img_encoded = cv2.imencode('.jpg', image)
            img_bytes = img_encoded.tobytes()

            # Upload the image to Azure Blob storage
            container_client.upload_blob(blob_name, img_bytes)

            return JsonResponse({'status': 'success'})

    return JsonResponse({'status': 'error'})


a = {'RDBMS': {'What is a relation in RDBMS?': ['Key', 'Table', 'Row', 'Data Types', 8, 2, 'Table', '2'], 'Which of the following is the full form of RDBMS?': ['Relational Data Management System', 'Relational Database Management System', ' Relative Database Management System', ' Regional Data Management System', 6, 2, 'Relational Database Management System', '2'], 'What is an RDBMS?': ['Database that stores data elements that are not linked.', 'Database that accesses data elements that are not linked.', 'Database that stores and allows access to data elements that are linked.', 'None of the mentioned', 7, 2, 'Database that stores and allows access to data elements that are linked.', '2'], 'Which of the following systems use RDMS?': ['Oracle.', ' Microsoft SQLServer.', 'IBM.', 'All of the mentioned.', 9, 2, 'All of the mentioned.', '2'], 'Which of the following constraints RDBS doesn’t check before creating the tables?': ['Not null.', 'Primary Keys.', 'data Structure', 'Data Integrity', 10, 2, 'data Structure', '2']}, 'python': {' Which of the following is the correct extension of the Python file?': ['python', '.pl', '.py', '.p', 19, 3, '.py', '2'], 'Who developed Python Programming Language?': ['Wick van Rossum', 'Vankata Rama Rao', 'Santosh Yenugula', 'Guido van Rossum', 16, 3, 'Guido van Rossum', '2'], 'All keywords in Python are in _________': ['Capitalized', 'Lower Case', 'UPPER CASE', 'None of the Mentioned', 20, 3, 'None of the Mentioned', '2']}}


def camera_part(request):
    return render(request, 'exam_portal/camera_part.html', {'questions':a})


def import_questions(request):
    if request.session.get('user_authenticated'):
        if request.method == 'POST' and request.FILES['file']:
            uploaded_file = request.FILES['file']
            if uploaded_file:
                # Read the Excel file into a DataFrame
                df = pd.read_excel(uploaded_file)

                # Now, you can work with the DataFrame 'df' as needed
                # For example, you can print it to the console:
                # print(df)
                cursor = connection.cursor()
                cursor.execute('Select * from tb_subject')
                subjectdata = cursor.fetchall()
                
                df['Subject'] = df['Subject'].str.lower()
                subject_mapping = {subject.lower(): subject_id for subject_id, subject, _ in subjectdata}
                print('subject_mapping     :',subject_mapping)
                # Replace values in the DataFrame
                df['Subject'] = df['Subject'].str.strip().map(subject_mapping).astype(str)
                df['level'] = df['level'].astype(str)
                df['typeflag'] = 'E'
                df['FLAG'] = '0'

                print(df)
                column_data_types = df.dtypes

                print(column_data_types)

                # Database connection parameters
                server_name = 'sysportaldbs.database.windows.net'
                database_name = 'OLT_DEV'
                username = 'SysPortalAdmin'
                password = 'spa@Systech2o23'

                # Create a database connection using SQLAlchemy
                db_url = f"mssql+pyodbc://{username}:{password}@{server_name}/{database_name}?driver=ODBC+Driver+17+for+SQL+Server"
                engine = create_engine(db_url)

                # Define the SQL statement for bulk insert
                insert_sql = """
                    INSERT INTO dbo.tb_Question_test (Subject_ID, level_ID, Questions, option1, option2, option3, option4, Answer, typeflag, FLAG)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """

                # Prepare data for bulk insert as a list of tuples
                data_to_insert = [tuple(row) for row in df.values]

                # Create a connection and cursor
                conn = engine.raw_connection()
                cursor = conn.cursor()

                # Execute the bulk insert
                cursor.executemany(insert_sql, data_to_insert)

                # Commit the transaction
                conn.commit()

                # Close the cursor and connection
                cursor.close()
                conn.close()

                # Optionally, close the SQLAlchemy engine
                engine.dispose()
                return render(request, 'dashboard/import_quest.html', {'message': 'File uploaded and processed successfully.'})
            else:
                return render(request, 'dashboard/import_quest.html', {'error_message': 'Please upload a valid Excel file.'})
            
        return render(request, 'dashboard/import_quest.html')
    return redirect('login')


def import_candidates(request):
    if request.session.get('user_authenticated'):
        if request.method == 'POST' and request.FILES['file']:
            uploaded_file = request.FILES['file']
            if uploaded_file:
                # Read the Excel file into a DataFrame
                df = pd.read_excel(uploaded_file)
                print(df)

                current_date_1 = datetime.date.today()
                current_date = datetime.datetime.now()
                date_part = current_date.strftime("%Y%m%d")

                cursor = connection.cursor()
                cursor.execute("SELECT MAX(Username) FROM dbo.tb_Candidate")
                last_id = cursor.fetchone()[0]
                cursor.close()
                

                if last_id:
                    cursor = connection.cursor()
                    # Check if the last entered ID has the same date
                    cursor.execute("SELECT id_date FROM dbo.tb_Candidate WHERE KeyID=%s", [last_id])
                    last_date = cursor.fetchone()[0]
                    cursor.close()

                    if last_date == str(current_date_1):
                        # Check the last entered ID in the database
                        a = int(last_id[-3:].lstrip('0'))

                        # Initialize an incrementing variable
                        increment = a+1
                        # Function to generate key_ID
                        def generate_key_id():
                            nonlocal increment  # Use global instead of nonlocal
                            key_id = date_part + str(increment).zfill(3)
                            increment += 1
                            return key_id

                        # Apply the function to create the key_ID column
                        df['key_ID'] = df.apply(lambda row: generate_key_id(), axis=1)
                    else:
                        # Initialize an incrementing variable
                        new_increment = 1
                        # Function to generate key_ID
                        def generate_key_id():
                            nonlocal new_increment  # Use global instead of nonlocal
                            key_id = date_part + str(new_increment).zfill(3)
                            new_increment += 1
                            return key_id

                        # Apply the function to create the key_ID column
                        df['key_ID'] = df.apply(lambda row: generate_key_id(), axis=1)
                else:
                    # Initialize an incrementing variable
                    new_increment = 1
                    # Function to generate key_ID
                    def generate_key_id():
                        nonlocal new_increment  # Use global instead of nonlocal
                        key_id = date_part + str(new_increment).zfill(3)
                        new_increment += 1
                        return key_id

                    # Apply the function to create the key_ID column
                    df['key_ID'] = df.apply(lambda row: generate_key_id(), axis=1)

                df['id_date'] = current_date_1
                df['Username'] = df['key_ID']
                df['Password'] = df['Phone']
                
                print(df)
                                
                # Database connection parameters
                server_name = 'sysportaldbs.database.windows.net'
                database_name = 'OLT_DEV'
                username = 'SysPortalAdmin'
                password = 'spa@Systech2o23'

                # Create a database connection using SQLAlchemy
                db_url = f"mssql+pyodbc://{username}:{password}@{server_name}/{database_name}?driver=ODBC+Driver+17+for+SQL+Server"
                engine = create_engine(db_url)

                # Define the SQL statement for bulk insert
                insert_sql = """
                    INSERT INTO dbo.tb_Candidate_test (First_Name, Email, Phone, Applied_For, KeyID, id_date, Username, Password)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """

                # Prepare data for bulk insert as a list of tuples
                data_to_insert = [tuple(row) for row in df.values]

                # Create a connection and cursor
                conn = engine.raw_connection()
                cursor = conn.cursor()

                # Execute the bulk insert
                cursor.executemany(insert_sql, data_to_insert)

                # Commit the transaction
                conn.commit()

                # Close the cursor and connection
                cursor.close()
                conn.close()

                # Optionally, close the SQLAlchemy engine
                engine.dispose()
                return render(request, 'dashboard/import_candidates.html', {'message': 'File uploaded and processed successfully.'})
            else:
                return render(request, 'dashboard/import_candidates.html', {'error_message': 'Please upload a valid Excel file.'})
            
        return render(request, 'dashboard/import_candidates.html')
    return redirect('login')



