"""
    pygments.styles.monokai
    ~~~~~~~~~~~~~~~~~~~~~~~

    Mimic the Monokai color scheme. Based on tango.py.

    http://www.monokai.nl/blog/2006/07/15/textmate-color-theme/

    :copyright: Copyright 2006-2023 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, Token, \
     Number, Operator, Generic, Whitespace, Punctuation, Other, Literal

class IntellijDarkStyle(Style):
    """
    This style mimics the Monokai color scheme.
    """

    background_color = "#1e2022" #"#272822"
    highlight_color = "#49483e"

    styles = {
        # No corresponding class for the following:
        Token:                     "#bcbec4", # class:  ''
        Whitespace:                "",        # class: 'w'
        Error:                     "#960050 bg:#1e0010", # class: 'err'
        Other:                     "",        # class 'x'

        Comment:                   "#7a7e85", # class: 'c'
        Comment.Multiline:         "#5f826b",        # class: 'cm'
        Comment.Preproc:           "",        # class: 'cp'
        Comment.Single:            "",        # class: 'c1'
        Comment.Special:           "",        # class: 'cs'

        Keyword:                   "#cf8e6e", # class: 'k'
        Keyword.Constant:          "",        # class: 'kc'
        Keyword.Declaration:       "",        # class: 'kd'
        Keyword.Namespace:         "#cf8e6e", # class: 'kn'
        Keyword.Pseudo:            "",        # class: 'kp'
        Keyword.Reserved:          "",        # class: 'kr'
        Keyword.Type:              "",        # class: 'kt'

        Operator:                  "#bcbec4", # class: 'o'  # bcbec4
        Operator.Word:             "",        # class: 'ow' - like keywords

        Punctuation:               "#bcbec4", # class: 'p'

        Name:                      "#bcbec4", # class: 'n'
        Name.Attribute:            "#a6e22e", # class: 'na' - to be revised
        Name.Builtin:              "#8788c6",        # class: 'nb'
        Name.Builtin.Pseudo:       "#94558d",        # class: 'bp'
        Name.Class:                "#bcbec4", # class: 'nc' - to be revised
        Name.Constant:             "#66d9ef", # class: 'no' - to be revised
        Name.Decorator:            "#b3ae61", # class: 'nd' - to be revised
        Name.Entity:               "",        # class: 'ni'
        Name.Exception:            "#8788c6", # class: 'ne'
        Name.Function:             "#56a8f5", # class: 'nf'
        Name.Function.Magic:       "#b205b2", # class: 'fm'
        Name.Property:             "#aa4826",        # class: 'py'
        Name.Label:                "",        # class: 'nl'
        Name.Namespace:            "",        # class: 'nn' - to be revised
        Name.Other:                "#8788c6", # class: 'nx'
        Name.Tag:                  "#cf8e6e", # class: 'nt' - like a keyword
        Name.Variable:             "",        # class: 'nv' - to be revised
        Name.Variable.Class:       "",        # class: 'vc' - to be revised
        Name.Variable.Global:      "",        # class: 'vg' - to be revised
        Name.Variable.Instance:    "",        # class: 'vi' - to be revised

        Number:                    "#2aacb8", # class: 'm'
        Number.Float:              "",        # class: 'mf'
        Number.Hex:                "",        # class: 'mh'
        Number.Integer:            "",        # class: 'mi'
        Number.Integer.Long:       "",        # class: 'il'
        Number.Oct:                "",        # class: 'mo'

        Literal:                   "#ae81ff", # class: 'l'
        Literal.Date:              "#e6db74", # class: 'ld'

        String:                    "#6aab73", # class: 's'
        String.Backtick:           "",        # class: 'sb'
        String.Char:               "#a5c261",        # class: 'sc'
        String.Doc:                "#5f826b",        # class: 'sd' - like a comment
        String.Double:             "#6aab73",        # class: 's2'
        String.Escape:             "#cf8e6e", # class: 'se'
        String.Heredoc:            "",        # class: 'sh'
        String.Interpol:           "#cf8e6e",        # class: 'si'
        String.Other:              "",        # class: 'sx'
        String.Regex:              "",        # class: 'sr'
        String.Single:             "#6aab73",        # class: 's1'
        String.Symbol:             "",        # class: 'ss'


        Generic:                   "",        # class: 'g'
        Generic.Deleted:           "#cf8e6e", # class: 'gd',
        Generic.Emph:              "italic",  # class: 'ge'
        Generic.Error:             "",        # class: 'gr'
        Generic.Heading:           "",        # class: 'gh'
        Generic.Inserted:          "#a6e22e", # class: 'gi'
        Generic.Output:            "#66d9ef", # class: 'go'
        Generic.Prompt:            "bold #cf8e6e", # class: 'gp'
        Generic.Strong:            "bold",    # class: 'gs'
        Generic.Subheading:        "#75715e", # class: 'gu'
        Generic.Traceback:         "",        # class: 'gt'
    }
