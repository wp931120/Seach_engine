from  elasticsearch import Elasticsearch

class Searchengine:
    def __init__(self):
        self.es = Elasticsearch(hosts="http://localhost:9200",
                                sniff_on_start=True,
                                sniff_on_connection_fail=True,
                                sniffer_timeout=60)

    def search(self,keywords):
        query = {
            "size": 10,
            "query": {
                "bool": {
                    "should": [
                        {"match": {"content": "{}".format(keywords)}},
                        {"match": {"title": "{}".format(keywords)}}
                    ]
                }
            },
            "highlight": {
                "fields": {
                    "title": {},
                    "content": {
                        "type": "plain"
                    }
                }
            }
        }
        # print(query)
        response = self.es.search(index='news', body=query)
        response_highlight = self._highlight(response)
        return response_highlight

    def _highlight(self,response_es):
        article_list = response_es["hits"]["hits"]
        for article in article_list:
            source = article["_source"]
            highlight = article["highlight"]
            for key in highlight.keys():
                item = highlight[key][0]
                temp = item
                temp = temp.replace("<em>", "")
                temp = temp.replace("</em>", "")
                item = item.replace("<em>","<span style='color:red'>")
                item = item.replace("</em>", "</span>")
                source[key] = source[key].replace(temp,item)
        return  article_list



if __name__ == "__main__":
    searchengine = Searchengine()
    res = searchengine.search("发现债券")
    print(res)
