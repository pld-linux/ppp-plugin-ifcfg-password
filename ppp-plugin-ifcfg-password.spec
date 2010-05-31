Summary:	ppp plugin reading passwords from ifcfg
Summary(pl.UTF-8):	Wtyczka ppp czytająca hasła z ifcfg
Name:		ppp-plugin-ifcfg-password
Version:	0.1
Release:	7
License:	distributable
Group:		Networking/Daemons
Source0:	ftp://dev.null.pl/pub/%{name}-%{version}.tar.gz
# Source0-md5:	926c7fc7bd73fcec8769dfcda66247d7
BuildRequires:	ppp-plugin-devel >= 2.4.1
BuildRequires:	rpmbuild(macros) >= 1.145
%{requires_eq_to ppp ppp-plugin-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ppp plugin reading passwords from ifcfg.

%description -l pl.UTF-8
Wtyczka ppp czytająca hasła z ifcfg.

%prep
%setup -q

rm -f *.h
ln -sf /usr/include/pppd/*.h .

%build
%{__make} \
	CC="%{__cc}" \
	LDFLAGS="%{rpmldflags} -shared" \
	CFLAGS="%{rpmcflags} %{rpmcppflags} -fPIC -Wall"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	LIBDIR=$RPM_BUILD_ROOT%{_libdir}/pppd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/pppd/*/*.so
