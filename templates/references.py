from string import Template


LISTING = Template(r"""
$name, $designation, $organization \hfill \href{mailto:$email}{$email}
""")

LAYOUT = Template(r"""
$heading\\

$listing
""")