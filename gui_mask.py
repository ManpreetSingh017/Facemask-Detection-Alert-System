'''
Manpreet Singh
Branch-D4CSE A2
University Roll No - 1706472
GNDEC,Ludhiana
"Face Mask Detection System"
 #'''

from tkinter import *
import tkinter.messagebox
from PIL import ImageTk, Image
import cv2
import wget
from tkinter import filedialog
from tkinter import messagebox
import smtplib

from email.message import EmailMessage
from tensorflow.keras.models import load_model
from time import sleep
from keras.preprocessing.image import img_to_array
from keras.preprocessing import image
import tkinter.filedialog as tkFileDialog
import cv2
import numpy as np

from email.message import EmailMessage


path = ""
image1 = ""
image2 = ""
panelA = None
panelB = None


path2 = "./sample1.jpg"
#show_image1(path2)


def select_image():
    global panelA, panelB,image1,plate,plate_text
    global path
    path = tkFileDialog.askopenfilename()
    if len(path) > 0:
        path1=path
        path1=(path1.split('/'))
        imgOriginalScene  = cv2.imread(path)
    
        image1 = cv2.resize(imgOriginalScene,(390,240))
        image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
        image1= Image.fromarray(image1)
        image1= ImageTk.PhotoImage(image1)

        image2 = cv2.imread(path2)

        image2 = cv2.resize(image2,(390,240))
        image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)
        image2= Image.fromarray(image2)
        image2= ImageTk.PhotoImage(image2)

        if panelA is None or panelB is None:
            panelA= Label(MainFrame, image = image1)
            panelA.grid(row=4,column=0,sticky=W)

            panelB = Label(MainFrame, image = image2)
            panelB.grid(row=4,column=1,sticky=W)
        

        else:
            panelA.configure(image=image1)
            panelA.grid(row=4,column=0,sticky=W)
            panelB.configure(image=image2)
            panelB.grid(row=4,column=1,sticky=W)
            panelA.image = image1
            panelA.grid(row=4,column=0,sticky=W)
            panelB.image =image2
            panelB.grid(row=4,column=1,sticky=W)




def show_image1(path2):
    #print(path2)
    image2 = cv2.imread(path2)

    image2 = cv2.resize(image2,(390,240))
    image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)
    image2= Image.fromarray(image2)
    image2= ImageTk.PhotoImage(image2)

    global panelA, panelB

    if panelA is None or panelB is None:
                    
        panelA= Label(MainFrame, image = image1)
        panelA.grid(row=4,column=0,sticky=W)


        

    # otherwise, update the image panels
    else:
        # update the pannels
        panelA.configure(image=image1)
        panelA.grid(row=4,column=0,sticky=W)
        panelB.configure(image=image2)
        panelB.grid(row=4,column=1,sticky=W)
        panelA.image = image1
        panelA.grid(row=4,column=0,sticky=W)
        panelB.image =image2
        panelB.grid(row=4,column=1,sticky=W)




flag = False

