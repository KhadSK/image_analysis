import json
from pathlib import Path
import os
import time
import subprocess
from datetime import datetime
import logging
from bs4 import BeautifulSoup
import re
import shutil
import skimage
#from skimage import data, io
from matplotlib import pyplot
import ast


def main():
    listOfValue = []
    try:
        if os.path.getsize(pathDirIn):
            for root, dirs, files in os.walk(pathDirIn):
                for subdir in dirs:
                    pathSubdir = root + '/' + subdir
                    # test if dir contains fish base data
                    if pathSubDirFishbase in pathSubdir and os.listdir(pathSubdir):
                        for file in os.listdir(pathSubdir):
                            pathDataFile = pathSubdir + '/' + file
                            if os.stat(pathDataFile).st_size > 0:
                                
                                # open / read data file
                                with open (pathDataFile, 'r') as dataFile:
                                    listOfValue = ast.literal_eval(dataFile.read())
                                    
                                    y_val = 0
                                    x_val = 0
                                    pic_name_val = 'null'
                                    sci_name_val = 'null'
                                    fam_name_val = 'null'                                    
                                    #listOfValue = [(480, 640, 3, 'Acanthurus_nigricauda_picture_Acnig_us.jpg', 'Acanthurus nigricauda', 'Acanthuridae')]
                                    # example : (480, 640, 3, 'Acanthurus_nigricauda_picture_Acnig_us.jpg', 'Acanthurus nigricauda', 'Acanthuridae')
                                    #for i in listOfValue:
                                        #y_val = i[0]
                                        #x_val = i[1]
                                        #pic_name_val = i[3]
                                        #sci_name_val = i[4]
                                        #fam_name_val = i[5]
                                    
                                    y_val = [i[0] for i in listOfValue]
                                    x_val = [i[1] for i in listOfValue]
                                    pic_name_val = [i[3] for i in listOfValue]
                                    sci_name_val = [i[4] for i in listOfValue]
                                    fam_name_val = [i[5] for i in listOfValue]
                                    
                                    fig = pyplot.figure()
                                    ax = fig.add_subplot()    
                                    
                                    ax.scatter(x_val, y_val)
                                    
                                    #for xy in zip(x_val, y_val):
                                    #    ax.annotate('(%s, %s)' % xy, xy=xy, textcoords='data')
                                    
                                    for i, txt in enumerate(sci_name_val):
                                        ax.annotate(txt, (x_val[i], y_val[i]))
                                    
                                    pyplot.grid()
                                    pyplot.show()                                    
  
                    else:
                        #print('Data directory does not exist ', pathSubdir)
                        pass
        else: 
            #print ('File is either non-existent or inaccessible ', pathDirIn)
            pass
                                
                                    
    except OSError as e:
        print ('Erreur : ', e.errno, ' - ', e.strerror)
        ##continue
        

    


def createInitLogger():
    # create log file
    with open(pathLog,'a+') as f:
        f.write('log file : ' + pathFailedFamily + '\n')
        f.close()
    # DEBUG, INFO, WARNING, ERROR
    logging.basicConfig(filename=pathLog, 
                        format='%(asctime)s : %(levelname)s : %(message)s', 
                        datefmt='%Y/%m/%d %H:%M:%S', 
                        encoding='utf-8', 
                        level=logging.DEBUG)
                        

if __name__ == "__main__":
    dateTime = datetime.today().strftime('%Y%m%d %H:%M:%S')
    # ./src/in/test_family.json
    pathDirIn = './src/in'
    pathSubDirFishbase = '/fishbase'
    pathFailedFamily = './log/json/family ' + dateTime + '.json'
    pathLog = './log/' + dateTime + '.log'
    familyName = None
    familyId = None
    urlWebPage = ''
    dirWebOutput = ''    
    main()
