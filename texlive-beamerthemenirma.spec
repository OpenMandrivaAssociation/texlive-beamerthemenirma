Name:		texlive-beamerthemenirma
Version:	20765
Release:	2
Summary:	A Beamer theme for academic presentations
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/beamer-contrib/themes/nirma
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamerthemenirma.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamerthemenirma.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
