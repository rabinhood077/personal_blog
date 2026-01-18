from django.urls import path


from report import views


urlpatterns = [
    path("users-report", views.UserReportView.as_view(), name="users-report"),
]
