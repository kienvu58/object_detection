import cv2


def detect(img, cascade):
    rects = cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4, minSize=(10, 10),
                                     flags=cv2.CASCADE_SCALE_IMAGE)
    if len(rects) == 0:
        return []
    rects[:, 2:] += rects[:, :2]  # x, y, h, w -> x1, y1, x2, y2
    return rects


def draw_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)


if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    # cascade = cv2.CascadeClassifier("data/haarcascades/haarcascade_frontalface_default.xml")
    # cascade = cv2.CascadeClassifier("data/phone_cascades/cascade.xml")
    cascade = cv2.CascadeClassifier("data/rubik_cascades/cascade.xml")
    # cascade = cv2.CascadeClassifier("data/card_cascades/cascade.xml")

    while True:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # gray = cv2.equalizeHist(gray)

        rects = detect(gray, cascade)
        draw_rects(img, rects, (0, 255, 0))
        cv2.imshow("detect", img)

        if 0xFF & cv2.waitKey(5) == 27:
            break

    cv2.destroyAllWindows()
