Summary:	Numerical Data Processing and Visualization Tool (grace)
Summary(pl.UTF-8):	Narzędzie do numerycznej obróbki i wizualizacji danych
Name:		grace
Version:	5.1.21
Release:	4
License:	GPL
Group:		Applications/Math
Source0:	ftp://plasma-gate.weizmann.ac.il/pub/grace/src/stable/%{name}-%{version}.tar.gz
# Source0-md5:	db02dee3c68179c41452e652bd469bb9
Source1:	%{name}.desktop
Patch0:		%{name}-FHS.patch
Patch1:		%{name}-home_etc.patch
Patch2:		%{name}-etc.patch
Patch3:		%{name}-fontsdir.patch
URL:		http://plasma-gate.weizmann.ac.il/Grace/
BuildRequires:	Xbae-devel
BuildRequires:	XmHTML-devel >= 1.1.5
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fftw-devel >= 2.1.3
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel >= 0.9.6
BuildRequires:	motif-devel >= 1.2
BuildRequires:	netcdf-devel >= 3.0
#BuildRequires:	pdflib-devel >= 5.0.0
BuildRequires:	t1lib-devel >= 5.0.0
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	xorg-lib-libXt-devel
Requires:	fonts-Type1-urw
Requires:	libpng >= 0.9.6
#Requires:	pdflib >= 5.0.0
Requires:	zlib >= 1.0.3
Obsoletes:	xmgr
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Grace is a Motif application for two-dimensional data visualization.
Grace can transform the data using free equations, FFT, cross- and
auto-correlation, differences, integrals, histograms, and much more.
The generated figures are of high quality. Grace is a very convenient
tool for data inspection, data transformation, and and for making
figures for publications.

%description -l pl.UTF-8
Grace jest motifową aplikacją służącą do dwuwymiarowej wizualizacji
danych. Może przekształcać dane za pomocą wolnych równań, FFT,
autokorelacji, różniczek, całek, histogramów itd. Powstałe wykresy
mają wysoką jakość. Grace jest bardzo użytecznym narzędziem jeśli
chodzi o monitorowanie i transformację danych oraz tworzenie wykresów
do publikacji.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
cp -f /usr/share/automake/config.* ac-tools
cp -f ac-tools/configure.in .
%{__autoconf}
%configure \
	--enable-grace-home=%{_datadir}/%{name} \
	--enable-editres \
	--enable-extra-incpath=$PKG_BUILD_DIR/include \
	--enable-extra-ldpath=$PKG_BUILD_DIR/lib \
	--without-bundled-xbae \
	%{!?debug:--disable-debug}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_datadir}/grace/doc/{*.sgml,*.dvi,*.1} \
	$RPM_BUILD_ROOT%{_datadir}/grace/examples/dotest

install -D %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop

gzip -9nf $RPM_BUILD_ROOT%{_datadir}/grace/doc/*.dat \
	$RPM_BUILD_ROOT%{_datadir}/grace/doc/*.agr \
	$RPM_BUILD_ROOT%{_datadir}/grace/doc/*.sh

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%docdir %{_datadir}/grace/doc
%docdir %{_datadir}/grace/examples
%{_datadir}/grace/doc
%{_datadir}/grace/examples
%dir %{_sysconfdir}/grace
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/grace/*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_libdir}/grace
%{_includedir}/*
%dir %{_datadir}/grace
%{_datadir}/grace/auxiliary
%dir %{_datadir}/grace/templates
%config(noreplace) %verify(not md5 mtime size) %{_datadir}/grace/templates/*
%dir %{_datadir}/grace/fonts
%{_datadir}/grace/fonts/enc
%{_datadir}/grace/fonts/type1
%{_datadir}/grace/fonts/FontDataBase
%{_desktopdir}/*.desktop
