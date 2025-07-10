import time
import jieba
from jieba import analyse as jieba_analyse, posseg as jieba_posseg, finalseg as jieba_finalseg

start_time = time.time()

with open("../data/test_corpus.txt", "r", encoding="utf-8") as f:
    corpus = f.readlines()
    for corpus_line in corpus:
        print("jieba 分词")
        res = jieba.cut(corpus_line)
        print(list(res))
        # res = jieba.cut_for_search(corpus_line)
        # print(list(res))
        print("=" * 20)

        print("jieba_analyse TF-IDF 关键词提取")
        res = jieba_analyse.extract_tags(corpus_line, topK=20)
        print(res)
        print("=" * 20)

        print("jieba_analyse TextRank 关键词提取")
        res = jieba_analyse.textrank(corpus_line, topK=20)
        print(res)
        print("=" * 20)

        print("jieba_posseg 词性标注")
        res = jieba_posseg.cut(corpus_line)
        print([(item.word, item.flag) for item in res])
        print("=" * 20)

        print("jieba_finalseg 词性标注")
        res = jieba_finalseg.cut(corpus_line)
        print(list(res))
        # res = jieba_finalseg.__cut(corpus_line)
        # print(list(res))

        print("分界线".center(100, "-"))

print("总耗时：%.2f 秒" % (time.time() - start_time))
