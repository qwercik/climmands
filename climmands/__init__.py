class Command:
    """
    Base command class
    """

    def initialize_arguments_parser(self, parser):
        """
        Initialize arguments parser (argparse)
        Add arguments of the command
        """

    def execute(self, parsed_arguments):
        """
        Execute the current command with arguments passed by user
        """


class CommandExecutor:
    """
    Execute a proper command with data passed by user
    """

    def __init__(self, commands_list):
        self.commands = {}
        for command in commands_list:
            self.commands[command.name] = command

    def execute(self, parsed_arguments):
        executing_command_name = parsed_arguments.command
        if executing_command_name is None:
            return False

        executing_command = self.commands[executing_command_name]
        executing_command.execute(parsed_arguments)
        return True


class CommandLoader:
    """
    Load all commands and initialize arguments parser with them
    """

    def __init__(self, parser):
        self.subparsers = parser.add_subparsers(dest='command')
        self.commands_loaded = []

    def load_commands(self):
        for CommandClass in Command.__subclasses__():
            command = CommandClass()
            parser = self.subparsers.add_parser(CommandClass.name,
                                                help=CommandClass.description)
            command.initialize_arguments_parser(parser)

            self.commands_loaded.append(command)

        return self.commands_loaded

