from PIL import Image
import os

img_dir = 'statics/img'

for root, dirs, files in os.walk(img_dir):
    for f in files:
        if f.lower().endswith(('.jpg', '.jpeg', '.png')):
            path = os.path.join(root, f)
            try:
                img = Image.open(path)
                if img.mode in ('RGBA', 'P'):
                    img = img.convert('RGB')
                if img.width > 1200 or img.height > 800:
                    img.thumbnail((1200, 800), Image.LANCZOS)
                if f.lower().endswith('.png'):
                    img.save(path, optimize=True)
                else:
                    img.save(path, quality=80, optimize=True)
                print(f'✓ {f}')
            except Exception as e:
                print(f'✗ {f}: {e}')

print('Done!')