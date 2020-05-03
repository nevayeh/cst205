import cv2

class webcam():
    def __init__(self):
        super().__init__()
        #which camera, should be the front one
        self.camera_port = 0

    def showWebcam(self):
        #shows new window with the webcam on
        cv2.namedWindow("preview")
        vc = cv2.VideoCapture(self.camera_port)

        if vc.isOpened(): # try to get the first frame
            rval, frame = vc.read()
        else:
            rval = False

        while rval: # keeps the webcam on until ESC key is press
            cv2.imshow("preview", frame)
            rval, frame = vc.read()
            key = cv2.waitKey(20)
            # exit on ESC, we can change it to something else
            # something fitting to the gui
            if key == 27:  
                break
        vc.release()
        #cv2.destroyAllWindows()

    def screenshot(self):
        #takes the screenshot
        camera = cv2.VideoCapture(self.camera_port, cv2.CAP_DSHOW)
        return_value, image = camera.read()
        
        #saves the image
        cv2.imwrite("image.png", image)
        name = "image.png"

        camera.release()
        """
        #shows the image the was taken in a new window
        cv2.imshow('show', image)
        cv2.waitKey(0)
        """
        #closes the cv2 windows
        cv2.destroyAllWindows()

        #returns image, we could also return the name
        return image


#for testing
webcam = webcam()

webcam.showWebcam()

img = webcam.screenshot()

cv2.imshow("screenshot", img)
cv2.waitKey(0)