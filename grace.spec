%define version 5.0.5
%define name grace
%define serial 28
Name: %{name}
Version: %{version}
Serial: %{serial}
Release: 1
Copyright: GPL
Source0: ftp://plasma-gate.weizmann.ac.il/pub/grace/src/%{name}-%{version}.tar.gz
Source1: xmgrace
Source2: fftw.tar.gz
Patch0: %{name}.perl.patch
Icon: %{name}.gif
BuildRoot: /tmp/%{name}-root
Packager: Henrik Seidel <Henrik.Seidel@gmx.de>
ExclusiveArch: i386 alpha
Group: Applications/Math
Summary: Numerical Data Processing and Visualization Tool (grace)
%description
Grace is a Motif application for two-dimensional data visualization.
Grace can transform the data using free equations, FFT, cross- and
auto-correlation, differences, integrals, histograms, and much more. The
generated figures are of high quality.  Grace is a very convenient tool
for data inspection, data transformation, and and for making figures for
publications.

%package dynamic
Group: Applications/Math
Summary: Numerical Data Processing and Visualization Tool (grace)
Provides: %{name}
Conflicts: %{name}-semistatic

%description dynamic
Grace is a Motif application for two-dimensional data visualization.
Grace can transform the data using free equations, FFT, cross- and
auto-correlation, differences, integrals, histograms, and much more. The
generated figures are of high quality.  Grace is a very convenient tool
for data inspection, data transformation, and and for making figures for
publications.

%package semistatic
Group: Applications/Math
Summary: grace with statically linked Motif libraries
Provides: %{name}
Conflicts: %{name}-dynamic

%description semistatic
Grace is a Motif application for two-dimensional data visualization.
Grace can transform the data using free equations, FFT, cross- and
auto-correlation, differences, integrals, histograms, and much more. The
generated figures are of high quality.  Grace is a very convenient tool
for data inspection, data transformation, and and for making figures for
publications.

In this package the Motif libraries are linked statically for users who have
no Motif runtime libraries.

%changelog

* Mon Oct 25 1999 Henrik Seidel <Henrik.Seidel@gmx.de>
- upgraded to 5.0.5pre3

* Fri Oct  8 1999 Henrik Seidel <Henrik.Seidel@gmx.de>
- upgraded to 5.0.5pre1
- added canvas patch

* Fri Oct  1 1999 Henrik Seidel <Henrik.Seidel@gmx.de>
- upgraded to 5.0.5pre0

