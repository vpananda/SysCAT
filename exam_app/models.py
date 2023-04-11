# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


# class Attendedquestion(models.Model):
#     candidate_id = models.IntegerField(db_column='Candidate_ID', blank=True, null=True)  # Field name made lowercase.
#     level1_tab1 = models.IntegerField(db_column='Level1_Tab1', blank=True, null=True)  # Field name made lowercase.
#     level1_tab2 = models.IntegerField(db_column='Level1_Tab2', blank=True, null=True)  # Field name made lowercase.
#     level2_tab1 = models.IntegerField(db_column='Level2_Tab1', blank=True, null=True)  # Field name made lowercase.
#     level2_tab2 = models.IntegerField(db_column='Level2_tab2', blank=True, null=True)  # Field name made lowercase.
#     level2_tab3 = models.IntegerField(db_column='Level2_tab3', blank=True, null=True)  # Field name made lowercase.
#     level2_tab4 = models.IntegerField(db_column='Level2_Tab4', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'AttendedQuestion'


# class EmailContent(models.Model):
#     keyid = models.AutoField(db_column='keyID', primary_key=True)  # Field name made lowercase.
#     subject = models.CharField(max_length=500, blank=True, null=True)
#     body = models.TextField(db_column='Body', blank=True, null=True)  # Field name made lowercase.
#     result_status = models.CharField(db_column='Result_status', max_length=200, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'Email_Content'


# class EmailAdmin(models.Model):
#     keyid = models.AutoField(db_column='keyID', primary_key=True)  # Field name made lowercase.
#     username = models.CharField(db_column='UserName', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     email_id = models.CharField(db_column='Email_ID', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     password = models.CharField(db_column='Password', max_length=100, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'Email_admin'


# class Messages(models.Model):
#     messageid = models.IntegerField(db_column='MessageID', blank=True, null=True)  # Field name made lowercase.
#     message = models.CharField(db_column='Message', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     emptymessage = models.CharField(db_column='EmptyMessage', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'Messages'


# class ResultHistory(models.Model):
#     candidate_id = models.IntegerField(db_column='CANDIDATE_ID', blank=True, null=True)  # Field name made lowercase.
#     question_id = models.IntegerField(db_column='QUESTION_ID', blank=True, null=True)  # Field name made lowercase.
#     answer = models.TextField(db_column='ANSWER', blank=True, null=True)  # Field name made lowercase.
#     score = models.IntegerField(db_column='SCORE', blank=True, null=True)  # Field name made lowercase.
#     subject_id = models.IntegerField(db_column='SUBJECT_ID', blank=True, null=True)  # Field name made lowercase.
#     isattended = models.IntegerField(db_column='ISATTENDED', blank=True, null=True)  # Field name made lowercase.
#     level = models.IntegerField(db_column='LEVEL', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'RESULT_HISTORY'


# class AuthGroup(models.Model):
#     name = models.CharField(unique=True, max_length=150)

#     class Meta:
#         managed = False
#         db_table = 'auth_group'


# class AuthGroupPermissions(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#     permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_group_permissions'
#         unique_together = (('group', 'permission'),)


# class AuthPermission(models.Model):
#     name = models.CharField(max_length=255)
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
#     codename = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'auth_permission'
#         unique_together = (('content_type', 'codename'),)


# class AuthUser(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.BooleanField()
#     username = models.CharField(unique=True, max_length=150)
#     first_name = models.CharField(max_length=150)
#     last_name = models.CharField(max_length=150)
#     email = models.CharField(max_length=254)
#     is_staff = models.BooleanField()
#     is_active = models.BooleanField()
#     date_joined = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'auth_user'


# class AuthUserGroups(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_user_groups'
#         unique_together = (('user', 'group'),)


# class AuthUserUserPermissions(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_user_user_permissions'
#         unique_together = (('user', 'permission'),)


# class DjangoAdminLog(models.Model):
#     action_time = models.DateTimeField()
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.SmallIntegerField()
#     change_message = models.TextField()
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'django_admin_log'


# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)


# class DjangoMigrations(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'django_migrations'


# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'django_session'


class Images(models.Model):
    data = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'images'


