from lruProgram import LRUSession

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Define Capacity max_size
    obj = LRUSession(5)

    obj.add_object(1,"Thanks for giving me ")
    obj.add_object(2,"an opportunity ")
    obj.add_object(3,"I want ")
    obj.add_object(4,"to work with ")
    obj.add_object(5,"UNITEDHEALTH GROUP ")

    obj.get_object(5)

    obj.add_object(6,"My name is Juan Carlos Manotas ")
    obj.get_object(8)

    obj.add_object(7,"I have experience ")

    obj.get_object(5)
    obj.get_object(7)
    obj.get_object(6)

    obj.print_node()
