import requests
import time

files = [
    {"file": "linkedinsample.txt",
     "type": "linkedin"},
    {"file": "neopetssample.txt",
     "type": "neopets"},
    #{"file": "neopets.txt",
     #"type": "neopets"}
]

if __name__ == '__main__':

    while True:
        try:
            r = requests.put(url="http://localhost:9200/binary", json={
                "settings": {
                    "analysis": {
                        "analyzer": {
                            "email": {
                                "tokenizer": "uax_url_email",
                                "filter": [
                                    "lowercase",
                                    "unique"
                                ]
                            }
                        }
                    }
                },
                "mappings": {
                    "linkedin": {
                        "properties": {
                            "email": {
                                "type": "text",
                                "analyzer": "email"
                            }
                        }
                    },
                    "neopets": {
                        "properties": {
                            "email": {
                                "type": "text",
                                "analyzer": "email"
                            }
                        }
                    }
                }
            })
        except requests.exceptions.ConnectionError:
            time.sleep(10)
            continue
        break

    print "create mapping"
    print r.status_code
    print r.text
    print ""

    i = 1

    for entry in files:
        with open(entry["file"]) as f:
            contents = f.readlines()

        data = ""
        N = 100000
        TOTAL = len(contents)

        while len(contents) != 0:
            for x in contents[:N]:
                data += '{"index":{"_id":"' + str(i) + '"}}\n{"email": "' + x.strip() + '"}\n'
                i += 1

            print "bulk " + entry["file"]

            r = requests.post(url="http://localhost:9200/binary/"+entry["type"]+"/_bulk",
                              headers={'Content-type': 'application/x-ndjson'},
                              data=data)

            print r.status_code

            contents = contents[N:]

            print str((1-((len(contents)*1.0)/(TOTAL*1.0)))*100), "%"
