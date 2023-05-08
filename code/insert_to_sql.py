import mysql.connector
from datetime import datetime


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="dfs"
    )
mycursor = mydb.cursor()


def get_patient_id(patient_name):
    sql = "SELECT * FROM patientMaster WHERE patient_name = %s"
    val = (patient_name,)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    patient_id =  myresult[0][0]
    return patient_id

#get the patient purpose id from the patient id
def get_patient_purpose_id(patient_id):
    sql = "SELECT * FROM patientMeta WHERE patient_id = %s"
    val = (patient_id,)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    patient_purpose_id =  myresult[0][0]
    return patient_purpose_id

#create a patient given the patient name and if the patient did not exist, create a new patient
def create_patient(patient_name):
    if check_if_patient_exists(patient_name) == True:
        return get_patient_purpose_id(get_patient_id(patient_name))
    else:
        now = datetime.now()
        formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
        sql = "INSERT INTO patientMaster (patient_name,created_at,updated_at) VALUES (%s,%s,%s)"
        val = (patient_name,formatted_date,formatted_date)
        mycursor.execute(sql, val)
        mydb.commit()
        
        patient_id = mycursor.lastrowid
        sql = "INSERT INTO patientMeta (patient_id,created_at,updated_at) VALUES (%s,%s,%s)"
        val = (patient_id,formatted_date,formatted_date)
        mycursor.execute(sql, val)
        mydb.commit()
        
        return mycursor.lastrowid

#check if a patient exists given the patient id

def check_if_patient_exists(patient_name):
    sql = "SELECT * FROM patientMaster WHERE patient_name = %s"
    val = (patient_name,)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    if len(myresult) > 0:
        return True
    else:
        return False

#check if a field exists given the field name
def check_if_field_exists(field_name):
    sql = "SELECT * FROM sampleFieldMaster WHERE field_name = %s"
    val = (field_name,)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    if len(myresult) > 0:
        return True
    else:
        return False

def insert_fields(fields_list):
    print(fields_list) 
    for ele in fields_list:
        if check_if_field_exists(ele) == True:
            continue
        
        now = datetime.now()
        formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
        sql = "INSERT INTO sampleFieldMaster (field_name,field_datatype,created_at,updated_at) VALUES (%s,%s,%s,%s)"
        val = (ele,"varchar(255)",formatted_date,formatted_date)
        mycursor.execute(sql, val)
        mydb.commit()
    
  
def get_field_id(field_name):
    sql = "SELECT * FROM sampleFieldMaster WHERE field_name = %s"
    val = (field_name,)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    return myresult[0][0]

def insert_row(row,columns):
    field_ids = []
    for ele in columns:
        field_ids.append(get_field_id(ele))
    patient_purpose_id = create_patient(row[0])
    visit_sample_id = create_visit_sample(patient_purpose_id)
    print(row)
    for i in range(len(row)):
        if i==0:
            continue
        if row[i] == None:
            row[i] = "NULL"
        else:
            row[i] = str(row[i])
        now = datetime.now()
        formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
        sql = "INSERT INTO sampleFieldValue (field_id,visit_sample_id,field_value,created_at,updated_at) VALUES (%s,%s,%s,%s,%s)"
        val = (field_ids[i],visit_sample_id,row[i],formatted_date,formatted_date)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "rows were inserted.")
    

def check_if_sample_exists(sample_id):
    sql = "SELECT * FROM sampleMaster WHERE sample_id = %s"
    val = (sample_id,)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    if len(myresult) > 0:
        return True
    else:
        return False

def create_sample():
    if check_if_sample_exists(4) == True:
        return 4
    now = datetime.now()
    formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
    sql = "INSERT INTO sampleMaster (sample_id,sample_name,created_at,updated_at) VALUES (%s,%s,%s,%s)"
    val = (4,"Brain_MRI_Scan",formatted_date,formatted_date)
    mycursor.execute(sql, val)
    mydb.commit()
    
    return mycursor.lastrowid

def create_visit(patient_purpose_id):
    now = datetime.now()
    formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
    sql = "INSERT INTO visitMaster (visit_date,patient_purpose_id,created_at,updated_at) VALUES (%s,%s,%s,%s)"
    val = (formatted_date,patient_purpose_id,formatted_date,formatted_date)
    mycursor.execute(sql, val)
    mydb.commit()
    
    return mycursor.lastrowid

def create_visit_sample(patient_purpose_id):
    now = datetime.now()
    formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
    sql = "INSERT INTO visitSampleMaster (visit_id,sample_id,created_at,updated_at) VALUES (%s,%s,%s,%s)"
    val = (create_visit(patient_purpose_id),4,formatted_date,formatted_date)
    mycursor.execute(sql, val)
    mydb.commit()
    
    return mycursor.lastrowid







