from django.shortcuts import render, redirect
from .models import *
from django.db import connection
from django.shortcuts import render
from imutils.video import VideoStream
from .models import *
from django.core.mail import EmailMessage
from django.views.decorators import gzip
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import never_cache
from django.http import HttpResponse,StreamingHttpResponse,JsonResponse,HttpResponseServerError,HttpResponseBadRequest
import cv2
import pycountry
import phonenumbers
import asyncio
import threading
import argparse
import datetime
import pyaudio
import imutils
import wave
import time
import pyaudio
import numpy as np
import math
import wave
import datetime
from django.core.paginator import Paginator
# import dlib
import socket
import os, sys
import io
import xlsxwriter
import base64
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Images
from django.core.files.base import ContentFile
import json
from datetime import datetime as dt,timedelta
from datetime import date

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
        worksheet.write(row_num + 1, 0, row_num + 1) # write the S.No        
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
            
            print(skip_level_1,unlock_ids)
            cursor = connection.cursor()
            if unlock_ids:
                for lockid in unlock_ids:
                    cursor.execute('exec unlockCandiadtes %s',[lockid])
            if skip_level_1:
                for skip_level in skip_level_1:
                    cursor.execute('exec skip_level_1_Candiadtes %s',[skip_level])
        if applied_for == None:
            applied_for = 'All'   
        cursor = connection.cursor()
        cursor.execute('exec get_data_dashboard')
        dash_data = cursor.fetchall()
        search_name = request.GET.get('search-bar')
        if search_name == "":
            search_name = None 
        cursor.execute('exec get_data_tb_candidate_av @name=%s,@applied_for=%s,@start_date=%s,@end_date=%s',[search_name,applied_for,start_date,end_date])
        candidate_data = cursor.fetchall()
        # candidate_data = [...]  # Your list of candidate data
        items_per_page = 10  # Number of items to display per page
        page_number = request.GET.get('page')  # Get the requested page number from the URL parameters
        paginator = Paginator(candidate_data, items_per_page)  # Create a paginator object
        page_obj = paginator.get_page(page_number)  
        print(candidate_data)
        cursor.execute('exec get_skill_applied_for_data')
        search_filter = cursor.fetchall()
        return render(request, 'dashboard/dashboard.html',{'dash_data':dash_data,'page_obj': page_obj,'search_filter':search_filter,'start_date':start_date,'end_date':end_date})
    return redirect('logout')

def candidate_dashboard(request):
    if request.session.get('user_authenticated'):
        applied_for = request.GET.get('applied_for')
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        from datetime import date
        today = date.today()
        first_day = date(today.year, today.month, 1)
        if start_date == '' or start_date == None:
            start_date = first_day
        if end_date == '' or end_date == None:
            end_date = today
        if request.method == 'POST':
            unlock_ids = request.POST.getlist('unlocked_ids[]')
            skip_level_1 = request.POST.getlist('skipped_level_1_ids[]')
            
            print(skip_level_1,unlock_ids)
            cursor = connection.cursor()
            if unlock_ids:
                for lockid in unlock_ids:
                    cursor.execute('exec unlockCandiadtes %s',[lockid])
            if skip_level_1:
                for skip_level in skip_level_1:
                    cursor.execute('exec skip_level_1_Candiadtes %s',[skip_level])
        if applied_for == None:
            applied_for = 'All'   
        cursor = connection.cursor()
        cursor.execute('exec get_data_dashboard')
        dash_data = cursor.fetchall()
        search_name = request.GET.get('search-bar')
        if search_name == "":
            search_name = None 

        cursor.execute('exec get_data_tb_candidate_av @name=%s,@applied_for=%s,@start_date=%s,@end_date=%s',[search_name,applied_for,start_date,end_date])
        candidate_data = cursor.fetchall()
        # candidate_data = [...]  # Your list of candidate data
        items_per_page = 5  # Number of items to display per page
        page_number = request.GET.get('page')  # Get the requested page number from the URL parameters
        paginator = Paginator(candidate_data, items_per_page)  # Create a paginator object
        page_obj = paginator.get_page(page_number)  
        print(candidate_data)
        cursor.execute('exec get_skill_applied_for_data')
        search_filter = cursor.fetchall()
        print(start_date)
        print(end_date)
        return render(request, 'dashboard/candidate_dashboard.html',{'dash_data':dash_data,'page_obj': page_obj,'search_filter':search_filter,'start_date':start_date,'end_date':end_date})
    return redirect('logout')

