#!/usr/bin/env python3
"""
GDCスライド写真のcropスクリプト
観客の頭などを除去してスライド部分だけを抽出します
"""
from PIL import Image
import os
from pathlib import Path

def crop_slide(input_path, output_path):
    """
    写真をcropしてスライド部分だけを抽出
    下部の観客と上部の余白を削除
    """
    img = Image.open(input_path)
    width, height = img.size

    # 上部10%、下部20%をカット（観客の頭を除去）
    # 左右も少しカット
    crop_top = int(height * 0.10)
    crop_bottom = int(height * 0.80)
    crop_left = int(width * 0.05)
    crop_right = int(width * 0.95)

    # crop: (left, top, right, bottom)
    cropped = img.crop((crop_left, crop_top, crop_right, crop_bottom))

    # 保存
    cropped.save(output_path, quality=95)
    print(f"✓ Cropped: {os.path.basename(input_path)}")

def main():
    # ディレクトリ設定
    base_dir = Path(__file__).parent
    output_dir = base_dir / "slide_photos"

    # 出力ディレクトリ作成
    output_dir.mkdir(exist_ok=True)

    # すべてのjpgファイルを処理
    jpg_files = sorted(base_dir.glob("PXL_*.jpg"))

    print(f"Found {len(jpg_files)} photos to process...")
    print()

    for i, jpg_file in enumerate(jpg_files, 1):
        output_file = output_dir / jpg_file.name
        crop_slide(jpg_file, output_file)

        if i % 10 == 0:
            print(f"Progress: {i}/{len(jpg_files)}")

    print()
    print(f"✓ Complete! Processed {len(jpg_files)} photos")
    print(f"✓ Saved to: {output_dir}")

if __name__ == "__main__":
    main()
