# YANS Hakathon 2018

```sh
ssh -i aws-yans.pem ubuntu@[AWSのホスト名]
```

## 1. 論文分類タスク コース
- `1`: Accept, `0`: Reject
- trainファイル: `train.txt`
- devファイル: `dev.txt`
- testファイル: `test.txt`


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
$ nohup ./run_featurize_classify_arxiv_yans.sh cl-lg > result_classify_arxiv_cl-lg_yans_test &
$ tail -f result_classify_arxiv_cl-lg_yans_test
```

## 2. 論文分析コース

（TODO: 書く）

## 3. 自由コース

（TODO: 書く）
