import torch
import torch.nn as nn
import torch.nn.functional as F
import matplotlib.pyplot as plt
import os
import numpy as np
import pandas as pd
from torch.autograd import Variable
import cv2
from random import shuffle
import torch.utils.data as Data
# 参数
from tqdm import tqdm

from TextDataLoader import TextDataLoader
from VGG16 import VGG16

EPOCH = 1
BATCH_SIZE = 10    # 批处理数量
TIME_STEP = 224       # rnn time step /image height
INPUT_SIZE = 224      # rnn input step /image width
LR = 0.01            # learning rate



# 设置自己的装载器


if __name__ == '__main__':
    dataset = TextDataLoader('picture_data/train')

    with torch.no_grad():
        model = VGG16()
    loss_func = torch.nn.CrossEntropyLoss()
    opt = torch.optim.Adam(model.parameters(), lr=0.01)

    train_dataset = Data.DataLoader(
        dataset=dataset,
        batch_size=16,
        shuffle=True
    )
    model.cpu()
    model.train()
    # model.cuda()

    for epoch_times in range(60):
        loss_count = []
        #异常处理
        # print(train_dataset)
        # for index in range(len(train_dataset)):
        for step, (batch_x, batch_y) in enumerate(tqdm(train_dataset)):
        #     try:
        #         batch_x,batch_y=train_dataset[index]
                batch_x = batch_x.float().cpu()
                # #print(batch_x.type())
                # batch_x=batch_x.cpu()
                batch_y = batch_y.long().cpu()
                # batch_y=batch_y.cpu()
                out = model(batch_x)
                output=out.cpu().detach().numpy().squeeze()
                # print("识别结果%s 正确结果: %s" % (np.argmax(output),batch_y))
                loss = loss_func(out, batch_y)
                opt.zero_grad()
                loss.backward()
                opt.step()
                loss_count.append(loss)
                if step !=0 and step % 500 == 0: #取模条件都忘记，，，，，
                    print("loss:%s " % (loss.item()))
                # if index!=0 and index%10==0:
                #     print("loss:%s " % (loss.item()))
                if epoch_times != 0 and epoch_times % 20 == 0:
                    save_path = './net_pkl/VGG16_' + str(epoch_times / 10) + '.pkl'
                    torch.save(model, save_path)
            # except Exception as e:
            #     continue

    # for epoch in range(1):
    #     for step, (batch_x, batch_y) in enumerate(torch_dataset):
    #         print(batch_y)
            # out = model(torch.from_numpy(batch_x.reshape([224, 224, 3])).float())
            # loss = loss_func(out, torch.tensor([batch_y]).long())
            # opt.zero_grad()
            # loss.backward()
            # opt.step()
            # loss_count.append(loss)
            # if step % 100 == 0:
            #     print("loss:%s " % (loss.item()))
#
#



