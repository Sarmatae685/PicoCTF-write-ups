![Task desc](../assets/images/Enhance!_image_1.png)


In this task, we have an SVG file that hides a flag. 



![image_2](../assets/images/Enhance!_image_2.png)


I tried various tools to find the flag in the image, such as: 

`binwalk -e`, `exiftool`, `strings`, `xxd`, `zsteg` but there is no mention of the flag in their outputs



![image_3](../assets/images/Enhance!_image_3.png)


The image does not provide us with any information about the flag, so let's look at the source code: 



![image_4](../assets/images/Enhance!_image_4.png)

The parts of the flag are located near `tpan`. Let's copy the code into a separate file: 


![image_5](../assets/images/Enhance!_image_5.png)

picoCTF{3nh4nc3d_d0a757bf}
