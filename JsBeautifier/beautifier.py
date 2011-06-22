#
# Author: Guillaume LO RE <lowreg@gmail.com> 
# Licensed under MIT License  
#
# Usage
# You can (multi)select the Javascript text you want to beautify. If no text is
# selected, the whole file will be beautified.  
#
# Key binding example 
# { "keys": ["alt+shift+b"], "command": "beau" }

import sublime, sublime_plugin, jsbeautifier

class BeauCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        selections = self.view.sel()
        for sel in selections:
            if sel.size() == 0 and len(selections) == 1:
                region = sublime.Region(0, self.view.size())
            else:
                region = sublime.Region(sel.begin(), sel.end())
            content = self.view.substr(region)
            opts = jsbeautifier.default_options()
            opts.brace_style = 'expand'
            res = jsbeautifier.beautify(content, opts)
            self.view.replace(edit, region, res)