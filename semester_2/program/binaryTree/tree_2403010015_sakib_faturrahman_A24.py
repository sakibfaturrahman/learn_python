class BinarySearchTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insert(self, newNode):
        if newNode < self.key:
            if self.leftChild is None:
                self.leftChild = BinarySearchTree(newNode)
            else:
                self.leftChild.insert(newNode)
        elif newNode > self.key:
            if self.rightChild is None:
                self.rightChild = BinarySearchTree(newNode)
            else:
                self.rightChild.insert(newNode)

    def find(self, val):
        if val == self.key:
            return True
        elif val < self.key and self.leftChild:
            return self.leftChild.find(val)
        elif val > self.key and self.rightChild:
            return self.rightChild.find(val)
        return False

    def delete(self, val):
        if val < self.key:
            if self.leftChild:
                self.leftChild = self.leftChild.delete(val)
        elif val > self.key:
            if self.rightChild:
                self.rightChild = self.rightChild.delete(val)
        else:
            if self.leftChild is None:
                return self.rightChild
            elif self.rightChild is None:
                return self.leftChild
            minLargerNode = self.rightChild._minValueNode()
            self.key = minLargerNode.key
            self.rightChild = self.rightChild.delete(minLargerNode.key)
        return self

    def _minValueNode(self):
        current = self
        while current.leftChild:
            current = current.leftChild
        return current

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def getRootVal(self):
        return self.key


def preorder(tree):
    return [tree.getRootVal()] + preorder(tree.getLeftChild()) + preorder(tree.getRightChild()) if tree else []

def inorder(tree):
    return inorder(tree.getLeftChild()) + [tree.getRootVal()] + inorder(tree.getRightChild()) if tree else []

def postorder(tree):
    return postorder(tree.getLeftChild()) + postorder(tree.getRightChild()) + [tree.getRootVal()] if tree else []

def countNodes(tree):
    return 0 if tree is None else 1 + countNodes(tree.getLeftChild()) + countNodes(tree.getRightChild())

def height(tree):
    if tree is None:
        return 0
    left_height = height(tree.getLeftChild())
    right_height = height(tree.getRightChild())
    return max(left_height, right_height) + 1


def menu(tree):
    while True:
        print("\nMenu:")
        print("1. Search")
        print("2. Delete")
        print("3. Keluar dari menu")

        pilihan = input("Pilih opsi (1/2/3): ")

        if pilihan == "1":
            while True:
                try:
                    cari = int(input("Masukkan nilai yang ingin dicari: "))
                    ditemukan = tree.find(cari)
                    print(f"Hasil: {cari} {'true' if ditemukan else 'false'}.")
                except:
                    print("Input tidak valid.")
                ulang = input("Ingin search lagi? (Y/T): ").lower()
                if ulang != "y":
                    break

        elif pilihan == "2":
            while True:
                try:
                    hapus = int(input("Masukkan nilai yang ingin dihapus: "))
                    if tree.find(hapus):
                        tree = tree.delete(hapus)
                        print(f"{hapus} berhasil dihapus.")
                        print("Inorder setelah hapus:", inorder(tree))
                    else:
                        print(f"{hapus} tidak ditemukan.")
                except:
                    print("Input tidak valid.")
                ulang = input("Ingin hapus lagi? (Y/T): ").lower()
                if ulang != "y":
                    break

        elif pilihan == "3":
            print("Keluar dari menu.")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih 1/2/3.")

    return tree  

# Penggunaan
if __name__ == "__main__":
    tree = BinarySearchTree(int(input("Masukkan root: ")))
    while True:
        val = input("Masukkan angka (atau 'selesai'): ")
        if val.lower() == "selesai":
            break   
        tree.insert(int(val))

    print("\nNama : Sakib Faturrahman")
    print("NIM  : 1234567890")
    print("Kelas: TI-A\n")

    print("Inorder :", inorder(tree))
    print("Preorder:", preorder(tree))
    print("Postorder:", postorder(tree))
    print("\nJumlah node:", countNodes(tree))
    print("Tinggi tree:", height(tree))

    # panggil menu
    tree = menu(tree)
