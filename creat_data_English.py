'''
想要学习Python？Python学习交流群：984632579满足你的需求，资料都已经上传群文件，可以自行下载！
'''
import random
import os
from PIL import Image, ImageDraw, ImageFont

#处理特殊字符
# def text_replace(text):
#     text=text.replace(' ','\t')
#     text = text.replace('’', '\t')


def getRandomFont():
    font_path='./font_ttf/font_English'
    dirs=os.listdir(font_path)
    font=random.choice(dirs)
    return str(font)

# 随机选取颜色
def getRandomColor():
    '''获取一个随机颜色(r, g, b)格式的'''
    c1 = random.randint(0, 255)
    c2 = random.randint(0, 255)
    c3 = random.randint(0, 255)
    return (c1, c2, c3)

# 设置字体样式
def setfont():
    font_size = random.randint(23, 40)
    font = ImageFont.truetype('./font_ttf/font_English/%s' % getRandomFont(), font_size, encoding='unic')
    name = getRandomFont()
    return name, font
class ImgText:

    def __init__(self,new_img, text):
        # 预设宽度 可以修改成你需要的图片宽度
        self.width = 256
        # 文本
        self.text = text
        self.new_img=new_img
        self.name,self.font=setfont()
        # 段落 , 行数, 行高
        self.duanluo, self.note_height, self.line_height = self.split_text()
    def get_duanluo(self,text):
        draw = ImageDraw.Draw(self.new_img)
        # 所有文字的段落
        duanluo = ""
        # 宽度总和
        sum_width = 0
        # 几行
        line_count = 1
        # 行高
        line_height = 0
        for char in text:
          width, height = draw.textsize(char, self.font)
          sum_width += width
          if sum_width > self.width: # 超过预设宽度就修改段落 以及当前行数
            line_count += 1
            sum_width = 0
            duanluo += '\n'
          duanluo += char
          line_height = max(height, line_height)
        if not duanluo.endswith('\n'):
          duanluo += '\n'
        return duanluo, line_height, line_count
    def split_text(self):
        # 按规定宽度分组
        max_line_height, total_lines = 0, 0
        allText = []
        for text in self.text.split('\n'):
          duanluo, line_height, line_count = self.get_duanluo(text)
          max_line_height = max(line_height, max_line_height)
          total_lines += line_count
          allText.append((duanluo, line_count))
        line_height = max_line_height
        total_height = total_lines * line_height
        return allText, total_height, line_height
    def draw_text(self):
        """
        绘图以及文字
        :return:
        """
        note_img=self.new_img
        draw = ImageDraw.Draw(note_img)
        image_size =self.new_img.size
        print(self.text)
        # 添加噪点
        for i in range(5):
            x1 = random.randint(0, image_size[1])
            x2 = random.randint(0, image_size[1])
            y1 = random.randint(0, image_size[0])
            y2 = random.randint(0, image_size[0])
            draw.line((x1, x2, y1, y2), fill=getRandomColor())
        fnt=self.font

        # x ,y=0,0

        x,y=0,0
        for duanluo, line_count in self.duanluo:
            fnt_size = fnt.getsize(duanluo)
            width=(image_size[0]-fnt_size[0])/2
            x=width if width>0 else 4
            # print(x)
            if(y==0):
                y=(image_size[1]-self.line_height * line_count)/2
            draw.text((x, y), duanluo, fill=getRandomColor(), font=fnt)
            y +=self.line_height * line_count
            # print("x,y",x,y)
        note_img.save("result.png")
def new_image(
        width,
        height,
        text='default',
        color=(255,255,218),
        show_image=False,number=0):
    color=getRandomColor()
    new_img = Image.new('RGBA', (int(width), int(height)), color)
    #text=text.replace(' ','\t')
    n=ImgText(new_img, text)
    n.draw_text()
    # 存文件
    #print(number)
    new_img.save(r'./picture_dateset/train/English/English_%s.png'%(str(number)).rjust(5,'0'))

# 读取批处理文件
def new_image_with_file(fn):
    image_number = 0
    with open(fn, encoding='utf-8')as f:

        for line in f:
            line = line.strip()
            if line:
                ls = line.split(',')
                if "#" == line[0] or len(ls) < 2:
                    continue
                new_image(*ls,number=image_number)
                image_number=image_number+1
if __name__ == '__main__':
  new_image_with_file('./image_data_English.txt')