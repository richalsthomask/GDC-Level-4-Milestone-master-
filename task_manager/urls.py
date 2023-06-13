from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.http import HttpResponseRedirect

pending_tasks=[]
completed_tasks=[]


     

def tasks_view(request):
    return render(
        request,
        "tasks.html",
        {
            "pending_tasks": pending_tasks,
        }
    )

def completed_tasks_view(request):
    return render(
        request,
        "completed_tasks.html",
        {
            "completed_tasks": completed_tasks,
        }
    )

def report_view(request):
    return render(
        request,
        "report_view.html",
        {
            "pending_tasks": pending_tasks,
            "completed_tasks": completed_tasks,
        }
    )

def add_task(request):
   task_name=request.GET.get('task')
   pending_tasks.append(task_name)
   return HttpResponseRedirect('/tasks/')

def complete_task(request,task_id):
   completed_tasks.append(pending_tasks[task_id-1])
   del pending_tasks[task_id-1]
   return HttpResponseRedirect('/tasks/')

def delete_task(request,task_id):
   del pending_tasks[task_id-1]
   return HttpResponseRedirect('/tasks/')


urlpatterns = [
    path("admin/", admin.site.urls),
    # Add all your views here
    path('tasks/', tasks_view),
    path('add-task/', add_task),
    path('delete-task/<int:task_id>/', delete_task),
    path('complete_task/<int:task_id>/', complete_task),
    path('completed_tasks/', completed_tasks_view),
    path('report/', report_view)
]
