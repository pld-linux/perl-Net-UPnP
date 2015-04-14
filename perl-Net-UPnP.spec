#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Net
%define		pnam	UPnP
%include	/usr/lib/rpm/macros.perl
Summary:	Net::UPnP - Perl extension for UPnP
Name:		perl-Net-UPnP
Version:	1.4.3
Release:	1
License:	BSD
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Net/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a30d7cc54290946aeb028650cfdc9279
URL:		http://search.cpan.org/dist/Net-UPnP/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides some functions to control UPnP devices.

Currently, the package provides only functions for the control point.  
To control UPnP devices, see Net::UPnP::ControlPoint.

As a sample of the control point, the package provides 
Net::UPnP::AV::MediaServer to control the devices such as
DLNA media servers. As the example, please dms2vodcast.pl
that converts from the MPEG2 movies to the MPEG4 one and 
outputs the RSS file for Vodcasting.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Net/*.pm
%{perl_vendorlib}/Net/UPnP
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
