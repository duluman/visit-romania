from django.shortcuts import render
from jobs.models import Job, Education


def nick_view(request):
    jobs = Job.objects.all()
    ed = Education.objects.all()

    template = 'jobs/nik.html'
    context = {
        'jobs': jobs,
        'ed': ed
    }

    return render(request, template, context)
