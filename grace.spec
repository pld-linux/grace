%define version 5.0.5
%define name grace
%define serial 28
Name:		%{name}
Version:	%{version}
Serial:		%{serial}
Release:	1
License:	GPL
Source0:	ftp://plasma-gate.weizmann.ac.il/pub/grace/src/%{name}-%{version}.tar.gz
Source1:	xmgrace
Source2:	fftw.tar.gz
Patch0:		%{name}.perl.patch
Icon:		%{name}.gif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
ExclusiveArch:	i386 alpha
Group:		Applications/Math
Summary:	Numerical Data Processing and Visualization Tool (grace)
%description
Grace is a Motif application for two-dimensional data visualization.
Grace can transform the data using free equations, FFT, cross- and
auto-correlation, differences, integrals, histograms, and much more. The
generated figures are of high quality.  Grace is a very convenient tool
for data inspection, data transformation, and and for making figures for
publications.

%package dynamic
Group:		Applications/Math
Summary:	Numerical Data Processing and Visualization Tool (grace)
Provides:	%{name}
Conflicts:	%{name}-semistatic

%description dynamic
Grace is a Motif application for two-dimensional data visualization.
Grace can transform the data using free equations, FFT, cross- and
auto-correlation, differences, integrals, histograms, and much more. The
generated figures are of high quality.  Grace is a very convenient tool
for data inspection, data transformation, and and for making figures for
publications.

%package semistatic
Group:		Applications/Math
Summary:	grace with statically linked Motif libraries
Provides:	%{name}
Conflicts:	%{name}-dynamic

%description semistatic
Grace is a Motif application for two-dimensional data visualization.
Grace can transform the data using free equations, FFT, cross- and
auto-correlation, differences, integrals, histograms, and much more. The
generated figures are of high quality.  Grace is a very convenient tool
for data inspection, data transformation, and and for making figures for
publications.

In this package the Motif libraries are linked statically for users who have
no Motif runtime libraries.
