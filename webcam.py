import cv2

class webcam():
    def __init__(self):
        super().__init__()
        #which camera, should be the front one
        self.camera_port = 0

    def showWebcam(self):
        #shows new window with the webcam on
        self.vc = cv2.VideoCapture(self.camera_port)

        if self.vc.isOpened(): # try to get the first frame
            rval, frame = self.vc.read()
        else:
            rval = False

        while rval: # keeps the webcam on until ESC key is press
            cv2.imshow("Preview", frame)
            rval, frame = self.vc.read()
            self.key = cv2.waitKey(20)
            # exit on ESC, we can change it to something else
            # something fitting to the gui
            if self.key == 32:
                self.ss = frame
                break;

            if self.key == 27: 
                self.ss = "" 
                break
        self.vc.release()

    def screenshot(self):    
        #closes the cv2 windows
        cv2.destroyAllWindows()    
        
        if(self.key == 32):
           #saves the image
            cv2.imwrite('temp.jpg', self.ss)
            return True
        elif(self.key == 27):
              # No Image
            return False