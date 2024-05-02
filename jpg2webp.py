from PIL import Image
import os
from multiprocessing import Pool

def process_image_train(i, file_name):
    rgb_path = "/kaggle/working/GAIIC2024-赛道1-目标检测任务/" + file_name + "/rgb/" + str(i).rjust(5, "0") + ".jpg"
    gray_path = "/kaggle/working/GAIIC2024-赛道1-目标检测任务/" + file_name + "/tir/" + str(i).rjust(5, "0") + ".jpg"
    output_path = "kaggle/working/dataset/" + file_name + "/" + str(i).rjust(5, "0") + ".webp"
    # 直接创建一个与RGB图像相同大小的RGBA图像，并将灰度图作为Alpha通道
    img_combined = Image.merge("RGBA", (*Image.open(rgb_path).split(), Image.open(gray_path).convert("L")))

    # 保存为带透明通道的WebP图片
    img_combined.save(output_path, format="WEBP")


if __name__ == "__main__":
    for file_name in [("train",17991), ("val",1470), ("test",1001)]:
        os.makedirs(f"kaggle/working/dataset/{file_name[0]}")
        with Pool(processes=8) as pool:  # 假设使用8个进程
            pool.map(process_image_train, [(i, file_name[0]) for i in range(1, file_name[1])])
