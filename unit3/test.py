import sqlite3
from collections import namedtuple

Link = namedtuple('Link', ['id', 'submitter_id', 'submitted_time', 'votes', 'title', 'url'])

links = [
    Link(0, 60398, 1334014208.0, 109, "C overtakes Java", "http://malarkey"),
    Link(1, 60254, 1334014208.0, 891, "This explains", "http://flabergasted"),
    Link(2, 62945, 1334014208.0, 341, "Lean Haskell", "http://shenanigan"),
]

db = sqlite3.connect(':memory:')
db.execute('create table links (id integer, submitter_id integer, submitted_time integer, votes integer, title text, url text)')
for l in links:
    db.execute('insert into links values (?, ?, ?, ?, ?, ?)', l)

def query():
    c = db.execute("select * from links where id=2")
    link = Link(*c.fetchone())    
    return link.votes

print (query())

