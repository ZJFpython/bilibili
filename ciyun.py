from wordcloud import WordCloud,ImageColorGenerator
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from os import path
import jieba

lj=path.dirname(__file__)
text=open(path.join(lj,'弹幕.txt'),encoding='utf-8').read()
jbText=' '.join(jieba.cut(text))
imgMask=np.array(Image.open(path.join(lj,'QQ截图20180812190927.png')))
wc=WordCloud(
    background_color='white',
    max_words=500,
    font_path='msyh.ttc',
    mask=imgMask,
    random_state=30
).generate(jbText)
ImageColorGenerator(imgMask)
plt.imshow(wc)
plt.axis('off')
plt.show()
wc.to_file(path.join(lj,'图1.png'))
print('成功保存词云图片！')


