import numpy as np
import os
from keras.models import load_model
from keras.preprocessing import image
import tensorflow as tf
global graph
graph = tf.get_default_graph()
from flask import Flask , request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

app = Flask(__name__)
model = load_model("nutrition.h5",compile=False)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/predict',methods = ['GET','POST'])
def upload():
    if request.method == 'POST':
        f = request.files['image']
        print("current path")
        basepath = os.path.dirname(__file__)
        print("current path", basepath)
        filepath = os.path.join(basepath,'uploads',f.filename)
        print("upload folder is ", filepath)
        f.save(filepath)
        
        img = image.load_img(filepath,target_size = (64,64))
        x = image.img_to_array(img)
        x = np.expand_dims(x,axis =0)
        
        with graph.as_default():
            preds = model.predict_classes(x)
            print("prediction",preds)

        index = ['Apple','Banana','brinjal','capsicum','cauliflower','corn','grapes','lady finger','Mango','orange','pineapple','watermelon']
        if(str(index[preds[0]])=="Apple"):
            
        	text = str(index[preds[0]]) + "-> the nutrition values are: calories=52g, protien=0.3g, fat=0.2g, carbohydrate=14 g"
        elif(str(index[preds[0]])=="Banana"):
        	text = str(index[preds[0]]) + "-> the nutrition values are: calories=89g, protein=1.1g, fat=0.3g, carbohydrates=23g"
        elif(str(index[preds[0]])=="brinjal"):
        	text = str(index[preds[0]]) + "-> the nutrition values are: calories=25g, protein=1g, fat=0.2 g, carbohydrates=6g"	
        elif(str(index[preds[0]])=="capsicum"):
        	text = str(index[preds[0]]) + "-> the nutrition values are: calories=40g, protein=1.9g, fat=0.2g, carbohydrates=9g"
        elif(str(index[preds[0]])=="cauliflower"):
        	text = str(index[preds[0]]) + "-> the nutrition values are: calories=25g,protein=1.9g, fat=0.3g, carbohydrates=5 g"
        elif(str(index[preds[0]])=="corn"):
        	text = str(index[preds[0]]) + "-> the nutrition values are: calories=44g,protein=1.6g, fat=0.8g, carbohydrates=7.8 g"
        elif(str(index[preds[0]])=="grapes"):
        	text = str(index[preds[0]]) + " -> the nutrition values are: calories=67g,protein=0.6g, fat=0.4g, carbohydrates=17 g"
        elif(str(index[preds[0]])=="lady finger"):
        	text = str(index[preds[0]]) + "-> the nutrition values are: calories=33g,protein=1.9g, fat=0.2g, carbohydrates=7 g"
        elif(str(index[preds[0]])=="Mango"):
        	text = str(index[preds[0]]) + " -> the nutrition values are: calories=60g,protein=0.8g, fat=0.4g, carbohydrates=15 g"
        elif(str(index[preds[0]])=="orange"):
        	text = str(index[preds[0]]) + "-> the nutrition values are: calories=47g,protein=0.9g, fat=0.1g, carbohydrates=12 g"		
        elif(str(index[preds[0]])=="pineapple"):
        	text = str(index[preds[0]]) + "-> the nutrition values are: calories=50g,protein=0.5g, fat=0.1g, carbohydrates=13 g"
        else:
        	text = str(index[preds[0]]) + "-> the nutrition values are: calories=30g,protein=0.6g, fat=0.2g, carbohydrates=8 g"


    return text
if __name__ == '__main__':
    app.run(debug = True, threaded = False)
        
        
        
    
    
    
