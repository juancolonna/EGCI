# EGCI (Ecoacoustic Global Complexity Index)

Article title: Estimating ecoacoustic activity in the Amazon rainforest through Information Theory quantifiers. [PDF](https://journals.plos.org/plosone/article/authors?id=10.1371/journal.pone.0229425)

Previous title: Amazon rainforest soundscape characterized by Information Theory quantifiers. [PDF](https://www.biorxiv.org/content/10.1101/2020.02.09.940916v1.abstract)

The jupyter notebooks available here allows to reproduce the images and results included in the PDF article.

### Dataset

A copy of the preprocessed dataset to reproduce the main results of the article is now delivered with this repository. The dataset files are located in the pkl_dataset folder.

Anyway, a copy of this data can be downloaded through the link [here](https://drive.google.com/file/d/10_gHdk4AAmWXhjtMnGFVkA7_9oeep1Gf/view?usp=sharing). If you choose to download the dataset on this link, note that the downloaded file must be unzipped into a folder called __pkl_datasets__.

### Library dependencies

python           : 3.6.9 \
pandas           : 0.25.3 \
numpy            : 1.17.3 \
matplotlib       : 3.1.2 \
scipy            : 1.3.1 \
statsmodels      : 0.10.2 \
soundfile        : 0.10.3 \
colorednoise     : 1.1.1 \
tqdm

### Instalation

`pip install EGCI`

### How to use it

`
import numpy as np
import soundfile as sf
import EGCI
import matplotlib.pyplot as plt

# download a record file from this url: "https://drive.google.com/file/d/1QL5GimLjGLKBIiMzoa7VXlCR4GCpWBwc/view?usp=drivesdk"
# load this record
x, fs = sf.read('Adenomera andre.wav') # record of an anuran call

lag = 256 # time lag
C, H, J = EGCI.index(x, lag=lag) # C is the EGCI

boundaries_C, boundaries_H = EGCI.boundaries(lag) # these boundaries are only useful for plotting

plt.figure()
plt.plot(boundaries_H, boundaries_C, '--k')
plt.scatter(H, C, marker='.', s=100, label='Adenomera andre')
plt.xlabel('Entropy')
plt.ylabel('EGCI (Complexity)')
plt.xlim([0, 1])
plt.ylim([0, np.max(boundaries_C)+0.01])
plt.title('Adenomera andre.wav')
plt.legend(loc = 'best')
plt.show()
`