def show_candidate_data(request,id):
    if request.session.get('user_authenticated'):
        cursor = connection.cursor()
        cursor.execute('EXEC get_candidate_data_by_id %s', [id])
        candidate_data = cursor.fetchone()
        jobPosition = candidate_data[31]
        user_id = candidate_data[0]
        cursor.execute('exec [get_pass_or_fail_candidate] %s,%s,%s',[jobPosition,user_id,1])
        result_1 = cursor.fetchall()
        cursor.execute('exec [get_pass_or_fail_candidate] %s,%s,%s',[jobPosition,user_id,2])
        result_2 = cursor.fetchall()

        context = {
            'candidate_data': candidate_data , 'result_1':result_1,'result_2':result_2      }
        return render(request, 'dashboard/candidatedata.html', context)
    return redirect('logout')



def registercandidate(request):
    if request.session.get('user_authenticated'):
        applied_for = request.GET.get('applied_for')
        if applied_for == None:
            applied_for = 'All'        
        cursor = connection.cursor()
        cursor.execute('exec get_skill_applied_for_data')
        search_filter = cursor.fetchall()
        search_name = request.GET.get('search-bar')
        if search_name == "":
            search_name = None        
        cursor.execute('exec get_data_tb_candidate @name=%s,@applied_for=%s',[search_name,applied_for])
        candidate_data = cursor.fetchall()

        context = {
            'candidate_data': candidate_data,
            'search_filter': search_filter        
            }
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
    # try:
        
    #     cursor = connection.cursor()
    #     cursor.execute('exec GetJobposition')
    #     jobs = cursor.fetchall()
    #     return render(request, 'dashboard/job_positions.html',{'jobs':jobs})
    # finally:
    #     cursor.close()
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

def edit_subject(request, id):
    if request.session.get('user_authenticated'):
        if request.method == 'POST':
            subject = request.POST['subject']
            cursor = connection.cursor()
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
                cursor.execute('exec insertSubject %s',[subject])
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
            print(Subject_ID)
            try:
                cursor = connection.cursor()
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
                cursor.execute('exec insertQuestiondata %s,%s,%s,%s,%s,%s,%s,%s',[subject_id,level_id,question,option1,option2,option3,option4,answer])
                return redirect('/quest_bank')  
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


import threading

# def exam_portal(request):
#     if request.session.get('user_authenticated'):
#         try:
#             level = request.GET.get('level')
#             jobPosition = request.GET.get('jobposition')
#             total_duration = request.GET.get('total_duration')
#             user_id = request.GET.get('user')
#             print('level:',level)
#             print(jobPosition)

#             # Start a new thread to run the start_recording function in parallel
#             recording_thread = threading.Thread(target=start_recording, args=(datetime.timedelta(minutes=int(total_duration)),))
#             recording_thread.start()

#             cursor = None  # Initialize the cursor variable to None
#             try:
#                 cursor = connection.cursor()
#                 cursor.execute('exec getExamQuestion %s,%s', [jobPosition,level])
#                 my_list = cursor.fetchall()
#                 print(my_list)
#                 appliedfor = my_list[0][9]
#                 for tup in my_list:
#                     quest_id, subject_id =  tup[6], tup[7]
#                     print(quest_id, subject_id,user_id)
#                     cursor.execute('exec insertinto_tb_results %s,%s,%s,%s', [quest_id, subject_id,user_id,level])
#                 my_dict = {}
#                 for tup in my_list:
#                     key1, key2 = tup[0], tup[1]
#                     values = list(tup[2:])

#                     if key1 in my_dict:
#                         my_dict[key1][key2] = values
#                     else:
#                         my_dict[key1] = {key2: values}

#                 print(my_dict)
#                 return render(request,"exam_portal/exam_portal.html",{'questions':my_dict,'total_duration':total_duration,'user_id':user_id,'level':level,'appliedfor':appliedfor})
#             finally:
#                 if cursor:
#                     cursor.close()

#         except Exception as e:
#             print(e)
#             return HttpResponseBadRequest("Bad Request")
#     return redirect('login')

    

def registration(request):

    cursor = connection.cursor()
    cursor.execute('exec getUGDegree')
    ug = cursor.fetchall()
    cursor.execute('exec getPGDegree')
    pg = cursor.fetchall()
    cursor.execute('exec getBranch')
    branch = cursor.fetchall()
    filter_by=1    
    cursor.execute('exec getPositiondata %s',[filter_by])      
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
       
        try:
            cursor = connection.cursor()
            cursor.execute('exec insertregistrationdata %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' ,[Applyingfor,firstname,lastname,gender,dob,MaritalStatus,phone,email,CAddress,PAddress,Institution10,CGPA10,YOP10,Institution12,CGPA12,YOP12,Branch12,Graduation,UGCollege,UGDiscipline,CGPAUG,YOPUG,PGraduation,PGDiscipline,PGCollege,CGPAPG,YOPPG,Source,Referredthrough,Applied,Adate,countrycode,Id_proof,ID_NO,iddata,facedata])
            return render(request, 'registration/login.html')
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
    return render(request, 'registration/registration_2.html',context)  

    
