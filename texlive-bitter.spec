%global tl_name bitter
%global tl_revision 77682

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	The Bitter family of fonts with LaTeX support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/bitter
License:	lppl ofl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bitter.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bitter.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides LaTeX, pdfLaTeX, XeLaTeX, and LuaLaTeX support for
the Bitter family of fonts, designed by Sol Matas for Huerta
Tipografica. Bitter is a contemporary slab-serif typeface for text.
There are regular and bold weights and an italic, but no bold italic.

