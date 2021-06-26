from string import Template

LISTING = Template(r"""
\item {\bf $school, $location} \hfill $duration\\ $description
""")

LAYOUT = Template(r"""
$heading
\begin{itemize}
\itemsep0em

$listing

\end{itemize}

""")
