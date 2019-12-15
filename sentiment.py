import pandas as pd
import numpy as np

def sentiment(message):
     pos=0
     neg=0
     
     df= pd.read_csv("sentiment.csv")
     message= message.lower()
     message=message.split(' ')
     for i in range(0,len(message)):
       
        if message[i] in np.array(df.words):
              senti = df.loc[df.words == message[i]].iloc[0]
             
              vr=  senti['sentiment']
              if int(vr)==1:
                  pos+=1
                 
              elif int(vr)==0:
                  neg+=1
                  

     t=pos+neg
     if t==0:
      mood='expecting' 
      return mood
     else:
      pos=pos/t
     if pos >=0.0 and pos<=0.142:
        mood='Angry'
     elif pos >0.142 and pos<=0.285:
        mood='Disappointed' 
     elif pos >0.285 and pos<=0.428:
        mood='Worried'
     elif pos >0.428 and pos<=0.571:
        mood='Neutral'
     elif pos >0.571 and pos<=0.714:
        mood='Positive'
     elif pos >0.714 and pos<=0.857:
        mood='Happy' 
     elif pos >0.857 and pos<=1.0:
        mood='Joy'
    
     return mood

#test
yo=sentiment(' do what I say')
print(yo)