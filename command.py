import time

class command_1:
    def test(time_sec):
        hours = 00
        while time_sec:
            mins, secs  = divmod(time_sec, 60)
            timeformat = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)
            #print(timeformat, end='\r')
            time_sec += 1
            if mins >= 59:
                hours += 1
                
                
            time.sleep(1)    
            
        
