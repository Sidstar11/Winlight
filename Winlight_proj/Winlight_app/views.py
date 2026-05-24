from django.shortcuts import render, redirect
from django.contrib import messages
from .models import RecentWork, UpcomingProject, CrewMember, Article
from .forms import RecentWorkForm, UpcomingProjectForm, CrewMemberForm, ArticleForm

def studio_home(request):
    # FILTERED: Only pull featured works for the homepage carousel slider
    recent_works = RecentWork.objects.filter(is_featured=True)
    upcoming_projects = UpcomingProject.objects.filter(is_featured=True)
    crew_members = CrewMember.objects.all()
    articles = Article.objects.filter(is_featured=True)

    if request.method == 'POST':
        form_type = request.POST.get('form_id')
        
        if form_type == 'recent_work_submit':
            form = RecentWorkForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "Portfolio item added successfully.")
                return redirect('studio_home')
        
        elif form_type == 'upcoming_project_submit':
            form = UpcomingProjectForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "Upcoming project logged successfully.")
                return redirect('studio_home')

        elif form_type == 'crew_submit':
            form = CrewMemberForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "Crew profile saved successfully.")
                return redirect('studio_home')

        elif form_type == 'article_submit':
            form = ArticleForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "Editorial story published successfully.")
                return redirect('studio_home')
    
    context = {
        'recent_works': recent_works,
        'upcoming_projects': upcoming_projects,
        'crew_members': crew_members,
        'articles': articles,
        'recent_form': RecentWorkForm(),
        'upcoming_form': UpcomingProjectForm(),
        'crew_form': CrewMemberForm(),
        'article_form': ArticleForm(),
    }
    return render(request, 'Winlight_app/index.html', context)
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import RecentWork, UpcomingProject, CrewMember, Article
from .forms import RecentWorkForm, UpcomingProjectForm, CrewMemberForm, ArticleForm

# def studio_home(request):
#     # Pure GET execution layer protects your scrolling timelines & slider tracks
#     recent_works = RecentWork.objects.filter(is_featured=True)
#     upcoming_projects = UpcomingProject.objects.filter(is_featured=True)
#     crew_members = CrewMember.objects.all()
#     articles = Article.objects.filter(is_featured=True)

#     context = {
#         'recent_works': recent_works,
#         'upcoming_projects': upcoming_projects,
#         'crew_members': crew_members,
#         'articles': articles,
#     }
#     return render(request, 'Winlight_app/index.html', context)

# NEW DESIGNATED DATA INPUT CORE CONTROL VIEW
def studio_control_desk(request):
    if request.method == 'POST':
        form_id = request.POST.get('form_id')
        
        if form_id == 'recent_work_submit':
            form = RecentWorkForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "Recent work entry published successfully!")
                return redirect('control_desk')
                
        elif form_id == 'upcoming_project_submit':
            form = UpcomingProjectForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "Upcoming roadmap project item logged!")
                return redirect('control_desk')
                
        elif form_id == 'crew_submit':
            form = CrewMemberForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "Artisan crew profile captured!")
                return redirect('control_desk')
                
        elif form_id == 'article_submit':
            form = ArticleForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "Editorial ledger release distributed!")
                return redirect('control_desk')

    # Instantiates forms smoothly on normal page lookups
    context = {
        'recent_form': RecentWorkForm(),
        'upcoming_form': UpcomingProjectForm(),
        'crew_form': CrewMemberForm(),
        'article_form': ArticleForm(),
    }
    return render(request, 'Winlight_app/control_desk.html', context)
# NEW: View to show archived portfolios (where is_featured is False)
def all_recent_works(request):
    archived_works = RecentWork.objects.all
    return render(request, 'Winlight_app/all_recent.html', {'works': archived_works})

# (Keep your all_pipeline_projects and all_editorial_articles views exactly as they are)
# View to show unfeatured pipeline assignments
def all_pipeline_projects(request):
    archived_projects = UpcomingProject.objects.all
    return render(request, 'Winlight_app/pipeline_archive.html', {'projects': archived_projects})

# View to show unfeatured editorial dispatches
def all_editorial_articles(request):
    archived_articles = Article.objects.all
    return render(request, 'Winlight_app/editorial_archive.html', {'articles': archived_articles})

def studio_home(request):
    recent_works = RecentWork.objects.filter(is_featured=True)
    upcoming_projects = UpcomingProject.objects.filter(is_featured=True)
    # UPDATED: Added true flag matching parameter
    crew_members = CrewMember.objects.filter(is_featured=True)
    articles = Article.objects.filter(is_featured=True)
    # ... keep your standard POST submission multi-form interceptors unchanged ...
    context = {
        'recent_works': recent_works, 'upcoming_projects': upcoming_projects,
        'crew_members': crew_members, 'articles': articles,
        'recent_form': RecentWorkForm(), 'upcoming_form': UpcomingProjectForm(),
        'crew_form': CrewMemberForm(), 'article_form': ArticleForm(),
    }
    return render(request, 'Winlight_app/index.html', context)

# NEW: Independent Roster Subpage
def all_crew_members(request):
    archived_crew = CrewMember.objects.all
    return render(request, 'Winlight_app/all_crew.html', {'crew_members': archived_crew})