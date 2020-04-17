import os
import cv2

if __name__=='__main__':
    path=r'E:/code/class_language/picture_data/train'
    file_path=os.listdir(path)
    data=[]
    for image_folder in file_path:
        folder_path = os.path.join(path, image_folder)
        image = [os.path.join(folder_path, x) for x in os.listdir(folder_path)]
        for im in image:
            data.append(im)
    # self.classes=file_path
    print(data,'\n',len(data)-1)
    for index in range(len(data)-1):
        # print(index)
        try:
            image=cv2.imread(data[index])
        except Exception as e:
            print(e)
            print(data[index])
        # print(image)
        if image is None:
            print(data[index])
            # data.pop(index)
    # print(data)