Summary: The Mandriva Linux First Time Wizard
Name: drakfirsttime
Version: 2.25.5
Release: 3
# http://svn.mandriva.com/cgi-bin/viewvc.cgi/soft/ftw/
Source0: %{name}-%{version}.tar.lzma
URL: http://qa.mandriva.com/
License: GPL
Group: System/Configuration/Other
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: drakxtools >= 12.77.1
Requires: perl-MDK-Common >= 1.1.17-3mdk
Requires: perl-libwww-perl >= 5.800-1mdk
# for connection test:
Requires: libdrakx-net
Requires: xinitrc >= 2.4.9-1mdk
Suggests: hcl
Requires: xrandr
Requires: drakx-installer-matchbox
BuildRequires: gettext perl-devel perl-MDK-Common-devel
BuildArch: noarch

%description
The First Time Wizard is a config tool to help a Mandriva Linux user to
set up some basic things, like registration at Mandriva Club/Mandriva Expert
and Mandriva Online the first time the system boots.
This package also includes the drakclub wizard, to set the club urpmi
sources.

%prep
%setup -q

%install
rm -rf %{buildroot}
%makeinstall_std PREFIX=%buildroot%_prefix

#we are using webkit, so  no ue shipping firefox ext
rm -fr %buildroot%_datadir/%name/firefox

#install lang
%{find_lang} drakfirstboot

%if %mdkversion < 200900
%post
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%clean_icon_cache hicolor
%endif

%clean
rm -rf %{buildroot}

%files -f drakfirstboot.lang
%defattr(-,root,root)
%doc README COPYING NEWS
%{_sysconfdir}/X11/xsetup.d/??firstboot.xsetup
%_bindir/*
%config(noreplace) %{_sysconfdir}/sysconfig/firstboot
%{_datadir}/drakfirsttime
