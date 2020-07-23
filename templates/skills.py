from string import Template

TYPE_HEADING = Template(r"""
\textbf{$type}
""")

LISTING = Template(r"""\textit{$level} in $skills. """)

LAYOUT = Template(r"""
$heading\\

$listing\\
""")