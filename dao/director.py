from dao.model.directors import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get(self, did=None):
        query = self.session.query(Director)
        if did:
            return query.get(did)
        else:
            return query.all()
