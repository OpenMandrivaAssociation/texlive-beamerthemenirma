%global tl_name beamerthemenirma
%global tl_revision 20765

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	A Beamer theme for academic presentations
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/beamer-contrib/themes/nirma
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamerthemenirma.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamerthemenirma.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package developed for academic purposes. The distribution includes
nothing more than style file needed for preparing presentations.

