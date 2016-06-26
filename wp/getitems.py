import MySQLdb
import re
import os

# Adhesives & Sealants,17130502470000000000000000000000,Business Directory|1713 > A|171305
# Adhesives & Glues,17130502470100000000000000000000,Business Directory|1713 > A|171305 > Adhesives & Sealants|17130502

rpass = os.getenv('RPASS')

db = MySQLdb.connect(host="localhost",
                     user='root',
                     passwd=rpass,
                     db='rcats')

cur = db.cursor()

recur = db.cursor()
headers = "Entry Type,Entry ID,Organization,Notes,Address 1 | Line One,Address 1 | City,Address 1 | State,Address 1 | Zipcode,Phone | Work Phone,Email | Work Email,Link | Website,Categories"
q = "select 'organization',r.id,r.name, r.short_content, z.addr, z.city, 'arizona', z.zip, z.phone, z.email,  r.url, r.itemcode from ab_biz_org as z join rcatdb_items as r on r.id = z.id"
cur.execute(q)

print headers

for row in cur.fetchall():

    line = ','.join(['"%s"' % str(x) for x in row[:-1]])

    cat = row[11].strip('\x00')

    # if not tucson, next; also don't keep news days
    if len(cat) < 3 or cat[0] != '\x17' or (cat[0:3] == '\x17\x13\x01') or (cat[0:2] == '\x17\x02'):
        continue
    
    slug = cat.encode("hex")
    line += ',' + slug

    print line

db.close()
