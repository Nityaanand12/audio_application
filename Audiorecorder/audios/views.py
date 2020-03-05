from django.shortcuts import render
from audios.models import AudioRecordFile
from django.views import View

# Create your views here.

def index_view(request):
	recorded_files = AudioRecordFile.object.all()
	return render(request, 'audios/index.html',{"recorded_files":recorded_files})

def home_view(request):
	return render(request,'audios/home.html')

class SaveAudio(View):
    """Use ajax to save audio sent by user."""

    def post(self, request):
        audio_file = request.FILES.get('recorded_audio')
        myObj = AudioRecordFile()
        myObj.voice_record = audio_file
        myObj.save()
        return JsonResponse({
            'success': True,
        })
