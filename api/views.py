from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileSerializer, FrameSerializer, UserSerializer
from .tasks import process_file
from api.models import Frame

column_list = ['author', 'start_time', 'road_type','gps_lag', 'gps_long','car','bike','man']
            
class FileView(APIView):
    
    parser_classes = (MultiPartParser, FormParser)
    
    def post(self, request, *args, **kwargs): 
        file_serializer = FileSerializer(data=request.data)
        
        if file_serializer.is_valid():
            file_serializer.save()
            process_file.delay(file_serializer.data) 
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        return Response(status=status.HTTP_400_BAD_REQUEST)

class UserView(APIView):
    #example: http://127.0.0.1:8000/api/data
    def get(self, request):
        return Response([frame.start_time for frame in Frame.objects.all()])
    def post(self, request):
        frames = Frame.objects.all()
        req = {}
        req['car'] = request.data.get('car')
        return Response([frame.start_time for frame in Frame.objects.all()])

class FrameView(APIView):
    # https://www.django-rest-framework.org/api-guide/views/
    
    #example: http://127.0.0.1:8000/api/frame/?columns=start_time&man=5
    def get(self, request):
        try:
            column_names = request.GET.get('columns') #GET is from params as dict
        #frame?columns=start_time
            frames = Frame.objects.all()
            #import ipdb; ipdb.set_trace()
            #for column in column_list:
            #    column_request = request.GET.get(column)
            #    # import ipdb; ipdb.set_trace()
            #    if column_request is not None:
            #        frames = frames.filter(column=column_request).all()
            man_req = request.GET.get('man')
            # import ipdb; ipdb.set_trace()
            if man_req is not None:
                frames = frames.filter(man=man_req).all()
                # frames = Frame.objects.filter(man=man).all()
            else:
                frames = Frame.objects.all()
            
            FrameSerializer.Meta.fields = tuple(column_names.split(','))
            serializer = FrameSerializer(frames, many=True)
            return Response(serializer.data) #serializer.datav returns the object in json
        except:
            pass

       #for query: https://docs.djangoproject.com/en/3.0/topics/db/queries/
        # start_times = [frame.start_time for frame in Frame.objects.all()]
        # return Response(start_times)
        return Response(status = 500)
    
    # example: http://127.0.0.1:8000/api/frame/
        # {
        #     "start_time": "20",
        #     "car": 3,
        #     "man": 5
        # }
    def post(self, request):

        FrameSerializer.Meta.fields = tuple(column_list)
        
        frame_serializer = FrameSerializer(data=request.data)
        if frame_serializer.is_valid():
            frame_serializer.save() # save function for frame model
            return Response(frame_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(frame_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    