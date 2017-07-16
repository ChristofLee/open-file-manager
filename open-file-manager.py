import sublime
import sublime_plugin

class OpenFileManagerCommand(sublime_plugin.WindowCommand):
    def run(self):
        print("Great Success!")
    # Get a list of all open files
        openViews = self.window.views()
        # x = 0
        # for i in openViews:
        #     print(openViews[x].file_name())
        #     x += 1

    # Re-order those files
        # Index the list
        # Sort alphabetically
        # Apply a new index
    # Get all open files
    def getFilenames(self):
        openFiles = self.window.views()
        return openFiles


    # Filter list by file extensions
        # Index the list
        # Filter by file extension
        # Apply a new index

# view.run_command('open_file_manager')
