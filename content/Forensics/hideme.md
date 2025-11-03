---
tags: [forensics, medium, steganography, picoctf-2023]
difficulty: medium
category: forensics
created: 2025-07-27
---

![Task desc](../assets/images/hideme_image_1.png)    

---

Try `zsteg` and see that there is a directory and at least 1 file in it.  

![image_2](../assets/images/hideme_image_2.png)  

Same is confirmed by `binwalk`:  

![image_3](../assets/images/hideme_image_3.png)  

Extract with the `-e` parameter:  

![image_4](../assets/images/hideme_image_4.png)  

![image_5](../assets/images/hideme_image_5.png)  

You can try the OSR tool `tesseract`, but it didn't work very well, so let's rewrite it manually:  

![image_6](../assets/images/hideme_image_6.png)  

`picoCTF{Hiddinng_An_imag3_within_@n_ima9e_96539bea}`  
