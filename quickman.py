#!/usr/bin/env python3

import subprocess

class QuickMan:
    def __init__(self):
        pass

    def print_help(self):
        print("Usage: ./qm.py command_name [flags/options]")

    def print_command_info(self, man_output):
        end_on_empty_line = False
        for line in man_output[2:]:
            if line.startswith("DESCRIPTION"):
                end_on_empty_line = True
            print(line)
            if not line and end_on_empty_line:
                break

    def print_flag_option(self, man_output, line_index):
        if self.print_flag_option_header:
            print("SPECIFIED FLAGS AND OPTIONS")

        first_line = True 
        while line_index < len(man_output) and man_output[line_index]:
            line = man_output[line_index].strip()
            if first_line:
                print(" " * 5, line, sep='')
                first_line = False
            else:
                print(" " * 12, line, sep='')
            line_index += 1
        print()

    def get_separated_args(self, args):
        actual_args = []
        for arg in args:
            if arg.startswith("--") and len(arg) > 3:
                actual_args.append(arg[2:])
            elif arg[0] == '-':
                sub_arg_list = [sub_arg for sub_arg in arg[1:] if sub_arg.isalpha()]
                if len(sub_arg_list) == len(arg) - 1:
                    actual_args += sub_arg_list
        return actual_args

    def check_flag_option(self, man_output, line_indices, args):
        self.print_flag_option_header = False
        first_flag_option = True 
        args = self.get_separated_args(args)
        for arg in args:
            for index in line_indices:
                next_arg = False
                man_args = man_output[index].split(" ")
                for man_arg in man_args:
                    man_arg = man_arg.strip(', ')
                    if not man_arg: 
                        continue
                    elif man_arg[0] != '-':
                        break
                    if ((len(arg) == 1 and arg == man_arg[1:]) or
                        (len(arg) != 1 and man_arg[2:].startswith(arg)
                            and (len(man_arg) <= (len(arg) + 2)
                            or not man_arg[len(arg) + 2].isalpha()
                            and man_arg[len(arg) + 2] != '-'))):
                        self.print_flag_option(man_output, index)
                        first_flag_option = False
                        next_arg = True
                        break
                if next_arg:
                    break

    def get_flag_option_indices(self, man_output):
        line_indices = []
        for line_index, man_output in enumerate(man_output):
            stripped_line = man_output.strip()
            if stripped_line and stripped_line[0] == '-':
                line_indices.append(line_index)

        return line_indices

    def parse_command(self, command):
        if not command or command[0] == "--help":
            self.print_help()
            return

        man_command_output = subprocess.run(['env', 'COLUMNS=32767', 'man', command[0]], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        man_output = man_command_output.stdout.decode('utf-8').strip().split("\n")
        man_error = man_command_output.stderr.decode('utf-8').strip()

        if man_error.startswith("No manual"):
            print(man_error)
            return

        self.print_command_info(man_output)
        line_indices = self.get_flag_option_indices(man_output)
        self.check_flag_option(man_output, line_indices, command[1:])

