# リストの作成
x = [1, 2, 3, 'a', 'b', 'c']
# インデックスを使ってアクセス
print(x[0])
print(x[3])
# リストの末尾からアクセスしたい場合
print(x[-1])
print(x[-2])

# スライス
# x[i:j] i <= k < jをお取り出す
x[1:3]
x[1:4]
x[4:]
x[:4]

# 要素の追加
x.append('d')
print(x)
# 要素の削除
x.remove('a')
print(x)

# リストの長さ
len(x)

# リスト内の出現回数
d = [1, 1, 1, 2, 3, 4]
d.count(1)

# リストのソート
y = [2, 3, 5 ,6, 1, 2]
y.sort()
y
# リストを逆順にする
y.reverse()
y

# 1行で降順にしたい場合
y.sort(reverse=True)


# リストの中にリストも入れられる
lists = [[1, 40, 3], ['f', 'a', 'c']]
lists[0]
lists[0][0]



# タプルの作成
z = (1, 2, 3, 'a', 'b', 'c')
z[0]
z[1:4]

len(z)
