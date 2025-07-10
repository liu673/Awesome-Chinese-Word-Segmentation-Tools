
import time
from cutword.cutword import Cutter, NER

start_time = time.time()

cutter = Cutter()
new = NER()

with open("../data/test_corpus.txt", "r", encoding="utf-8") as f:
    corpus = f.readlines()
    for corpus_line in corpus:
        print("cutword分词")
        res = cutter.cutword(corpus_line)
        print(res)
        print("=" * 20)

        print("cutword NER 命名体识别")
        res = new.predict(corpus_line)
        print(res)
        print("分界线".center(100, "-"))

print("总耗时：%.2f 秒" % (time.time() - start_time))
