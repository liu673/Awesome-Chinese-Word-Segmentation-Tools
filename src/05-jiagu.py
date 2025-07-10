import time
import jiagu

start_time = time.time()

with open("../data/test_corpus.txt", "r", encoding="utf-8") as f:
    corpus = f.readlines()
    for corpus_line in corpus:
        print("jiagu 分词")
        res = jiagu.seg(corpus_line)
        print(res)
        print("=" * 20)

        print("jiagu 词性标注")
        res = jiagu.pos(res)
        print(res)
        print("=" * 20)

        print("jiagu 命名实体识别")
        res = jiagu.ner(res)
        print(res)
        print("=" * 20)

        print("jiagu 关键词抽取")
        res = jiagu.keywords(corpus_line, topkey=10)
        print(res)
        print("=" * 20)

        print("jiagu 自动摘要")
        res = jiagu.summarize(str(corpus_line), topsen=1)
        print(res)

        print("分界线".center(100, "-"))

print("总耗时：%.2f 秒" % (time.time() - start_time))
