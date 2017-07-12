# http://docs.sublimetext.info/en/latest/extensibility/plugins.html
# http://www.sublimetext.com/docs/3/api_reference.html
# https://learnxinyminutes.com/docs/python3/

import sublime
import sublime_plugin


class ExampleCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.insert(edit, 0, "Hello, World!")