def save_image(request):
    if request.method == 'POST':
        data_url = request.POST.get('image')
        if data_url:
            # Decode the data URL and save the image to a file
            image_data = base64.b64decode(data_url.split(',')[1])
            now = datetime.datetime.now()
            image_path = 'C:/Users/KJayavel/Downloads/Systech_merged_latest/Systech/exam_app/img/image{}.png'.format(str(now).replace(":",''))  # Replace with the desired image path
            with open(image_path, 'wb') as f:
                f.write(image_data)

            try:
                cursor = connection.cursor()
                cursor.execute('exec saveImage %s', [image_data])
            finally:
                cursor.close()
                return JsonResponse({'status':'success'})
    
    return JsonResponse({'status': 'error'})



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            cursor = connection.cursor()
            cursor.execute('EXEC check_valid_email @username=%s', [username])
            user = cursor.fetchone()

            # If the user was not found by username, try to find by email address     
                   
            if not user:
                cursor.execute('EXEC check_valid_email @email=%s', [username])
                user = cursor.fetchone()
            print(user)
            if user:
                # If the user is valid and password is correct                
                if user[3] == password and user[4] == True:
                    user_name = user[5]
                    email = user[2]
                    request.session['username'] = user_name
                    request.session['email'] = email                  
                    request.session['user_authenticated'] = True                    
                    return redirect('dashboard')
                
                # If the user is valid but password is incorrect                
                elif user[3] == password and user[4] == False:
                    user_name = user[5]
                    email = user[2]
                    request.session['username'] = user_name  
                    request.session['email'] = email                    
                    request.session['user_authenticated'] = True                    
                    return redirect('/exam_main_dashboard')
                
                # If the user is valid but not yet activated                
                elif user[3] != password:
                    return render(request, 'registration/login.html', {'perror': 'Invalid Password'})
                
            # If the user is invalid    
            elif user == None:
                return render(request, 'registration/login.html', {'errors': 'Invalid credentials'})        
            else:
                return render(request, 'registration/login.html', {'error': 'Invalid Email ID'})
        finally:
            cursor.close()
    # Render the login page    
    return render(request, 'registration/login.html')

def exam_main_dashboard(request):
    if request.session.get('user_authenticated'):
        email = request.session['email']
        cursor = connection.cursor()
        cursor.execute('EXEC check_valid_email @email=%s', [email])
        user = cursor.fetchone()
        print(user)
        ip_address = socket.gethostbyname(socket.gethostname())
        print(ip_address)
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
                return HttpResponse('Completed your exam any quries contact HR')
            cursor = connection.cursor()
            cursor.execute('exec [get_candidate_applied_job_details] %s,%s',[level,candidate_data[31]])
            subjects = cursor.fetchall()
            if subjects == []:
                return redirect('logout')
            print(subjects)
            jobposition = subjects[0][1]
            total_duration = subjects[0][10]
            # print(level,jobposition)
            return render(request,"exam_portal/exam_portal_dashboard.html",{'user':user,'candidate_data':candidate_data,'subjects':subjects,'level':level,'jobposition':jobposition,'total_duration':total_duration})
        return redirect('alertpage')
    return redirect('logout')

def alertpage(request):
    return render(request,"exam_portal/alertpage.html")



def logout(request):
    request.session.flush()
    request.session['user_authenticated'] = False    
    return render(request, 'registration/logout.html')


