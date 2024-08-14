import pytest
from flaskr.db import get_db




def test_mod(client, auth, app):
    auth.login()
    assert client.get("/auth/mod").status_code == 200
    client.post("/auth/mod", data={"email": "Mod@gmail.com"})

    with app.app_context():
        db = get_db()
        user = db.execute("SELECT * FROM user WHERE id = 1").fetchone()
        assert user["email"] == "Mod@gmail.com"


