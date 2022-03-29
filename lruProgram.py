#Name:  Juan Carlos Manotas
#Email: jmanotas@gmail.com

#* An LRU cache is temporary storage for objects.
#* An object is a key-value pair (String key, Object value).
class ObjectNode(object):
    # Method Contruct receive or set
    def __init__(self, llave, valor):
        self.llave = llave
        self.valor = valor
        self.siguiente = None
        self.anterior = None

class LRUSession:
    # Constructor inicial que recibe el parametro max_size elements
    # * The cache can contain max_size elements.
    def __init__(self, num_elementos: int):
        self.num_elementos = num_elementos
        self.lookup = {}
        self.obj_initial = ObjectNode(0,0)
        self.cabeza = self.obj_initial.siguiente
        self.cola = self.obj_initial.siguiente

    # add the new node to the cola 
    def add_new_node(self, new_node):
        if not self.cola:
            self.cabeza = self.cola = new_node
        else:
            self.cola.next = new_node
            new_node.prev = self.cola
            self.cola = self.cola.next

    # unlink curent node
    def unlink_node(self, node):
        if self.cabeza is node:
            self.cabeza = node.next
            print(f"Unlink node head: key={node.next.llave}, value={node.next.valor}")
            if node.next:
                node.next.prev = None
                print(f"Unlink node previous: key={node.next.prev}, value={node.next.prev}")
            return

        # removing the node from somewhere in the middle; update pointers
        prev, nex = node.prev, node.next
        prev.next = nex    
        nex.prev = prev


    def get_object(self, llave: int) -> int:
        print(f"Get_object key search: {llave}")
        if llave not in self.lookup:
            print("We return -1 because it does not exist.")
            return -1

        node = self.lookup[llave]

        if node is not self.cola:
            self.unlink_node(node)
            self.add_new_node(node)
            print(f"Add_object linea 58 to node key={node.llave}, value={node.valor}")
        
        print(f"We return the value:{node.valor} according to the key search:{llave}")
        return node.valor


    def add_object(self, llave: int, valor: str) -> None:
        if llave in self.lookup:
            print(f"this node already exists key={llave}, value={valor}")
            self.lookup[llave].val = valor
            self.get_object(llave)
            return

        if (len(self.lookup) == self.num_elementos):
            # remove head node and correspond key
            print(f"remove the node with key={llave}, value={valor}")
            self.lookup.pop(self.cabeza.llave)
            self.del_node_head()
        
        # add new node and hash key
        new_node = ObjectNode(valor=valor, llave=llave)
        self.lookup[llave] = new_node
        self.add_new_node(new_node)
        print(f"add_object linea 80 to node key={new_node.llave}, value={new_node.valor}")

    #remove node head
    def del_node_head(self):
        if not self.cabeza:
            return
        prev = self.cabeza
        self.cabeza = self.cabeza.next
        if self.cabeza:
            self.cabeza.prev = None
        del prev

    def print_node(self):
        print("========================================")
        print("             FINAL RESULT               ")
        print("========================================")
        print("Least Recently Used (LRU):")
        print("")
        for k, v in self.lookup.items():
            print(f"key={k}, value={v.valor}")
