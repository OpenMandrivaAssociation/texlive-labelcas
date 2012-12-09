# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/labelcas
# catalog-date 2007-03-08 21:58:53 +0100
# catalog-license lppl
# catalog-version 1.12
Name:		texlive-labelcas
Version:	1.12
Release:	2
Summary:	Check the existence of labels, and fork accordingly
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/labelcas
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/labelcas.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/labelcas.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/labelcas.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package defines two commands: - \eachlabelcase, which
distinguishes whether a set of labels is defined, and for each
label either queues action accordingly, or appends the action
to a macro; and - \lotlabelcase, which takes a comma-separated
list of label names, and distinguishes the resulting action on
whether all were defined, whether none were defined, whether
not all were defined, or whether the lest is empty (again, the
action resulting from \lotlabelcase may be written to a macro).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.12-2
+ Revision: 753073
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.12-1
+ Revision: 718800
- texlive-labelcas
- texlive-labelcas
- texlive-labelcas
- texlive-labelcas

