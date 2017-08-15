#coding=utf-8

from keras.models import model_from_json, load_model
import numpy as np
from PIL import Image

table_jwc = ['0','1','2','3','4','5','6','7','8','9',\
               'a','b','c','d','e','f','g','h','i','j','k',\
               'l','m','n','o','p','q','r','s','t','u','v',\
               'w','x','y','z','A','B','C','D','E','F','G',\
               'H','I','J','K','L','M','N','O','P','Q','R',\
               'S','T','U','V','W','X','Y','Z']

table_phylab = ['0','1','2','3','4','5','6','7','8','9']

model_jwc = model = model_from_json(open('models/jwc_structure.json').read())
model_jwc.load_weights('models/jwc_weights.h5')
model_phylab = model_from_json(open('models/phylab_structure.json').read())
model_phylab.load_weights('models/phylab_weights.h5')

def solve_jwc(im):
  X_list=[]
  result=''
  for i in range(4):
    region = (15*i,0,15*i+15,22)
    cim = im.crop(region)
    X_list.append(np.array(cim))
  p = model.predict(np.array(X_list))
  for each in p:
    index=0
    for i in range(len(each)):
      if(each[i]>each[index]):
        index=i
    result+=(table_jwc[index])
  return (result)

def solve_phylab(pic):
  pic = np.array(pic.convert('RGB'))[:, :, ::-1].copy()
  #a little bit tricky, this line is trying to converting PIL image to opencv-python format, that's all

  x=[]
  result=''
  x.append(pic[:, 5:14])
  x.append(pic[:, 14:23])
  x.append(pic[:, 24:33])
  x.append(pic[:, 34:43])

  p = model_phylab.predict(np.array(x))
  for each in p:
    index=0
    for i in range(len(each)):
      if(each[i]>each[index]):
        index=i
    result+=(table_phylab[index])
  return (result)