def submission(request):
    if request.session.get('user_authenticated'):
    # request.session.flush()
    # request.session['user_authenticated'] = False  
        level = request.GET.get('level')
        jobPosition = request.GET.get('applied_for')
        user_id = request.GET.get('user')
        print(level,jobPosition,user_id)
        cursor = connection.cursor()
        cursor.execute('exec [save_And_Get_Result] %s,%s,%s',[user_id,jobPosition,level])
        cursor.execute('exec [get_pass_or_fail_candidate] %s,%s,%s',[jobPosition,user_id,level])
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
        cursor.execute('exec update_tb_candidate_status %s,%s',[user_id,passorfail])
        return render(request, 'dashboard/exam_submission.html',{'result':result,'level':level,'passorfail':passorfail})
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
                question_id,subject_id,user_id = key.split('$')
                print(question_id,ans,subject_id,user_id)
                cursor = connection.cursor()
                cursor.execute('exec update_ans_candidate %s,%s,%s,%s',[question_id,ans,subject_id,user_id])
            else:
                ans = 'Null'
                question_id,subject_id,user_id = key.split('$')
                print(question_id,ans,subject_id,user_id)
                cursor = connection.cursor()
                cursor.execute('exec update_ans_candidate %s,%s,%s,%s',[question_id,ans,subject_id,user_id])
            # return redirect('submission')
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'})

# def gen():
#     """Video streaming generator function."""

#     cap = cv2.VideoCapture(0)

#     # Detect the coordinates
#     detector = dlib.get_frontal_face_detector()
#     img_counter = 0

#     # Capture frames continuously
#     while True:

#         # Capture frame-by-frame
#         ret, frame = cap.read()
#         frame = cv2.flip(frame, 1)

#         # RGB to grayscale
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         faces = detector(gray)

#         # Iterator to count faces
#         i = 0
#         for face in faces:

#             # Get the coordinates of faces
#             x, y = face.left(), face.top()
#             x1, y1 = face.right(), face.bottom()
#             cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2)

#             # Increment iterator for each face in faces
#             i = i+1

#             # Display the box and faces
#             cv2.putText(frame, ' '+str(i), (x-10, y-10),
#                         cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)    
        
#         if i > 1:
#             now = datetime.datetime.now()
#             p = os.path.sep.join(['img', "More than one face detected{}.png".format(str(now).replace(":",''))])
#             # data.append("More than one face detected.")
#             cv2.imwrite(p, frame)
#             img_counter += 1

#         if i == 0:
#             now = datetime.datetime.now()
#             p = os.path.sep.join(['img', "No face detected{}.png".format(str(now).replace(":",''))])
#             # data.append("No face detected.")
#             cv2.imwrite(p, frame)
#             img_counter += 1

#         frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5) 
#         ret, buffer = cv2.imencode('.jpg', frame)
#         frame = buffer.tobytes()
#         yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
                  

# Load the Haar Cascade classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

import time

