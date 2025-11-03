---
tags: [forensics, medium, pcap, picoctf-2023]
difficulty: medium
category: forensics
created: 2025-08-09
---

![Task desc](../assets/images/PcapPoisoning_image_1.png)

This task boils down to simply reviewing packages and looking for clues.

---

The traffic itself consists mainly of FTP Data protocols and related TCP packets.

Let's try to trace the TCP stream:

![image_2](../assets/images/PcapPoisoning_image_2.png)


Found: `username root    password toor624a8b6}`


![image_3](../assets/images/PcapPoisoning_image_3.png)


Leafing through the packages, I found the following clues:


```
iBwaWNvQ1RGe1 Flag is close=
gc2VjcmV0OiBwaWNvQ1RGe
```


None of these entries produce readable text when decoded from base64.

And finally, in package 507, we find the flag:


![image_4](../assets/images/PcapPoisoning_image_4.png)

![image_5](../assets/images/PcapPoisoning_image_5.png)

`picoCTF{P64P_4N4L7S1S_SU55355FUL_4624a8b6}`
 
