class TreeObj:
    """для описания вершин и листьев решающего дерева"""

    def __init__(self, indx, value=None):
        self.indx = indx
        self.value = value
        self.__left = None
        self.__right = None

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, left):
        self.__left = left

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, right):
        self.__right = right


class DecisionTree:
    """для работы с решающим деревом в целом"""
    list_obj = []

    @classmethod
    def add_obj(cls, obj, node=None, left=True):
        """для добавления вершин в решающее дерево
         (метод должен возвращать добавленную вершину - объект класса TreeObj);"""
        if len(cls.list_obj) == 0:
            cls.list_obj.append(obj)
        else:
            if left:
                node.left = obj
            else:
                node.right = obj
            cls.list_obj.append(obj)
        return obj

    @classmethod
    def predict(cls, root, x):
        """ для построения прогноза (прохода по решающему дереву) для вектора x из корневого узла дерева root"""
        res = root
        if x[0]==0:
            x.pop(1)
        for i in x:
            if i == 1:
                res = res.left
            else:
                res = res.right

            if res.left == None:
                break
        return res.value


root = DecisionTree.add_obj(TreeObj(0))
v_11 = DecisionTree.add_obj(TreeObj(1), root)
v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
DecisionTree.add_obj(TreeObj(-1, "программист"), v_11)
DecisionTree.add_obj(TreeObj(-1, "кодер"), v_11, False)
DecisionTree.add_obj(TreeObj(-1, "посмотрим"), v_12)
DecisionTree.add_obj(TreeObj(-1, "нет"), v_12, False)
# root = DecisionTree.add_obj(TreeObj(0))
# v_11 = DecisionTree.add_obj(TreeObj(1), root)
# v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
# DecisionTree.add_obj(TreeObj(-1, "будет программистом"), v_11)
# DecisionTree.add_obj(TreeObj(-1, "будет кодером"), v_11, False)
# DecisionTree.add_obj(TreeObj(-1, "не все потеряно"), v_12)
# DecisionTree.add_obj(TreeObj(-1, "безнадежен"), v_12, False)
# j=0
# for i in DecisionTree.list_obj:
#     print(f'{i.indx} значение с индексом {j}')
#     j+=1
print(DecisionTree.predict(root, [1, 0,1]))
