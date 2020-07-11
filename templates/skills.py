from string import Template

LISTING = Template(r"""
\textbf{$level} in $skills.
""")

LAYOUT = Template(r"""
$heading\\

$listing\\
""")