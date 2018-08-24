# YANS Hakathon 2018

## 開発環境
共通タスク、オープンタスク1では、 GPU の使用を可能にするため、チーム毎に AWS のインスタンスを2台まで立ち上げることができます。
インスタンスは運営側で用意し、それにパスワードでアクセスすることができます。
各チーム代表者に、ホスト名及びパスワードをお伝えしますので、他のメンバーなど、適宜ユーザを追加してください。
```sh
ssh -i aws-yans.pem ubuntu@[AWSのホスト名]
```

## 1. 論文分類タスク コース
- `1`: Accept, `0`: Reject
- trainファイル: `train.txt`
- devファイル: `dev.txt`
- testファイル: `test.txt`

ローカルに入れたい場合は
```
$ wget http://sato-motoki.com/research/yans/data_yans_train_dev.tar.gz
```
## word2vec
```
$ data_yans/word2vec
```
の中にword2vec/gloveが入っています

## 評価
- testデータのダウンロード (2日目の夜 or 3日目の朝に配布します)
```
$ ./download_test_data.sh
```
※配布前はスクリプトが正しく動かないようになっています. 
- test.txtの最後のカラムに `\t` 0 or 1を追加して提出してください.

（TODO: 書く）


ベースラインの動かし方 (20 - 40分くらいかかります.)
```
$ cd ~/code/accept_classify
$ source ~/.bashrc_baseline
$ pyenv shell 2.7.11
$ nohup ./run_featurize_classify_arxiv_yans.sh cl-lg > result_classify_arxiv_cl-lg_yans_test &
$ tail -f result_classify_arxiv_cl-lg_yans_test
```

## 2. 論文分析コース

（TODO: 書く）

## 3. 自由コース

（TODO: 書く）
