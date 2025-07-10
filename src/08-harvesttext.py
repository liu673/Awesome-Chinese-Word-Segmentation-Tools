import time
from harvesttext import HarvestText

start_time = time.time()

ht = HarvestText()

with open("../data/test_corpus.txt", "r", encoding="utf-8") as f:
    corpus = f.readlines()
    for corpus_line in corpus:
        print("harvestext 分词")  # 用的jieba
        res = ht.seg(corpus_line)
        print(res)
        # res = ht.seg(corpus_line, return_sent=True)
        # print(res)
        print("=" * 20)

        # print("harvestext 依存句法分析") # 用的pyhanlp
        # res = ht.triple_extraction(corpus_line)
        # print(res)
        # print("=" * 20)

print("总耗时：%.2f 秒" % (time.time() - start_time))
