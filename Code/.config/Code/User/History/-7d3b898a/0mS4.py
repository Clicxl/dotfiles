import PIL.Image as pimg
import pilgram

def filter(file):
    img = pimg.open(file)
    pilgram.brannan(img).save("filtered.jpg")
    img.show("Filtered.jpg")


filter('InstaFilters/fearwell.jpg')


