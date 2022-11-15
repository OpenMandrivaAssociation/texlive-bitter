Name:		texlive-bitter
Version:	64541
Release:	1
Summary:	The Bitter family of fonts with LaTeX support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bitter
License:	lppl ofl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bitter.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bitter.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides LaTeX, pdfLaTeX, XeLaTeX, and LuaLaTeX
support for the Bitter family of fonts, designed by Sol Matas
for Huerta Tipografica. Bitter is a contemporary slab-serif
typeface for text. There are regular and bold weights and an
italic, but no bold italic.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/bitter
%{_texmfdistdir}/fonts/vf/huerta/bitter
%{_texmfdistdir}/fonts/type1/huerta/bitter
%{_texmfdistdir}/fonts/truetype/huerta/bitter
%{_texmfdistdir}/fonts/tfm/huerta/bitter
%{_texmfdistdir}/fonts/map/dvips/bitter
%{_texmfdistdir}/fonts/enc/dvips/bitter
%doc %{_texmfdistdir}/doc/fonts/bitter

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
