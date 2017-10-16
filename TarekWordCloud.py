from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import numpy as np

def word(texto,bkgd,saida,rand):

    text = open(texto,'r').read()
    stopwords = set(STOPWORDS)
    img = np.array(Image.open(bkgd))

    wc = WordCloud(background_color="white", max_words=2000, mask=img,stopwords=stopwords, random_state=rand,width=8000,height=8000) #, random_state=42
    wc.generate(text)
    image_colors = ImageColorGenerator(img)

    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.figure(figsize=(80,80))
    plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
    plt.axis("off")
    plt.savefig(saida, facecolor='k')
    plt.figure()
    plt.imshow(img, cmap=plt.cm.gray, interpolation="bilinear")
    plt.axis("off")
    plt.show()