def gen():
    # Open the camera
    cap = cv2.VideoCapture(0)

    # Initialize image counter
    img_counter = 0

    # Initialize the flag for capturing an image
    capture_flag = False

    while True:
        # Read a frame from the camera
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)

        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        # Draw a rectangle around each detected face
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Display the number of faces detected
        cv2.putText(frame, ' ' + str(len(faces)), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        if len(faces) > 1:
            now = datetime.datetime.now()
            p = os.path.sep.join(['img', "More than one face detected{}.png".format(str(now).replace(":",''))])

            # Set the capture flag to True and save the image to the disk
            capture_flag = True
            cv2.imwrite(p, frame)
            img_counter += 1
            # Add a delay of 2 seconds if the capture flag is set to True
            if capture_flag:
                time.sleep(2)
                capture_flag = False

        if len(faces) == 0:
            now = datetime.datetime.now()
            p = os.path.sep.join(['img', "No face detected{}.png".format(str(now).replace(":",''))])

            # Set the capture flag to True and save the image to the disk
            capture_flag = True
            cv2.imwrite(p, frame)
            img_counter += 1
            # Add a delay of 2 seconds if the capture flag is set to True
            if capture_flag:
                time.sleep(2)
                capture_flag = False

        # Resize and encode the frame
        frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        # Yield the frame to the calling function
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

        




@gzip.gzip_page
def dynamic_stream(request,stream_path="video"):
    try :
        return StreamingHttpResponse(gen(),content_type="multipart/x-mixed-replace;boundary=frame")
    except :
        return "error"




@csrf_exempt
def capture(request):
    if request.method == 'POST':
        image = request.POST.get('image')
        # do something with the image
    return render(request, 'registration/camera.html')

@csrf_exempt
def capture_card(request):
    if request.method == 'POST':
        image = request.POST.get('image')
        # do something with the image
    return render(request, 'registration/camera_card.html')


# define function to generate video frames
def video_feed():
    # initialize camera
    camera = cv2.VideoCapture(0)

    while True:
        success, frame = camera.read()
        if not success:
            break
        ret, jpeg = cv2.imencode('.jpg', frame)
        frame = jpeg.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

# decorate video_feed function with gzip compression
@gzip.gzip_page
def video(request):
    return StreamingHttpResponse(video_feed(), content_type='multipart/x-mixed-replace; boundary=frame')


def result(request):
    if request.session.get('user_authenticated'):
        cursor = connection.cursor()
        cursor.execute('exec get_skill_applied_for_data')
        search_filter = cursor.fetchall()
        applied_for = request.GET.get('applied_for')
        filter = request.GET.get('filter_by')
        level = request.GET.get('level')
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        
        if applied_for:
            job_name,job_id  = applied_for.split('|')
        else:
            job_id = 0
            job_name = None
        if job_name == 'ALL':
            job_name = None
        if filter == 'ALL':
            filter = None
        if level == '0':
            level = None
        if start_date == '':
            start_date= None
        if end_date == '':
            end_date = None
        print(job_name)
        print(filter)
        print(level)
        print(start_date)
        print(end_date)
        cursor.execute('exec [view_results_bycandidate] %s,%s,%s,%s,%s',[job_name,level,filter,start_date,end_date])
        user = cursor.fetchall()
        # result_1 = cursor.fetchall()
        # cursor.execute('exec [get_pass_or_fail_candidate] %s,%s,%s',[jobPosition,user_id,2])
        # result_2 = cursor.fetchall()
        return render(request, 'dashboard/Result.html',{'user':user,'search_filter':search_filter,'job_name':job_name,'start_date':start_date,'end_date':end_date})
    return redirect('logout')






############################################AUDIO################################################
# Set chunk size (number of frames per buffer)
CHUNK = 1024

# Set sample format
FORMAT = pyaudio.paInt16

# Set channels
CHANNELS = 1

# Set sample rate
RATE = 44100

is_recording = True

# Create empty list to store audio data
frames = []



# Initialize PyAudio object
p = pyaudio.PyAudio()

# Define a function to start recording
def start_recording(duration):
    # Open input stream
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    
    # Set output filename
    FILENAME = "recording_" + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".wav"

    print("Listening...")

    # Flag to indicate recording
    recording = False

    # Set start time
    start_time = datetime.datetime.now()

    try:
        # Loop through stream and record audio
        while datetime.datetime.now() - start_time < duration and is_recording:
            # Read chunk of audio data
            data = stream.read(CHUNK)

            # Convert data to numpy array
            numpydata = np.frombuffer(data, dtype=np.int16)

            # Calculate root mean square (RMS) of audio chunk
            rms = np.sqrt(np.mean(np.square(numpydata)))

            # Calculate decibel (dB) level
            db = 20 * math.log10(rms)

            # Check if dB level exceeds threshold and start recording
            if db > 30 and not recording:
                print("Sound detected! dB level: ", db)
                recording = True

            # Record audio data if flag is set
            if recording:
                frames.append(data)

            # Stop recording after 5 seconds
            if len(frames) > 0 and len(frames) * CHUNK / RATE >= 5:
                print("Sound stopped. dB level: ", db)
                recording = False

    except KeyboardInterrupt:
        print("Interrupted.")

    # Close stream
    stream.stop_stream()
    stream.close()

    # Save audio data to WAV file if frames are not empty
    if frames:
        wf = wave.open(FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

        print("Recording saved as", FILENAME)
    else:
        print("No recording saved.")

    return FILENAME


def stop_recording():
    global is_recording 
    is_recording= False
    print("Recording stopped.")


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

            # Start a new thread to run the start_recording function in parallel
            is_recording = True
            recording_thread = threading.Thread(target=start_recording, args=(datetime.timedelta(minutes=int(total_duration)),))
            recording_thread.start()

            cursor = None  # Initialize the cursor variable to None
            try:
                cursor = connection.cursor()
                cursor.execute('exec getExamQuestion %s,%s', [jobPosition,level])
                my_list = cursor.fetchall()
                print(my_list)
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

def submission(request):
    global is_recording
    # request.session.flush()
    # request.session['user_authenticated'] = False  
    stop_recording()
    level = request.GET.get('level')
    jobPosition = request.GET.get('applied_for')
    user_id = request.GET.get('user')
    print(level,jobPosition,user_id)
    cursor = connection.cursor()
    cursor.execute('exec [save_And_Get_Result] %s,%s,%s',[user_id,jobPosition,level])
    cursor.execute('exec [get_pass_or_fail_candidate] %s,%s,%s',[jobPosition,user_id,level])
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
    cursor.execute('exec update_tb_candidate_status %s,%s',[user_id,passorfail])
    return render(request, 'dashboard/exam_submission.html',{'result':result,'level':level,'passorfail':passorfail})
