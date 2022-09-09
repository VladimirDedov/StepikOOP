class Vertex:
    """Представление вершин графа (на карте это могут
    быть: здания, остановки, достопримечательности и т.п.)"""

    def __init__(self):
        self._links = []  # список связей с другими вершинами графа (список объектов класса Link)

    @property
    def links(self):
        return self._links


class Link:
    """для описания связи между двумя произвольными вершинами
     графа (на карте: маршруты, время в пути и т.п.)"""

    def __init__(self, v1, v2):#v1, v2 - объекты класса Vertex (вершины графа)
        self._v1 = v1
        self._v2 = v2
        self._dist=1

    @property
    def v1(self):
        return self._v1

    @property
    def v2(self):
        return self._v2

    @property
    def dist(self):
        return self._dist


class LinkedGraph:
    """Для представления связного графа в целом (карта целиком).
    """
    def __init__(self):
        self._links