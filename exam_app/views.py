from django.shortcuts import render, redirect
from .models import *
from django.db import connection
from django.shortcuts import render
from imutils.video import VideoStream
from .models import *
from django.core.mail import EmailMessage
from django.views.decorators import gzip
from django.views.decorators.cache import never_cache
from django.http import HttpResponse,StreamingHttpResponse,JsonResponse,HttpResponseServerError
import cv2
import pycountry
import phonenumbers
import threading
import argparse
import datetime
import pyaudio
import imutils
import wave
import time
import dlib
import os, sys
import base64






# Create your views here.
def sidebar(request):
    return render(request,'base.html')

@never_cache
def dashboard(request):
    if request.session.get('user_authenticated'):
        cursor = connection.cursor()
        cursor.execute('exec get_data_dashboard')
        dash_data = cursor.fetchall()
        cursor.execute('exec get_data_tb_candidate')
        candidate_data = cursor.fetchall()
        return render(request, 'dashboard/dashboard.html',{'dash_data':dash_data,'candidate_data':candidate_data})
    return redirect('logout')

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
    try:
        cursor = connection.cursor()
        cursor.execute('exec Activate_skill_config %s',[id])
        return redirect('/skill_set_config')  
    finally:
        cursor.close()
        
def create_Skill(request):
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
          

def quest_bank(request):
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
    try:
        cursor = connection.cursor()
        cursor.execute('exec get_SearchQuestiondata %s, %s', [sub_id, active_value])
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
    

def add_quest(request):
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

def exam_portal(request):
    if request.session.get('user_authenticated'):
        try:
            cursor = connection.cursor()
            cursor.execute('exec getExamQuestion %s,%s', [2,2])
            my_list = cursor.fetchall()
            print(my_list)
            questions = {}
            i=1
            for tup in my_list:
                key = tup[0]
                values = list(tup[1:])
                values.append(i)
                i = i+1
                if key in questions:
                    questions[key].append(values)
                else:
                    questions[key] = [values]

            print(questions)
            return render(request,"exam_portal/exam_portal.html",{'questions':questions})
        finally:
            cursor.close()

    return redirect('login')
    

def registration(request):
    if request.method == "POST":  
        Applyingfor = request.POST.get('Applyingfor')
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        gender=request.POST.get('gender')
        dob=request.POST.get('dob')
        MaritalStatus=request.POST.get('MaritalStatus')
        countrycode=request.POST.get('country_code')
        Phone=request.POST.get('phone')
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
        print(countrycode)
        print(Phone)      
        try:
            cursor = connection.cursor()
            cursor.execute('exec insertregistrationdata %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' ,[Applyingfor,firstname,lastname,gender,dob,MaritalStatus,Phone,email,CAddress,PAddress,Institution10,CGPA10,YOP10,Institution12,CGPA12,YOP12,Branch12,Graduation,UGCollege,UGDiscipline,CGPAUG,YOPUG,PGraduation,PGDiscipline,PGCollege,CGPAPG,YOPPG,Source,Referredthrough,Applied,Adate,countrycode])
            return redirect('/')
        finally:
            cursor.close()

    countries = []
    for country in pycountry.countries:
        try:
            phone_code = phonenumbers.country_code_for_region(country.alpha_2)
            phone_label = phonenumbers.region_code_for_country_code(phone_code)
            countries.append((country.alpha_2, f"+{phone_code} ({country.name})", phone_label,phone_code))
        except:
            pass    
    context = {'countries': countries}

    return render(request, 'registration/dummy_reg.html',context)

def face_id(request):
    return render(request, 'registration/face.html')
    
def save_image(request):
    if request.method == 'POST':
        print("Hi")
        image_data = request.FILES['image'].read()
        print("Success")
    return HttpResponse


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
                if user[2] == password and user[3] == True:
                    user_name = user[0]
                    request.session['username'] = user_name                    
                    request.session['user_authenticated'] = True                    
                    return redirect('dashboard')
                
                # If the user is valid but password is incorrect                
                elif user[2] == password and user[3] == False:
                    user_name = user[0]
                    request.session['username'] = user_name                    
                    request.session['user_authenticated'] = True                    
                    return redirect('/exam_portal')
                
                # If the user is valid but not yet activated                
                elif user[2] != password:
                    return render(request, 'registration/login.html', {'error': 'Invalid login credentials'})
                
            # If the user is invalid            
            else:
                return render(request, 'registration/login.html', {'error': 'Invalid login credentials'})
        finally:
            cursor.close()
    # Render the login page    
    return render(request, 'registration/login.html')


def logout(request):
    request.session.flush()
    request.session['user_authenticated'] = False    
    return render(request, 'registration/logout.html')

def submission(request):
    request.session.flush()
    request.session['user_authenticated'] = False    
    return render(request, 'dashboard/exam_submission.html')


def capture_image(request):
    # open camera    
    cap = cv2.VideoCapture(0)
    # capture frame    
    ret, frame = cap.read()
    # release camera    
    cap.release()
    # convert frame to bytes    
    _, buffer = cv2.imencode('.jpg', frame)
    image_bytes = buffer.tobytes()
    # render image in template    
    return HttpResponse(image_bytes, content_type='image/jpeg')

def gen():
    """Video streaming generator function."""

    cap = cv2.VideoCapture(0)

    # Detect the coordinates
    detector = dlib.get_frontal_face_detector()
    img_counter = 0

    # Capture frames continuously
    while True:

        # Capture frame-by-frame
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)

        # RGB to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector(gray)

        # Iterator to count faces
        i = 0
        for face in faces:

            # Get the coordinates of faces
            x, y = face.left(), face.top()
            x1, y1 = face.right(), face.bottom()
            cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2)

            # Increment iterator for each face in faces
            i = i+1

            # Display the box and faces
            cv2.putText(frame, ' '+str(i), (x-10, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)    
        
        # if i > 1:
        #     now = datetime.datetime.now()
        #     p = os.path.sep.join(['img', "More than one face detected{}.png".format(str(now).replace(":",''))])
        #     # data.append("More than one face detected.")
        #     cv2.imwrite(p, frame)
        #     img_counter += 1

        # if i == 0:
        #     now = datetime.datetime.now()
        #     p = os.path.sep.join(['img', "No face detected{}.png".format(str(now).replace(":",''))])
        #     # data.append("No face detected.")
        #     cv2.imwrite(p, frame)
        #     img_counter += 1

        frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5) 
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
                  

@gzip.gzip_page
def dynamic_stream(request,stream_path="video"):
    try :
        return StreamingHttpResponse(gen(),content_type="multipart/x-mixed-replace;boundary=frame")
    except :
        return "error"
    







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
    return render(request, 'dashboard/Result.html')


