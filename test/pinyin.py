from pypinyin import pinyin, lazy_pinyin, Style

sentences = ["今日颱風外圍環流影響", "臺灣西半部及東北部地區有短暫陣雨或雷雨", "易有局部大雨或豪雨發生", 	"東部東南部地區及澎湖金門馬祖亦有局部短暫陣雨或雷雨"]

for sentence in sentences:
	pinyin = lazy_pinyin(sentence, style=Style.TONE3)
	print('{pinyin}'.format(pinyin=" ".join(pinyin)))
