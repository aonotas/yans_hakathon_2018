# YANS Hakathon 2018

## 開発環境
共通タスク、オープンタスク1では、 GPU の使用を可能にするため、チーム毎に AWS のインスタンスを2台まで立ち上げることができます。
インスタンスは運営側で用意し、それにパスワードでアクセスすることができます。
各チーム代表者に、ホスト名及びパスワードをお伝えしますので、他のメンバーなど、適宜ユーザを追加してください。
```sh
$ ssh yans@[AWSのホスト名]
```

一つのインスタンスは1GPUが使えます。

```
$ cd ~/hackathon
の中に訓練データなど入っています。
```

## 1. 論文分類タスク コース
- `1`: Accept, `0`: Reject
- trainファイル: `train.txt`
- devファイル: `dev.txt`
- testファイル: `test.txt`

ローカルに入れたい場合は (200MBあるのでポケットWifi使う場合はHDDからコピーしてください)
```
$ wget http://sato-motoki.com/research/yans/data_yans_train_dev.tar.gz
```
もしくは, @Motoki Satoまで聞いてください. HDDがあります.

## word2vec
```
$ ~/hackathon/data_yans/word2vec
```
の中にword2vec/gloveが入っています

## 評価
- testデータのダウンロード (2日目の夜 or 3日目の朝に配布します)
```
$ ./download_test_data.sh
```
※配布前はスクリプトが正しく動かないようになっています. 
- test.txtの最後のカラムに `\t` 0 or 1を追加して提出してください.


## ベースライン　の性能
```
# arxiv cs + lg (train/dev/test)
Train majority: 66.873, Dev majority: 67.93 Test majorit: 69.723
Train accuracy: 76.64 in 1818 examples
Dev accuracy: 71.14 in 220 examples
Test accuracy: 71.91 in 208 examples
```


- ベースラインの動かし方 (60分くらいかかります.)
```
$ ./copy_hackathon.sh # これを事前に行っておいてください
$ cd ~/hackathon/code/accept_classify
$ source ~/.bashrc_baseline
$ pyenv shell 2.7.11
$ echo -e "import nltk\nnltk.download('punkt')\nnltk.download('stopwords')" | python
$ nohup ./run_featurize_classify_arxiv_yans.sh cl-lg > result_classify_arxiv_cl-lg_yans_test &
$ tail -f result_classify_arxiv_cl-lg_yans_test
```

### anaconda で GPU の利用
```
$ source ../ubuntu/anaconda3/bin/activate chainer_p36 # Python3 環境で Chainer 利用
$ source ../ubuntu/anaconda3/bin/activate pytorch_p36 # Python3 環境で PyTorch 利用
```
などで、いろいろな深層学習用のフレームワークを切り替えることができます。
例えば一つ目のコマンドを実行すると Chainer がインストールされた python 環境に切り替えられます。
```
(chainer_p36) yans@ip-172-31-45-56:~$ python
Python 3.6.6 |Anaconda, Inc.| (default, Jun 28 2018, 17:14:51)
[GCC 7.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import chainer
```

## 2. 論文分析コース
まず, 分類器を作ってから、分類器の分析とかでもOK
もしくは, 論文に関する分析. 

## 3. 自由コース
- 論文執筆時にあるとちょっと嬉しいツール
- 日々の実験管理を便利にするツール
- 形態素解析用辞書の整備
- SoTAのSequence Labelingの整備 (deep-crf)
- Word2color ：“ピカチュー”→ 黄色　の変換ツール
- アイドルの握手会コーパスの分析
- NIPSなどの会議の著者が日本人だけのものを抽出するツール
- なんでもOK！ネタツールでもOK. 

