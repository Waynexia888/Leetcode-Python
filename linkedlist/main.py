from LinkedList import LinkedList

linked_list = LinkedList()

linked_list.add(0, 10)
linked_list.add(1, 20)
linked_list.add(2, 30)
print linked_list.get(0)
print linked_list.get(1)
linked_list.remove(0)
linked_list.remove(0)
linked_list.remove(0)

print linked_list.empty()