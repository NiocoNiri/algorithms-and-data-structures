
class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self, values=()):
        self.root = None
        self._size = 0
        for value in values:
            self.insert(value)

    def __len__(self):
        return self._size

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            while True:
                if value <= current.value:
                    if current.left is None:
                        current.left = new_node
                        break
                    current = current.left
                else:
                    if current.right is None:
                        current.right = new_node
                        break
                    current = current.right
        self._size += 1

    def search(self, value):
        current = self.root
        while current is not None:
            if value == current.value:
                return current
            if value < current.value:
                current = current.left
            else:
                current = current.right
        return None

    def __contains__(self, value):
        return self.search(value) is not None

    def delete(self, value):
        parent = None
        current = self.root

        while current is not None and current.value != value:
            parent = current
            if value < current.value:
                current = current.left
            else:
                current = current.right

        if current is None:
            return False

        if current.left is not None and current.right is not None:
            replacement_parent = current
            replacement = current.left
            while replacement.right is not None:
                replacement_parent = replacement
                replacement = replacement.right
            current.value = replacement.value
            parent = replacement_parent
            current = replacement

        child = current.left if current.left is not None else current.right
        if parent is None:
            self.root = child
        elif parent.left is current:
            parent.left = child
        else:
            parent.right = child

        self._size -= 1
        return True

    def minimum(self):
        if self.root is None:
            raise ValueError("Дерево пустое")
        current = self.root
        while current.left is not None:
            current = current.left
        return current.value

    def maximum(self):
        if self.root is None:
            raise ValueError("Дерево пустое")
        current = self.root
        while current.right is not None:
            current = current.right
        return current.value

    def inorder(self):
        result = []
        stack = []
        current = self.root
        while current is not None or stack:
            while current is not None:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.value)
            current = current.right
        return result

    def preorder(self):
        result = []
        stack = [self.root] if self.root is not None else []
        while stack:
            current = stack.pop()
            result.append(current.value)
            if current.right is not None:
                stack.append(current.right)
            if current.left is not None:
                stack.append(current.left)
        return result

    def postorder(self):
        """Лево — право — узел."""
        result = []
        stack = [(self.root, False)] if self.root is not None else []
        while stack:
            current, visited = stack.pop()
            if visited:
                result.append(current.value)
            else:
                stack.append((current, True))
                if current.right is not None:
                    stack.append((current.right, False))
                if current.left is not None:
                    stack.append((current.left, False))
        return result


if __name__ == "__main__":
    tree = BinarySearchTree([12, 6, 17, 3, 7, 15, 31, 9])
    print("По возрастанию:", tree.inorder())
    print("Есть 9:", 9 in tree)
    tree.insert(8)
    tree.delete(12)
    print("После вставки 8 и удаления 12:", tree.inorder())
    print("Количество элементов:", len(tree))
