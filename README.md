# Awesome-Chinese-Word-Segmentation-Tools

[![Awesome](https://awesome.re/badge.svg)](https://github.com/liu673/Awesome-Chinese-Word-Segmentation-Tools)
![License](https://badgen.net/github/license/liu673/Awesome-Chinese-Word-Segmentation-Tools)
![forks](https://badgen.net/github/forks/liu673/Awesome-Chinese-Word-Segmentation-Tools)
![issues](https://badgen.net/github/issues/liu673/Awesome-Chinese-Word-Segmentation-Tools)
![last commit](https://badgen.net/github/last-commit/liu673/Awesome-Chinese-Word-Segmentation-Tools)

中文分词（Chinese Word Segmentation,CWS）是自然语言处理（NLP）的基础任务之一，其效果直接影响文本分析、情感分析、机器学习等下游任务的质量。本项目对 13 种主流中文分词工具 进行总结并简单测评，涵盖通用工具与垂域能力，旨在为开发者提供选型参考。

> 环境：Python 3.10.18
> 
> 目前是对python环境下的中文分词进行测试，对以下工具中的分词效果进行测试，若需使用工具中的其他功能，可参考对应工具的github地址。

# 🛠️ 分词工具

## 01-jieba

- 简介：jieba是Python中文分词库，支持精确、全模式和搜索引擎模式，基于统计词典与动态规划算法实现高效分词。
- github地址：https://github.com/fxsjy/jieba
- 开源协议：[MIT license](https://github.com/fxsjy/jieba#MIT-1-ov-file)
- 下载：`pip install jieba`
- 测试案例及使用说明：[01-jieba.py](src/01-jieba.py)
    - 测试案例中jieba版本为`0.42.1`

## 02-cutword

- 简介：cutword 是一个中文分词库，字典文件根据截止到2024年1月份的最新数据统计得到，词频更加合理。
  基于ac自动机实现的分词算法，分词速度是jieba的两倍。
- github地址：https://github.com/liwenju0/cutword
- 开源协议：[Apache-2.0 license](https://github.com/liwenju0/cutword#Apache-2.0-1-ov-file)
- 下载：`pip install cutword`
- 测试案例及使用说明：[02-cutword.py](src/02-cutword.py)
    - 测试案例中cutword版本为`0.1.1`

## 03-pkuseg

- 简介：pkuseg
  是基于论文[Luo et. al, 2019](https://github.com/lancopku/pkuseg-python#%E8%AE%BA%E6%96%87%E5%BC%95%E7%94%A8)
  的工具包。其简单易用，支持细分领域分词，有效提升了分词准确度。
- github地址：https://github.com/lancopku/pkuseg-python
- 开源协议：[MIT license](https://github.com/lancopku/pkuseg-python#MIT-1-ov-file)
- 下载：`pip install pkuseg`
- 测试案例及使用说明：[03-pkuseg.py](src/03-pkuseg.py)
    - 测试案例中pkuseg版本为`0.0.25`
- 目前pkuseg支持细分领域模型的分词

    ```json
    {
      "mixed": "混合领域，默认模型", 
      "default_v2": "领域自适应通用模型，相较于默认模型规模更大，但泛化性能更好",
      "medicine": "医药领域模型", 
      "news": "MSRA（新闻语料）模型",
      "web": "微博（网络文本语料）模型",
      "tourism": "旅游领域模型",
      "art": "艺术领域模型",
      "entertainment": "娱乐体育领域模型",
      "science": "科技领域模型",
      "postag": "词性标注模型，这个在参数postag=True时使用"
    }
    
    ```
  细分领域模型下载地址：https://github.com/lancopku/pkuseg-python/releases

## 04-baidu lac

- 简介：LAC全称Lexical Analysis of Chinese，是百度自然语言处理部研发的一款联合的词法分析工具，实现中文分词、词性标注、专名识别等功能。
- github地址：https://github.com/baidu/lac
- 开源协议：[Apache-2.0 license](https://github.com/baidu/lac#Apache-2.0-1-ov-file)
- 下载：`pip install lac`
- 测试案例及使用说明：[04-baidu_lac.py](src/04-baidu_lac.py)
    - 测试案例中lac版本为`2.1.2`
  > TIPS:
  > 注意paddlepaddle版本(paddlepaddle==2.5.2)、python版本(python==3.10.18)、lac版本(lac==2.1.2)
  ，得三者匹配（在这吐槽baidu，尾大不掉，在各个开源上摆烂了）

## 05-jiagu

- 简介：Jiagu使用大规模语料训练而成。将提供中文分词、词性标注、命名实体识别、情感分析、知识图谱关系抽取、关键词抽取、文本摘要、新词发现、情感分析、文本聚类等常用自然语言处理功能。
- github地址：https://github.com/ownthink/Jiagu
- 开源协议：[MIT license](https://github.com/ownthink/Jiagu#MIT-1-ov-file)
- 下载：`pip install jiagu`
- 测试案例及使用说明：[05-jiagu.py](src/05-jiagu.py)
    - 测试案例中jiagu版本为`0.2.3`

## 06-HanLP

- 简介：HanLP覆盖新闻、社交媒体、金融、法律等多个领域，在分词标准上，HanLP提供细粒度和粗粒度两种颗粒度，细粒度适合搜索引擎业务，粗粒度适合文本挖掘业务。
- github地址：https://github.com/hankcs/HanLP
    - pyhanlp:https://github.com/hankcs/pyhanlp
- 开源协议：[Apache-2.0 license](https://github.com/hankcs/pyhanlp#Apache-2.0-1-ov-file)
- 下载：`pip install pyhanlp`
- 测试案例及使用说明：[06-pyhanlp.py](src/06-pyhanlp.py)
    - 测试案例中pyhanlp版本为`0.1.89`
  > TIPS:
  > pyhanlp下载的内容挺多的，占用空间大，请自行选择:
  >
  > 1. 手动下载 [dara-for-1.7.5.zip](https://file.hankcs.com/hanlp/data-for-1.7.5.zip)为637
       MB，hanlp-1.8.6-release.zip为1.75 MB，都将放在`{your env}\Lib\site-packages\pyhanlp\static\`，
       > 手动下载完之后，得将data-for-1.7.5.zip重命名为 data-for-1.8.6.zip
  > 2. 得配置Java环境，否则无法运行
  > 3. 还得再conda下安装openjdk, `conda install -c conda-forge openjdk=11.0.24`
  > 4. 已经安装好JDK8,并且在系统变量中配置好JAVA_HOME
  > 5. 执行上面的步骤，依旧没有成功，还是报 找不到Java，请安装JDK8,

## 07-jiojio

- 简介：基于 CPU 的高性能、持续优化 中文分词器，支持中文分词、词性标注、添加自定义词典（静态、动态）
- github地址：https://github.com/dongrixinyu/jiojio
- 开源协议：[GPL-3.0 license](https://github.com/dongrixinyu/jiojio?tab=readme-ov-file#GPL-3.0-1-ov-file)
- 下载：`pip install jiojio`
- 测试案例及使用说明：[07-jiojio.py](src/07-jiojio.py)
    - 测试案例中jiojio版本为`1.2.8`

## 08-HarvestText

- 简介：HarvestText是一个专注无（弱）监督方法，能够整合领域知识（如类型，别名）对特定领域文本进行简单高效地处理和分析的库。其中分词器用的应该是jieba分词
- github地址：https://github.com/blmoistawinde/HarvestText
- 开源协议：[MIT license](https://github.com/blmoistawinde/HarvestText?tab=readme-ov-file#MIT-1-ov-file)
- 下载：`pip install harvesttext`
- 测试案例及使用说明：[08-harvesttext.py](src/08-harvesttext.py)
    - 测试案例中harvesttext版本为`0.8.2.1`

## 09-pynlpir

- 简介：NLPIR大数据语义智能分析平台是针对大数据内容处理的需要，融合了网络精准采集、自然语言理解、文本挖掘和网络搜索技术的十三项功能：精准采集、文档转换、新词发现、批量分词、语言统计、文本聚类、文本分类、摘要实体、情感分析、智能过滤、文档去重、全文检索、编码转换。
- github地址：https://github.com/tsroten/pynlpir
- 开源协议：[MIT license](https://github.com/tsroten/pynlpir#MIT-1-ov-file)
- 下载：`pip install pynlpir`，然后魔法运行 `pynlpir update`
  > TIPS:
  > 运行 `pynlpir update`，依旧不能使用，貌似是因为官方不再更新权限了，在 https://github.com/NLPIR-team/NLPIR/
  中有相关的权限文件下载，但是我测试的时候，是在七个月前更新的权限，目前没有最新的权限文件。
  >
  若你遇到这个问题的时候，先看上面这个repo是否更新到最近日期的权限文件，可以参考这个教程 https://cloud.tencent.com/developer/article/2030029
- 测试案例及使用说明：[09-pynlpir.py](src/09-pynlpir.py)
    - 测试案例中pynlpir版本为`0.6.1`

## 10-THULAC

- 简介：一个高效的中文词法分析工具包，具有中文分词和词性标注功能。
- github地址：https://github.com/thunlp/THULAC-Python
- 开源协议：[MIT license](https://github.com/thunlp/THULAC-Python#MIT-1-ov-file)
- 下载：`pip install thulac`
- 测试案例及使用说明：[10-thulac.py](src/10-thulac.py)
    - 测试案例中thulac版本为`0.2.2`

## 11-macropodus

- 简介：Macropodus是一个以Albert+BiLSTM+CRF网络架构为基础，用大规模中文语料训练的自然语言处理工具包。将提供中文分词、词性标注、命名实体识别、关键词抽取、文本摘要、新词发现、文本相似度、计算器、数字转换、拼音转换、繁简转换等常见NLP功能。
- github地址：https://github.com/yongzhuo/Macropodus
- 开源协议：[MIT license](https://github.com/yongzhuo/Macropodus?tab=readme-ov-file#MIT-1-ov-file)
- 下载：`pip install macropodus`
- 测试案例及使用说明：[11-macropodus.py](src/11-macropodus.py)
    - 测试案例中macropodus版本为`0.0.7`

## 12-pyltp & ltp
- 简介：LTP（Language Technology Platform） 提供了一系列中文自然语言处理工具，用户可以使用这些工具对于中文文本进行分词、词性标注、句法分析等等工作。
- github地址：https://github.com/HIT-SCIR/pyltp
- 开源协议：[MIT license](https://github.com/HIT-SCIR/pyltp?tab=readme-ov-file#MIT-1-ov-file)
- 测试案例及使用说明：[12-pyltp.py](src/12-pyltp.py)
  - 测试案例中pyltp版本为`0.4.0`
  > TIPS: 
  > 在测试时，找不到pyltp的模型，因此用了ltp,`pip install ltp`, 使用ltp的[感知机算法模型 legacy](https://hf-mirror.com/LTP/legacy)，感知机算法实现的分词、词性和命名实体识别，速度比较快，但是精度略低 
  > ltp的版本为 `4.2.14`，使用ltp得用到torch，因此在gpu下运行会加速，cpu下运行慢
  > ltp的[模型地址](https://huggingface.co/LTP) ,模型有legacy、tiny、small、base、base1、base2，共6个

# ⌨️ 总结

测试了13个分词工具，因为测试数据偏向于新闻数据集，因此效果最好的分词工具是pkuseg中模型为 `news`
的分词和`baidu lac`，两者效果很接近，【没有专门测试数据批量测试，仅人为感知测试】，其余的工具测试在本次效果中都差不多，因此可见在垂域中进行分词，最好是能够结合自己的场景下进行单独的分词训练，或者在分词工具中加入自己的词典，效果会提升。

# 📈 TODO
目前是对中文分词的工具进行了简单测评，并没有形成一个完整的测评标准，后续考虑进行测评框架，进行批量测试。

若您有更好的分词工具，欢迎提issue，欢迎PR。

# resources

- https://github.com/crownpku/awesome-chinese-nlp?tab=readme-ov-file#chinese-word-segment-%E4%B8%AD%E6%96%87%E5%88%86%E8%AF%8D-1
- https://github.com/topics/chinese-word-segmentation
- https://github.com/ownthink/evaluation/tree/master
- https://github.com/neulab/InterpretEval?tab=readme-ov-file

