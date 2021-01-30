
import sentry
import time
 

var=1


#enters a while loop , and exits the while loop when the script is stopped in the main software

while var == 1 : 


 var=sentry.getscriptrunning()



 #get angle in radians
 radanglea=sentry.getangle()
 radangle=float(2)  
 radangle=radanglea[0]
 
 #convert to degrees
 degreesangle=float(3)
 degreesangle=float(57.296)*radangle
 
 #set range so that a vertical orientation=90 degrees
 if degreesangle < 0 :
  degreesangle=degreesangle+float(180)
  
with open('angle.txt', 'w') as the_file:
    the_file.write('{} \n'.format(degreesangle))

    time.sleep(0.03)





 



   
        
















