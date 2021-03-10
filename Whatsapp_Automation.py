#import py importing the module 
import pywhatkit 
  
# using Exception Handling to avoid  
# unprecedented errors 
try: 
    
  # sending message to reciever 
  # using pywhatkit 
  pywhatkit.sendwhatmsg("Any Number",  
                        "This is an auto generated mail from python code ", 20
                         , 49) 
  print("Successfully Sent!") 
  
except: 
    
  # handling exception  
  # and printing error message 
  print("An Unexpected Error!")
 
