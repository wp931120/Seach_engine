import glob
import json
import tqdm
import requests


def article2dic(file):
    dic_article = {}
    with open(file, "r") as f:
        title = ""
        content = ""
        for i, line in enumerate(f.readlines()):
            line = line.strip()
            line = line.replace("\u3000", "")
            if i == 0:
                title += line
            else:
                content += line
        dic_article["title"] = title
        dic_article["content"] = content
    return dic_article


def save_news2jsons(file_list):
    article_list = []
    for file in tqdm.tqdm(file_list):
        article_dic = article2dic(file)
        article_list.append(article_dic)
    return article_list


def load_data2es(article_list):
    for i in tqdm.tqdm(article_list):
        data = json.dumps(i)
        try:
            base_url = "http://localhost:9200/" + "news" + "/" + "_doc" + "/"
            response = requests.post(base_url, headers={"Content-Type": "application/json"}, data=data.encode())
        except:
            print("失败")

if __name__ == "__main__":
    file_list = glob.glob("./THUCNews/房产/*")
    articlelist = save_news2jsons(file_list)
    load_data2es(articlelist)

