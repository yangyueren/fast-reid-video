

import glob
import os.path as osp
import re

from .bases import ImageDataset
from ..datasets import DATASET_REGISTRY


@DATASET_REGISTRY.register()
class CarlaVehicle(ImageDataset):
    """
    """
    dataset_dir = "carla_vehicles_random_1000"
    dataset_name = "carla_vehicles_random_1000"
    # dataset_dir = "carla_vehicles_108"
    # dataset_name = "carla_vehicles_108"

    EXTRACT = False


    def __init__(self, root='datasets', **kwargs):
        self.dataset_dir = osp.join(root, self.dataset_dir)
        if self.EXTRACT == True:
            # change dir
            self.dataset_dir = "carla_cameras_big_epic_video_1000"
            self.dataset_name = "carla_cameras_big_epic_video_1000"
            self.dataset_dir = osp.join(root, self.dataset_dir)
            self.train_dir = osp.join(self.dataset_dir, 'train_nouse')
            self.query_dir = osp.join(self.dataset_dir, 'query_nouse')
            self.gallery_dir = osp.join(self.dataset_dir, 'traffic-camera-output-combine')
        else:
            self.train_dir = osp.join(self.dataset_dir, 'train_test')
            self.query_dir = osp.join(self.dataset_dir, 'query2_random1000')
            self.gallery_dir = osp.join(self.dataset_dir, 'test2_random1000')

            # self.train_dir = osp.join(self.dataset_dir, 'train2')
            # self.query_dir = osp.join(self.dataset_dir, 'query2')
            # self.gallery_dir = osp.join(self.dataset_dir, 'test2')

            # self.query_dir = osp.join(self.dataset_dir, 'query2_epic')
            # self.query_dir = osp.join(self.dataset_dir, 'query2_epic1k')
            
            
            # self.gallery_dir = osp.join(self.dataset_dir, 'test2_epic')
            # self.gallery_dir = osp.join(self.dataset_dir, 'test2_epic1k')

        required_files = [
            self.dataset_dir,
            self.train_dir,
            self.query_dir,
            self.gallery_dir,
        ]
        self.check_before_run(required_files)
        if self.EXTRACT:
            train = self.process_carla_camera_dir(self.train_dir)
            query = self.process_carla_camera_dir(self.query_dir, is_train=False)
            gallery = self.process_carla_camera_dir(self.gallery_dir, is_train=False)
        else:
            train = self.process_dir(self.train_dir)
            query = self.process_dir(self.query_dir, is_train=False)
            gallery = self.process_dir(self.gallery_dir, is_train=False)

        super(CarlaVehicle, self).__init__(train, query, gallery, **kwargs)
    
    
    def process_carla_camera_dir(self, dir_path, is_train=True):
        img_paths = glob.glob(osp.join(dir_path, '*.jpg'))
        
        #test格式 c0113_0000182_0000020.jpg
        #query格式 c0113_0000182_0000020.jpg camid, frame, idxinframe
        pattern = re.compile(r'c([\d]+)[-_]([\d]+)[-_]([\d]+)')

        data = []
        for img_path in img_paths:
            # print(img_path)
            camid, frame, idx_in_frame = map(int, pattern.search(img_path).groups())
            # pid, camid = map(int, pattern.search(img_path).groups())
            if frame == -1: continue  # junk images are just ignored
            assert 0 <= camid <= 192
            # assert 0 <= pid <= 150
            assert 0 <= frame <= 100000000
            if is_train:
                pid = self.dataset_name + "_" + str(frame)
                camid = self.dataset_name + "_" + str(camid)
            else:
                pid = str(frame) + '_' + str(idx_in_frame)
            data.append((img_path, pid, camid))


        return data

    def process_dir(self, dir_path, is_train=True):
        #c0000_0980_0000006.jpg camid vehicleid junkinfo
        img_paths = glob.glob(osp.join(dir_path, '*.jpg'))
        pattern = re.compile(r'c(\d\d\d\d)_(\d\d\d\d)')

        data = []
        for img_path in img_paths:
            camid, pid = map(int, pattern.search(img_path).groups())
            if pid == -1: continue  # junk images are just ignored
            assert 0 <= pid <= 1000
            assert 0 <= camid <= 2
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
