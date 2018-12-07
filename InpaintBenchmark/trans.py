
f = open('val_rect_mask_img_flist.txt')
ff = open('temp.txt', 'w')

for per in f:
    print (per)
    new_dir = './' + str ( per.strip().replace('/home/lhy/datasets/', '') )
    print (new_dir)
    ff.write(new_dir + '\n')

f.close()
ff.close()
