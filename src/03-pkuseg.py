import time
import pkuseg

start_time = time.time()

with open("../data/test_corpus.txt", "r", encoding="utf-8") as f:
    corpus = f.readlines()

    for corpus_line in corpus:
        # 使用pkuseg的细分领域分词模型：postag、medicine、tourism、news、web、mixed、default_v2、art、entertainment、science
        # 注意：使用的分词模型和词性模型是不同的模型权重
        # 可以从release中下载模型，默认下载用github会有点慢
        print("pkuseg 默认模型mixed分词")
        res = pkuseg.pkuseg().cut(corpus_line)
        print(list(res))
        print("=" * 20)

        print("pkuseg news模型分词")
        news_model_path = r"C:\Users\jrj\.pkuseg\news"
        res = pkuseg.pkuseg(model_name=news_model_path).cut(corpus_line)
        print(list(res))
        print("=" * 20)

        print("pkuseg postag词性分析")
        pos_model_path = r"C:\Users\jrj\.pkuseg\postag"
        res = pkuseg.pkuseg(model_name=pos_model_path, postag=True).cut(corpus_line)
        print(list(res))
        print("=" * 20)

        print("pkuseg default_v2领域自适应模型分词")
        default_v2_path = "../default_v2"
        res = pkuseg.pkuseg(model_name=default_v2_path).cut(corpus_line)
        print(list(res))
        print("分界线".center(100, "-"))

print("总耗时：%.2f 秒" % (time.time() - start_time))
