
%define version 0.1
%define ppp_version 2.4.1

Summary:	ppp plugin reading passwords from ifcfg
Summary(pl):	Wtyczka ppp czytaj±ca has³a z ifcfg
Name:		ppp-plugin-ifcfg-password
Version:	%{version}
Release:	1
License:	distributable
Group:		Networking/Daemons
Source0:	ftp://dev.null.pl/pub/%{name}-%{version}.tar.gz
Requires:	ppp-%{ppp_version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ppp plugin reading passwords from ifcfg

%description -l pl
Wtyczka ppp czytaj±ca has³a z ifcfg

%prep
%setup -q

%build
%{__make} CC=%{__cc}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/pppd/%{ppp_version}
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/pppd/%{ppp_version}/*
