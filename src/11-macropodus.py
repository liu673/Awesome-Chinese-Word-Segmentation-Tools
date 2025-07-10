import time
import macropodus

# 遇到scipy问题，降低版本 pip install scipy==1.12.0
# 遇到 ImportError: cannot import name 'Mapping' from 'collections'，将依赖导入改为from collections.abc import Mapping
# 遇到 AttributeError: module 'numpy' has no attribute 'int'. 降低numpy版本 pip install numpy==1.23.5

start_time = time.time()

with open("../data/test_corpus.txt", "r", encoding="utf-8") as f:
    corpus = f.readlines()
    for corpus_line in corpus:
        print("macropodus 分词")
        # type_cut: str, like 'cut_dag', 'cut_forward', 'cut_reverse', 'cut_bidirectional', 'cut_search'
        res = macropodus.cut(corpus_line)  # 默认切词方式cut_dag
        res = list(res)
        print(res)
        # res = macropodus.cut(corpus_line, type_cut='cut_search')
        # res = list(res)
        # print( res)
        # res = macropodus.cut(corpus_line, type_cut='cut_forward')
        # res = list(res)
        # print( res)
        # res = macropodus.cut(corpus_line, type_cut='cut_reverse')
        # res = list(res)
        # print( res)
        # res = macropodus.cut(corpus_line, type_cut='cut_bidirectional')
        # res = list(res)
        # print( res)

        print("=" * 20)

        print("macropodus 关键词抽取")
        res = macropodus.keyword(corpus, num=10)
        print(res)

        print("分界线".center(100, "-"))

print("总耗时：%.2f 秒" % (time.time() - start_time))
