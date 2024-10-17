# revision 20033
# category Package
# catalog-ctan /fonts/gentium
# catalog-date 2010-10-09 15:59:49 +0200
# catalog-license ofl
# catalog-version undef
Name:		texlive-gentium
Version:	20101009
Release:	12
Summary:	Gentium font and support files
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/gentium
License:	OFL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gentium.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gentium.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gentium.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package includes TrueType fonts from SIL, files needed to
use them in pdfTeX in multiple encodings (agr, t2a, ec/T1,
texnansi, l7x, qx, t5) and support files for ConTeXt. Other
encodings, and LaTeX support remain to be added.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/gentium/GenBasB.afm
%{_texmfdistdir}/fonts/afm/public/gentium/GenBasBI.afm
%{_texmfdistdir}/fonts/afm/public/gentium/GenI102.afm
%{_texmfdistdir}/fonts/afm/public/gentium/GenR102.afm
%{_texmfdistdir}/fonts/enc/dvips/gentium/gentium-agr.enc
%{_texmfdistdir}/fonts/enc/dvips/gentium/gentium-ec.enc
%{_texmfdistdir}/fonts/enc/dvips/gentium/gentium-l7x.enc
%{_texmfdistdir}/fonts/enc/dvips/gentium/gentium-qx.enc
%{_texmfdistdir}/fonts/enc/dvips/gentium/gentium-t2a.enc
%{_texmfdistdir}/fonts/enc/dvips/gentium/gentium-t5.enc
%{_texmfdistdir}/fonts/enc/dvips/gentium/gentium-texnansi.enc
%{_texmfdistdir}/fonts/map/pdftex/gentium/gentium-agr.map
%{_texmfdistdir}/fonts/map/pdftex/gentium/gentium-ec.map
%{_texmfdistdir}/fonts/map/pdftex/gentium/gentium-l7x.map
%{_texmfdistdir}/fonts/map/pdftex/gentium/gentium-qx.map
%{_texmfdistdir}/fonts/map/pdftex/gentium/gentium-t2a.map
%{_texmfdistdir}/fonts/map/pdftex/gentium/gentium-t5.map
%{_texmfdistdir}/fonts/map/pdftex/gentium/gentium-texnansi.map
%{_texmfdistdir}/fonts/map/pdftex/gentium/gentium.map
%{_texmfdistdir}/fonts/tfm/public/gentium/agr-gentium-italic.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium/agr-gentium-roman.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium/ec-gentium-italic.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium/ec-gentium-roman.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium/ec-gentiumbasic-bold.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium/ec-gentiumbasic-bolditalic.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium/l7x-gentium-italic.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium/l7x-gentium-roman.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium/l7x-gentiumbasic-bold.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium/l7x-gentiumbasic-bolditalic.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium/qx-gentium-italic.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium/qx-gentium-roman.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium/qx-gentiumbasic-bold.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium/qx-gentiumbasic-bolditalic.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium/t2a-gentium-italic.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium/t2a-gentium-roman.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium/t5-gentium-italic.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium/t5-gentium-roman.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium/t5-gentiumbasic-bold.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium/t5-gentiumbasic-bolditalic.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium/texnansi-gentium-italic.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium/texnansi-gentium-roman.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium/texnansi-gentiumbasic-bold.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium/texnansi-gentiumbasic-bolditalic.tfm
%{_texmfdistdir}/fonts/truetype/public/gentium/GenAI102.ttf
%{_texmfdistdir}/fonts/truetype/public/gentium/GenAR102.ttf
%{_texmfdistdir}/fonts/truetype/public/gentium/GenBasB.ttf
%{_texmfdistdir}/fonts/truetype/public/gentium/GenBasBI.ttf
%{_texmfdistdir}/fonts/truetype/public/gentium/GenBasI.ttf
%{_texmfdistdir}/fonts/truetype/public/gentium/GenBasR.ttf
%{_texmfdistdir}/fonts/truetype/public/gentium/GenBkBasB.ttf
%{_texmfdistdir}/fonts/truetype/public/gentium/GenBkBasBI.ttf
%{_texmfdistdir}/fonts/truetype/public/gentium/GenBkBasI.ttf
%{_texmfdistdir}/fonts/truetype/public/gentium/GenBkBasR.ttf
%{_texmfdistdir}/fonts/truetype/public/gentium/GenI102.ttf
%{_texmfdistdir}/fonts/truetype/public/gentium/GenR102.ttf
%{_texmfdistdir}/tex/context/third/gentium/type-gentium.tex
%doc %{_texmfdistdir}/doc/fonts/gentium/Gentium_1.02/FONTLOG.txt
%doc %{_texmfdistdir}/doc/fonts/gentium/Gentium_1.02/GENTIUM-FAQ.txt
%doc %{_texmfdistdir}/doc/fonts/gentium/Gentium_1.02/OFL-FAQ.txt
%doc %{_texmfdistdir}/doc/fonts/gentium/Gentium_1.02/OFL.txt
%doc %{_texmfdistdir}/doc/fonts/gentium/Gentium_1.02/QUOTES.txt
%doc %{_texmfdistdir}/doc/fonts/gentium/Gentium_1.02/README.txt
%doc %{_texmfdistdir}/doc/fonts/gentium/Gentium_Basic_1.1/FONTLOG.txt
%doc %{_texmfdistdir}/doc/fonts/gentium/Gentium_Basic_1.1/GENTIUM-FAQ.txt
%doc %{_texmfdistdir}/doc/fonts/gentium/Gentium_Basic_1.1/OFL-FAQ.txt
%doc %{_texmfdistdir}/doc/fonts/gentium/Gentium_Basic_1.1/OFL.txt
%doc %{_texmfdistdir}/doc/fonts/gentium/README
#- source
%doc %{_texmfdistdir}/source/fonts/gentium/generate-tfm-files.sh
%doc %{_texmfdistdir}/source/fonts/gentium/gentium-ec-source.enc
%doc %{_texmfdistdir}/source/fonts/gentium/gentium-t5-source.enc

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20101009-2
+ Revision: 752254
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20101009-1
+ Revision: 718533
- texlive-gentium
- texlive-gentium
- texlive-gentium
- texlive-gentium

