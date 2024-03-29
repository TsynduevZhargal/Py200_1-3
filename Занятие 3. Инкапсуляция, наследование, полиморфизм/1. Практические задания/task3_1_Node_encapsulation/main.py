from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """
        Создаем новый узел для односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        """
        self.value = value

        self.__next = None  # TODO заменить на private
        self.set_next(next_)

    def __repr__(self) -> str:
        return f"Node({self.value}, {None})" if self.__next is None else f"Node({self.value}, Node({self.__next}))"  # TODO заменить на private

    def __str__(self) -> str:
        return str(self.value)

    def is_valid(self, node: Any) -> None:
        if not isinstance(node, (type(None), Node)):
            raise TypeError

    def set_next(self, next_: Optional["Node"] = None) -> None:
        self.is_valid(next_)
        self.__next = next_  # TODO заменить на private


if __name__ == "__main__":
    first_node = Node("first_node")
    second_node = Node("second_node")
    dg_node = Node("second_node")

    first_node.set_next(second_node)
    print(repr(first_node), repr(second_node))
