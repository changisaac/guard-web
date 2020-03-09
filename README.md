Notes:

- pretrained yolov3 weights, configuration, and classfications need to be copied into api/object_detection/nn_data
- need to install redis-server for celery
- run in guardenv, requirements.txt provided in root directory


- Example API query: http://127.0.0.1:8000/api/data/
```
{
"column_names":"car,start_time,man",
"man":"=,5",
"car":">=,8",
"start_time":"<,21",
"road_type":"high_way",
"gps_lag":"=,40",
"gps_long":"=,40"
}
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