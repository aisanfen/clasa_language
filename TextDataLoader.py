import cv2
import numpy as np
import os
import torch.utils.data as Data

class TextDataLoader:
    """
    path:图像存放的地址
    """
    def __init__(self,path):
        file_path=os.listdir(path)
        self.data=[]
        # self.classes=file_path
        # for index in self.data:
        #     image=cv2.imread(self.data[index])
        #     if image.empty():
        #         self.data.pop(index-1)
        self.classes=dict()  #分类
        # 取classes的映射
        for index,folder in enumerate(file_path):
            self.classes[folder]=index
        for image_folder in file_path:
            folder_path=os.path.join(path,image_folder)
            image=[os.path.join(folder_path,x) for x in os.listdir(folder_path)]
            for im in image:
                self.data.append([im,self.classes[image_folder]])

    def __getitem__(self, index):
        data_x=cv2.imread(self.data[index][0])
        data_x=cv2.resize(data_x,(224,224))
        data_x=cv2.cvtColor(data_x,cv2.COLOR_RGB2BGR)
        data_x = data_x.astype('float64') / 255
        data_x = np.array([data_x[:,:,0],data_x[:,:,1],data_x[:,:,2]])
        data_y=self.data[index][1]
        return data_x, data_y
    def __len__(self):
        return len(self.data)
    def flush(self):
        pass

if __name__ == '__main__':
    path='./picture_data/train'
    dataset=TextDataLoader(path)
    for index,(batch_x,batch_y) in enumerate(dataset):
        print(batch_x.shape,batch_y)
        break
    test_dataset = Data.DataLoader(
        dataset=dataset,
        batch_size=16,
        shuffle=True
    )
    # for index,(batch_x,batch_y) in enumerate(test_dataset):
    #     print(batch_x.shape,batch_y.shape)
    #     print(batch_x.shape,batch_y)
    #     break