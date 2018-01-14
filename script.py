## script to parse directory and reorganize the files
papers = sorted(os.listdir('../socialchoice/Paper'))
base = 'http://github.com/horsehour/socialchoice/blob/master/Paper/'
for paper in papers:
    if '.' == paper[0]:
        continue
    year = paper[:4]
    i, rid = paper.index('-'), paper.rindex('-')
    if rid == -1 or i == rid:
        rid = paper.index('.')
    name = paper[paper.index('-') + 1:rid].strip(' ')
    author = paper[rid + 1:paper.rindex('.')].strip(' ')
    paper = paper.replace(' ', '%20')
    pdf = '- <a href="{0}" target="_blank">{1}</a>, {2}, by {3}'.format(base + paper, name, year, author)
    print(pdf)
