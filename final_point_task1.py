class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insertAtHead(self, value):
        newNode = Node(data=value)
        if self.head is not None:
            newNode.next = self.head
        self.head = newNode
        return

    def insertAtEnd(self, value):
        if self.head is None:
            self.insertAtHead(value)
        newNode = Node(value)
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = newNode

    def searchAndDelete(self, searchItem):
        temp = Node()
        if self.head is searchItem:
            temp = self.head
            self.head = self.head.next
        else:
            currentNode = self.head
            while currentNode.next is not None:
                if currentNode.next.data is searchItem:
                    temp = currentNode.next
                    currentNode.next = currentNode.next.next
                else:
                    currentNode = currentNode.next

        return

    def insertAfter(self, searchItem, value):
        newNode = Node(data=value)
        temp = self.head
        while temp.next is not None and temp.data is not searchItem:
            temp = temp.next
        newNode.next = temp.next
        temp.next = newNode

        return

    def insertbefore(self, searchItem, value):
        newNode = Node(data=value)
        temp = self.head
        while temp.next is not None and temp.next.data is not searchItem:
            temp = temp.next
        newNode.next = temp.next
        temp.next = newNode

        return

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next

        return result


def func_reverse(arr, i=0):
    if i == len(arr.list())-1:
        return arr

    arr.insertAtHead(arr.list()[-1])
    arr.searchAndDelete(arr.list()[0])
    return func_reverse(arr, i+1)


def func_sorted(arr):
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        return merge(merge_sort(left_half), merge_sort(right_half))

    def merge(left, right):
        merged = []
        left_index = 0
        right_index = 0

        # Спочатку об'єднайте менші елементи
        while left_index < len(left) and right_index < len(right):
            if left[left_index] <= right[right_index]:
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1

        # Якщо в лівій або правій половині залишилися елементи,
                # додайте їх до результату
        while left_index < len(left):
            merged.append(left[left_index])
            left_index += 1

        while right_index < len(right):
            merged.append(right[right_index])
            right_index += 1

        return merged

    def create_link_sorted(arr):
        sortedSinglyLinkedList = SinglyLinkedList()
        sortedSinglyLinkedList.insertAtHead(arr[0])
        for element in arr[1:]:
            sortedSinglyLinkedList.insertAtEnd(element)

        return sortedSinglyLinkedList

    sortedList = merge_sort(arr.list())
    newSinglyLinkedList = create_link_sorted(sortedList)

    return newSinglyLinkedList


def func_union(link1, link2):
    for element in link2.list():
        link1.insertAtEnd(element)

    return link1


SinglyLinkedList1 = SinglyLinkedList()
SinglyLinkedList1.insertAtHead(5)
SinglyLinkedList1.insertAtHead(6)
SinglyLinkedList1.insertAtHead(7)
SinglyLinkedList1.insertAtEnd(9)
SinglyLinkedList1.insertAfter(7, 10)
SinglyLinkedList1.insertbefore(9, 11)


print("Орігінал:\t", SinglyLinkedList1.list())

# Завдання 1
print("Реверсія:\t", func_reverse(SinglyLinkedList1).list())
print("\n")

# Завдання 2
print("Сортування:\t", func_sorted(SinglyLinkedList1).list())
print("\n")

# Завдання 3
SinglyLinkedList2 = SinglyLinkedList()
SinglyLinkedList2.insertAtHead(5)
SinglyLinkedList2.insertAtEnd(6)
SinglyLinkedList2.insertAtEnd(7)
SinglyLinkedList2.insertAtEnd(9)

SinglyLinkedList3 = SinglyLinkedList()
SinglyLinkedList3.insertAtHead(10)
SinglyLinkedList3.insertAtEnd(12)
SinglyLinkedList3.insertAtEnd(14)

print("Список1:\t", SinglyLinkedList2.list())
print("Список2:\t", SinglyLinkedList3.list())
print("Об'єднання:\t", func_union(SinglyLinkedList2, SinglyLinkedList3).list())
