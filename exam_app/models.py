# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models





class TbCandidate(models.Model):
    keyid = models.CharField(db_column='KeyID', max_length=11)  # Field name made lowercase.
    first_name = models.CharField(db_column='First_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    last_name = models.CharField(db_column='Last_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dob = models.DateField(db_column='DOB', blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=10, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=15, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    temp_address = models.CharField(db_column='Temp_Address', max_length=500, blank=True, null=True)  # Field name made lowercase.
    perm_address = models.CharField(db_column='Perm_Address', max_length=500, blank=True, null=True)  # Field name made lowercase.
    marietal_status = models.CharField(db_column='Marietal_Status', max_length=3, blank=True, null=True)  # Field name made lowercase.
    ug_degree = models.CharField(db_column='UG_Degree', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ug_college = models.CharField(db_column='UG_College', max_length=450, blank=True, null=True)  # Field name made lowercase.
    ug_yearofpassing = models.IntegerField(db_column='UG_Yearofpassing', blank=True, null=True)  # Field name made lowercase.
    ug_grade = models.CharField(db_column='UG_Grade', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pg_degree = models.CharField(db_column='PG_Degree', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pg_college = models.CharField(db_column='PG_College', max_length=450, blank=True, null=True)  # Field name made lowercase.
    pg_yearofpassing = models.IntegerField(db_column='PG_Yearofpassing', blank=True, null=True)  # Field name made lowercase.
    pg_grade = models.CharField(db_column='PG_Grade', max_length=10, blank=True, null=True)  # Field name made lowercase.
    referalby = models.CharField(db_column='ReferalBY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(db_column='Source', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isbondaccepted = models.IntegerField(db_column='IsBondAccepted', blank=True, null=True)  # Field name made lowercase.
    isattendedpreviously = models.IntegerField(db_column='IsAttendedPreviously', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='Createddate', blank=True, null=True)  # Field name made lowercase.
    systemip = models.CharField(db_column='SystemIP', max_length=20, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=50, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=15, blank=True, null=True)  # Field name made lowercase.
    islocked = models.IntegerField(db_column='Islocked', blank=True, null=True)  # Field name made lowercase.
    loggedintime = models.DateTimeField(db_column='LoggedinTime', blank=True, null=True)  # Field name made lowercase.
    loggedouttime = models.DateTimeField(db_column='LoggedOutTime', blank=True, null=True)  # Field name made lowercase.
    isautologgedout = models.IntegerField(db_column='IsAutologgedout', blank=True, null=True)  # Field name made lowercase.
    lastsavedtime = models.DateTimeField(db_column='LastSavedTime', blank=True, null=True)  # Field name made lowercase.
    applied_for = models.CharField(db_column='Applied_For', max_length=50, blank=True, null=True)  # Field name made lowercase.
    flag = models.IntegerField(db_column='Flag', blank=True, null=True)  # Field name made lowercase.
    diploma_degree = models.CharField(db_column='DIPLOMA_Degree', max_length=50, blank=True, null=True)  # Field name made lowercase.
    diploma_college = models.CharField(db_column='DIPLOMA_College', max_length=500, blank=True, null=True)  # Field name made lowercase.
    diploma_yearofpassing = models.IntegerField(db_column='DIPLOMA_Yearofpassing', blank=True, null=True)  # Field name made lowercase.
    diploma_grade = models.CharField(db_column='DIPLOMA_Grade', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lad = models.DateTimeField(db_column='LAD', blank=True, null=True)  # Field name made lowercase.
    islevel1_skiiped = models.IntegerField(db_column='IsLevel1_Skiiped', blank=True, null=True)  # Field name made lowercase.
    tenth_institution = models.CharField(db_column='Tenth_Institution', max_length=450, blank=True, null=True)  # Field name made lowercase.
    tenth_percentage = models.CharField(db_column='Tenth_Percentage', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tenth_yop = models.IntegerField(db_column='Tenth_YOP', blank=True, null=True)  # Field name made lowercase.
    ug_department = models.CharField(db_column='UG_Department', max_length=70, blank=True, null=True)  # Field name made lowercase.
    ug_discipline = models.CharField(db_column='UG_Discipline', max_length=70, blank=True, null=True)  # Field name made lowercase.
    pg_department = models.CharField(db_column='PG_Department', max_length=70, blank=True, null=True)  # Field name made lowercase.
    pg_descipline = models.CharField(db_column='PG_DESCIPLINE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mail_status = models.IntegerField(db_column='Mail_status', blank=True, null=True)  # Field name made lowercase.
    islogged = models.IntegerField(db_column='Islogged', blank=True, null=True)  # Field name made lowercase.
    isadmin = models.BooleanField(db_column='isAdmin', blank=True, null=True)  # Field name made lowercase.
    country_code = models.CharField(db_column='Country_code', max_length=10, blank=True, null=True)  # Field name made lowercase.
    id_proof = models.CharField(db_column='Id_proof', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id_no = models.CharField(db_column='ID_NO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id_image = models.TextField(db_column='ID_Image', blank=True, null=True)  # Field name made lowercase.
    profile_image = models.TextField(db_column='Profile_Image', blank=True, null=True)  # Field name made lowercase.
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    remaining_time = models.IntegerField(db_column='Remaining_time', blank=True, null=True)  # Field name made lowercase.
    level = models.IntegerField(db_column='Level', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=10, blank=True, null=True)
    id_date = models.CharField(max_length=10, blank=True, null=True)
    twelfth_degree = models.CharField(db_column='Twelfth_degree', max_length=50, blank=True, null=True)  # Field name made lowercase.
    twelfth_college = models.CharField(db_column='Twelfth_College', max_length=500, blank=True, null=True)  # Field name made lowercase.
    twelfth_yearofpassing = models.IntegerField(db_column='Twelfth_Yearofpassing', blank=True, null=True)  # Field name made lowercase.
    twelfth_grade = models.CharField(db_column='Twelfth_Grade', max_length=50, blank=True, null=True)  # Field name made lowercase.
    extra1_degree = models.CharField(db_column='Extra1_Degree', max_length=50, blank=True, null=True)  # Field name made lowercase.
    extra1_college = models.CharField(db_column='Extra1_College', max_length=500, blank=True, null=True)  # Field name made lowercase.
    extra1_yearofpassing = models.IntegerField(db_column='Extra1_Yearofpassing', blank=True, null=True)  # Field name made lowercase.
    extra1_grade = models.CharField(db_column='Extra1_Grade', max_length=50, blank=True, null=True)  # Field name made lowercase.
    extra2_degree = models.CharField(db_column='Extra2_Degree', max_length=50, blank=True, null=True)  # Field name made lowercase.
    extra2_college = models.CharField(db_column='Extra2_College', max_length=500, blank=True, null=True)  # Field name made lowercase.
    extra2_yearofpassing = models.IntegerField(db_column='Extra2_Yearofpassing', blank=True, null=True)  # Field name made lowercase.
    extra2_grade = models.CharField(db_column='Extra2_Grade', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_Candidate'


class TbQuestion(models.Model):
    keyid = models.AutoField(db_column='KeyID', primary_key=True)  # Field name made lowercase.
    subject_id = models.IntegerField(db_column='Subject_ID', blank=True, null=True)  # Field name made lowercase.
    level_id = models.IntegerField(db_column='Level_ID', blank=True, null=True)  # Field name made lowercase.
    questions = models.TextField(db_column='Questions', blank=True, null=True)  # Field name made lowercase.
    option1 = models.CharField(db_column='Option1', max_length=500, blank=True, null=True)  # Field name made lowercase.
    option2 = models.CharField(db_column='Option2', max_length=500, blank=True, null=True)  # Field name made lowercase.
    option3 = models.CharField(db_column='Option3', max_length=500, blank=True, null=True)  # Field name made lowercase.
    option4 = models.CharField(db_column='Option4', max_length=500, blank=True, null=True)  # Field name made lowercase.
    answer = models.CharField(db_column='Answer', max_length=500, blank=True, null=True)  # Field name made lowercase.
    typeflag = models.CharField(max_length=2, blank=True, null=True)
    flag = models.BooleanField(db_column='FLAG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_Question'


