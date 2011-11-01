Name:		texlive-beamerthemenirma
Version:	0.1
Release:	1
Summary:	A Beamer theme for academic presentations
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/beamer-contrib/themes/nirma
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamerthemenirma.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamerthemenirma.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
The package developed for academic purposes. The distribution
includes nothing more than style file needed for preparing
presentations.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
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
