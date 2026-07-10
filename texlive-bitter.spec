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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides LaTeX, pdfLaTeX, XeLaTeX, and LuaLaTeX support for
the Bitter family of fonts, designed by Sol Matas for Huerta
Tipografica. Bitter is a contemporary slab-serif typeface for text.
There are regular and bold weights and an italic, but no bold italic.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/fonts
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/fonts
%dir %{_datadir}/texmf-dist/fonts/enc
%dir %{_datadir}/texmf-dist/fonts/map
%dir %{_datadir}/texmf-dist/fonts/tfm
%dir %{_datadir}/texmf-dist/fonts/truetype
%dir %{_datadir}/texmf-dist/fonts/type1
%dir %{_datadir}/texmf-dist/fonts/vf
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/fonts/bitter
%dir %{_datadir}/texmf-dist/fonts/enc/dvips
%dir %{_datadir}/texmf-dist/fonts/map/dvips
%dir %{_datadir}/texmf-dist/fonts/tfm/huerta
%dir %{_datadir}/texmf-dist/fonts/truetype/huerta
%dir %{_datadir}/texmf-dist/fonts/type1/huerta
%dir %{_datadir}/texmf-dist/fonts/vf/huerta
%dir %{_datadir}/texmf-dist/tex/latex/bitter
%dir %{_datadir}/texmf-dist/fonts/enc/dvips/bitter
%dir %{_datadir}/texmf-dist/fonts/map/dvips/bitter
%dir %{_datadir}/texmf-dist/fonts/tfm/huerta/bitter
%dir %{_datadir}/texmf-dist/fonts/truetype/huerta/bitter
%dir %{_datadir}/texmf-dist/fonts/type1/huerta/bitter
%dir %{_datadir}/texmf-dist/fonts/vf/huerta/bitter
%doc %{_datadir}/texmf-dist/doc/fonts/bitter/OFL.txt
%doc %{_datadir}/texmf-dist/doc/fonts/bitter/README
%doc %{_datadir}/texmf-dist/doc/fonts/bitter/bitter-samples.pdf
%doc %{_datadir}/texmf-dist/doc/fonts/bitter/bitter-samples.tex
%{_datadir}/texmf-dist/fonts/enc/dvips/bitter/bttr_6upxhe.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/bitter/bttr_72jdjw.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/bitter/bttr_azarls.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/bitter/bttr_b5i5mx.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/bitter/bttr_f2umud.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/bitter/bttr_gljolu.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/bitter/bttr_ncjtqa.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/bitter/bttr_ssdm5h.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/bitter/bttr_vzfpnj.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/bitter/bttr_w3wxei.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/bitter/bttr_x2bjkb.enc
%{_datadir}/texmf-dist/fonts/map/dvips/bitter/bitter.map
%{_datadir}/texmf-dist/fonts/tfm/huerta/bitter/Bttr-Bold-tlf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/huerta/bitter/Bttr-Bold-tlf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/huerta/bitter/Bttr-Bold-tlf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/huerta/bitter/Bttr-Bold-tlf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/huerta/bitter/Bttr-Bold-tlf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/huerta/bitter/Bttr-Bold-tlf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/huerta/bitter/Bttr-Bold-tlf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/huerta/bitter/Bttr-Italic-tlf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/huerta/bitter/Bttr-Italic-tlf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/huerta/bitter/Bttr-Italic-tlf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/huerta/bitter/Bttr-Italic-tlf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/huerta/bitter/Bttr-Italic-tlf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/huerta/bitter/Bttr-Italic-tlf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/huerta/bitter/Bttr-Italic-tlf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/huerta/bitter/Bttr-Regular-tlf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/huerta/bitter/Bttr-Regular-tlf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/huerta/bitter/Bttr-Regular-tlf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/huerta/bitter/Bttr-Regular-tlf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/huerta/bitter/Bttr-Regular-tlf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/huerta/bitter/Bttr-Regular-tlf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/huerta/bitter/Bttr-Regular-tlf-ts1.tfm
%{_datadir}/texmf-dist/fonts/truetype/huerta/bitter/Bitter-Bold.ttf
%{_datadir}/texmf-dist/fonts/truetype/huerta/bitter/Bitter-Italic.ttf
%{_datadir}/texmf-dist/fonts/truetype/huerta/bitter/Bitter-Regular.ttf
%{_datadir}/texmf-dist/fonts/type1/huerta/bitter/Bttr-Bold.pfb
%{_datadir}/texmf-dist/fonts/type1/huerta/bitter/Bttr-Italic.pfb
%{_datadir}/texmf-dist/fonts/type1/huerta/bitter/Bttr-Regular.pfb
%{_datadir}/texmf-dist/fonts/vf/huerta/bitter/Bttr-Bold-tlf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/huerta/bitter/Bttr-Bold-tlf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/huerta/bitter/Bttr-Bold-tlf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/huerta/bitter/Bttr-Italic-tlf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/huerta/bitter/Bttr-Italic-tlf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/huerta/bitter/Bttr-Italic-tlf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/huerta/bitter/Bttr-Regular-tlf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/huerta/bitter/Bttr-Regular-tlf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/huerta/bitter/Bttr-Regular-tlf-ts1.vf
%{_datadir}/texmf-dist/tex/latex/bitter/LY1Bttr-TLF.fd
%{_datadir}/texmf-dist/tex/latex/bitter/OT1Bttr-TLF.fd
%{_datadir}/texmf-dist/tex/latex/bitter/T1Bttr-TLF.fd
%{_datadir}/texmf-dist/tex/latex/bitter/TS1Bttr-TLF.fd
%{_datadir}/texmf-dist/tex/latex/bitter/bitter.sty
