###
 # @Author: your name
 # @Date: 2020-11-12 18:37:58
 # @LastEditTime: 2020-11-16 23:33:55
 # @LastEditors: your name
 # @Description: In User Settings Edit
 # @FilePath: /fast-reid/demo/run_demo.sh
### 
python demo/visualize_result.py --config-file logs/dukemtmc/mgn_R50-ibn/config.yaml \
--parallel --vis-label --dataset-name 'DukeMTMC' --output logs/mgn_duke_vis \
--opts MODEL.WEIGHTS logs/dukemtmc/mgn_R50-ibn/model_final.pth