* Fri Sep 17 1999 Henrik Seidel <Henrik.Seidel@gmx.de>
- fixed the string copy problem (#611)

* Tue Sep 14 1999 Henrik Seidel <Henrik.Seidel@gmx.de>
- upgraded to 5.0.4gamma

* Tue Jun 29 1999 Henrik Seidel <Henrik.Seidel@gmx.de>
- upgraded to 990629

* Fri Jun 18 1999 Henrik Seidel <Henrik.Seidel@gmx.de>
- upgraded to 990614

* Wed May 19 1999 Henrik Seidel <Henrik.Seidel@gmx.de>
- upgraded to 990519

* Mon Apr 26 1999 Henrik Seidel <Henrik.Seidel@gmx.de>
- upgraded to 990424

* Wed Apr  7 1999 Henrik Seidel <Henrik.Seidel@gmx.de>
- patched pars.yacc to enable "(cond) ? a : b"

* Sun Feb 28 1999 Henrik Seidel <Henrik.Seidel@gmx.de>
- upgraded to 5.0.2beta

* Mon Feb  1 1999 Henrik Seidel <seidel@mpimg-berlin-dahlem.mpg.de>
- upgraded to grace-990131

* Tue Jan 12 1999 Henrik Seidel <seidel@mpimg-berlin-dahlem.mpg.de>
- upgraded to grace-981231

* Tue Dec 15 1998 Henrik Seidel <seidel@mpimg-berlin-dahlem.mpg.de>
- upgraded to grace-981203

* Tue Nov  3 1998 Henrik Seidel <seidel@mpimg-berlin-dahlem.mpg.de>
- upgraded to grace-981102

* Thu Oct 22 1998 Henrik Seidel <seidel@mpimg-berlin-dahlem.mpg.de>
- upgraded to grace-981021
- added patch for using -bxy "0:1", i.e. for using column specification
  "0" for index.

* Tue Sep  8 1998 Henrik Seidel <seidel@mpimg-berlin-dahlem.mpg.de>
- upgraded to grace-5.0.1pre

* Thu Jul 16 1998 Henrik Seidel <seidel@mpimg-berlin-dahlem.mpg.de>
- added autoscale patch

* Wed Jul 15 1998 Henrik Seidel <seidel@mpimg-berlin-dahlem.mpg.de>
- initial revision of GRACE rpms


%prep
%setup
%patch0 -p1
tar -xzf $RPM_SOURCE_DIR/fftw.tar.gz

%build
PKG_BUILD_DIR=$RPM_BUILD_DIR/%{name}-%{version}
mkdir -p $PKG_BUILD_DIR/include
mkdir -p $PKG_BUILD_DIR/lib
cd fftw-1.3
%ifarch i386
./configure --prefix=$PKG_BUILD_DIR --enable-i386-hacks
%else
./configure --prefix=$PKG_BUILD_DIR
%endif
make
make install
cd ..
rm -rf gd1.3 fftw-1.3
./configure --prefix=/usr/X11R6 --enable-grace-home=/usr/X11R6/lib/X11/grace \
	--enable-editres \
	--enable-extra-incpath=$PKG_BUILD_DIR/include \
	--enable-extra-ldpath=$PKG_BUILD_DIR/lib --enable-debug
make
cd src
rm xmgrace
`make -n xmgrace | grep '^gcc' | head -1 | \
 sed -e 's/\([ \t]\|^\)-lnetcdf\b/\1-Wl,-Bstatic,-lnetcdf,-Bdynamic/g'`
mv xmgrace xmgrace.dynamic
`make -n xmgrace | grep '^gcc' | head -1 | \
 sed -e 's/\([ \t]\|^\)-lXm\b/\1-Wl,-Bstatic,-lXm,-Bdynamic/g' \
     -e 's/\([ \t]\|^\)-lXbae\b/\1-Wl,-Bstatic,-lXbae,-Bdynamic/g' \
     -e 's/\([ \t]\|^\)-lnetcdf\b/\1-Wl,-Bstatic,-lnetcdf,-Bdynamic/g'`
cd ..

%install
if [ "x$RPM_BUILD_ROOT" != "x/" ]; then
    rm -rf $RPM_BUILD_ROOT
fi
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/bin
make PREFIX=$RPM_BUILD_ROOT/usr/X11R6 \
     GRACE_HOME=$RPM_BUILD_ROOT/usr/X11R6/lib/X11/grace \
     install
strip $RPM_BUILD_ROOT/usr/X11R6/lib/X11/grace/bin/xmgrace
mv $RPM_BUILD_ROOT/usr/X11R6/lib/X11/grace/bin/xmgrace \
    $RPM_BUILD_ROOT/usr/X11R6/lib/X11/grace/bin/xmgrace.semistatic
strip $RPM_BUILD_ROOT/usr/X11R6/lib/X11/grace/bin/grconvert
install -s src/xmgrace.dynamic $RPM_BUILD_ROOT/usr/X11R6/lib/X11/grace/bin
rm -f $RPM_BUILD_ROOT/usr/X11R6/bin/xmgrace
rm -f $RPM_BUILD_ROOT/usr/X11R6/bin/gracebat
install -m755 $RPM_SOURCE_DIR/xmgrace $RPM_BUILD_ROOT/usr/X11R6/bin/xmgrace
ln -sf /usr/X11R6/bin/xmgrace $RPM_BUILD_ROOT/usr/X11R6/bin/gracebat
mkdir -p $RPM_BUILD_ROOT/usr/include
ln -sf /usr/X11R6/lib/X11/grace/include/grace_np.h \
    $RPM_BUILD_ROOT/usr/include/grace_np.h
mkdir -p $RPM_BUILD_ROOT/usr/lib
ln -sf /usr/X11R6/lib/X11/grace/lib/libgrace_np.a \
    $RPM_BUILD_ROOT/usr/lib/libgrace_np.a

cd $RPM_BUILD_ROOT
find ./usr/X11R6/lib/X11/grace -type d \
	| sed 's,^\.,\%attr(-\,root\,root) \%dir ,' \
	> $RPM_BUILD_DIR/file.list.%{name}
find . -type f \
	| egrep -v 'xmgrace\.(dynamic|semistatic)' \
	| sed 's,^\.,\%attr(-\,root\,root) ,' \
       	>> $RPM_BUILD_DIR/file.list.%{name}
find . -type l \
	| sed 's,^\.,\%attr(-\,root\,root) ,' \
       	>> $RPM_BUILD_DIR/file.list.%{name}

%clean
if [ "x$RPM_BUILD_ROOT" != "x/" ]; then
    rm -rf $RPM_BUILD_ROOT
fi
rm -f $RPM_BUILD_DIR/file.list.%{name}

%files dynamic -f ../file.list.%{name}
/usr/X11R6/lib/X11/grace/bin/xmgrace.dynamic

%files semistatic -f ../file.list.%{name}
/usr/X11R6/lib/X11/grace/bin/xmgrace.semistatic
