'''
Author: your name
Date: 2020-10-30 21:41:18
LastEditTime: 2020-11-12 17:14:27
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /fast-reid/fastreid/data/datasets/veri.py
'''
# encoding: utf-8
"""
@author:  Jinkai Zheng
@contact: 1315673509@qq.com
"""

import glob
import os.path as osp
import re

from .bases import ImageDataset
from ..datasets import DATASET_REGISTRY


@DATASET_REGISTRY.register()
class VeRi(ImageDataset):
    """VeRi.
    Reference:
        Liu et al. A Deep Learning based Approach for Progressive Vehicle Re-Identification. ECCV 2016.
    URL: `<https://vehiclereid.github.io/VeRi/>`_
    Dataset statistics:
        - identities: 775.
        - images: 37778 (train) + 1678 (query) + 11579 (gallery).
    """
    dataset_dir = "veri"
    dataset_name = "veri"

    def __init__(self, root='datasets', **kwargs):
        self.dataset_dir = osp.join(root, self.dataset_dir)

        self.train_dir = osp.join(self.dataset_dir, 'image_train')
        self.query_dir = osp.join(self.dataset_dir, 'image_query')
        self.gallery_dir = osp.join(self.dataset_dir, 'image_test')

        required_files = [
            self.dataset_dir,
            self.train_dir,
            self.query_dir,
            self.gallery_dir,
        ]
        self.check_before_run(required_files)

        train = self.process_dir(self.train_dir)
        query = self.process_dir(self.query_dir, is_train=False)
        gallery = self.process_dir(self.gallery_dir, is_train=False)

        super(VeRi, self).__init__(train, query, gallery, **kwargs)

    def process_dir(self, dir_path, is_train=True):
        img_paths = glob.glob(osp.join(dir_path, '*.jpg'))
        pattern = re.compile(r'([\d]+)_c(\d\d\d)')

        data = []
        for img_path in img_paths:
            pid, camid = map(int, pattern.search(img_path).groups())
            if pid == -1: continue  # junk images are just ignored
            assert 1 <= pid <= 776
            assert 1 <= camid <= 20
            camid -= 1  # index starts from 0
            if is_train:
                pid = self.dataset_name + "_" + str(pid)
                camid = self.dataset_name + "_" + str(camid)
            data.append((img_path, pid, camid))

        return data


# import glob
# import os.path as osp
# import re

# from .bases import ImageDataset
# from ..datasets import DATASET_REGISTRY


# @DATASET_REGISTRY.register()
# class VeRi(ImageDataset):
#     """VeRi.

#     Reference:
#         Liu et al. A Deep Learning based Approach for Progressive Vehicle Re-Identification. ECCV 2016.

#     URL: `<https://vehiclereid.github.io/VeRi/>`_

#     Dataset statistics:
#         - identities: 775.
#         - images: 37778 (train) + 1678 (query) + 11579 (gallery).
#     """
#     # dataset_dir = "carla_vehicles"
#     dataset_dir = "carla_cameras"
#     dataset_name = "veri"

#     def __init__(self, root='datasets', **kwargs):
#         self.dataset_dir = osp.join(root, self.dataset_dir)

#         self.train_dir = osp.join(self.dataset_dir, 'train')
#         self.query_dir = osp.join(self.dataset_dir, 'query')
#         self.gallery_dir = osp.join(self.dataset_dir, 'traffic-camera-output-combine')
#         # self.train_dir = osp.join(self.dataset_dir, 'train2')
#         # self.query_dir = osp.join(self.dataset_dir, 'query2')
#         # self.gallery_dir = osp.join(self.dataset_dir, 'test2')

#         required_files = [
#             self.dataset_dir,
#             self.train_dir,
#             self.query_dir,
#             self.gallery_dir,
#         ]
#         self.check_before_run(required_files)

#         train = self.process_carla_camera_dir(self.train_dir)
#         query = self.process_carla_camera_dir(self.query_dir, is_train=False)
#         gallery = self.process_carla_camera_dir(self.gallery_dir, is_train=False)

#         super(VeRi, self).__init__(train, query, gallery, **kwargs)

#     def process_carla_camera_dir(self, dir_path, is_train=True):
#         img_paths = glob.glob(osp.join(dir_path, '*.jpg'))
#         pattern = re.compile(r'c([\d]+)-(\d\d\d\d\d\d)-(\d\d\d)')
#         # pattern = re.compile(r'([\d]+)_c(\d\d\d)')

#         data = []
#         for img_path in img_paths:
#             camid, frame, idx_in_frame = map(int, pattern.search(img_path).groups())
#             # pid, camid = map(int, pattern.search(img_path).groups())
#             if frame == -1: continue  # junk images are just ignored
#             assert 0 <= camid <= 21
#             # assert 0 <= pid <= 150
#             assert 0 <= frame <= 10000000
#             # camid -= 1  # index starts from 0
#             if is_train:
#                 pid = self.dataset_name + "_" + str(frame)
#                 camid = self.dataset_name + "_" + str(camid)
#             else:
#                 pid = str(frame) + '_' + str(idx_in_frame)
#             data.append((img_path, pid, camid))

#         return data

    # def process_dir(self, dir_path, is_train=True):
    #     img_paths = glob.glob(osp.join(dir_path, '*.jpg'))
    #     pattern = re.compile(r'c([\d]+)-(\d\d\d\d\d\d)')
    #     # pattern = re.compile(r'([\d]+)_c(\d\d\d)')

    #     data = []
    #     for img_path in img_paths:
    #         camid, pid = map(int, pattern.search(img_path).groups())
    #         # pid, camid = map(int, pattern.search(img_path).groups())
    #         if pid == -1: continue  # junk images are just ignored
    #         assert 0 <= camid <= 21
    #         # assert 0 <= pid <= 150
    #         assert 0 <= pid <= 10000000
    #         # camid -= 1  # index starts from 0
    #         if is_train:
    #             pid = self.dataset_name + "_" + str(pid)
    #             camid = self.dataset_name + "_" + str(camid)
    #         else:
                
    #         data.append((img_path, pid, camid))

    #     return data
