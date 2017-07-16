import sublime
import sublime_plugin

class OpenFileManagerCommand(sublime_plugin.WindowCommand):
    def run(self):
    # Get a list of all open files
        openViews = self.window.views()
        # x = 0
        # for i in openViews:
        #     print(openViews[x].file_name())
        #     x += 1
        openFiles = self.getFilenames()
        sortedFiles = self.sortByFilename(openFiles)
        self.printFilenames(sortedFiles)

    # Re-order those files
        # Index the list
        # Sort alphabetically
        # Apply a new index
    # Get all open files
    def getFilenames(self):
        openFiles = self.window.views()
        return openFiles

    # Sort files alphabetically
    def sortByFilename(self, list):
        sortedFilenames = sorted(list, key=lambda x: x.file_name())
        return sortedFilenames

    # Display filenames (for debugging purposes)
    def printFilenames(self, list):
        for i in list:
            print(i.file_name())

    # Filter list by file extensions
        # Index the list
        # Filter by file extension
        # Apply a new index
