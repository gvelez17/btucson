import MySQLdb
import re


db = MySQLdb.connect(host="localhost",
                     user='root',
                     passwd='grummich',
                     db='rcats')


cur = db.cursor()

recur = db.cursor()

cur.execute("SELECT * from rcatdb_categories")



for row in cur.fetchall():
    relurl = row[3]
    if not relurl:
        continue
    parts = re.split('/', relurl)
    if len(parts) < 5:
        continue
    # if not tucson, next; also don't keep news days
    if row[4][0] != '\x17' or (row[4][0:3] == '\x17\x13\x01') or (row[4][0:2] == '\x17\x02'):
        continue
    
    slug = row[4].encode("hex")

    name = parts[-2]
    mx = len(parts) - 2
    shlugs = [parts[j] + '|' + row[4][0:j].encode("hex") for j in range(3, mx)]
    parent = ' > '.join(shlugs)
    if not parent:
        continue
    print "%s,%s,%s" % (name, slug, parent)

db.close()
