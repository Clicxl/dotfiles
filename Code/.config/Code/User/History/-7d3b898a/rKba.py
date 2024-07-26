import PIL.Image as pimg
import pilgram

def filter(file):
    img = pimg.open(file)
    pilgram.gingham(img).save("filtered.jpg")
    img.show("Filtered.jpg")


filter('InstaFilters/fearwell.jpg')


