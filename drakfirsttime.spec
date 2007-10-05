%define version 2.11
%define		    name drakfirsttime

Summary:	    The Mandriva Linux First Time Wizard
Name:		    %{name}
Version:	    %{version}
Release:        %mkrel 1
# http://svn.mandriva.com/cgi-bin/viewvc.cgi/soft/ftw/
Source0:	    %{name}-%{version}.tar.bz2
URL:		    http://qa.mandriva.com/
License:	    GPL
Group:		    System/Configuration/Other
Requires:	    drakxtools >= 10.1-0.17mdk, perl-MDK-Common >= 1.1.17-3mdk, perl-libwww-perl >= 5.800-1mdk
Requires:		xinitrc >= 2.4.9-1mdk, hwdb-clients >= 0.15.1-1mdk
Requires:      xrandr evilwm mozilla-firefox
#Obsoletes:		mdkonline
BuildRoot:	    %{_tmppath}/%{name}-buildroot
BuildRequires:  gettext perl-devel perl-MDK-Common-devel
BuildArch:		noarch

%description
The First Time Wizard is a config tool to help a Mandriva Linux user to
set up some basic things, like registration at Mandriva Club/Mandriva Expert
and Mandriva Online the first time the system boots.
This package also includes the drakclub wizard, to set the club urpmi
sources.

%prep
rm -rf %{buildroot}

%setup -q

%build

%install
rm -rf %{buildroot}
%makeinstall_std PREFIX=%buildroot%_prefix

mkdir -p %buildroot%_prefix/X11R6/bin/

#install lang
%{find_lang} drakfirstboot

%post
%{update_menus}
%update_icon_cache hicolor

%postun
%{clean_menus}
%clean_icon_cache hicolor

%clean
rm -rf %{buildroot}

%files -f drakfirstboot.lang
%defattr(-,root,root)
%doc README COPYING NEWS
%{_sysconfdir}/X11/xsetup.d/??firstboot.xsetup
%_bindir/*
%config(noreplace) %{_sysconfdir}/sysconfig/firstboot
%{_datadir}/drakfirsttime

