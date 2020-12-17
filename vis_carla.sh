###
 # @Author: your name
 # @Date: 2020-10-31 10:36:53
 # @LastEditTime: 2020-11-16 23:36:49
 # @LastEditors: Please set LastEditors
 # @Description: In User Settings Edit
 # @FilePath: /fast-reid/run_carla.sh
### 
export FASTREID_DATASETS=/home/zju/yangyueren/dataset
CUDA_VISIBLE_DEVICES=4 python demo/visualize_result.py --config-file ./configs/VERIWild/bagtricks_R50-ibn.yml \
--parallel --vis-label --dataset-name 'CarlaVehicle' --output logs/carla_vis \
--opts MODEL.WEIGHTS logs/veriwild/bagtricks_R50-ibn_4gpu/model_0039599.pth
# python tools/train_net.py --config-file ./configs/VeRi/sbs_R50-ibn.yml MODEL.DEVICE "cuda:7"
# python tools/train_net.py --config-file ./configs/VeRi/sbs_R50-ibn.yml --num-gpus 8
# CUDA_VISIBLE_DEVICES=2,4,6,7 python tools/train_net.py --config-file ./configs/VERIWild/bagtricks_R50-ibn.yml --num-gpus 4
