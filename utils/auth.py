import hashlib, sqlite3


def signup( email, user, pazz, pazz2):
    if(pazz != pazz2):
        return False

    f="data/user.db"
    db = sqlite3.connect(f);
    c = db.cursor()
    c.execute("SELECT username FROM userdata WHERE username="+"'"+ user"'"+";")
    if len(c.fetchall()) > 0:
        return false

    else:
        c.execute('INSERT INTO data (username, password, email) VALUES("'+user+'","'+pazz+'","'+email+'");')

    db.commit()
    db.close()
    return True


def login(user, pazz):
    f="data/user.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    c.execute("SELECT password FROM data WHERE username="+"'"+user+"'"+";")
    account = c.fetchall()
    db.commit()
    db.close()

    for line in account:
        for entry in line:
            if(pazz == entry):
                return True
    return False
