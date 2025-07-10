import time
import pyltp
# import ltp
from ltp import LTP

start_time = time.time()
legacy_model_path = "../models/legacy"
ltp = LTP(
    pretrained_model_name_or_path=legacy_model_path,
    local_files_only=True,
    cache_dir=legacy_model_path
)

with open("../data/test_corpus.txt", "r", encoding="utf-8") as f:
    corpus = f.readlines()
    for corpus_line in corpus:
        print("ltp 分词")

        cws = ltp.pipeline([corpus_line], tasks=["cws"]).cws[0]
        print(cws)
        print("=" * 20)

print("总耗时：%.2f 秒" % (time.time() - start_time))
