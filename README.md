# Climmands
Climmands is a small package that provides a convenient abstraction for cli subcommands.

Each command is described by different class. These classes should inherit from `Command` class. The `CommandLoader` class is responsible for collecting all commands in module scope. `CommandExecutor` execute a proper command and pass it the rest of command line arguments.

**Warning: it's a toy and untested package. Use only for your own responsibility!**

## Installation
```bash
$ pip install climmands
```

## Example
```python
#!/usr/bin/env python

import argparse
import climmands

class HelloWorldCommand(climmands.Command):
	name = 'hello'
	description = 'Print Hello World message'

	def execute(self, parsed_arguments):
		print('Hello world')

class AddTwoNumbersCommand(climmands.Command):
	name = 'add'
	description = 'Add two numbers and print result'

	def initialize_arguments_parser(self, parser):
		parser.add_argument('first', help='First number')
		parser.add_argument('second', help='Second number')

	def execute(self, parsed_arguments):
		first = int(parsed_arguments.first)
		second = int(parsed_arguments.second)
		result = first + second

		print(f'{first} + {second} = {result}')

def main():
	parser = argparse.ArgumentParser(description='My great command')
	commands = climmands.CommandLoader(parser).load_commands()
	executor = climmands.CommandExecutor(commands)

	parsed_arguments = parser.parse_args()
	if not executor.execute(parsed_arguments):
		parser.print_help()

if __name__ == '__main__':
	main()

```

