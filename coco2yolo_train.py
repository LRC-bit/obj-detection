import json
import os

def convert_coco_to_yolo(coco_json_path, output_dir):
    # 1. 创建类别列表文件（class.txt）
    with open(os.path.join(output_dir, 'class.txt'), 'w') as f:
        for cat_name in ["car","truck","bus","van","freight_car"]:
            f.write(cat_name + '\n')

    # 2. 加载COCO JSON文件
    with open(coco_json_path, 'r') as f:
        coco_data = json.load(f)

    # 3. 提取COCO数据中的基本信息
    annotations = coco_data['annotations']

    image_id_now = None
    for i in annotations:

        if image_id_now != i['image_id']:
            if f is not None:
                f.close
            image_id_now = i['image_id']
            img_file_name = str(i['image_id']).rjust(5, "0")+".txt"
            yolo_txt_path = os.path.join(output_dir, img_file_name)
            f = open(yolo_txt_path, 'w')

        category_id = i['category_id'] - 1
        x, y, w, h = i['bbox']
        x_center = (x + w / 2) / 640
        y_center = (y + h / 2) / 512
        width_scaled = w / 640
        height_scaled = h / 512
        f.write(f'{category_id} {x_center} {y_center} {width_scaled} {height_scaled}\n')

    f.close()

# 使用函数进行转换
coco_json_path = '/kaggle/working/GAIIC2024-赛道1-目标检测任务/train/train.json'  # 替换为实际COCO标注文件路径
output_dir = '/kaggle/working/dataset/train'  # 替换为期望的输出目录

convert_coco_to_yolo(coco_json_path, output_dir)
