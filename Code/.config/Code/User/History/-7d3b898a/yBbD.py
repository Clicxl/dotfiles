import PIL.Image as pimg
import pilgram

def filter(file):
    img = pimg.open(file)
    pilgram.lofi(im).save("filtered.jpg")


filter('InstaFilters/fearwell.jpg')