# class QuestionsLoad(models.Model):
#     keyid = models.AutoField(db_column='KeyID', primary_key=True)  # Field name made lowercase.
#     subject_id = models.IntegerField(db_column='Subject_ID', blank=True, null=True)  # Field name made lowercase.
#     level_id = models.IntegerField(db_column='Level_ID', blank=True, null=True)  # Field name made lowercase.
#     questions = models.TextField(db_column='Questions', blank=True, null=True)  # Field name made lowercase.
#     option1 = models.TextField(db_column='Option1', blank=True, null=True)  # Field name made lowercase.
#     option2 = models.TextField(db_column='Option2', blank=True, null=True)  # Field name made lowercase.
#     option3 = models.TextField(db_column='Option3', blank=True, null=True)  # Field name made lowercase.
#     option4 = models.TextField(db_column='Option4', blank=True, null=True)  # Field name made lowercase.
#     answer = models.TextField(db_column='Answer', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'questions_load'


# class Sysdiagrams(models.Model):
#     name = models.CharField(max_length=128)
#     principal_id = models.IntegerField()
#     diagram_id = models.AutoField(primary_key=True)
#     version = models.IntegerField(blank=True, null=True)
#     definition = models.BinaryField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'sysdiagrams'
#         unique_together = (('principal_id', 'name'),)


# class TbCandidate(models.Model):
#     keyid = models.AutoField(db_column='KeyID', primary_key=True)  # Field name made lowercase.
#     first_name = models.CharField(db_column='First_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     last_name = models.CharField(db_column='Last_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     dob = models.DateField(db_column='DOB', blank=True, null=True)  # Field name made lowercase.
#     gender = models.CharField(db_column='Gender', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     phone = models.CharField(db_column='Phone', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     temp_address = models.CharField(db_column='Temp_Address', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     perm_address = models.CharField(db_column='Perm_Address', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     marietal_status = models.CharField(db_column='Marietal_Status', max_length=3, blank=True, null=True)  # Field name made lowercase.
#     ug_degree = models.CharField(db_column='UG_Degree', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     ug_college = models.CharField(db_column='UG_College', max_length=450, blank=True, null=True)  # Field name made lowercase.
#     ug_yearofpassing = models.IntegerField(db_column='UG_Yearofpassing', blank=True, null=True)  # Field name made lowercase.
#     ug_grade = models.CharField(db_column='UG_Grade', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     pg_degree = models.CharField(db_column='PG_Degree', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     pg_college = models.CharField(db_column='PG_College', max_length=450, blank=True, null=True)  # Field name made lowercase.
#     pg_yearofpassing = models.IntegerField(db_column='PG_Yearofpassing', blank=True, null=True)  # Field name made lowercase.
#     pg_grade = models.CharField(db_column='PG_Grade', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     referalby = models.CharField(db_column='ReferalBY', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     source = models.CharField(db_column='Source', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     isbondaccepted = models.IntegerField(db_column='IsBondAccepted', blank=True, null=True)  # Field name made lowercase.
#     isattendedpreviously = models.IntegerField(db_column='IsAttendedPreviously', blank=True, null=True)  # Field name made lowercase.
#     createddate = models.DateTimeField(db_column='Createddate', blank=True, null=True)  # Field name made lowercase.
#     systemip = models.CharField(db_column='SystemIP', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     username = models.CharField(db_column='Username', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     password = models.CharField(db_column='Password', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     islocked = models.IntegerField(db_column='Islocked', blank=True, null=True)  # Field name made lowercase.
#     loggedintime = models.DateTimeField(db_column='LoggedinTime', blank=True, null=True)  # Field name made lowercase.
#     loggedouttime = models.DateTimeField(db_column='LoggedOutTime', blank=True, null=True)  # Field name made lowercase.
#     isautologgedout = models.IntegerField(db_column='IsAutologgedout', blank=True, null=True)  # Field name made lowercase.
#     lastsavedtime = models.DateTimeField(db_column='LastSavedTime', blank=True, null=True)  # Field name made lowercase.
#     applied_for = models.CharField(db_column='Applied_For', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     flag = models.IntegerField(db_column='Flag', blank=True, null=True)  # Field name made lowercase.
#     diploma_degree = models.CharField(db_column='DIPLOMA_Degree', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     diploma_college = models.CharField(db_column='DIPLOMA_College', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     diploma_yearofpassing = models.IntegerField(db_column='DIPLOMA_Yearofpassing', blank=True, null=True)  # Field name made lowercase.
#     diploma_grade = models.CharField(db_column='DIPLOMA_Grade', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     lad = models.DateTimeField(db_column='LAD', blank=True, null=True)  # Field name made lowercase.
#     islevel1_skiiped = models.IntegerField(db_column='IsLevel1_Skiiped', blank=True, null=True)  # Field name made lowercase.
#     tenth_institution = models.CharField(db_column='Tenth_Institution', max_length=450, blank=True, null=True)  # Field name made lowercase.
#     tenth_percentage = models.CharField(db_column='Tenth_Percentage', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     tenth_yop = models.IntegerField(db_column='Tenth_YOP', blank=True, null=True)  # Field name made lowercase.
#     ug_department = models.CharField(db_column='UG_Department', max_length=70, blank=True, null=True)  # Field name made lowercase.
#     ug_discipline = models.CharField(db_column='UG_Discipline', max_length=70, blank=True, null=True)  # Field name made lowercase.
#     pg_department = models.CharField(db_column='PG_Department', max_length=70, blank=True, null=True)  # Field name made lowercase.
#     pg_descipline = models.CharField(db_column='PG_DESCIPLINE', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     mail_status = models.IntegerField(db_column='Mail_status', blank=True, null=True)  # Field name made lowercase.
#     islogged = models.IntegerField(db_column='Islogged', blank=True, null=True)  # Field name made lowercase.
#     isadmin = models.BooleanField(db_column='isAdmin', blank=True, null=True)  # Field name made lowercase.
#     country_code = models.CharField(db_column='Country_code', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     id_proof = models.CharField(db_column='Id_proof', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     id_no = models.CharField(db_column='ID_NO', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     id_image = models.TextField(db_column='ID_Image', blank=True, null=True)  # Field name made lowercase.
#     profile_image = models.TextField(db_column='Profile_Image', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'tb_Candidate'


