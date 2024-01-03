from huggingface_hub import hf_hub_download
from os import chdir, path

chdir(path.dirname(__file__))

hf_hub_download(repo_id="clarin-pl/word2vec-kgr10", filename="cbow.v300.m8.hs.mwe.w2v.gensim", local_dir="./gensim models")
hf_hub_download(repo_id="clarin-pl/word2vec-kgr10", filename="cbow.v300.m8.hs.mwe.w2v.gensim.vectors.npy", local_dir="./gensim models")
