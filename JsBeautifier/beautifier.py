#
# Author: Guillaume LO RE <lowreg@gmail.com> 
# Licensed under MIT License  
#
# Usage
# You can (multi)select the Javascript text you want to beautify. If no text is
# selected, the whole file will be beautified.  
#
# Key binding example 
# { "keys": ["alt+shift+b"], "command": "beau", "args": {"indent_size": 4, "brace_style": "collapse"} }
# You can change the indent_size and brace_style according to jsbeautifier options.

import sublime, sublime_plugin, jsbeautifier

class BeauCommand(sublime_plugin.TextCommand):
    def run(self, edit, indent_size, brace_style):
        selections = self.view.sel()
        for sel in selections:
            if sel.size() == 0 and len(selections) == 1:
                region = sublime.Region(0, self.view.size())
            else:
                region = sel
            content = self.view.substr(region)
            opts = jsbeautifier.default_options()
            opts.brace_style = brace_style
            opts.indent_size = int(indent_size)
            res = jsbeautifier.beautify(content, opts)
            self.view.replace(edit, region, res)