''' Question:
*   Given the following interface, implement its methods.
*       interface Monarchy {
*           void birth(String child, String parent);
*           void death(string name);
*           List<String> getOrderOfSuccession();
*       }
'''


class Monarchy:
    class Person:
        def __init__(self, name):
            self.name = name
            self.children = []
            self.is_alive = True

    def __init__(self, king: str):
        self.king = self.Person(king)
        self._persons = {self.king.name: self.king}

    def birth(self, child: str, parent: str):
        if self._persons.get(parent) is None:
            raise KeyError(f'{parent} is not a member of the monarchy.')
        new_child = self.Person(child)
        self._persons[parent].children.append(new_child)
        self._persons[new_child.name] = new_child

    def death(self, name: str):
        if self._persons.get(name) is None:
            raise KeyError(f'{name} is not a member of the monarchy.')
        self._persons[name].is_alive = False

    def get_order_of_succession(self):
        person = self.king
        order = []
        self._dfs_succession(person, order)
        return order

    def _dfs_succession(self, person, order):
        if person.is_alive:
            order.append(person.name)
        for child in self._persons[person.name].children:
            self._dfs_succession(child, order)


if __name__ == '__main__':
    monarchy = Monarchy('Jake')
    monarchy.birth('Catherine', 'Jake')
    monarchy.birth('Tom', 'Jake')
    monarchy.birth('Celine', 'Jake')
    monarchy.birth('Jane', 'Catherine')
    monarchy.birth('Mark', 'Catherine')
    monarchy.birth('Peter', 'Celine')
    monarchy.birth('Farah', 'Jane')
    monarchy.death('Catherine')
    print(monarchy.get_order_of_succession())
