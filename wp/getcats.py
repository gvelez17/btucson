import MySQLdb
import re
import os

rpass = os.getenv('RPASS')

db = MySQLdb.connect(host="localhost",
                     user='root',
                     passwd=rpass,
                     db='rcats')


cur = db.cursor()

recur = db.cursor()


cur.execute(" select * from rcatdb_categories where LEFT(catcode, 2) = (select LEFT(catcode,2) from rcatdb_categories where name = 'Tucson') order by catcode")

for row in cur.fetchall():
    relurl = row[3]
    if not relurl:
        continue
    parts = re.split('/', relurl)
    parts = parts[1:-1]  # has blank at each end 
    if len(parts) < 2:
        continue
    # if not tucson, next; also don't keep news days
    if row[4][0] != '\x17' or (row[4][0:3] == '\x17\x13\x01') or (row[4][0:2] == '\x17\x02'):
        continue
    
    slug = row[4].encode("hex")

    name = parts[-1]
    mx = len(parts) -1
    # first item in code is 'tucson' but is not in the categories
    # keep it in the code anyway so it matches back to original
    shlugs = [parts[j] + '|' + row[4][0:j+2].encode("hex") for j in range(1, mx)]
    parent = ' > '.join(shlugs)
    if not parent:
        continue
    parent = re.sub(',',' ',parent)
    print "%s,%s,%s" % (name, slug, parent)

db.close()
