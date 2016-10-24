import urllib
import cv2
import os
import numpy as np
import uuid


def download_images(link, path, width, height):
    urls = urllib.urlopen(link).read().decode(encoding="utf8")

    if not os.path.exists(path):
        os.makedirs(path)

    for url in urls.split('\n'):
        try:
            print str(url)
            filename = path + str(uuid.uuid4()).replace("-", "") + ".jpg"
            urllib.urlretrieve(url, filename)
            image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
            if image is None:
                os.remove(filename)
            else:
                resized_image = cv2.resize(image, (width, height))
                cv2.imwrite(filename, resized_image)

        except Exception as e:
            print str(e)


def remove_uglies(images_path, ugly_images_path):
    for img_file in os.listdir(images_path):
        for ugly_file in os.listdir(ugly_images_path):
            try:
                img_fn = images_path + str(img_file)
                ugly_img = cv2.imread(ugly_images_path + str(ugly_file))
                img = cv2.imread(img_fn)
                if ugly_img.shape == img.shape and not (np.bitwise_xor(ugly_img, img).any()):
                    print "Delete ugly image: "
                    print img_file
                    os.remove(img_fn)

            except Exception as e:
                print str(e)


def create_description_file_for_negative_images(images_path, filename):
    for image in os.listdir(images_path):
        with open(filename, 'a') as f:
            line = images_path + str(image) + '\n'
            f.write(line)


def create_description_file_for_positive_images(images_path, filename, width, height):
    for image in os.listdir(images_path):
        with open(filename, 'a') as f:
            coordinates = " %d %d %d %d %d" % (1, 0, 0, height, width)
            line = images_path + str(image) + coordinates + '\n'
            f.write(line)


def crop_square(images_path, saved_path):
    for img_fn in os.listdir(images_path):
        img = cv2.imread(images_path + str(img_fn))
        h, w, _ = img.shape
        a = min(w, h)
        img = img[0:a, 0:a]
        cv2.imwrite(saved_path + str(img_fn), img)


def resize(images_path, width, height):
    for img_fn in os.listdir(images_path):
        img = cv2.imread(images_path + str(img_fn), cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, (width, height))
        cv2.imwrite(images_path + str(img_fn), img)


if __name__ == "__main__":
    # bg_images_link = "http://image-net.org/api/text/imagenet.synset.geturls?wnid=n04105893"
    # bg_images_link = "http://image-net.org/api/text/imagenet.synset.geturls?wnid=n03045800"
    # bg_images_link = "http://image-net.org/api/text/imagenet.synset.geturls?wnid=n02472987"
    bg_path = "data/bg/"
    uglies_path = "data/uglies/"
    pos_path = "data/pos/"
    # download_images(bg_images_link, bg_path, 100, 100)
    # remove_uglies(bg_path, uglies_path)
    # create_description_file_for_negative_images(bg_path, "bg.txt")
    # crop_square("data/raw_phone_images/", pos_path)
    # resize(pos_path, 100, 100)
    # create_description_file_for_positive_images(pos_path, "pos.txt", 100, 100)
