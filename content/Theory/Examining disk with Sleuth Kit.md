---
date: 2025-08
tags:
  - forensics
  - sleuthkit
  - theory
---

📒 Notes with command examples to examine a disk in forensics challenges like:
- [Sleuthkit Apprentice](../Forensics/Sleuthkit%20Apprentice.md)
- [DISKO 2](../Forensics/DISKO%202.md)
- [DISKO 3](../Forensics/DISKO%203.md)
- [Dear Diary](../Forensics/Dear%20Diary.md)

and many more (some of them I solved via `Autopsy 4.22.0` for Windows 11)

#### View the partitions on the disk and find out from which offset they start:
```bash
mmls disk.flag.img (easier to perceive)
fdisk -x disk.flag.img (or -l option, does literally the same)
```
#### Detailed information about partition:
```bash
fsstat -o 1140736 disk.flag.img > info.txt
```

#### Find out what file system is in the partition:
```bash
fsstat -o 1140736 disk.flag.img | grep 'File System Type'
# -o 1140736: offset - number of sectors from the beginning of the image
# for ex. if the sector = 512 bytes, offset in bytes: 1140736 × 512 = 584.056.832 
```

#### Check directories:
```bash
fls -o 1140736 disk.flag.img (easier)
fls -i raw -f ext4 -o 2048 -r disko-2.dd > <filename>
# -i raw: specify. that the input file disk.flag.img is the "raw" image of the disk.
# -f ext4: the type of file system inside the disk image
```

> [!NOTE]
> 📌 Why `raw`?: Because `fls` (and other Sleuth Kit tools) should know how to interpret the input file. If it were an E01 (EnCase) image, we would use `-i ewf`. If it were an > aff (Advanced Forensic Format) image, it would be `-i aff`. 
> But since `disk.flag.img` is a simple sequence of bytes, `raw` is the correct choice.

#### If found right dir (usually `/root`), check what's inside recursively: 
```bash
fls -o 1140736 disk.flag.img -r 204
# -r: Recurse on directory entries
# 204: inode 
```

> [!NOTE]
> 📌 `inode` stores metadata about a file or directory, but does NOT store the actual contents of the file.

#### View contents of the file by its inode:
```bash
icat -i raw -f ext4 -o 1140736 -r disk.flag.img 1844
```

#### Download file by its inode:
```bash
icat -o 1140736 disk.flag.img 1844 > <filename>
```

#### Extract the partition into an `.img` format and mount the volume:
```bash
dd if=disko-2.dd of=part1.img bs=512 skip=2048 count=51200
sudo mkdir /mnt/part1
sudo mount -o loop part1.img /mnt/part1/
```

#### Extract raw binary data by inode and output in hex-dump format:
```bash
icat -o 1140736 disk.flag.img <inode> | xxd
```

#### Example in Dear Diary:
```bash
icat -o 1140736 disk.flag.img 8 | xxd | grep '.txt' -A4 -B2
# 8: inode 8 - system inode, ext4 file system journal
# xxd: shows offset + hex bytes + ASCII interpretation
# -A4 (--after-context=NUM): will show 4 lines AFTER the line with the found match
# -B2 (--before-context=NUM): will show 2 lines BEFORE the line with the found match
```
#### Example output:
```bash
001f8820: 666f 7263 652d 7761 6974 2e73 6800 0000  force-wait.sh...
001f8830: 3407 0000 c403 1201 696e 6e6f 6375 6f75  4.......innocuou
001f8840: 732d 6669 6c65 2e74 7874 0000 0000 0000  s-file.txt......
001f8850: 0000 0000 0000 0000 0000 0000 0000 0000  ................
001f8860: 0000 0000 0000 0000 0000 0000 0000 0000  ................
001f8870: 0000 0000 0000 0000 0000 0000 0000 0000  ................
001f8880: 0000 0000 0000 0000 0000 0000 0000 0000  ................
--
001fbc20: 666f 7263 652d 7761 6974 2e73 6800 0000  force-wait.sh...
001fbc30: 3407 0000 1c00 1201 696e 6e6f 6375 6f75  4.......innocuou
001fbc40: 732d 6669 6c65 2e74 7874 0000 3507 0000  s-file.txt..5...
001fbc50: a803 1101 6f72 6967 696e 616c 2d66 696c  ....original-fil
001fbc60: 656e 616d 6500 0000 0000 0000 0000 0000  ename...........
001fbc70: 0000 0000 0000 0000 0000 0000 0000 0000  ................
001fbc80: 0000 0000 0000 0000 0000 0000 0000 0000  ................
```





