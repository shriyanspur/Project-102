import dropbox
import cv2
import time
import random

startTime = time.time()
token = input('Enter your dropbox app access token: ')
folder_Name = input('Enter the folder name to be created: ')

def takeSnapshot():
  number = random.randint(0, 200)

  videoCaptureObject = cv2.VideoCapture(0)
  result = True

  while (result):
    ret, frame = videoCaptureObject.read()

    imgName = 'img' + str(number) + '.png'

    cv2.imwrite(imgName, frame)
    startTime = time.time()
    result = False

  return imgName

  videoCaptureObject.release()

  cv2.destroyAllWindows()

def uploadImage(imgName):
  file_from = imgName
  file_to = '/' + folder_Name + '/' + file_from
  dbx = dropbox.Dropbox(token)

  with open(file_from, 'rb') as file:
    dbx.files_upload(file.read(), file_to)

def main():
  while (True):
    if ((time.time() - startTime) >= 5):
      img = takeSnapshot()
      uploadImage(img)
      print(img, 'has been uploaded')

main()