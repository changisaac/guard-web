from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileSerializer, FrameSerializer, UserSerializer
from .tasks import process_file
from api.models import Frame
from math import cos

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

        try:
            frames = Frame.objects.all()
            req = {}
            
            column_names = request.data.get('column_names')
            radius = request.data.get('radius') or 5
            #note: calculation is based on the following equations
            # Latitude: 1 deg = 110.574 km
            # Longitude: 1 deg = 111.320*cos(latitude) km
            

            # print("column_names",column_names)
            
            for col_name in ['author', 'start_time', 'road_type','gps_lag', 'gps_long','car','bike','man']:
                req[col_name] = request.data.get(col_name)
                if req[col_name] is not None:
                    print("req[col_name]", req[col_name])
                    if col_name is 'author':
                        frames = frames.filter(author=req[col_name]).all()
                    elif col_name is 'road_type':
                        frames = frames.filter(road_type=req[col_name]).all()
                    elif col_name is 'start_time':
                        req[col_name] = req[col_name].split(',')
                        if req[col_name][0] is '=':
                            frames = frames.filter(start_time=int(req[col_name][1])).all()
                        elif req[col_name][0] is '<=':
                            frames = frames.filter(start_time__lte=int(req[col_name][1])).all()
                        elif req[col_name][0] is '>=':
                            frames = frames.filter(start_time__gte=int(req[col_name][1])).all()
                        elif req[col_name][0] is '>':
                            frames = frames.filter(start_time__gt=int(req[col_name][1])).all()
                        elif req[col_name][0] is '<':
                            frames = frames.filter(start_time__lt=int(req[col_name][1])).all()
                        else:
                            return Response("Error: incorrect filter syntax", status = 400)
                    elif col_name is 'gps_lag':
                        frames = frames.filter(gps_lag__range=(req[col_name]-radius*0.00904,radius*0.00904+req[col_name])).all()
                    elif col_name is 'gps_long':
                        long_range = radius/(cos(req[col_name])*111.32)
                        frames = frames.filter(gps_long__range=(req[col_name]-long_range,req[col_name]+long_range)).all()
                    elif col_name is 'man':
                        req[col_name] = req[col_name].split(',')
                        if req[col_name][0] is '=':
                            frames = frames.filter(man=int(req[col_name][1])).all()
                        elif req[col_name][0] is '<=':
                            frames = frames.filter(man__lte=int(req[col_name][1])).all()
                        elif req[col_name][0] is '>=':
                            frames = frames.filter(man__gte=int(req[col_name][1])).all()
                        elif req[col_name][0] is '>':
                            frames = frames.filter(man__gt=int(req[col_name][1])).all()
                        elif req[col_name][0] is '<':
                            frames = frames.filter(man__lt=int(req[col_name][1])).all()
                        else:
                            return Response("Error: incorrect filter syntax", status = 400)
                    elif col_name is 'car':
                        req[col_name] = req[col_name].split(',')
                        print(req[col_name])
                        if req[col_name][0] is '=':
                            frames = frames.filter(car=int(req[col_name][1])).all()
                        elif req[col_name][0] is '<=':
                            frames = frames.filter(car__lte=int(req[col_name][1])).all()
                        elif req[col_name][0] is '>=':
                            print("yes")
                            frames = frames.filter(car__gte=int(req[col_name][1])).all()
                        elif req[col_name][0] is '>':
                            frames = frames.filter(car__gt=int(req[col_name][1])).all()
                        elif req[col_name][0] is '<':
                            frames = frames.filter(car__lt=int(req[col_name][1])).all()
                        else:
                            return Response("Error: incorrect filter syntax", status = 400)
                    elif col_name is 'bike':
                        req[col_name] = req[col_name].split(',')
                        if req[col_name][0] is '=':
                            frames = frames.filter(bike=int(req[col_name][1])).all()
                        elif req[col_name][0] is '<=':
                            frames = frames.filter(bike__lte=int(req[col_name][1])).all()
                        elif req[col_name][0] is '>=':
                            frames = frames.filter(bike__gte=int(req[col_name][1])).all()
                        elif req[col_name][0] is '>':
                            frames = frames.filter(bike__gt=int(req[col_name][1])).all()
                        elif req[col_name][0] is '<':
                            frames = frames.filter(bike__lt=int(req[col_name][1])).all()
                        else:
                            return Response("Error: incorrect filter syntax", status = 400)
                    
                    # if col_name is 'man':
                    #     frames = frames.filter(man=req[col_name]).all()
                    
            
            
            print("tup:",tuple(column_names.split(',')))
            UserSerializer.Meta.fields = tuple(column_names.split(','))
            serializer = UserSerializer(frames, many=True)
            return Response(serializer.data)
        except:
            pass
        return Response("error", status = 500)

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
        return Response("error", status = 500)
    
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
    