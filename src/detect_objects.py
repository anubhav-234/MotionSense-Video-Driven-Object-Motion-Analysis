# ***************************************** IMPORTING LIBRARIES *********************************
import cv2
import math
import matplotlib.pyplot as plt
from get_background import get_background
from graphical_output import plot_graphs

# ************************************* SPEED DETECTION MAIN CODING ****************************

def main(video_path,fov,min_area) : 

    # Caputuring the video in a object named cap
    cap = cv2.VideoCapture(video_path)

    # Setting the height and width of the ouput screen
    width = 300
    height = 300
    mpp = fov/width # meter per pixel = field of View(meter) / width of screen

    # ***********************MAKING THE BACKGROUND FRAME USING RANDOM SAMPLING PROCEDURE**********

    # get the background model
    background = get_background(video_path,width,height)

    # convert the background model to grayscale format
    background = cv2.cvtColor(background, cv2.COLOR_BGR2GRAY)

    # Smoothening the image (Guassian Blurring followed by median Blurring)
    background = cv2.GaussianBlur(background,(5,5),0)
    background = cv2.medianBlur(background,5)

    # Background image
    # cv2.imshow('Detected Objects', background)

    #***************************GETTING THE FRAMES FROM VIDEO ONE BY ONE USING LOOP *********************
    
    # Making Some Global Varibles
    frame_count = 0
    speed_graph = []
    accelaration_graph = [] 
    first_idx=-1
    lastCentroids = []
    currentCentroids = []
    fps = cap.get(cv2.CAP_PROP_FPS)

    while (cap.isOpened()):
        ret, frame = cap.read()
        if(ret == False):
            break
        frame = cv2.resize(frame,(width,height))
        
        orig_frame = frame.copy()

        # IMPORTANT STEP: convert the frame to grayscale first
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Showing the black and white Picture 
        cv2.imshow("Black and white",gray)

        # Smoothening the image (Guassian Blurring followed by median Blurring)
        blur1 = cv2.GaussianBlur(gray,(5,5),0)
        blur2 = cv2.medianBlur(blur1,5)

        #showing the blur images
        cv2.imshow("Applied Guassian and Median Filter",blur2)

        # find the difference between current frame and base frame
        frame_diff = cv2.absdiff(blur2, background)
        #imges after background subtraction
        cv2.imshow("Background Substraction ",frame_diff)

        # thresholding to convert the frame to binary
        ret, thres = cv2.threshold(frame_diff, 50, 255, cv2.THRESH_BINARY)

        # Showing After threshold
        cv2.imshow("After Threholding ",thres)

        # USING SOME MORPHOLOGICAL OPERATIONS 
        # dilate the frame a bit to get some more white area...
        # ... makes the detection of contours a bit easier
        dilate_frame = cv2.dilate(thres, None, iterations=2)

        #After performing diltate operation
        cv2.imshow("After Morphological Operations ", dilate_frame)
        
        # append the final result into the `frame_diff_list`
        # find the contours around the white segmented areas
        contours, hierarchy = cv2.findContours(dilate_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        
        distance = []
        currentCentroids = []

        #Itterating Over contours
        for i, val in enumerate(contours):
            M = cv2.moments(val)
            if M['m00'] > min_area:
                cx = int(M['m10']/M['m00'])
                cy = int(M['m01']/M['m00'])
                cv2.drawContours(frame, contours, i, (0, 255, 0), 3) 
                cv2.circle(frame, (cx, cy), 7, (0, 0, 255), -1)   
                
                allDist = []
                for prev in lastCentroids:
                    allDist += [[prev[0],math.sqrt((cx-prev[1])**2 + (cy-prev[2])**2)]]
                
                dist = 10000000
                id   = -1
                if len(allDist) > 0:
                    for l in allDist:
                        if l[1] < dist:
                            dist = l[1]
                            id   = l[0]
                else :
                    dist = 0
                    id = first_idx+1
                    first_idx = first_idx+1
                    speed_graph += [[]]
                    accelaration_graph += [[]]

                distance += [[dist,id]]
                
                currentCentroids += [[id,cx,cy]]
            # print(f"x: {cx} y: {cy}")
        lastCentroids = currentCentroids
        idx = -1

        for contour in contours:
            # continue through the loop if contour area is less than 500...
            # ... helps in removing noise detection
            if cv2.contourArea(contour) > min_area:
                idx = idx+1
                speed = round(distance[idx][0]*fps*mpp,2)
                accelaration = 0
                last_idx = len(speed_graph[distance[idx][1]])-1
                if last_idx >= 0:
                    accelaration = round((speed - speed_graph[distance[idx][1]][last_idx])*fps,2)
                if frame_count % 50 == 0 :
                    speed_graph[distance[idx][1]] += [speed]
                    accelaration_graph[distance[idx][1]] += [accelaration]

                # get the xmin, ymin, width, and height coordinates from the contours
                (x, y, wb, hb) = cv2.boundingRect(contour)
                # draw the bounding boxes
                cv2.rectangle(orig_frame, (x, y), (x+wb, y+hb), (0, 0, 255), 2)
            
                orig_frame = cv2.putText(orig_frame, str(speed)+' MPS ', (x, y-20),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (100,0,100), 3)
                orig_frame = cv2.putText(orig_frame, str(accelaration)+' MPS2 ', (x, y+hb+20),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (100,0,100), 3)

        #Original Frame Countours
        cv2.imshow('Detected Objects with Countours',frame)                    
        #Original Frame bounding box
        frame_count = frame_count+1
        cv2.imshow('Detected Objects with bounding box', orig_frame)
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
            
    cap.release()
    cv2.destroyAllWindows()
    plot_graphs(speed_graph,accelaration_graph,fps)  

    

    

