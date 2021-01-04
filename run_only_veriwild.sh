###
 # @Author: your name
 # @Date: 2020-10-31 10:36:53
 # @LastEditTime: 2020-11-18 02:26:16
 # @LastEditors: Please set LastEditors
 # @Description: In User Settings Edit
 # @FilePath: /fast-reid/run_carla.sh
### 
export FASTREID_DATASETS=/home/zju/yangyueren/dataset

# CUDA_VISIBLE_DEVICES=0 python tools/train_net.py --config-file ./configs/VERIWild/sbs_R101-ibn-carla.yml
#CUDA_VISIBLE_DEVICES=6 python tools/train_net.py --config-file ./configs/VERIWild/bagtricks_R50-ibn-carla.yml  MODEL.WEIGHTS logs/veriwild/bagtricks_R50-ibn_4gpu-carla/model_0167249.pth
CUDA_VISIBLE_DEVICES=0,3 python tools/train_net.py --config-file ./configs/VERIWild/bagtricks_R50-ibn-only-veriwild.yml --num-gpus 2
# CUDA_VISIBLE_DEVICES=2 python tools/train_net.py --config-file ./configs/VERIWild/bagtricks_R50-ibn-only-veriwild.yml --eval-only  MODEL.WEIGHTS logs/veriwild/bagtricks_R50-ibn_4gpu-only-veriwild/model_68mAP.pth

# python  tools/train_net.py --config-file ./configs/VeRi/sbs_R50-ibn.yml --num-gpus 4 --eval-only MODEL.WEIGHTS ./logs/veri/sbs_R50-ibn/model_final.pth
# CUDA_VISIBLE_DEVICES=1 python  tools/train_net.py --config-file ./configs/VeRi/sbs_R50-ibn.yml --eval-only MODEL.DEVICE "cuda:0"  MODEL.WEIGHTS ./logs/veri/sbs_R50-ibn/model_0082599.pth
