#usage:
# need to place in one directory with *.png
# chmod +x cut_frames.py
# python3 cut_frames.py
from PIL import Image

def extract_frames():
    print('Start frame extraction')

    img = Image.open('concat_v.png')
    print(f'Sprite sheet size (pix): {img.size}')

    frame_height = 720
    frame_width = 1280

    for i in range(66): #0-65
        frame_num = i + 1

        y_start = i * frame_height
        y_end = y_start + frame_height

        print(f'==Extracting frame {frame_num} (y: {y_start}-{y_end})==')

        # Cutting the frame (left, top, right, bottom)
        frame = img.crop((0, y_start, frame_width, y_end))

        frame_name = f"frame_{frame_num}.png"
        frame.save(frame_name)
        print(f'==Saved frame {frame_num}.png==')

    print('Extraction completed')

if __name__ == "__main__":
    extract_frames()
