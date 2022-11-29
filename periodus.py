import sqlite3

con = sqlite3.connect(':memory:')

cur = con.cursor()

class Adatbazis:
    def __init__(self,sor):
        AtomicNumber,Element,Symbol,AtomicMass, *felesleg  = sor.strip().split(",")
        self.AtomicNumber = AtomicNumber
        self.Element = Element
        self.Symbol = Symbol
        self.AtomicMass = AtomicMass
        
        
        
with open("tablazat.csv","r",encoding="latin2") as f:
    fejlec = f.readline()
    adat = [Adatbazis(sor) for sor in f]
cur.execute("DROP TABLE IF EXISTS period")



cur.execute("""CREATE TABLE period
        (AtomicNumber TEXT,
        Element TEXT,
        Symbol TEXT,
        AtomicMass TEXT)
""")


for i in adat:
    lista = [(i.AtomicNumber,i.Element,i.Symbol,i.AtomicMass)]
    cur.executemany("INSERT INTO period VALUES (?,?,?,?) ", lista)
    
con.commit()




uzenet = cur.execute("SELECT * FROM period")

print(uzenet.fetchall())

for sor in cur.execute("SELECT * FROM period"):
    print(sor)

beker = input('Kérek: ')

beker = beker.lower().capitalize()

def fuggveny(beker):
    cur.execute("SELECT * FROM period WHERE symbol = ?",(beker,))
    return(f"elemszam:{cur.fetchall()}")

print(fuggveny(beker))







