import cv2
cap = cv2.VideoCapture(0)
if not cap:
    print('vedio does not captured')
else:    
    frame_widht = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    codecc = cv2.VideoWriter_fourcc(*'mp4v')
    record = int(input("do u wanna record the video:"))
    if record == 0:
        print("ohk , thanks")
        while True:
            ret , frames = cap.read()
            if not ret:
                break
            cv2.imshow("capturing",frames)
            if cv2.waitKey(1) & 0xFF == ord('r'):
                break
        cap.release()   
    else:
        video_name = input("tell the name of the video to be saved:")
        recorder = cv2.VideoWriter(video_name,codecc,20,(frame_widht,frame_height))
        while True:
            ret , frames = cap.read()
            if not ret:
                break
            else:
                cv2.imshow("recording",frames)
                recorder.write(frames)
                if cv2.waitKey(1) & 0xFF == ord('r'):
                    break
        recorder.release()   
        cap.release()
    cv2.destroyAllWindows()         
    
