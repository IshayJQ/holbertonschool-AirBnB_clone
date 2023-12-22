import cmd


class HBNBCommand(cmd.Cmd):
    """
    Command line interpreter handler to loop and interact within classes.
    """
    prompt = "(hbnb) "

    def do_quit():
        """This method is to exit from the program"""
        return True

    def do_EOF():
        """This·method·is·to·exit·from the program when the last line is EOF"""
        return True

    def do_create():
        pass

    def do_update():
        pass

    def do_delete():
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
