import cv2
import dropbox
import time
import random

start_time=time.time()

def takescreenshot():
    number=random.randint(1,100)
    print(number)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        img_name="img"+str(number)+".png"
        cv2.imwrite(img_name,frame)

        result=False
    videoCaptureObject.release()
    cv2.destroyAllWindows()
    print("snapshot taken")  
    return img_name

def upload_file(img_name):
    access_token='PulTDnhs8DAAAAAAAAAAAfKTgCjUCGhqdUHTAuFSpx9uhskQfTOqKJ33YDL8Mcyu'
    file=img_name
    file_from=file
    file_to="/newfolder143/"+(img_name)
    dbx=dropbox.Dropbox(access_token)

    with open(file_from,'rb')as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")

def main():
    while(True):
        if((time.time()-start_time)>=200):
            name=takescreenshot()
            upload_file(name)        



main()