## 训练步骤
1. 将数据集（wav音频和lab标注数据）放于raw下，文件夹名为说话者的名字
2. 运行gen_train_txt.py生成训练集和验证集的txt文件
3. 运行resample.py对音频进行重采样
4. 运行preprocess_rext.py进行bert clean和切分训练集和验证集
5. 运行bert_gen.py生成bert训练数据
6. 运行python train_ms.py -m genshin -c ./config/config/json