# class TbJobposition(models.Model):
#     key_id = models.AutoField(db_column='Key_ID', primary_key=True)  # Field name made lowercase.
#     job_position = models.CharField(db_column='Job_Position', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     isoptionrequired = models.BooleanField(db_column='IsoptionRequired', blank=True, null=True)  # Field name made lowercase.
#     isbondrequired = models.BooleanField(db_column='IsBondRequired', blank=True, null=True)  # Field name made lowercase.
#     flag = models.BooleanField(db_column='FLAG', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'tb_JobPosition'


# class TbLevel(models.Model):
#     keyid = models.AutoField(db_column='KeyID')  # Field name made lowercase.
#     level_name = models.CharField(db_column='Level_Name', max_length=100, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'tb_Level'


# class TbQuestion(models.Model):
#     keyid = models.AutoField(db_column='KeyID', primary_key=True)  # Field name made lowercase.
#     subject_id = models.IntegerField(db_column='Subject_ID', blank=True, null=True)  # Field name made lowercase.
#     level_id = models.IntegerField(db_column='Level_ID', blank=True, null=True)  # Field name made lowercase.
#     questions = models.TextField(db_column='Questions', blank=True, null=True)  # Field name made lowercase.
#     option1 = models.CharField(db_column='Option1', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     option2 = models.CharField(db_column='Option2', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     option3 = models.CharField(db_column='Option3', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     option4 = models.CharField(db_column='Option4', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     answer = models.CharField(db_column='Answer', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     typeflag = models.CharField(max_length=2, blank=True, null=True)
#     flag = models.BooleanField(db_column='FLAG', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'tb_Question'


# class TbResult(models.Model):
#     keyid = models.AutoField(db_column='KeyID', primary_key=True)  # Field name made lowercase.
#     candidate_id = models.IntegerField(db_column='Candidate_id', blank=True, null=True)  # Field name made lowercase.
#     question = models.ForeignKey(TbQuestion, models.DO_NOTHING, db_column='Question_ID', blank=True, null=True)  # Field name made lowercase.
#     answer = models.TextField(db_column='Answer', blank=True, null=True)  # Field name made lowercase.
#     score = models.IntegerField(blank=True, null=True)
#     subject_id = models.IntegerField(db_column='Subject_ID', blank=True, null=True)  # Field name made lowercase.
#     isattended = models.IntegerField(blank=True, null=True)
#     createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'tb_Result'


