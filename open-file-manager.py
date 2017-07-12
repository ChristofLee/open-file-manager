import sublime
import sublime_plugin


class OpenFileManagerCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.insert(edit, 0, "Hello, World!")

# view.run_command('open_file_manager')
