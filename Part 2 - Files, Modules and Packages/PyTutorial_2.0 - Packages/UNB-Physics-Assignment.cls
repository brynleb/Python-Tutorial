\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{UNB-Physics-Assignment}[2022 University of New Brunswick Physics Assignments]

\LoadClass[11pt,letterpaper]{article}

\setlength{\textwidth}{6.0in}
\setlength{\textheight}{9.0in}
\setlength{\oddsidemargin}{0in}
\setlength{\headheight}{0in}

\RequirePackage[margin=2cm]{geometry}

\RequirePackage{color}
\definecolor{codegreen}{rgb}{0,0.6,0}
\definecolor{codegray}{rgb}{0.5,0.5,0.5}
\definecolor{codepurple}{rgb}{0.58,0,0.82}
\definecolor{backcolour}{rgb}{0.95,0.95,0.92}

\RequirePackage{listings}
\lstdefinestyle{mystyle}{
    backgroundcolor=\color{backcolour},
    commentstyle=\color{codegreen},
    keywordstyle=\color{magenta},
    numberstyle=\tiny\color{codegray},
    stringstyle=\color{codepurple},
    basicstyle=\footnotesize,
    breakatwhitespace=false,
    breaklines=true,
    captionpos=b,
    keepspaces=true,
    numbers=left,
    numbersep=5pt,
    showspaces=false,
    showstringspaces=false,
    showtabs=false,
    tabsize=2
}
\lstset{style=mystyle}

\RequirePackage{graphicx}
\RequirePackage{fancybox}
\RequirePackage[utf8]{inputenc}
\RequirePackage{epsfig,graphicx}
\RequirePackage{multicol,pst-plot}
\RequirePackage{pstricks}
\RequirePackage{amsmath}
\RequirePackage{amsfonts}
\RequirePackage{amssymb}
\RequirePackage{eucal}
\RequirePackage{etoolbox}

\def\dd{\mathrm{d}}
\def\Fig{Fig.~}
\def\Eq{Eq.~}
\def\Eqs{Eqs.~}
\def\be{\begin{equation}}
\def\ee{\end{equation}}
\def\ba{\begin{align}}
\def\ea{\end{align}}

\newcommand*{\op}[1]{\check{\mathbf#1}}
\newcommand{\bra}[1]{\langle #1 |}
\newcommand{\ket}[1]{| #1 \rangle}
\newcommand{\braket}[2]{\langle #1 | #2 \rangle}
\newcommand{\mean}[1]{\langle #1 \rangle}
\newcommand{\opvec}[1]{\check{\vec #1}}
\renewcommand{\sp}[1]{$${\begin{split}#1\end{split}}$$}

\renewcommand\maketitle{
    \begin{flushright}
        \vspace{-1.0cm}
        \includegraphics[height=2.25cm]{Logo.png}
    \end{flushright}

    \begin{center}
        \vspace{-2cm}
        {\Large \Course} \\
        \vspace{0.4cm}
        {\huge \Assignment} \\
        \vspace{0.4cm}
        {\Large \DueDate}
    \end{center}

    \begin{flushleft}
      \rule{\textwidth}{0.2mm}
    \end{flushleft}

    \medskip
}