def predict():

    if(path==""):
        tkinter.messagebox.showinfo("Image Not Selected","Please select an image first \n ")
    else:
        print("[INFO] loading network...")
        model =load_model('./face_mask_detection.h5')

        labels = ['Mask ON','NO Mask'] #These labels will be used for showing output
        start_point = (15, 15)
        end_point = (370, 80)
        thickness = -1

        print("[INFO] reading image...")
        frame = cv2.imread(path)

        roi_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        roi_gray = cv2.resize(frame,(224,224))
        roi = roi_gray.astype('float')/255.0
        roi = img_to_array(roi)
        roi = np.expand_dims(roi,axis=0)

        print("[INFO] classifying image...")

        preds = model.predict(roi)[0]

        label=labels[preds.argmax()]


        if(label=='NO Mask'):
            image = cv2.rectangle(frame, start_point, end_point, (0,0,255), thickness)
            cv2.putText(image,label,(30,60),cv2.FONT_HERSHEY_SIMPLEX,2,(255,255,255),3)

            cv2.imwrite("./Output/detected.jpg", frame)
            show_image1('./Output/detected.jpg')
            messagebox.showwarning("Warning", "Access Denied. Please wear a Face Mask")

            msg = EmailMessage()
            msg['Subject'] = 'Subject - Attention! Someone violated our facemask policy.'
            msg['From'] = 'manisekhon018@gmail.com'
            msg['To'] = 'manisekhon018@gmail.com'
            msg.set_content(
                'A person has been detected without a face mask. Below is the attached image of that person.Please Alert the Authorities.\n'
                'From:\n'
                'Name- Manpreet Singh\n'
                'Branch-D4CSE-A2\n'
                'Univ Roll No.-1706472\n'
                'GNDEC,Ludhiana'

                )

            with open("Output/detected.jpg", "rb") as f:
                fdata = f.read()
                fname = f.name
                msg.add_attachment(fdata, maintype='Image', subtype="jpg", filename=fname)

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login('manisekhon018@gmail.com', '$ekhoN123')
                smtp.send_message(msg)
            print('[INFO] alert mail Sent to authorities')







        if(label=='Mask ON'):
            image = cv2.rectangle(frame, start_point, end_point, (0,255,0), thickness)
            cv2.putText(image,label,(30,60),cv2.FONT_HERSHEY_SIMPLEX,1.6,(0,0,0),3)


        print("[INFO] saving image...")
        cv2.imwrite("./Output/detected.jpg",frame)
        #select_image()
        show_image1('./Output/detected.jpg')
        global flag
        flag = True

        


root = Tk()
root.title("GUI :Facemask Detection Alert System")

root.geometry("1200x720")

root.configure(background = 'Orange')
Tops = Frame(root,bg = 'red',pady = 1, width =1750, height = 90, relief = "ridge")
Tops.grid(row=0,column=0)


Title_Label = Label(Tops,font=('Comic Sans MS',20,'bold'),text = "    ' Manpreet Singh, D4CSE-A2, 1706472 ' \n\t Facemask Detection Alert System using Open-CV,\n\t\t Keras/Tensorflow and Deep Learning\t\t",pady=9,bg= 'orange',fg='blue',justify ="center")
Title_Label.grid(row=0,column=0)
MainFrame = Frame(root,bg = 'orange',pady=2,padx=2, width =1350, height = 100, relief = RIDGE)
MainFrame.grid(row=1,column=0)



Label_1 =Label(MainFrame, font=('Comic Sans MS', 18,'bold'), text="\t    Detect whether a person is wearing a mask or not",padx=2,pady=2, bg="orange",fg ="white",justify="center")
Label_1.grid(row=0, column=0)

Label_2 =Label(MainFrame, font=('arial', 15,'bold'), text="",padx=2,pady=2, bg="orange",fg = "black")
Label_2.grid(row=1, column=0,sticky=W)

Label_9 =Button(MainFrame, font=('arial', 19,'bold'), text=" Select Image ",padx=2,pady=2, bg="blue",fg = "white",command=select_image)
Label_9.grid(row=2, column=0)

Label_9 =Button(MainFrame, font=('arial', 19,'bold'), text=" Detect Mask ",padx=2,pady=2, bg="blue",fg = "white",command=predict)
Label_9.grid(row=2, column=1,sticky=W)

Label_2 =Label(MainFrame, font=('arial', 10,'bold'), text="",padx=2,pady=2, bg="orange",fg = "black")
Label_2.grid(row=3, column=0,sticky=W)

Label_3 =Label(MainFrame, font=('arial', 30,'bold'), text="          \t\t\t",padx=2,pady=2, bg="orange",fg = "black")
Label_3.grid(row=4, column=0)


Label_3 =Label(MainFrame, font=('arial', 10,'bold'), text="\t\t\t\t          ",padx=2,pady=2, bg="orange",fg = "black")
Label_3.grid(row=5, column=1)





root.mainloop()
