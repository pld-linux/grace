Summary:	Numerical Data Processing and Visualization Tool (grace)
Summary(pl):	Narzêdzie do numerycznej obróbki i wizualizacji danych
Name:		grace
Version:	5.1.9
Release:	3
License:	GPL
Group:		Applications/Math
Source0:	ftp://plasma-gate.weizmann.ac.il/pub/grace/src/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-FHS.patch
Patch1:		%{name}-home_etc.patch
Patch2:		%{name}-etc.patch
Patch3:		%{name}-fontsdir.patch
Patch4:		%{name}-ac25x.patch
URL:		http://plasma-gate.weizmann.ac.il/Grace/
BuildRequires:	XFree86-devel
BuildRequires:	Xbae-devel
BuildRequires:	XmHTML-devel >= 1.1.5
BuildRequires:	autoconf
BuildRequires:	fftw-devel
BuildRequires:	lesstif-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel >= 0.9.6
BuildRequires:	libtiff-devel
BuildRequires:	netcdf-devel >= 3.0
BuildRequires:	pdflib-devel >= 4.0.3
BuildRequires:	t1lib-devel
Requires:	ghostscript-fonts-std
Requires:	libpng >= 0.9.6
Requires:	pdflib >= 4.0.3
Requires:	zlib >= 1.0.3
Obsoletes:	xmgr
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

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
%patch4 -p1

%build
cp -f ac-tools/configure.in .
%{__autoconf}
%configure \
	--enable-grace-home=%{_datadir}/%{name} \
	--enable-editres \
	--enable-extra-incpath=$PKG_BUILD_DIR/include \
	--enable-extra-ldpath=$PKG_BUILD_DIR/lib \
	%{!?debug:--disable-debug}
%{__make}

gzip -9nf $RPM_BUILD_ROOT%{_datadir}/grace/doc/*.dat \
	$RPM_BUILD_ROOT%{_datadir}/grace/doc/*.agr \
	$RPM_BUILD_ROOT%{_datadir}/grace/doc/*.sh

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_datadir}/grace/doc/{*.sgml,*.dvi,*.1} \
	$RPM_BUILD_ROOT%{_datadir}/grace/examples/dotest

install -d $RPM_BUILD_ROOT%{_applnkdir}/Scientific/Plotting
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Scientific/Plotting/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%docdir %{_datadir}/grace/doc
%docdir %{_datadir}/grace/examples
%{_datadir}/grace/doc
%{_datadir}/grace/examples
%dir %{_sysconfdir}/grace
%config(noreplace) %verify(not size, mtime, md5) %{_sysconfdir}/grace/*
%attr(755,root,root)%{_bindir}/*
%{_mandir}/man1/*
%{_libdir}/grace
%{_includedir}/*
%dir %{_datadir}/grace
%{_datadir}/grace/auxiliary
%dir %{_datadir}/grace/templates
%config(noreplace) %verify(not size, mtime, md5) %{_datadir}/grace/templates/*
%dir %{_datadir}/grace/fonts
%{_datadir}/grace/fonts/enc
%{_datadir}/grace/fonts/FontDataBase
