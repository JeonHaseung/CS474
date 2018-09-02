import sqlite3 as lite

database_filename = 'temp.db'
conn = lite.connect(database_filename)
cs = conn.cursor()

Query = "SELECT title, content from data where date like '%{}%'"

years = ["2018"]#, "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017"]
month = ["01","02","03","04","05","06","07","08"]#,"09","10","11","12"]

for y in years:
    for m in month:
        query = Query.format(y+m)
        cs.execute(query)
        x = cs.fetchall()
        d = dict()
        for a in x:
            title = a[0]
            content = a[1]
            
            word_in_title = title.split()
            word_in_content = title.split()
            
            for word in word_in_title:
                if word in d:
                    d[word] = d[word] + 1
                else:
                    d[word] = 1
            
            for word in word_in_content:
                if word in d:
                    d[word] = d[word] + 1
                else:
                    d[word] = 1
            
        result = sorted(d.items(), key=(lambda x: x[1]))
        result.reverse()
        print(y+m)
        print(result[:10])