# -*- encoding: utf-8 -*-
import sublime
import sublime_plugin
import re


class Python2UnicodeFixer(sublime_plugin.EventListener):
    def on_post_save(self, view):
        default_encoding = 'utf-8'

        if re.search(r'\.(py)$', view.file_name()):
            content = self.get_buffer_contents(view)

            if not re.search(r'#\s*(-\*-)?\s*coding', content):
                view.run_command("goto_line", {"line": 1})
                view.run_command('insert_snippet', {"contents": "# -*- coding: %s -*-\n" % default_encoding})

            if not re.search(r'from\s+__future__\s+import\s+unicode_literals', content):
                view.run_command("goto_line", {"line": 2})
                view.run_command('insert_snippet', {"contents": "from __future__ import unicode_literals\n"})

    def get_region(self, view):
        return sublime.Region(0, view.size())

    def get_buffer_contents(self, view):
        return view.substr(self.get_region(view))

