import time
import thulac

start_time = time.time()

with open("../data/test_corpus.txt", "r", encoding="utf-8") as f:
    corpus = f.readlines()
    for corpus_line in corpus:
        print("thulac分词")
        res = thulac.thulac(seg_only=True).cut(corpus_line, text=True)
        res = res.split(" ")
        print(res)
        print("=" * 20)

        print("thulac 词性标注")
        res = thulac.thulac(seg_only=False).cut(corpus_line, text=True)
        res = res.split(" ")
        print(res)

        print("分界线".center(100, "-"))

print("总耗时：%.2f 秒" % (time.time() - start_time))
