from faker import Faker
from .models import *
import random
fake = Faker()

def create_subject_marks()->None:
    student_obj=Student.objects.all()
    for student in student_obj:
        subject_obj=Subject.objects.all()
        for subjects in subject_obj:
            SubjectMarks.objects.create(
                student=student,
                subject=subjects,
                marks=random.randint(0, 100)
            )
    
def seed_db(n=10)->None:

    try:   
        for i in range(n):
            student_id=f'STU-0{random.randint(100, 999)}'
            depart_obj=Department.objects.all()
            random_index=random.randint(0, len(depart_obj-1))
            department=depart_obj[random_index]
            student_name=fake.name()
            student_age=random.randint(18, 25)
            student_address= fake.address()
            student_email=fake.email()

            student_id_obj=StudentID.objects.create(student_id=student_id)

            student_obj=Student.objects.create(
                department=department,
                student_id=student_id_obj,
                student_name=student_name,
                student_age=student_age,
                student_address=student_address,
                student_email=student_email,
            )
    except Exception as e:
        print(e)        

