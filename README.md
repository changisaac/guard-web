Notes:

- pretrained yolov3 weights, configuration, and classfications need to be copied into api/object_detection/nn_data
- need to install redis-server for celery
- run in guardenv, requirements.txt provided in root directory


- Example API query: http://127.0.0.1:8000/api/data/
```
{
"column_names":"car,start_time,man",
"man":"=,5",
"car":">,8",
"start_time":"<,21",
"road_type":"high_way",
"radius":1
"gps_lag":40
"gps_long":30
}
```
To calculate gps location within radius(km), we used the following equation:
```
Latitude: 1 deg = 110.574 km
Longitude: 1 deg = 111.320*cos(latitude) km
```

- Example API for inserting a frame's data http://127.0.0.1:8000/api/frame/
```
{
    "start_time": "20",
    "car": 3,
    "road_type": "high_way",
    "man": 5
}
```