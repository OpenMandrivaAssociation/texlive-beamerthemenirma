# revision 20765
# category Package
# catalog-ctan /macros/latex/contrib/beamer-contrib/themes/nirma
# catalog-date 2010-12-16 01:15:22 +0100
# catalog-license lppl
# catalog-version 0.1
Name:		texlive-beamerthemenirma
Version:	0.1
Release:	9
Summary:	A Beamer theme for academic presentations
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/beamer-contrib/themes/nirma
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamerthemenirma.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamerthemenirma.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package developed for academic purposes. The distribution
includes nothing more than style file needed for preparing
presentations.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/beamerthemenirma/beamerthemenirma.sty
%doc %{_texmfdistdir}/doc/latex/beamerthemenirma/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.1-2
+ Revision: 749535
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.1-1
+ Revision: 717901
- texlive-beamerthemenirma
- texlive-beamerthemenirma
- texlive-beamerthemenirma
- texlive-beamerthemenirma
- texlive-beamerthemenirma

