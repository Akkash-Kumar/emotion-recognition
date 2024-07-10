
---- Used to detect human emotion using facial expressions ----

Python libraries to install :
1. pip install torch
2. pip install torchvision
3. pip install facial-emotion-recognition
4. pip install opencv-python
5. pip install opencv-contrib-python

Configure torch for CPU:
-> Open serialization.py file from site-packages/torch
-> Change this line to 
def load(f,map_location = 'cpu',pickle_module = pickle,**pickle_load_args);
