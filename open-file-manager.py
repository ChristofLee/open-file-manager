import sublime
import sublime_plugin

class OpenFileManagerCommand(sublime_plugin.WindowCommand):
    debug = False
    group_rules = {
        "1": [".php", ".html", ".py"],
        "2": [".css", ".scss", "LICENSE"],
        "3": [".js", ".todo", "opening.php", ".sublime-menu"]
    }

    def run(self):
        open_files = self.get_filenames()
        if self.debug == True:
            print("open_files")
            self.printListFilenames(open_files)
        grouped_files = self.group_by_group_rules(open_files)
        if self.debug == True:
            print("grouped_files")
            self.printDictFilenames(grouped_files)
        ordered_files = self.order_files(grouped_files)
        if self.debug == True:
            print("ordered_files")
            self.printDictFilenames(ordered_files)
        self.index_by_filename(ordered_files)

    def group_by_group_rules(self, files):
        return_dict = {}
        for file in files:
            file_placed = False
            filename = file.file_name()
            for group, rules in self.group_rules.items():
                for rule in rules:
                    if filename and rule in filename:
                        if group not in return_dict:
                            return_dict[group] = []
                        return_dict[group].append(file)
                        file_placed = True
            if file_placed == False:
                if '4' not in return_dict:
                    return_dict['4'] = []
                return_dict['4'].append(file)
        return return_dict

    def order_files(self, file_dict):
        return_dict = {}
        for group, file_list in file_dict.items():
            if group not in return_dict:
                return_dict[group] = sorted(
                    file_list, key=lambda view: view.file_name()
                )
        return return_dict

    def get_filename_extension(self, view):
        filename_array = str(view.file_name()).split('.')
        return filename_array[-1]

    # Get all open files
    def get_filenames(self):
        open_files = self.window.views()
        return open_files

    # Sort files alphabetically
    def index_by_filename(self, ordered_files):
        group_count = 0
        window_count = len(ordered_files)
        if window_count == 1:
            layout = {
                "cols": [0.0, 1.0],
                "rows": [0.0, 1.0],
                "cells": [
                    [0, 0, 1, 1],
                ]
            }
        elif window_count == 2:
            layout = {
                "cols": [0.0, 0.5, 1.0],
                "rows": [0.0, 1.0],
                "cells": [
                    [0, 0, 1, 1],
                    [1, 0, 2, 1],
                ]
            }
        elif window_count == 3:
            layout = {
                "cols": [0.0, 0.5, 1.0],
                "rows": [0.0, 0.5, 1.0],
                "cells": [
                    [0, 0, 1, 2],
                    [1, 0, 2, 1],
                    [1, 1, 2, 2]
                ]
            }
        else:
            layout = {
                "cols": [0.0, 0.5, 1.0],
                "rows": [0.0, 0.5, 1.0],
                "cells": [
                    [0, 0, 1, 1],
                    [1, 0, 2, 1],
                    [0, 1, 1, 2],
                    [1, 1, 2, 2]
                ]
            }
        self.window.run_command('set_layout', layout)
        for group, files in ordered_files.items():
            file_count = 0
            for file in files:
                self.window.set_view_index(file, group_count, file_count)
                file_count += 1
            group_count += 1

    ## DEBUG FUCNTIONS
    # Display filenames of list
    def printListFilenames(self, list):
        for i in list:
            print(i.file_name())

    # Display filenames of dict
    def printDictFilenames(self, dict):
        for key,value in dict.items():
            for i in value:
                print(i.file_name())
