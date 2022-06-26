from tqdm.auto import tqdm
import os
import numpy as np

# download glove
def downLoad_glove(dir='.', dim=50):
    if not os.path.exists(os.path.join(dir, 'glove.6B.50d.txt')):
        os.system("!wget http://nlp.stanford.edu/data/glove.6B.zip")
        # wget.download("http://nlp.stanford.edu/data/glove.6B.zip")
        os.system(f"!unzip glove.6B.zip -d {dir}")

    gloves = {}
    with open(f"./glove.6B.{dim}d.txt", "r") as f:
        for line in tqdm(f, total=400000):
            word, coefs = line.split(maxsplit=1)
            coefs = np.fromstring(coefs, "f", sep=" ")
            gloves[word] = coefs

    return gloves

