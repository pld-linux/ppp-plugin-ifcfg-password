
%define ppp_version 2.4.2

Summary:	ppp plugin reading passwords from ifcfg
Summary(pl):	Wtyczka ppp czytaj±ca has³a z ifcfg
Name:		ppp-plugin-ifcfg-password
Version:	0.1
Release:	2
License:	distributable
Group:		Networking/Daemons
Source0:	ftp://dev.null.pl/pub/%{name}-%{version}.tar.gz
# Source0-md5:	926c7fc7bd73fcec8769dfcda66247d7
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
