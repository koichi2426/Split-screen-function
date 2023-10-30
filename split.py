from PIL import Image

# 入力ファイル名
input_file = "input/input.jpg"
# 出力ディレクトリ
output_dir = "output/"

# 2×8のグリッドに分割する
rows, columns = 2, 8

# 画像を読み込む
img = Image.open(input_file)

# 画像の幅と高さを取得
img_width, img_height = img.size

# 1つのサブイメージの幅と高さを計算
subimg_width = img_width // columns
subimg_height = img_height // rows

# 出力ディレクトリを作成
import os
os.makedirs(output_dir, exist_ok=True)

# 画像を分割して保存
for row in range(rows):
    for col in range(columns):
        # サブイメージの位置を計算
        left = col * subimg_width
        upper = row * subimg_height
        right = (col + 1) * subimg_width
        lower = (row + 1) * subimg_height

        # サブイメージを切り取り
        subimg = img.crop((left, upper, right, lower))

        # サブイメージを保存
        output_file = os.path.join(output_dir, f"subimage_{row}_{col}.jpg")
        subimg.save(output_file)

print("画像を2×8のグリッドに分割しました。")
