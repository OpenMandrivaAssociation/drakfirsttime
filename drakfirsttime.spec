Summary:	The Mandriva Linux First Time Wizard
Name:		drakfirsttime
Version:	2.25.5
Release:	9
License:	GPLv2
Group:		System/Configuration/Other
# http://svn.mandriva.com/cgi-bin/viewvc.cgi/soft/ftw/
Url:		http://qa.mandriva.com/
Source0:	%{name}-%{version}.tar.lzma
BuildArch:	noarch

BuildRequires:	gettext
BuildRequires:	perl-devel
BuildRequires:	perl-MDK-Common-devel
Requires:	drakxtools >= 12.77.1
Requires:	drakx-installer-matchbox
# for connection test:
Requires:	libdrakx-net
Requires:	perl-MDK-Common
Requires:	perl-libwww-perl
Requires:	xinitrc
Requires:	xrandr
Suggests:	hcl

%description
The First Time Wizard is a config tool to help a Mandriva Linux user to
set up some basic things, like registration at Mandriva Club/Mandriva Expert
and Mandriva Online the first time the system boots.
This package also includes the drakclub wizard, to set the club urpmi
sources.

%prep
%setup -q

%install
%makeinstall_std PREFIX=%{buildroot}%{_prefix}

#we are using webkit, so  no ue shipping firefox ext
rm -fr %{buildroot}%{_datadir}/%{name}/firefox

#install lang
%find_lang drakfirstboot

%files -f drakfirstboot.lang
%doc README COPYING NEWS
%{_sysconfdir}/X11/xsetup.d/??firstboot.xsetup
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/sysconfig/firstboot
%{_datadir}/drakfirsttime

