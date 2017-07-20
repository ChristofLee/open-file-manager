import sublime
import sublime_plugin

class OpenFileManagerCommand(sublime_plugin.WindowCommand):
    def run(self):
        openFiles = self.getFilenames()
        sortedFiles = self.sortByFilename(openFiles)
        self.indexByFilename(sortedFiles)

    # Get all open files
    def getFilenames(self):
        openFiles = self.window.views()
        return openFiles

    # Sort files alphabetically
    def sortByFilename(self, list):
        sortedFilenames = sorted(list, key=lambda x: x.file_name())
        return sortedFilenames

    # Sort files alphabetically
    def indexByFilename(self, list):
        x = 0
        for i in list:
            print(x)
            self.window.set_view_index(i, x, x)
            x += 1

    # Display filenames (for debugging purposes)
    def printFilenames(self, list):
        for i in list:
            print(i.file_name())

    # Filter list by file extensions
        # Index the list
        # Filter by file extension
        # Apply a new index
