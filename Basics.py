# for face detection

# import cv2
# img = cv2.imread("D:\\Photos\\InFrame_1573848717736.jpg",1)
# resized = cv2.resize(img, (int (img.shape[1]/2),int (img.shape[0]/2)))
# # print(img.shape)
# cv2.imshow("SS",resized)
# cv2.waitKey()
# cv2.destroyAllWindows()



# for capturing first frame through webcam

# import cv2,time
# video = cv2.VideoCapture(0)
# check,frame = video.read()
# print(check)
# print(frame)
# time.sleep(3)
# cv2.imshow("Capture",frame)
# cv2.waitKey(0)
# video.release()
# cv2.destroyAllWindows()




# now capturing the video

# import cv2,time
# video = cv2.VideoCapture(0)
# a = 1
# while True:
#     a = a + 1
#     check,frame = video.read()
#     print(frame)
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     cv2.imshow("Capture",gray)
#     key = cv2.waitKey(1)
#     if key == ord('q'):
#         break
# print(a)
# video.release()
# cv2.destroyAllWindows()




