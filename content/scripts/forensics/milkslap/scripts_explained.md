## `cut_frames.py`


### Visual explanation


How the frames are cropped:

`.crop()` takes 1 tuple as parameter with coords:
```python
img.crop((left, top, right, bottom))
```

`.crop()` parameters, that will be passed to the method:
```python
frame = img.crop((0, y_start, frame_width, y_end))
#                 ↑  ↑        ↑           ↑
#                 │  │        │           └─ bottom (y2)
#                 │  │        └─ right (x2) = 1280
#                 │  └─ top (y1) = y_start  
#                 └─ left (x1) = 0
```

```
Original image (1280x47520):
      0                               1280
   0  ┌─────────────────────────────────┐ (0,0)      (1280,0)
      │                                 │
      │         Frame 1                 │ ← crop(0, 0, 1280, 720)
      │                                 │
 720  ├─────────────────────────────────┤ (0,720)    (1280,720)
      │                                 │
      │         Frame 2                 │ ← crop(0, 720, 1280, 1440)  
      │                                 │
1440  ├─────────────────────────────────┤ (0,1440)   (1280,1440)
      │                                 │
      │         Frame 3                 │ ← crop(0, 1440, 1280, 2160)
      │                                 │
2160  ├─────────────────────────────────┤ (0,2160)   (1280,2160)
      │                                 │
      │            ...                  │
      │                                 │
47520 └─────────────────────────────────┘ (0,47520)  (1280,47520)
```
As we move through the frames from top to bottom, we can imagine that we are moving at `-720`, `-1440`, `-2160` pixels, and so on. Like at the math.
But `PIL` (Python Imaging Library) coords are always Positive and always go down:

```
PIL coordinates (always positive):
     0  ┌─────────────→ X (to the right)
        │
        │  (100, 50)  ← x=100, y=50
        │      ●
        │
        ↓
        Y (down)
```
this would be wrong:
```python
frame = img.crop((0, -720, 1280, -1440))
```

in the script:
```python
# concat_v.png 1280x47520, 66 frames with 720 pixel height
frame_width = 1280
frame_height = 720

for i in range(3):  # ex. first 3 frames 
    # Calculating the position of the first frame
    y_start = i * 720    # 0, 720, 1440
    y_end = y_start + 720    # 720, 1440, 2160
    
    print(f"Frame {i+1}: y={y_start} to {y_end}")
    
    # cropping (left=0, top=y_start, right=1280, bottom=y_end)
    frame = img.crop((0, y_start, 1280, y_end))
    
    # Result: frame sized 1280x720
    print(f"Result size: {frame.size}")  # (1280, 720)
```

## `zsteg_to_each_frame.py`
```bash
for frame in frame_*.png;
```

Here bash searches for all files matching the pattern and extends `frame_*.png` to file-list.
```bash
frame_*.png → frame_1.png frame_2.png frame_3.png ... frame_66.png
```

it equals to 
```bash
echo frame_*.png
```
output.


### `2>/dev/null`

Streams in bash:
```
0 = stdin  (standard input)
1 = stdout (standard output) 
2 = stderr (error stream)
```

```bash
zsteg $frame 2>/dev/null | grep -iE "pico|ctf|flag"
```

So what;s going on:
1. `zsteg` has bugs with some PNG
2. errors go to `stderr` (stream 2)
3. `grep` filters only stdout (stream 1)
4. errors go through `grep` ass well and clog the outlet


Here `2>/dev/null` is needed to avoid `zsteg` `stderr` about it's buffer overloaded. Without it we would see the following:
```bash
NOTHING YET
NOTHING YET
NOTHING YET
NOTHING YET
NOTHING YET
NOTHING YET
/var/lib/gems/3.3.0/gems/zsteg-0.2.13/lib/zsteg/checker/wbstego.rb:41:in `to_s': stack level too deep (SystemStackError)
        from /var/lib/gems/3.3.0/gems/iostruct-0.5.0/lib/iostruct.rb:180:in `inspect'
        from /var/lib/gems/3.3.0/gems/zsteg-0.2.13/lib/zsteg/checker/wbstego.rb:41:in `to_s'
        from /var/lib/gems/3.3.0/gems/iostruct-0.5.0/lib/iostruct.rb:180:in `inspect'
        from /var/lib/gems/3.3.0/gems/zsteg-0.2.13/lib/zsteg/checker/wbstego.rb:41:in `to_s'
        from /var/lib/gems/3.3.0/gems/iostruct-0.5.0/lib/iostruct.rb:180:in `inspect'
        from /var/lib/gems/3.3.0/gems/zsteg-0.2.13/lib/zsteg/checker/wbstego.rb:41:in `to_s'
        from /var/lib/gems/3.3.0/gems/iostruct-0.5.0/lib/iostruct.rb:180:in `inspect'
        from /var/lib/gems/3.3.0/gems/zsteg-0.2.13/lib/zsteg/checker/wbstego.rb:41:in `to_s'
         ... 10906 levels...
        from /var/lib/gems/3.3.0/gems/zsteg-0.2.13/lib/zsteg.rb:26:in `run'
        from /var/lib/gems/3.3.0/gems/zsteg-0.2.13/bin/zsteg:8:in `<top (required)>'
        from /usr/local/bin/zsteg:25:in `load'
        from /usr/local/bin/zsteg:25:in `<main>'
NOTHING YET
NOTHING YET
```

with `2>dev/null` we'll have:
```bash
zsteg frame_1.png 2>/dev/null | grep -iE "pico|ctf|flag"
├── stdout: "b1,r,lsb,xy .. text: "picoCTF{..."  → PASSED to grep
└── stderr: "SystemStackError..."                → NOT PASSED to grep (will be IGNORED due 2>dev/null)
```

