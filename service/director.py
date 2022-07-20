from dao.director import DirectorDAO


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get(self, director_id=None):
        return self.dao.get(director_id)
