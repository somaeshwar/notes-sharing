from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import NotesForm

@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')


@login_required(login_url='login')
def upload_notes(request):
    if request.method == 'POST':
        form = NotesForm(request.POST, request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            note.uploaded_by = request.user
            note.save()
            return redirect('home')
    else:
        form = NotesForm()

    return render(request, 'upload.html', {'form': form})


from .models import Notes

@login_required(login_url='login')
def notes_list(request):
    notes = Notes.objects.all().order_by('-upload_date')
    return render(request, 'notes_list.html', {'notes': notes})


from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

@login_required(login_url='login')
def download_note(request, note_id):
    note = get_object_or_404(Notes, id=note_id)
    note.download_count += 1
    note.save()
    return HttpResponseRedirect(note.file.url)
