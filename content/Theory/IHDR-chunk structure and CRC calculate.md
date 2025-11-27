---
date: 2025-08
tags:
  - forensics
  - png
  - theory
---

> [!TIP]
> This note may be helpful for solving:
> * [advanced-potion-making](../Forensics/advanced-potion-making.md) 

<br/>

![IHDR Structure](../content/assets/images/IHDR_structure.png)  
[Source](https://stackoverflow.com/questions/54845745/not-able-to-read-ihdr-chunk-of-a-png-file) that helped me.

<br/>

> [!NOTE]
> `89 50 4E 47 0D 0A 1A 0A` .PNG signature (Check other sigs [here](https://en.wikipedia.org/wiki/List_of_file_signatures))

**IHDR chuck follows after signature with no padding inbetween**

```
00 00 00 0D : IHDR chunk length(4 bytes) | IHDR length always fixed for PNG - 13 bytes!
49 48 44 52 : IHDR chunk type(Identifies chunk type to be IHDR)
00 00 05 90 : Image width in pixels(variable 4)  | 1424 pixels
00 00 01 11 : Image height in pixels(variable 4) | 273  pixels
08	        : Bit depth (1 byte)
06          : Color type (1 byte)
00          : Compression method (1 byte) 
00          : Filter method (1 byte)
00          : Interlace method (1 byte)
E5 8A 82 33 : CRC checksum (4 bytes) 
```

Detailed PNG Specification found [here](https://www.libpng.org/pub/png/spec/1.2/PNG-Chunks.html).<br><br>
`PNG` uses `CRC-32` 
To calculate `CRC-32`, we need to take ONLY:
```
   -----     length NOT INCLUDED
49 48 44 52  (IHDR - chunk type)
00 00 05 90  (width)
00 00 01 11  (height) 
08           (bit depth)
06           (color type)
00           (compression)
00           (filter)
00           (interlace)
```
the whole IHDR EXCEPT length (first 4 bytes): `4948445200000590000001110806000000` --> CRC input  
CRC32/ISO-HDLC: `E58A8233`  Good online tool: [CRC Calculator Online](https://calctools.online/en/checksum/crc)                                      