# class TbResultView(models.Model):
#     jobid = models.IntegerField(db_column='JobID', blank=True, null=True)  # Field name made lowercase.
#     jobposition = models.CharField(db_column='JobPosition', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     candidateid = models.IntegerField(db_column='CandidateID', blank=True, null=True)  # Field name made lowercase.
#     candidatename = models.CharField(db_column='CandidateName', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     examdate = models.CharField(db_column='ExamDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     logggedindate = models.DateTimeField(db_column='LogggedinDate', blank=True, null=True)  # Field name made lowercase.
#     subject = models.CharField(db_column='Subject', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     testlevel = models.IntegerField(db_column='TestLevel', blank=True, null=True)  # Field name made lowercase.
#     score = models.IntegerField(db_column='Score', blank=True, null=True)  # Field name made lowercase.
#     teststatus = models.CharField(db_column='TestStatus', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     levelsubject = models.CharField(db_column='LevelSubject', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     level1result = models.CharField(db_column='Level1Result', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     level2result = models.CharField(db_column='Level2Result', max_length=100, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'tb_Result_View'


# class TbSubject(models.Model):
#     keyid = models.AutoField(db_column='KeyID')  # Field name made lowercase.
#     subject = models.CharField(db_column='Subject', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     flag = models.BooleanField(db_column='Flag', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'tb_Subject'


# class TbSubjectlevel(models.Model):
#     keyid = models.AutoField(db_column='KeyID', primary_key=True)  # Field name made lowercase.
#     appliedfor = models.CharField(db_column='AppliedFor', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     subject_id = models.IntegerField(db_column='Subject_ID', blank=True, null=True)  # Field name made lowercase.
#     level = models.IntegerField(db_column='Level', blank=True, null=True)  # Field name made lowercase.
#     no_of_question = models.IntegerField(db_column='No_of_Question', blank=True, null=True)  # Field name made lowercase.
#     cutoffmarks = models.IntegerField(db_column='CutOffMarks', blank=True, null=True)  # Field name made lowercase.
#     duration = models.IntegerField(db_column='Duration', blank=True, null=True)  # Field name made lowercase.
#     ismandatory = models.IntegerField(db_column='IsMandatory', blank=True, null=True)  # Field name made lowercase.
#     optionalgroupname = models.CharField(db_column='OptionalGroupName', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     flag = models.BooleanField(db_column='FLAG', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'tb_SubjectLevel'


# class TbSubjectResult(models.Model):
#     keyid = models.AutoField(db_column='KeyID', primary_key=True)  # Field name made lowercase.
#     candidate_id = models.IntegerField(db_column='Candidate_id', blank=True, null=True)  # Field name made lowercase.
#     level = models.IntegerField(db_column='Level', blank=True, null=True)  # Field name made lowercase.
#     score = models.IntegerField(blank=True, null=True)
#     status = models.CharField(max_length=20, blank=True, null=True)
#     subject_id = models.IntegerField(db_column='subject_ID', blank=True, null=True)  # Field name made lowercase.
#     createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'tb_Subject_Result'


