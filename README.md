# Face-Mask-Detection-Alert-System
My project is basically based on Deep Learning’s Convolutional Neural Network(CNN) architecture . It contains facemask classifier model whose task is to detect whether a person is wearing a mask or not in the image, if he/she is not wearing a mask it sends an alert email to authorities containing attached image of that individual.
You can run the project using the gui_mask.py file.

To get an idea of how this project actually works, please go through the Project Presentation file in which I have thoroghly explained this project.
Brief description of project is as followed:
1. It contains train.py file using which I have trained our face mask classifier model using VGG16 Convolutional Neural Network  with dataset conatining: 1,376 images-686    with mask and 690 without mask.
2. I have used keras/tensorflow,sklearn,numpy,matplotlib,tkinter,smtp module libraries for this project.
3. Once the model i.e.face_mask_detection.h5 is trained,I created a gui for user using this model to detect 'Mask ON' or 'NO Mask'.
4. GUI contains two buttons 'Select Image' and 'Detect Mask'.
5. After selecting input image,user can click on 'Detect Mask'.If the person in that image is wearing a mask it labels Mask ON in green label on image.If not it labels NO    mask in red rectangular label & sends an alert email to authorities(i.e. person whose email address is mentioned in project) containing attached image of that person . 
