Name:		texlive-labelcas
Version:	1.12
Release:	1
Summary:	Check the existence of labels, and fork accordingly
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/labelcas
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/labelcas.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/labelcas.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/labelcas.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package defines two commands: - \eachlabelcase, which
distinguishes whether a set of labels is defined, and for each
label either queues action accordingly, or appends the action
to a macro; and - \lotlabelcase, which takes a comma-separated
list of label names, and distinguishes the resulting action on
whether all were defined, whether none were defined, whether
not all were defined, or whether the lest is empty (again, the
action resulting from \lotlabelcase may be written to a macro).

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/labelcas/labelcas.sty
%doc %{_texmfdistdir}/doc/latex/labelcas/README
%doc %{_texmfdistdir}/doc/latex/labelcas/labelcas.pdf
#- source
%doc %{_texmfdistdir}/source/latex/labelcas/labelcas.dtx
%doc %{_texmfdistdir}/source/latex/labelcas/labelcas.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
