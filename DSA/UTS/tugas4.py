class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Tambah node di akhir
    def tambah_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Hapus node berdasarkan value
    def hapus_node(self, target):
        temp = self.head
        if temp is not None and temp.data == target:
            self.head = temp.next
            temp = None
            return
        
        prev = None
        while temp is not None and temp.data != target:
            prev = temp
            temp = temp.next
            
        if temp is None:
            return
            
        prev.next = temp.next
        temp = None

    # Tampilkan data
    def tampilkan(self):
        temp = self.head
        hasil = []
        while temp:
            hasil.append(temp.data)
            temp = temp.next
        print(" -> ".join(hasil))

# Implementasi
ll = LinkedList()
ll.tambah_node("User_A")
ll.tambah_node("User_B")
ll.tambah_node("User_C")

print("Data Linked List Awal:")
ll.tampilkan()

ll.hapus_node("User_B")
print("\nSetelah 'User_B' dihapus:")
ll.tampilkan()
