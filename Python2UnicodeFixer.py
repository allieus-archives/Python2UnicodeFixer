import sublime
import sublime_plugin
import re


class Python2UnicodeFixer(sublime_plugin.EventListener):
    def on_post_save(self, view):
        if re.search(r'\.(py)$', view.file_name()):
            content = self.get_buffer_contents(view)

            if '# coding' not in content:
                view.run_command("goto_line", {"line": 1})
                view.run_command('insert_snippet', {"contents": "# coding: utf8\n"})

            if 'unicode_literals' not in content:
                view.run_command("goto_line", {"line": 2})
                view.run_command('insert_snippet', {"contents": "from __future__ import unicode_literals\n"})

    def get_region(self, view):
        return sublime.Region(0, view.size())

    def get_buffer_contents(self, view):
        return view.substr(self.get_region(view))

