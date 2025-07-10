import time
import pynlpir

start_time = time.time()
pynlpir.open(encoding="utf-8")

with open("../data/test_corpus.txt", "r", encoding="utf-8") as f:
    corpus = f.readlines()
    for corpus_line in corpus:
        print("pynlpir分词")
        res = pynlpir.segment(corpus_line, pos_tagging=False)
        print(res)
        print("=" * 20)

        print("pynlpir 关键词提取")
        res = pynlpir.get_key_words(corpus_line)
        print(res)
        print("=" * 20)

        print("分界线".center(100, "-"))

pynlpir.close()

print("总耗时：%.2f 秒" % (time.time() - start_time))
