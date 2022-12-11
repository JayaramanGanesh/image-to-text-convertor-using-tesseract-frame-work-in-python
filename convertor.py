from PIL import Image
import cv2
import pytesseract

print("which one u have extract ...")
print("image based samples given 1 ")
print("video based samples given 2")
inpp= input(" your choose given only number : ")



if inpp == "1":
    filepath = str(input(" given the tesseract exe file path :"))
    image = input(" set image path :")
    img = Image.open(image)
    pytesseract.tesseract_cmd = filepath
    outcome = pytesseract.image_to_string(img)
    print(outcome[:-1])
    
elif inpp == "2":   
    while True:
         filepath = str(input(" given the tesseract exe file path :"))
         cam =cv2.videoCapture()
         _,vid =cam.read()
         gray =cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
         pytesseract.tesseract_cmd = filepath
         outcome = pytesseract.image_to_string(gray)
         ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
         rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))
         dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)
         contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
         im2 = vid.copy()
         file = open("recognized.txt", "w+")
         file.write("")
         file.close()
         for cnt in contours:
                x, y, w, h = cv2.boundingRect(cnt)
                rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cropped = im2[y:y + h, x:x + w]
                file = open("recognized.txt", "a")
                text = pytesseract.image_to_string(cropped)
                file.write(text)
                file.write("\n")
                file.close
         cv2.imshow('Grayscale Image', im2)
         cv2.waitKey(0)
         cv2.destroyAllWindows() 

else:
    print("your choose is out of range and select the numbers 1 or 2 ")        
    
    
    
    
    