# class TbBackupcnandidate(models.Model):
#     keyid = models.AutoField(db_column='KeyID')  # Field name made lowercase.
#     first_name = models.CharField(db_column='First_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     last_name = models.CharField(db_column='Last_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     dob = models.DateField(db_column='DOB', blank=True, null=True)  # Field name made lowercase.
#     gender = models.CharField(db_column='Gender', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     phone = models.CharField(db_column='Phone', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     temp_address = models.CharField(db_column='Temp_Address', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     perm_address = models.CharField(db_column='Perm_Address', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     marietal_status = models.CharField(db_column='Marietal_Status', max_length=3, blank=True, null=True)  # Field name made lowercase.
#     ug_degree = models.CharField(db_column='UG_Degree', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     ug_college = models.CharField(db_column='UG_College', max_length=450, blank=True, null=True)  # Field name made lowercase.
#     ug_yearofpassing = models.IntegerField(db_column='UG_Yearofpassing', blank=True, null=True)  # Field name made lowercase.
#     ug_grade = models.CharField(db_column='UG_Grade', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     pg_degree = models.CharField(db_column='PG_Degree', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     pg_college = models.CharField(db_column='PG_College', max_length=450, blank=True, null=True)  # Field name made lowercase.
#     pg_yearofpassing = models.IntegerField(db_column='PG_Yearofpassing', blank=True, null=True)  # Field name made lowercase.
#     pg_grade = models.CharField(db_column='PG_Grade', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     referalby = models.CharField(db_column='ReferalBY', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     source = models.CharField(db_column='Source', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     isbondaccepted = models.IntegerField(db_column='IsBondAccepted', blank=True, null=True)  # Field name made lowercase.
#     isattendedpreviously = models.IntegerField(db_column='IsAttendedPreviously', blank=True, null=True)  # Field name made lowercase.
#     createddate = models.DateTimeField(db_column='Createddate', blank=True, null=True)  # Field name made lowercase.
#     systemip = models.CharField(db_column='SystemIP', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     username = models.CharField(db_column='Username', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     password = models.CharField(db_column='Password', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     islocked = models.IntegerField(db_column='Islocked', blank=True, null=True)  # Field name made lowercase.
#     loggedintime = models.DateTimeField(db_column='LoggedinTime', blank=True, null=True)  # Field name made lowercase.
#     loggedouttime = models.DateTimeField(db_column='LoggedOutTime', blank=True, null=True)  # Field name made lowercase.
#     isautologgedout = models.IntegerField(db_column='IsAutologgedout', blank=True, null=True)  # Field name made lowercase.
#     lastsavedtime = models.DateTimeField(db_column='LastSavedTime', blank=True, null=True)  # Field name made lowercase.
#     applied_for = models.CharField(db_column='Applied_For', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
#     diploma_degree = models.CharField(db_column='DIPLOMA_Degree', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     diploma_college = models.CharField(db_column='DIPLOMA_College', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     diploma_yearofpassing = models.IntegerField(db_column='DIPLOMA_Yearofpassing', blank=True, null=True)  # Field name made lowercase.
#     diploma_grade = models.CharField(db_column='DIPLOMA_Grade', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     lad = models.DateTimeField(db_column='LAD', blank=True, null=True)  # Field name made lowercase.
#     islevel1_skiiped = models.IntegerField(db_column='IsLevel1_Skiiped', blank=True, null=True)  # Field name made lowercase.
#     tenth_institution = models.CharField(db_column='Tenth_Institution', max_length=450, blank=True, null=True)  # Field name made lowercase.
#     tenth_percentage = models.CharField(db_column='Tenth_Percentage', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     tenth_yop = models.IntegerField(db_column='Tenth_YOP', blank=True, null=True)  # Field name made lowercase.
#     ug_department = models.CharField(db_column='UG_Department', max_length=70, blank=True, null=True)  # Field name made lowercase.
#     ug_discipline = models.CharField(db_column='UG_Discipline', max_length=70, blank=True, null=True)  # Field name made lowercase.
#     pg_department = models.CharField(db_column='PG_Department', max_length=70, blank=True, null=True)  # Field name made lowercase.
#     pg_descipline = models.CharField(db_column='PG_DESCIPLINE', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     mail_status = models.IntegerField(db_column='Mail_status', blank=True, null=True)  # Field name made lowercase.
#     islogged = models.IntegerField(db_column='Islogged', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'tb_backupcnandidate'


