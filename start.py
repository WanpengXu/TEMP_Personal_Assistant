import os

# python 环境配置
os.chdir('/home/xlab-app-center')
os.system('mkdir -p download/xtuner019')
os.chdir('download/xtuner019')
os.system('git clone -b v0.1.9 https://gitee.com/Internlm/xtuner')
os.chdir('xtuner')
os.system("pip install -e '.[all]'")

# OpenXLab 环境配置
# 导入基座模型
from openxlab.model import download
download(model_repo='OpenLMLab/InternLM-chat-7b', output='/home/xlab-app-center/model/InternLM-chat-7b')
# 导入 Adapter
download(model_repo='WanpengXu/Personal_Assistant_Adapter', output='/home/xlab-app-center/model/pa_hf_weights')

os.system('echo "模型和Adapter融合开始"')
# Merge
os.system('''
xtuner convert merge \
    '/home/xlab-app-center/model/InternLM-chat-7b' \
    '/home/xlab-app-center/model/pa_hf_weights' \
    '/home/xlab-app-center/model/pa_merged' \
    --max-shard-size 2GB
''')

# run
os.chdir('/home/xlab-app-center/model/')
os.system('echo "----"')
os.system('pwd')
os.system('ls')
os.system('echo "----"')

os.chdir('/home/xlab-app-center/model/pa_merged')
os.system('echo "----"')
os.system('pwd')
os.system('ls')
os.system('echo "----"')

# os.system('cd /home/xlab-app-center/code/InternLM_Lite')
os.chdir('/home/xlab-app-center/code/InternLM_Lite')
os.system('echo "----"')
os.system('pwd')
os.system('ls')
os.system('echo "----"')
os.system('streamlit run web_demo.py --server.address=0.0.0.0 --server.port 7860')