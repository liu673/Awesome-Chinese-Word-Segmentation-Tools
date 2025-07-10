
import time
from LAC import LAC

start_time = time.time()

lac_seg = LAC(mode='seg')
lac_lac = LAC(mode='lac')
lac_rank = LAC(mode='rank')

with open("../data/test_corpus.txt", "r", encoding="utf-8") as f:
    corpus = f.readlines()
    for corpus_line in corpus:
        print("baidu-lac 分词")
        res = lac_seg.run(corpus_line)
        print(res)
        print("=" * 20)

        print("baidu-lac 词性分析")
        res = lac_lac.run(corpus_line)
        print(res)
        print("=" * 20)

        print("baidu-lac 关键词分析")
        res = lac_rank.run(corpus_line)
        print(res)

        print("分界线".center(100, "-"))

print("总耗时：%.2f 秒" % (time.time() - start_time))

