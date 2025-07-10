import time
import jiojio

# jiojio.help()

start_time = time.time()

with open("../data/test_corpus.txt", "r", encoding="utf-8") as f:
    corpus = f.readlines()
    for corpus_line in corpus:
        print("jiojio 分词")
        jiojio.init()
        res = jiojio.cut(corpus_line)
        print(res)
        print("=" * 20)

        print("jiojio 分词-添加正则")
        jiojio.init(cws_rule=True)
        res = jiojio.cut(corpus_line)
        print(res)
        print("=" * 20)

        print("jiojio 分词-词性标注")
        jiojio.init(pos=True)
        res = jiojio.cut(corpus_line)
        print(res)

        print("分界线".center(100, "-"))

print("总耗时：%.2f 秒" % (time.time() - start_time))
