import numpy as np
import cv2


def frameFromCam(camNum=1):
    """

    :param camNum: מספר המצלמה, מצלמה 0 זו המצלמה הראשונה, ומצלמה 1 זו המצלמה השניה. בד"כ המצלמה השניה המצלמה החיצונית, אך במחשב נייח שאין בו מצלמה פנימית המצלמה החיצונית תהיה מצלמה 0
    :return: frame Object.
    """
    cap = cv2.VideoCapture(camNum)
    ret, frame = cap.read()
    cap.release()
    return frame
