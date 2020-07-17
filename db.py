import sqlite3



def findLama(id):
    conn = sqlite3.connect('alpashop.db', check_same_thread=False)
    c = conn.cursor()
    lstLamas = []
    if id != "*":
        query = "SELECT nom from animal a where a.nom = " + str(id)
        # retourne un lama (id)
        c.execute(str(query))
        print (c.fetchone())
        for lama in c:
            # lama[0] = nom
            lstLamas.append(lama[0])
    else:
        
        # retourne tous les lamas
        query = "SELECT nom, age, poids, c.libelle, t.libelle, a.description, a.image, l.puht FROM animal a INNER JOIN lama l ON a.id = l.id INNER JOIN couleur c ON a.fk_couleur = c.id INNER JOIN temperament t ON l.fk_temperament = t.id"
        c.execute(query)
    

        lstLamas = []
        for lama in c:
            # lama[0] = nom, lama[1] = age, lama[2] = poids, lama[3] = couleur, lama[4] = temperament, lama[5] = description, lama[6] = image, lama[7] = puht
            lstLamas.append([lama[0],lama[1],lama[2],lama[3],lama[4],lama[5],lama[6], lama[7]])
    c.close()
    conn.close()

    return lstLamas

def findAll(id):
    conn = sqlite3.connect('alpashop.db', check_same_thread=False)
    c = conn.cursor()

    if id != "*":
        # retourne tous les lamas
        query = "SELECT nom, age, poids, c.libelle, a.description, a.image FROM animal a INNER JOIN couleur c ON a.fk_couleur = c.id WHERE l.id = " + str(id)
    else:
        # retourne un lama (id)
        query = "SELECT nom, age, poids, c.libelle, a.description, a.image FROM animal a INNER JOIN couleur c ON a.fk_couleur = c.id"

    c.execute(query)

    lstLamas = []
    for lama in c:
        # lama[0] = nom, lama[1] = age, lama[2] = poids, lama[3] = couleur, lama[4] = description, lama[5] = image
        lstLamas.append([lama[0],lama[1],lama[2],lama[3],lama[4],lama[5]])
    c.close()
    conn.close()

    return lstLamas







