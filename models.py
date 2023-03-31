from extensions import db

db.metadata.clear()

class Game(db.Model):
    name = db.Column(db.String(100),primary_key=True)
    console = db.Column(db.String(20))
    price = db.Column(db.Float,nullable = False)
    grade = db.Column(db.Integer,nullable = False)

    def __repr__(self) -> str:
        return f"{self.name} - {self.console} - RS {self.price} - {self.grade}"
    


if __name__ == "__main__":
    from app import app

    with app.app_context():
        db.drop_all()
        db.create_all()

        games_list = [{"name":"DEAD SPACE REMAKE","console":"PS5","price":350.00,"grade":10},
                        {"name":"FORSPOKEN","console":"PC","price":299.00,"grade":8},
                        {"name":"DEAD ISLAND 2","console":"PS5","price":350.00,"grade":10},
                        {"name":"HOGWARTS LEGACY","console":"PC","price":219.00,"grade":7},
                        {"name":"WILD HEARTS","console":"XBox Series","price":350.00,"grade":7},
                        {"name":"RESIDENT EVIL 4","console":"PS5","price":289.00,"grade":10},
                        {"name":"THE LEGEND OF ZELDA: TEARS OF THE KINGDOM","console":"Switch","price":350.00,"grade":10}
                        ]
        for game in games_list:

            game = Game(name = game["name"],console=game["console"],price = game["price"], grade =game["grade"])
            db.session.add(game)
            db.session.commit()

            result = db.session.query(Game).all()

            for game in result:
                print(game)