from django.contrib import admin

from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "student_id",
        "last_name",
        "first_name",
        "course",
        "year_level",
        "section",
        "enrollment_status",
    )
    list_filter = ("course", "year_level", "section", "enrollment_status", "gender")
    search_fields = (
        "student_id",
        "first_name",
        "middle_name",
        "last_name",
        "email",
        "phone",
        "guardian_name",
    )
    ordering = ("last_name", "first_name")

    fieldsets = (
        ("Personal Information", {
            "fields": (
                "student_id", "first_name", "middle_name", "last_name",
                "date_of_birth", "gender", "email", "phone", "address",
            )
        }),
        ("Enrollment Information", {
            "fields": (
                "course", "year_level", "section", "enrollment_status",
            )
        }),
        ("Guardian Information", {
            "fields": ("guardian_name", "guardian_phone")
        }),
        ("Academic Background", {
            "fields": ("previous_school",)
        }),
    )