# class TbCandidate01062020(models.Model):
#     keyid = models.AutoField(db_column='KeyID')  # Field name made lowercase.
#     first_name = models.CharField(db_column='First_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     last_name = models.CharField(db_column='Last_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     dob = models.DateField(db_column='DOB', blank=True, null=True)  # Field name made lowercase.
#     gender = models.CharField(db_column='Gender', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     phone = models.CharField(db_column='Phone', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     temp_address = models.CharField(db_column='Temp_Address', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     perm_address = models.CharField(db_column='Perm_Address', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     marietal_status = models.CharField(db_column='Marietal_Status', max_length=3, blank=True, null=True)  # Field name made lowercase.
#     ug_degree = models.CharField(db_column='UG_Degree', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     ug_college = models.CharField(db_column='UG_College', max_length=450, blank=True, null=True)  # Field name made lowercase.
#     ug_yearofpassing = models.IntegerField(db_column='UG_Yearofpassing', blank=True, null=True)  # Field name made lowercase.
#     ug_grade = models.CharField(db_column='UG_Grade', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     pg_degree = models.CharField(db_column='PG_Degree', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     pg_college = models.CharField(db_column='PG_College', max_length=450, blank=True, null=True)  # Field name made lowercase.
#     pg_yearofpassing = models.IntegerField(db_column='PG_Yearofpassing', blank=True, null=True)  # Field name made lowercase.
#     pg_grade = models.CharField(db_column='PG_Grade', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     referalby = models.CharField(db_column='ReferalBY', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     source = models.CharField(db_column='Source', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     isbondaccepted = models.IntegerField(db_column='IsBondAccepted', blank=True, null=True)  # Field name made lowercase.
#     isattendedpreviously = models.IntegerField(db_column='IsAttendedPreviously', blank=True, null=True)  # Field name made lowercase.
#     createddate = models.DateTimeField(db_column='Createddate', blank=True, null=True)  # Field name made lowercase.
#     systemip = models.CharField(db_column='SystemIP', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     username = models.CharField(db_column='Username', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     password = models.CharField(db_column='Password', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     islocked = models.IntegerField(db_column='Islocked', blank=True, null=True)  # Field name made lowercase.
#     loggedintime = models.DateTimeField(db_column='LoggedinTime', blank=True, null=True)  # Field name made lowercase.
#     loggedouttime = models.DateTimeField(db_column='LoggedOutTime', blank=True, null=True)  # Field name made lowercase.
#     isautologgedout = models.IntegerField(db_column='IsAutologgedout', blank=True, null=True)  # Field name made lowercase.
#     lastsavedtime = models.DateTimeField(db_column='LastSavedTime', blank=True, null=True)  # Field name made lowercase.
#     applied_for = models.CharField(db_column='Applied_For', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
#     diploma_degree = models.CharField(db_column='DIPLOMA_Degree', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     diploma_college = models.CharField(db_column='DIPLOMA_College', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     diploma_yearofpassing = models.IntegerField(db_column='DIPLOMA_Yearofpassing', blank=True, null=True)  # Field name made lowercase.
#     diploma_grade = models.CharField(db_column='DIPLOMA_Grade', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     lad = models.DateTimeField(db_column='LAD', blank=True, null=True)  # Field name made lowercase.
#     islevel1_skiiped = models.IntegerField(db_column='IsLevel1_Skiiped', blank=True, null=True)  # Field name made lowercase.
#     tenth_institution = models.CharField(db_column='Tenth_Institution', max_length=450, blank=True, null=True)  # Field name made lowercase.
#     tenth_percentage = models.CharField(db_column='Tenth_Percentage', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     tenth_yop = models.IntegerField(db_column='Tenth_YOP', blank=True, null=True)  # Field name made lowercase.
#     ug_department = models.CharField(db_column='UG_Department', max_length=70, blank=True, null=True)  # Field name made lowercase.
#     ug_discipline = models.CharField(db_column='UG_Discipline', max_length=70, blank=True, null=True)  # Field name made lowercase.
#     pg_department = models.CharField(db_column='PG_Department', max_length=70, blank=True, null=True)  # Field name made lowercase.
#     pg_descipline = models.CharField(db_column='PG_DESCIPLINE', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     mail_status = models.IntegerField(db_column='Mail_status', blank=True, null=True)  # Field name made lowercase.
#     islogged = models.IntegerField(db_column='Islogged', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'tb_candidate_01062020'


