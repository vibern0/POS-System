from datetime import datetime
import os

class Log:

    ###
    def add(user, list):
        fmt = '%d/%m/%Y %H:%M:%S'
        f = open('log_'+ user + '.txt','a')
        d = datetime.now()

        for item in list:
            f.write(d.strftime(fmt) + " -> " + item + os.linesep)
        
        f.close()