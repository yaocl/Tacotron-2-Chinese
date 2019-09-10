import csv
import re
from pypinyin import pinyin, lazy_pinyin, Style

path_pattern = re.compile(r'common_voice_zh-TW_([\d]+).mp3', re.S)


with open('validated-sample.tsv') as tsvfile:
	reader = csv.DictReader(tsvfile, delimiter='\t')
	for row in reader:
		pinyin = lazy_pinyin(row['sentence'], style=Style.TONE3)

		path_match = re.match(path_pattern, row['path'])
		if path_match:
			path_index = path_match.group(1)
		else:
			path_index = -1

		if path_index != -1 and row['gender']=='female' :
			print('path={path}, path_index={path_index}, sentence={sentence}, gender={gender}, pinyin={pinyin}'.format(path=row['path'], path_index=path_index, sentence=row['sentence'], gender=row['gender'], pinyin=" ".join(pinyin)) )