# class TbCandidateBkp(models.Model):
#     keyid = models.AutoField(db_column='KeyID')  # Field name made lowercase.
#     first_name = models.CharField(db_column='First_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     last_name = models.CharField(db_column='Last_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     dob = models.DateTimeField(db_column='DOB', blank=True, null=True)  # Field name made lowercase.
#     gender = models.CharField(db_column='Gender', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     phone = models.CharField(db_column='Phone', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     temp_address = models.CharField(db_column='Temp_Address', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     perm_address = models.CharField(db_column='Perm_Address', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     marietal_status = models.CharField(db_column='Marietal_Status', max_length=3, blank=True, null=True)  # Field name made lowercase.
#     ug_degree = models.CharField(db_column='UG_Degree', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     ug_college = models.CharField(db_column='UG_College', max_length=450, blank=True, null=True)  # Field name made lowercase.
#     ug_yearofpassing = models.IntegerField(db_column='UG_Yearofpassing', blank=True, null=True)  # Field name made lowercase.
#     ug_grade = models.CharField(db_column='UG_Grade', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     pg_degree = models.CharField(db_column='PG_Degree', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     pg_college = models.CharField(db_column='PG_College', max_length=450, blank=True, null=True)  # Field name made lowercase.
#     pg_yearofpassing = models.IntegerField(db_column='PG_Yearofpassing', blank=True, null=True)  # Field name made lowercase.
#     pg_grade = models.CharField(db_column='PG_Grade', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     referalby = models.CharField(db_column='ReferalBY', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     source = models.CharField(db_column='Source', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     isbondaccepted = models.IntegerField(db_column='IsBondAccepted', blank=True, null=True)  # Field name made lowercase.
#     isattendedpreviously = models.IntegerField(db_column='IsAttendedPreviously', blank=True, null=True)  # Field name made lowercase.
#     createddate = models.DateTimeField(db_column='Createddate', blank=True, null=True)  # Field name made lowercase.
#     systemip = models.CharField(db_column='SystemIP', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     username = models.CharField(db_column='Username', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     password = models.CharField(db_column='Password', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     islocked = models.IntegerField(db_column='Islocked', blank=True, null=True)  # Field name made lowercase.
#     loggedintime = models.DateTimeField(db_column='LoggedinTime', blank=True, null=True)  # Field name made lowercase.
#     loggedouttime = models.DateTimeField(db_column='LoggedOutTime', blank=True, null=True)  # Field name made lowercase.
#     isautologgedout = models.IntegerField(db_column='IsAutologgedout', blank=True, null=True)  # Field name made lowercase.
#     lastsavedtime = models.DateTimeField(db_column='LastSavedTime', blank=True, null=True)  # Field name made lowercase.
#     applied_for = models.CharField(db_column='Applied_For', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
#     diploma_degree = models.CharField(db_column='DIPLOMA_Degree', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     diploma_college = models.CharField(db_column='DIPLOMA_College', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     diploma_yearofpassing = models.IntegerField(db_column='DIPLOMA_Yearofpassing', blank=True, null=True)  # Field name made lowercase.
#     diploma_grade = models.CharField(db_column='DIPLOMA_Grade', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     lad = models.DateTimeField(db_column='LAD', blank=True, null=True)  # Field name made lowercase.
#     islevel1_skiiped = models.IntegerField(db_column='IsLevel1_Skiiped', blank=True, null=True)  # Field name made lowercase.
#     tenth_institution = models.CharField(db_column='Tenth_Institution', max_length=450, blank=True, null=True)  # Field name made lowercase.
#     tenth_percentage = models.CharField(db_column='Tenth_Percentage', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     tenth_yop = models.IntegerField(db_column='Tenth_YOP', blank=True, null=True)  # Field name made lowercase.
#     ug_department = models.CharField(db_column='UG_Department', max_length=70, blank=True, null=True)  # Field name made lowercase.
#     ug_discipline = models.CharField(db_column='UG_Discipline', max_length=70, blank=True, null=True)  # Field name made lowercase.
#     pg_department = models.CharField(db_column='PG_Department', max_length=70, blank=True, null=True)  # Field name made lowercase.
#     pg_descipline = models.CharField(db_column='PG_DESCIPLINE', max_length=50, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'tb_candidate_bkp'


# class TbDiscipline(models.Model):
#     key_id = models.AutoField(db_column='Key_ID', primary_key=True)  # Field name made lowercase.
#     branch = models.CharField(max_length=100, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'tb_discipline'


# class TbEmailResult(models.Model):
#     keyid = models.AutoField(db_column='KeyID', primary_key=True)  # Field name made lowercase.
#     result = models.CharField(db_column='Result', max_length=40, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'tb_email_result'


# class TbGraduation(models.Model):
#     key_id = models.AutoField(db_column='Key_ID', primary_key=True)  # Field name made lowercase.
#     degree = models.CharField(max_length=100, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'tb_graduation'


# class TbQuestionBk29062021(models.Model):
#     keyid = models.AutoField(db_column='KeyID')  # Field name made lowercase.
#     subject_id = models.IntegerField(db_column='Subject_ID', blank=True, null=True)  # Field name made lowercase.
#     level_id = models.IntegerField(db_column='Level_ID', blank=True, null=True)  # Field name made lowercase.
#     questions = models.TextField(db_column='Questions', blank=True, null=True)  # Field name made lowercase.
#     option1 = models.CharField(db_column='Option1', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     option2 = models.CharField(db_column='Option2', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     option3 = models.CharField(db_column='Option3', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     option4 = models.CharField(db_column='Option4', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     answer = models.CharField(db_column='Answer', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     typeflag = models.CharField(max_length=2, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'tb_question_bk_29062021'


