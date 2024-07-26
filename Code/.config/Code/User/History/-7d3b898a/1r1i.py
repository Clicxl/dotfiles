import PIL.Image as pimg
import pilgram

def filter(file):
    img = pimg.open(file)
    print(pilgram)
    pilgram.lofi(img).save("filtered.jpg")


filter('InstaFilters/fearwell.jpg')

