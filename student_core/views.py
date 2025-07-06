from django.shortcuts import render
from .models import *
from django.db.models import Q,Sum
from django.core.paginator import Paginator

# Create your views here.

def get_student(request):

    queryset=Student.objects.all()
    if request.GET.get('search'):
        search=request.GET.get('search')
        queryset=queryset.filter(   
            Q(student_name__icontains=search)|
            Q(student_id__student_id__icontains=search)|
            Q(student_email__icontains=search)|
            Q(student_age__icontains=search)|
            Q(department__department__icontains=search)
        )
      
       
    paginator = Paginator(queryset, 10)  # Show 10 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
        
    context={"page_obj": page_obj}
    return render(request, 'student.html', context)

def get_marks(request,student_id):
    queryset=SubjectMarks.objects.filter(student__student_id__student_id=student_id)
    total_marks=queryset.aggregate(total_marks= Sum('marks'))
    current_rank=-1
    rank=Student.objects.annotate(marks=Sum('studentmarks__marks')).order_by('-marks')
    
    i=1
    for ranks in rank:
        if student_id == ranks.student_id.student_id:
            current_rank=i
            break

    i += 1
    
    context={'queryset':queryset, 'total_marks':total_marks,'current_rank':current_rank}
    return render(request,'marks.html',context) 