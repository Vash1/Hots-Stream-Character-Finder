import numpy as np
from PIL import Image

list_im = [(str(i)+'_blue.png',str(i)+'_red.png') for i in range(76)]

#imgs_l    = [ Image.open('./avatars/'+i[0]) for i in list_im ] 
#imgs_r    = [ Image.open('./avatars/'+i[1]) for i in list_im ] 

imgs_l    = [ Image.open('./avatars360p/'+i[0]) for i in list_im ] 
imgs_r    = [ Image.open('./avatars360p/'+i[1]) for i in list_im ] 

# for a vertical stacking it is simple: use vstack
imgs_comb = np.vstack( i for i in imgs_l )
imgs_comb = Image.fromarray( imgs_comb)

imgs_comb2 = np.vstack( i for i in imgs_r )
imgs_comb2 = Image.fromarray( imgs_comb2)

new_im = Image.new('RGB', (imgs_comb.width*2, imgs_comb.height))
new_im.paste(imgs_comb, (0, 0))
new_im.paste(imgs_comb2, (imgs_comb.width, 0))
"""
new_im = Image.new('RGB', (imgs_comb.width*2,imgs_comb.height))
print(new_im.height)
print(new_im.width)

new_im.paste(imgs_comb, (0,0))
i = 0
for im in imgs_r:
  new_im.paste(im, (45*i,14))
  i+=1
"""
new_im.save( 'smallHeroes.jpg' )