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

class StripeStyle(Style):
    """
    This style mimics the Monokai color scheme.
    """

    background_color = "#202d63" #"#272822"
    highlight_color = "#49483e"

    styles = {
        # No corresponding class for the following:
        Token:                     "#f5fbff", # class:  ''
        Whitespace:                "",        # class: 'w'
        Error:                     "#960050 bg:#1e0010", # class: 'err'
        Other:                     "",        # class 'x'

        Comment:                   "#bcc5cf", # class: 'c'
        Comment.Multiline:         "#bcc5cf",        # class: 'cm'
        Comment.Preproc:           "",        # class: 'cp'
        Comment.Single:            "",        # class: 'c1'
        Comment.Special:           "",        # class: 'cs'

        Keyword:                   "bold #a4cdfe", # class: 'k'
        Keyword.Constant:          "",        # class: 'kc'
        Keyword.Declaration:       "",        # class: 'kd'
        Keyword.Namespace:         "#a4cdfe", # class: 'kn'
        Keyword.Pseudo:            "",        # class: 'kp'
        Keyword.Reserved:          "",        # class: 'kr'
        Keyword.Type:              "",        # class: 'kt'

        Operator:                  "#f5fbff", # class: 'o'  # bcbec4
        Operator.Word:             "bold #a4cdfe",        # class: 'ow' - like keywords

        Punctuation:               "#f5fbff", # class: 'p'

        Name:                      "#f5fbff", # class: 'n'
        Name.Attribute:            "#a6e22e", # class: 'na' - to be revised
        Name.Builtin:              "bold #a4cdff",        # class: 'nb'
        Name.Builtin.Pseudo:       "#f8b886",        # class: 'bp'
        Name.Class:                "#7ed3ed", # class: 'nc' - to be revised
        Name.Constant:             "#66d9ef", # class: 'no' - to be revised
        Name.Decorator:            "#f5fbff", # class: 'nd' - to be revised
        Name.Entity:               "",        # class: 'ni'
        Name.Exception:            "#7ed3ed", # class: 'ne'
        Name.Function:             "#7ed3ed", # class: 'nf'
        Name.Function.Magic:       "#7ed3ed", # class: 'fm'
        Name.Property:             "#fbb5b2",        # class: 'py'
        Name.Label:                "",        # class: 'nl'
        Name.Namespace:            "",        # class: 'nn' - to be revised
        Name.Other:                "#a4cdff", # class: 'nx'
        Name.Tag:                  "#cf8e6e", # class: 'nt' - like a keyword
        Name.Variable:             "",        # class: 'nv' - to be revised
        Name.Variable.Class:       "",        # class: 'vc' - to be revised
        Name.Variable.Global:      "",        # class: 'vg' - to be revised
        Name.Variable.Instance:    "",        # class: 'vi' - to be revised

        Number:                    "#f8b886", # class: 'm'
        Number.Float:              "",        # class: 'mf'
        Number.Hex:                "",        # class: 'mh'
        Number.Integer:            "",        # class: 'mi'
        Number.Integer.Long:       "",        # class: 'il'
        Number.Oct:                "",        # class: 'mo'

        Literal:                   "#ae81ff", # class: 'l'
        Literal.Date:              "#e6db74", # class: 'ld'

        String:                    "#86d996", # class: 's'
        String.Backtick:           "",        # class: 'sb'
        String.Char:               "#a5c261",        # class: 'sc'
        String.Doc:                "#c1c9d2",        # class: 'sd' - like a comment
        String.Double:             "#86d996",        # class: 's2'
        String.Escape:             "#cf8e6e", # class: 'se'
        String.Heredoc:            "",        # class: 'sh'
        String.Interpol:           "#cf8e6e",        # class: 'si'
        String.Other:              "",        # class: 'sx'
        String.Regex:              "",        # class: 'sr'
        String.Single:             "#86d996",        # class: 's1'
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
