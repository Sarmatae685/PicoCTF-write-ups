---
tags: [Reverse Engineering, medium, binary, packed, picoctf-2022]
difficulty: medium
category: reverse-engineering
created: 2025-07-19
---

![Task desc](../assets/images/unpackme_image_1.png)


In this task, we are prompted to unpack the file `unpackme-upx`. 

---

As you see from the name and hint, the UPX packer was used. First, let's check if UPX was really used:  

![image_2](../assets/images/unpackme_image_2.png)  

This can also be seen by applying the `strings` command to the file and viewing the readable strings:

![image_3](../assets/images/unpackme_image_3.png)    

We can see to what filesize UPX has compressed the file. To "uncompress" it:

![image_4](../assets/images/unpackme_image_4.png)    
 
Let's use `ghidra` for decompilation:

```bash
sudo apt install ghidra
```

> [!TIP]
> How to create a project and import a file for decompilation shown in this [video](https://youtu.be/3Ikn8Y775Lk?si=Q16yBvc9Gy_5LyEs)    

![image_5](../assets/images/unpackme_image_5.png)    

Find the same `if` that is executed when you run the program, after first running `chmod +x unpackme_upx`.   

Let's convert hex to dec:  

![image_6](../assets/images/unpackme_image_6.png)    

![image_7](../assets/images/unpackme_image_7.png)

`picoCTF{up><_m3_f7w_5769b54e}`