# class TbResult02202020(models.Model):
#     keyid = models.AutoField(db_column='KeyID')  # Field name made lowercase.
#     candidate_id = models.IntegerField(db_column='Candidate_id', blank=True, null=True)  # Field name made lowercase.
#     question_id = models.IntegerField(db_column='Question_ID', blank=True, null=True)  # Field name made lowercase.
#     answer = models.TextField(db_column='Answer', blank=True, null=True)  # Field name made lowercase.
#     score = models.IntegerField(blank=True, null=True)
#     subject_id = models.IntegerField(db_column='Subject_ID', blank=True, null=True)  # Field name made lowercase.
#     isattended = models.IntegerField(blank=True, null=True)
#     createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'tb_result_02202020'


# class TbResultBk03252020(models.Model):
#     keyid = models.AutoField(db_column='KeyID')  # Field name made lowercase.
#     candidate_id = models.IntegerField(db_column='Candidate_id', blank=True, null=True)  # Field name made lowercase.
#     question_id = models.IntegerField(db_column='Question_ID', blank=True, null=True)  # Field name made lowercase.
#     answer = models.TextField(db_column='Answer', blank=True, null=True)  # Field name made lowercase.
#     score = models.IntegerField(blank=True, null=True)
#     subject_id = models.IntegerField(db_column='Subject_ID', blank=True, null=True)  # Field name made lowercase.
#     isattended = models.IntegerField(blank=True, null=True)
#     createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'tb_result_bk_03252020'


# class TbResultNew(models.Model):
#     keyid = models.AutoField(db_column='KeyID')  # Field name made lowercase.
#     candidate_id = models.IntegerField(db_column='Candidate_id', blank=True, null=True)  # Field name made lowercase.
#     question_id = models.IntegerField(db_column='Question_ID', blank=True, null=True)  # Field name made lowercase.
#     answer = models.TextField(db_column='Answer', blank=True, null=True)  # Field name made lowercase.
#     score = models.IntegerField(blank=True, null=True)
#     subject_id = models.IntegerField(db_column='Subject_ID', blank=True, null=True)  # Field name made lowercase.
#     isattended = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'tb_result_new'


# class TbSubjectResult03022020(models.Model):
#     keyid = models.AutoField(db_column='KeyID')  # Field name made lowercase.
#     candidate_id = models.IntegerField(db_column='Candidate_id', blank=True, null=True)  # Field name made lowercase.
#     level = models.IntegerField(db_column='Level', blank=True, null=True)  # Field name made lowercase.
#     score = models.IntegerField(blank=True, null=True)
#     status = models.CharField(max_length=20, blank=True, null=True)
#     subject_id = models.IntegerField(db_column='subject_ID', blank=True, null=True)  # Field name made lowercase.
#     createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'tb_subject_result_03022020'


# class TbSubjectResultBkup0316220(models.Model):
#     keyid = models.AutoField(db_column='KeyID')  # Field name made lowercase.
#     candidate_id = models.IntegerField(db_column='Candidate_id', blank=True, null=True)  # Field name made lowercase.
#     level = models.IntegerField(db_column='Level', blank=True, null=True)  # Field name made lowercase.
#     score = models.IntegerField(blank=True, null=True)
#     status = models.CharField(max_length=20, blank=True, null=True)
#     subject_id = models.IntegerField(db_column='subject_ID', blank=True, null=True)  # Field name made lowercase.
#     createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'tb_subject_result_bkup_0316220'


# class Tempquest(models.Model):
#     rownumber = models.IntegerField(db_column='Rownumber', blank=True, null=True)  # Field name made lowercase.
#     questionid = models.IntegerField(db_column='QuestionID', blank=True, null=True)  # Field name made lowercase.
#     subjects = models.CharField(db_column='Subjects', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     subject_id = models.IntegerField(db_column='Subject_ID', blank=True, null=True)  # Field name made lowercase.
#     level_id = models.IntegerField(db_column='Level_ID', blank=True, null=True)  # Field name made lowercase.
#     questions = models.TextField(db_column='Questions', blank=True, null=True)  # Field name made lowercase.
#     option1 = models.CharField(db_column='Option1', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     option2 = models.CharField(db_column='Option2', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     option3 = models.CharField(db_column='Option3', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     option4 = models.CharField(db_column='Option4', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     userid = models.IntegerField(db_column='UserID', blank=True, null=True)  # Field name made lowercase.
#     answer = models.CharField(db_column='Answer', max_length=500, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'tempQuest'
