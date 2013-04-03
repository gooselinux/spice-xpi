%define tarname spice-xpi
%define tarversion 2.4

Name:           spice-xpi
Version:        2.4
Release:        1%{?dist}.2
Summary: SPICE extension for Mozilla
Group: Applications/Internet
License:        GPLv2+
URL:            http://www.redhat.com/
Source0:        %{tarname}-%{tarversion}.tar.bz2
BuildRoot:      %{_tmppath}/%{tarname}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  gcc-c++
BuildRequires:  zip
BuildRequires:  log4cpp-devel
BuildRequires:  libX11-devel
BuildRequires:  xulrunner-devel
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  autoconf

Patch1:         spice-xpi-01-getset-issue.patch
Patch2:         spice-xpi-02-usbrdrctrl.patch

ExclusiveArch:  x86_64 %{ix86}

Requires: firefox
Requires: spice-client >= 0.4.2-18
Requires: log4cpp

%description
SPICE extension for mozilla allows the client to be used from a web browser.

%prep
%setup -q -n %{tarname}-%{tarversion}
%patch1 -p1 -b .getset
%patch2 -p1 -b .usbrdrctrl

%build
aclocal
libtoolize --automake
autoheader
automake --add-missing
autoconf

%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%{_libdir}/mozilla/*
%{_datadir}/spice/
%exclude %{_libdir}/mozilla/*.rdf
%exclude %{_libdir}/mozilla/plugins/*.a
%exclude %{_libdir}/mozilla/plugins/*.la
%doc COPYING README

%changelog
* Thu Mar 31 2011 Peter Hatina <phatina@redhat.com> 2.4-1.el6_0.2
- Fix security vulnerability CVE-2011-0012 (rhbz#639869)
  Resolves: rhbz#639870

* Tue Mar 29 2011 Peter Hatina <phatina@redhat.com> 2.4-1.el6_0.1
- Fix security vulnerability CVE-2011-1179 (rhbz#689931)
  Resolves: rhbz#689932

* Wed Aug 4 2010 Martin Stransky <stransky@redhat.com > 2.4-1
- fixed rhbz#620445, rhbz#620447, rhbz#620448

* Tue Jul 27 2010 Martin Stransky <stransky@redhat.com > 2.3-0.5
- rhbz#618292 - NPRuntime support

* Wed Jul 14 2010 Uri Lublin <uril@redhat.com> 2.3-0.4
- ~nsPluginInstance: check mScriptablePeer before accessing it
  Resolves: #604678

* Thu Jun 24 2010 Uri Lublin <uril@redhat.com> 2.3-0.3
- Build packages for i686 too.
  Resolves: #604661

* Tue Jun 15 2010 Ray Strode <rstrode@redhat.com> 2.3-0.2
- Change dep to spice-client from qspice-client
  Resolves: #604202

* Thu Jun 10 2010 Dennis Gregorovic <dgregor@redhat.com> - 2.3-0.1
- Rebuilt for RHEL 6
- Related: rhbz#552646

* Mon Feb 01 2010 Yuval Kashtan <ykashtan@redhat.com> - 2.3-0.el6
- RHEL-6.0 with new controller

* Wed Jan 20 2010 Yuval Kashtan <ykashtan@redhat.com> - 2.2-0.el5
- Initial package

