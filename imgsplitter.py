import sys
import argparse
import imageio
import os

def split(img,out_folder,rows,cols,name,ext):
    for f in os.listdir(out_folder): #remove in case previous spliot exists
        os.remove(os.path.join(out_folder,f))

    width,height = img.shape[1]//cols,img.shape[0]//rows
    
    for i in range(rows):
        for j in range(cols): #save slice of the image
            imageio.imsave(os.path.join(out_folder,f'{name}_{i}{j}{ext}'),img[i*height:(i+1)*height,j*width:(j+1)*width,:])

def exec(args):
    rows,cols = map(int,args.style)
    image_name = os.path.basename(args.image)
    
    name,ext = image_name[:image_name.find(".")],image_name[image_name.find("."):]
    img = imageio.imread(args.image)
    out_dir = os.path.join(args.out,name)

    os.makedirs(out_dir,exist_ok=True)
    split(img,out_dir,rows,cols,name,ext)
        
parse = argparse.ArgumentParser()
parse.add_argument('image' ,type=str,help='image to split')
parse.add_argument('--style','-s',default="33", type=str,help='How the image should be split string of two characters with row and col Example: 23 (2 rows,3 cols)')
parse.add_argument('--out','-o' ,default="",type=str,help='Output Directory')
args = parse.parse_args()
exec(args)