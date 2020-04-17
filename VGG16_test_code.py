import torch
from PIL import Image
from torchvision import transforms
import numpy as np

device = torch.device('cuda')
classes=('Chinese','English')
# 修改图片大小
transform = transforms.Compose([transforms.Resize(256),  # 更改大小
                                transforms.CenterCrop(224),  # 中心切割
                                transforms.ToTensor(),  # 归一化
                                transforms.Normalize(
    mean=(
        0.5, 0.5, 0.5), std=(
            0.5, 0.5, 0.5))
])


def prediect(image_path):
    net = torch.load('E:/code/class_language/VGG16.pkl')  # 加载模型
    net=net.to(device)
    torch.no_grad()
    img = Image.open(image_path)
    img = transform(img).unsqueeze(0)
    print(img.size())
    img_ = img.to(device)

    outputs = net(img_)
    outputs=outputs.cpu().detach().numpy().squeeze()
    prediected = np.argmax(outputs)
    print(prediected)
    print("this picture maybe:", classes[prediected])


def handle_uploaded_file(f):
    prediect(f)

if __name__ == '__main__':
    handle_uploaded_file('E:/code/class_language/test_image/test_2.jpg')
