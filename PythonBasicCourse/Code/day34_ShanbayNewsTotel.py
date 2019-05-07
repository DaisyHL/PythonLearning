from urllib.request import urlopen
import re
#shanbay_news = urlopen("https://www.shanbay.com/news/articles")
shanbay_news = urlopen("https://assets.baydn.com/baydn/public/codetime/1/shanbay_news.html")
news_data = shanbay_news.read().decode()
# 获取标题
find_news = re.findall("news-title\">.*?</i></span></p></div>",news_data)
title_start = "news-title\">"
title_end = "</p>"
view_start = "读后感：<!-- /react-text --><i>"
word_start = "单词：<!-- /react-text --><i>"
diff_start = "难度：<!-- /react-text --><i>"
find_end = "</i>"
count = 0
for news in find_news:
    title = re.findall("news-title\">.*?</p>",news)
    view = re.findall("读后感.*?</i>",news)
    word = re.findall("单词.*?</i>",news)
    difficulty = re.findall("难度.*?</i>",news)
    title = str(title)[len(title_start)+2:-len(title_end)-2]
    view = str(view)[len(view_start)+2:-len(find_end)-2]
    word = str(word)[len(word_start)+2:-len(find_end)-2]
    difficulty = str(difficulty)[len(diff_start)+2:-len(find_end)-2]
    count += 1
    print("标题{}:{},读后感:{},{}单词,难度:{}".format(count,title,view,word,difficulty))
