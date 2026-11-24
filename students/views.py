from django.shortcuts import get_object_or_404, render

from .models import Student


def student_list(request):
    students = Student.objects.all()
    query = request.GET.get("q", "").strip()
    if query:
        students = students.filter(
            first_name__icontains=query
        ) | students.filter(last_name__icontains=query) | students.filter(
            student_id__icontains=query
        )

    return render(request, "students/student_list.html", {
        "students": students,
        "query": query,
        "student_count": students.count(),
    })


def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, "students/student_detail.html", {"student": student})
