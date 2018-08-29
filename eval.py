


import sys
filename = sys.argv[1]


def get_result(filename):
    tags = []
    dicts = {}
    for l in open(filename):
        l = l.strip().replace('\t', ',')
        filename = l.split(',')[0]
        tag = int(l.split(',')[-1])
        dicts[filename] = tag
    return dicts


predict = get_result(filename)
gold = get_result('test_gold.txt')

correct_num = 0
total_num = len(predict)
# print(len(predict), len(gold))


# for p, g in zip(predict_list, gold_list):
for filename in predict.keys():
    p = predict[filename]
    g = gold[filename]
    correct_num = correct_num + int(p == g)
print('correct_num:', correct_num)
print('total_num:  ', total_num)
print (float(correct_num) / total_num) * 100.0
