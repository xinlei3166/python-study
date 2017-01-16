# _*_ coding:utf-8 _*_
from django.shortcuts import render,HttpResponse
import time


# Create your views here.

def index(request):
    return HttpResponse('django hello world!')

def bbs(request):
    return HttpResponse('This is a django bbs!')

def face(request):
    if request.method == 'GET':
        return render(request, 'face.html')
    if request.method == 'POST':
        try:
            image = request.FILES.get('file').read() # 获取到文件的二进制码
            # path = 'demo/static/faceimg/%s.jpg' % time.time()
            path_t = 'demo/static/faceimg/%s.jpg' % time.time()
            open('path_t', 'wb').write(image)
            return render(request, 'face.html', {'urlpath': path_t})
        except:
            # 进行人脸识别
            pass
