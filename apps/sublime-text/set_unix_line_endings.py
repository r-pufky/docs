import sublime_plugin

class SetUnixLineEndingsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.set_line_endings("unix")

class SetLineEndings(sublime_plugin.EventListener):
    def on_pre_save(self, view):
        view.run_command("set_unix_line_endings")