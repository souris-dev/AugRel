# The OpenCV thread module

import sys
from gen_ui3 import *
from img_utils import *
import threading as th
import time

cam = cv2.VideoCapture(0)
face_casc = cv2.CascadeClassifier("D:\\Documents\\Projects\\AugRel\\haarcascade_frontalface_default.xml")
png_dir = "D:\\Documents\\Projects\\AugRel\\png"
curr_filter = ["one_devil_horn"]


def take_snap(image, file_folder):
    filename_append = []

    for i in list(time.ctime()):
        if i == ' ' or i == ':':
            filename_append.append('_')
        else:
            filename_append.append(i)

    cv2.imwrite(file_folder + "/" + "snap" + "".join(filename_append) + ".jpg", image)
    print("Snappy-snappied! to ", file_folder + "/" + "".join(filename_append), " at ", time.ctime())


def cam_loop():
    scale_percent = 150  # percent of original size, for camera img
    while True:
        # the first var is true if camera is working
        cam_ok, img = cam.read()

        if cam_ok:
            grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_casc.detectMultiScale(grey, scaleFactor=1.2, minNeighbors=5)

            # faces is a numpy.ndarray only when faces are detected, else it is a tuple
            print(faces)

            if type(faces) == np.ndarray and faces.size > 4:
                # sort the ndarray according to the x value of the detected faces
                # I have to use an indirect method for this
                # as np.ndarray.sort(axis=0 or 1) gives problems

                # Hence, I convert the ndarray to a list, sort it
                # as per the first element and then make it an ndarray again
                temp = []
                for row in faces:
                    temp.append(list(row))
                temp.sort()
                faces = np.array(temp)

            print(faces)
            i = 0
            for (x, y, w, h) in faces:
                # cv2.rectangle(img, (x, y), (x+w, y+h), (0, 120, 255), 2)
                try:
                    global curr_filter
                    i += 1
                    if i > len(curr_filter):
                        i = 1
                    # see the line before except ValueError, you'll know why it is i = 1 and not i = 0
                    img = get_with_overlay(img, curr_filter[i - 1], x, y, w, h)
                except ValueError:
                    pass

            # make the image a bit larger

            width = int(img.shape[1] * scale_percent / 100)
            height = int(img.shape[0] * scale_percent / 100)
            dim = (width, height)
            # resize image
            img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

            cv2.imshow("Camera", img)

            k = cv2.waitKey(1)

            if k == ord('q'):
                break
            elif k == 13:  # 13 is the enter key
                try:
                    take_snap(img, file_folder="C:\\Users\\suore\\Desktop\\Snappies")
                except:
                    print("Taking snapshot failed")

            # The next part checks for events from the GUI thread

            # snap event
            if event_snp.is_set():
                file_folder = pass_q.get()
                take_snap(img, file_folder)
                event_snp.clear()

            # change camera window size event
            if event_size.is_set():
                scale_percent = pass_q.get()
                print("Size change triggered, scale passed: ", scale_percent)
                event_size.clear()

            # change filter event
            if event_filter_change.is_set():
                curr_filter = pass_q.get()
                print("Filters changed to: ", curr_filter)
                event_filter_change.clear()

            # quit signal
            if event_quit.is_set():
                break

        else:
            print("Camera is not working!")
            break

    cv2.destroyAllWindows()
    cam.release()


def show_ui():
    app = QtWidgets.QApplication(sys.argv)
    win = AppWindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":

    # The OpenCV thread
    t1 = th.Thread(target=cam_loop)
    # The UI thread is the main thread

    # start the OpenCV thread
    t1.start()
    show_ui()
    t1.start()
