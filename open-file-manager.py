import sublime
import sublime_plugin


class OpenFileManagerCommand(sublime_plugin.WindowCommand):
    def run(self):
        print("Great Success!")
        views = self.window.views()
        print(views)
        x = 0
        for i in views:
            print(views[x].file_name())
            x += 1

# view.run_command('open_file_manager')
