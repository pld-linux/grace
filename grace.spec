Summary:	Numerical Data Processing and Visualization Tool (grace)
Summary(pl):	Narzêdzie do numerycznej obróbki i wizualizacji danych
Name:		grace
Version:	5.1.2
Release:	1
License:	GPL
Group:		Applications/Math
Group(de):	Applikationen/Mathematik
Group(pl):	Aplikacje/Matematyczne
Source0:	ftp://plasma-gate.weizmann.ac.il/pub/grace/src/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-HOME-ETC.patch
Patch2:		%{name}-PDFlib.patch
Patch3:		%{name}-FFTW.patch
URL:		http://plasma-gate.weizmann.ac.il/Grace/
BuildRequires:	fftw-devel
BuildRequires:	zlib-devel >= 1.0.3
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel >= 0.9.6
BuildRequires:	libtiff-devel
BuildRequires:	pdflib-devel >= 3.0
BuildRequires:	lesstif-devel
BuildRequires:	XFree86-devel
BuildRequires:	Xbae-devel
Requires:	pdflib >= 3.0
Requires:	zlib >= 1.0.3
Requires:	libpng >= 0.9.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define _prefix /usr/X11R6
%define _mandir %{_prefix}/man
%define _docdir /usr/share/doc

%description
Grace is a Motif application for two-dimensional data visualization.
Grace can transform the data using free equations, FFT, cross- and
auto-correlation, differences, integrals, histograms, and much more.
The generated figures are of high quality. Grace is a very convenient
tool for data inspection, data transformation, and and for making
figures for publications.

%description -l pl
Grace jest Motiffow± aplikacj± s³u¿±c± do dwuwymiarowej wizualizacji
danych. Mo¿e przekszta³caæ dane za pomoc± wolnych równañ, FFT,
autokorelacji, ró¿niczek, ca³ek, histogramów itd. Powsta³e wykresy
maj± wysok± jako¶æ. Grace jest bardzo u¿ytecznym narzêdziem je¶li
chodzi o monitorowanie i transformacjê danych oraz tworzenie wykresów
do publikacji.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%configure \
	--enable-grace-home=%{_datadir}/%{name} \
	--enable-editres \
	--enable-extra-incpath=$PKG_BUILD_DIR/include \
	--enable-extra-ldpath=$PKG_BUILD_DIR/lib \
	--enable-debug
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_docdir}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_datadir}/doc
gzip -9nf $RPM_BUILD_ROOT%{_docdir}/%{name}/*.dat\
	$RPM_BUILD_ROOT%{_docdir}/%{name}/*.agr\
	$RPM_BUILD_ROOT%{_docdir}/%{name}/mygraph.png\
	$RPM_BUILD_ROOT%{_docdir}/%{name}/shiftdata.sh\
	$RPM_BUILD_ROOT%{_docdir}/%{name}/examples/*

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%dir %{_sysconfdir}/grace
%config(noreplace) %verify(not size, mtime, md5) %{_sysconfdir}/grace/*
%doc /usr/share/doc/grace/*.html
%doc /usr/share/doc/grace/*.dat.gz
%doc /usr/share/doc/grace/*.agr.gz
%doc /usr/share/doc/grace/mygraph.png.gz
%doc /usr/share/doc/grace/philosophical-gnu-sm.jpg
%doc /usr/share/doc/grace/shiftdata.sh.gz
%doc /usr/share/doc/grace/examples/*
%attr(755,root,root)%{_bindir}/*
%{_libdir}/grace
%{_includedir}/*
%dir %{_datadir}/grace
%{_datadir}/grace/auxiliary
%dir %{_datadir}/grace/templates
%config(noreplace) %verify(not size, mtime, md5) %{_datadir}/grace/templates/*
%{_datadir}/grace/fonts
