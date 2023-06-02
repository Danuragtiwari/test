from django.shortcuts import render
from .models import Transcription

def home(request):
    transcriptions = Transcription.objects.all().order_by('-created_at')
    print(transcriptions)
    return render(request, 'index.html', {'transcriptions': transcriptions})

