#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    
    '''
    if request.method == 'POST':
         Pclass = int(request.form['Pclass'])
         Gender=request.form['Gender']
         if(Gender=='Male'):
            Sex_male=1
            Sex_female=0
         
         if(Gender=='Female'):
            Sex_male=0
            Sex_female=1
        
         Embarked=request.form['Embarked']
         if(Embarked=='C'):
            Embarked_C=1
            Embarked_Q=0
            Embarked_S=0
         if(Embarked=='Q'): 
            Embarked_C=0
            Embarked_Q=1
            Embarked_S=0

         if(Embarked=='S'): 
            Embarked_C=0
            Embarked_Q=0
            Embarked_S=1
            
         prediction = model.predict([[Pclass,Sex_female,Sex_male,Embarked_C,Embarked_Q,Embarked_S]])
         output = int(prediction[0])
         if output==1:
            text="Survived"
         else:
            text='Not Survived'
            
         return render_template('index.html', prediction_text=text)
    
    
    else:
        return render_template('index.html')

        
         
            
            
        
        
        
           
            
            
                
                
            
                
                
            
           



      
            


            

            



            


@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)


# In[ ]:





# In[ ]:




