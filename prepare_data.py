import moxing as mox  

import os
import shutil
import argparse

import os
import shutil
import argparse


def convert2MultiClass(srcPath, dstPath):
    imgs_path = os.path.join(srcPath, 'images')
    mask_path = os.path.join(srcPath, 'masks')

    images = os.listdir(imgs_path)
    target_path = dstPath

    for i, img in enumerate(images):
        name = img.split('.')[0]
        dst_path = os.path.join(target_path, name)  # 目标目录
        if not os.path.exists(dst_path):
            os.mkdir(dst_path)  # 创建新目录
        img_src = os.path.join(imgs_path, img)  # 原图片目录
        mask_src = os.path.join(mask_path, name + '_mask.png')  # 原标签目录

        shutil.copyfile(img_src, dst_path + '/image.png')
        shutil.copyfile(mask_src, dst_path + '/mask.png')


if __name__ == '__main__':

    # 创建对象
    parser = argparse.ArgumentParser()

    # 添加参数
    parser.add_argument('train', help='是否是训练模式')
    parser.add_argument('--datapath','-d', default='evaldata', help='验证模式下可选，验证数据存放目录', type=str)
    parser.add_argument('--dstPath',help='验证模式下可选，更改格式后的验证文件存放目录', help='integer', type=int)

    # 使用parse_args解析参数
    args = parser.parse_args()


    # train = False
    if args.train:
        mox.file.copy_parallel('obs://data410/dataset/YG56723/images', 'rawdataset/images')
        mox.file.copy_parallel('obs://data410/dataset/YG56723/labels', 'rawdataset/masks')
        srcPath = 'rawdataset'
        dstPath = 'dataset'
        convert2MultiClass(srcPath, dstPath)
    else:
        srcPath = args.dataptah
        dstPath = 'evaldata'
        convert2MultiClass(srcPath, dstPath)
