Summary: The Mandriva Linux First Time Wizard
Name: drakfirsttime
Version: 2.25.5
Release: 4
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


%changelog
* Tue May 03 2011 Funda Wang <fwang@mandriva.org> 2.25.5-3
+ Revision: 664489
- we are using webkit to show wizard, so bye bye firefox stuff

  + Oden Eriksson <oeriksson@mandriva.com>
    - mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 2.25.5-2mdv2011.0
+ Revision: 604817
- rebuild

* Thu May 20 2010 Olivier Blin <oblin@mandriva.com> 2.25.5-1mdv2010.1
+ Revision: 545455
- 2.25.5
- test network connection again after starting network-up service if
  needed (#59338)

* Tue Feb 02 2010 Thierry Vignaud <tv@mandriva.org> 2.25.4-1mdv2010.1
+ Revision: 499542
- fix local page URI now that we compute it as user an no more as root (#57171)
  (regression introduce in 2.25.3)

* Wed Nov 18 2009 Thierry Vignaud <tv@mandriva.org> 2.25.3-1mdv2010.1
+ Revision: 467255
- bump require on drakxtools for window.close() event fix (#55099)
- require libdrakx-net for connection test
- add ftw version to URL
- readd back HML "close" button from disconnected page now that
  display_help handle closing window from JS (#55099)
- run hclcollector in background in case lshw got stuck (#50994)
- use drakx-net instead of ping in order to check whether network is
  up or down; do the test as user (http test instead of ping (#36727))
- updated style for small screen (#53864)

* Tue Oct 06 2009 Thierry Vignaud <tv@mandriva.org> 2.25.2-1mdv2010.0
+ Revision: 454828
- remove HTML "close" button from disconnected page

* Fri Sep 25 2009 Thierry Vignaud <tv@mandriva.org> 2.25.1-1mdv2010.0
+ Revision: 448817
- fix webkit browser startup

* Tue Sep 22 2009 Thierry Vignaud <tv@mandriva.org> 2.25-1mdv2010.0
+ Revision: 447514
- fix installing extensions with firefox-3.5 (r-kiosk is kept so that we can
  rallback to using firefox if needed)
- use webkit instead of firefox in order to run first time wizard
- use externally packaged R-kiosk extension

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild

* Tue Apr 14 2009 Thierry Vignaud <tv@mandriva.org> 2.23-1mdv2009.1
+ Revision: 367164
- make firefox profile less permisive using R-kiosk extension (#43718)

* Tue Apr 14 2009 Thierry Vignaud <tv@mandriva.org> 2.22-1mdv2009.1
+ Revision: 366894
- fixes the offline page theme

* Mon Mar 30 2009 Thierry Vignaud <tv@mandriva.org> 2.21.1-1mdv2009.1
+ Revision: 362300
- translation updates

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 2.21-2mdv2009.1
+ Revision: 350837
- rebuild

* Mon Oct 06 2008 Thierry Vignaud <tv@mandriva.org> 2.21-1mdv2009.0
+ Revision: 291140
- disable google toolbar
- really run as a user

* Wed Oct 01 2008 Thierry Vignaud <tv@mandriva.org> 2.20-1mdv2009.0
+ Revision: 290411
- force firefox to not show the EULA

* Tue Sep 23 2008 Thierry Vignaud <tv@mandriva.org> 2.19-1mdv2009.0
+ Revision: 287564
- really force writing no network HTML page in UTF-8 (#44025)

* Wed Sep 17 2008 Frederic Crozat <fcrozat@mandriva.com> 2.18-1mdv2009.0
+ Revision: 285480
- Release 1.28 :
 - switch to matchbox instead of evilwm

* Fri Jun 20 2008 Pixel <pixel@mandriva.com> 2.17-3mdv2009.0
+ Revision: 227421
- rebuild for fixed %%update_icon_cache/%%clean_icon_cache/%%post_install_gconf_schemas
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 2.17-2mdv2009.0
+ Revision: 220683
- rebuild

* Thu Apr 03 2008 Thierry Vignaud <tv@mandriva.org> 2.17-1mdv2008.1
+ Revision: 192098
- updated translations

* Tue Mar 25 2008 Thierry Vignaud <tv@mandriva.org> 2.16-1mdv2008.1
+ Revision: 190088
- run HCL collector for later upload now that is no more run by
  initsripts (#39259)

* Fri Mar 14 2008 Thierry Vignaud <tv@mandriva.org> 2.15-1mdv2008.1
+ Revision: 187940
- fix image path

* Fri Mar 14 2008 Thierry Vignaud <tv@mandriva.org> 2.14-1mdv2008.1
+ Revision: 187832
- update CSS for 2008 Spring
- update images

* Thu Feb 14 2008 Thierry Vignaud <tv@mandriva.org> 2.13-2mdv2008.1
+ Revision: 168587
- fix update-menus-without-menu-file-in-%%post(|un)
- only suggests hcl since it's not really needed
- require hcl instead of hwdb-clients
- fix no-buildroot-tag

* Mon Feb 11 2008 Thierry Vignaud <tv@mandriva.org> 2.13-1mdv2008.1
+ Revision: 165233
- kill evimwm with SIGKILL once wizard exits
- kill re-definition of %%buildroot on Pixel's request

* Mon Oct 15 2007 Olivier Blin <oblin@mandriva.com> 2.12-1mdv2008.1
+ Revision: 98707
- 2.12
- move user code from xsetup script into new ftw-start-browser.sh,
  so that xsetup script does not run "exit" and aborts the whole
  Xsetup process

* Fri Oct 05 2007 Thierry Vignaud <tv@mandriva.org> 2.11-1mdv2008.0
+ Revision: 95596
- do not perform a ping if not needed (helps boxes with network issues)

* Thu Oct 04 2007 Thierry Vignaud <tv@mandriva.org> 2.10-1mdv2008.0
+ Revision: 95448
- fix disconnected URL

* Wed Oct 03 2007 Thierry Vignaud <tv@mandriva.org> 2.9-1mdv2008.0
+ Revision: 95087
- updated translation

* Wed Oct 03 2007 Thierry Vignaud <tv@mandriva.org> 2.8-1mdv2008.0
+ Revision: 94972
- prevent rerunning all xsetup.d entries

* Wed Oct 03 2007 Thierry Vignaud <tv@mandriva.org> 2.7-1mdv2008.0
+ Revision: 94962
- run ping as root in case it's not allowed to regular users

* Wed Oct 03 2007 Thierry Vignaud <tv@mandriva.org> 2.6-1mdv2008.0
+ Revision: 94948
- prevent extensions to popup (anne)

* Mon Oct 01 2007 Thierry Vignaud <tv@mandriva.org> 2.5-1mdv2008.0
+ Revision: 94154
- adapt CSS to RTL languages (Dotan Kamber)
- cleanups
- make sure to place local disconnected page in the proper place
- refuse to run as non root & non ftw
- account is now dynamically created

* Thu Sep 27 2007 Thierry Vignaud <tv@mandriva.org> 2.4-1mdv2008.0
+ Revision: 93388
- updated translations

* Tue Sep 25 2007 Thierry Vignaud <tv@mandriva.org> 2.3-1mdv2008.0
+ Revision: 92940
- updated translations

* Tue Sep 25 2007 Thierry Vignaud <tv@mandriva.org> 2.2-1mdv2008.0
+ Revision: 92845
- make default page when network is unavaillable be translatable

* Wed Sep 19 2007 Thierry Vignaud <tv@mandriva.org> 2.1.1-1mdv2008.0
+ Revision: 90590
- fix a path

* Tue Sep 18 2007 Thierry Vignaud <tv@mandriva.org> 2.1-1mdv2008.0
+ Revision: 89537
- add a close button in not connected case
- run the wizard as user
- update URL
- create "ftw" user

* Fri Sep 14 2007 Thierry Vignaud <tv@mandriva.org> 2.0-1mdv2008.0
+ Revision: 85684
- drakfirsttime 2, using a browser


* Tue Apr 03 2007 Thierry Vignaud <tvignaud@mandriva.com> 1.15-1mdv2007.1
+ Revision: 150321
- update background

* Wed Mar 28 2007 Thierry Vignaud <tvignaud@mandriva.com> 1.14-1mdv2007.1
+ Revision: 149187
- fix two crashes

* Thu Mar 22 2007 Adam Williamson <awilliamson@mandriva.com> 1.13-1mdv2007.1
+ Revision: 147938
- fix Club media addition
- update icon cache in post
- package fd.o icons too

* Mon Mar 12 2007 Thierry Vignaud <tvignaud@mandriva.com> 1.11-1mdv2007.1
+ Revision: 141824
- translation snapshot

* Wed Mar 07 2007 Thierry Vignaud <tvignaud@mandriva.com> 1.10-1mdv2007.1
+ Revision: 134739
- fix crash when pressing the "confidentiality" button (#29253)

* Wed Feb 07 2007 Olivier Blin <oblin@mandriva.com> 1.9-1mdv2007.1
+ Revision: 117022
- 1.9
- Import drakfirsttime

* Sat Sep 23 2006 Thierry Vignaud <tvignaud@mandriva.com> 1.8-1mdv2007.0
- require xrandr
- workaround UIM bug that makes first time wizard crash (#24472)

* Sun Sep 17 2006 Thierry Vignaud <tvignaud@mandriva.com> 1.7-1mdv2007.0
- updated translation

* Fri Sep 15 2006 Thierry Vignaud <tvignaud@mandriva.com> 1.6-1mdv2007.0
- fix the keyboard focus

* Thu Sep 14 2006 Thierry Vignaud <tvignaud@mandriva.com> 1.5-1mdv2007.0
- improved layout, notably:
  o better looking when using a RTL language
  o better looking with new background
  o improved spacing

* Wed Sep 13 2006 Thierry Vignaud <tvignaud@mandriva.com> 1.4-1mdv2007.0
- use %%mkrel
- fix menu group
- new background
- updated translations
- XDG menu

* Wed Sep 21 2005 Daouda LO <daouda@mandriva.com> 1.3-1mdk
- center exit dialog window on parent
- read existing mdkonline conf
- po updates

* Tue Sep 20 2005 Daouda LO <daouda@mandriva.com> 1.3-0.4mdk
- change xsetup file to source proxy.sh before running 
  drakfirsboot (cavassin)
- update translations

* Sat Sep 17 2005 Daouda LO <daouda@mandriva.com> 1.3-0.3mdk
- support http proxy settings (#18611)
- translation updates

* Wed Sep 14 2005 Daouda LO <daouda@mandriva.com> 1.3-0.2mdk
- po updates 
- fix #18249
- unified background to fit install colormap
- pass nointeractive option to mdkonline to create and upload config
- wizard steps building is decide at runtime
- layout cosmetics fixes

* Sat Sep 03 2005 Daouda LO <daouda@mandriva.com> 1.3-0.1mdk
- New layout similar to drakx install
- Generic mandriva account for all web services 
  (Mandriva Club, Mandriva Online, Mandriva Expert, ...)
- moved to SOAP technology on both client and server

* Sat Apr 30 2005 Daouda LO <daouda@mandrakesoft.com> 1.2-1mdk
- switch to mandriva(pablo)
- po updates (pablo)

* Tue Apr 05 2005 Daouda LO <daouda@mandrakesoft.com> 1.2-0.1mdk
- fixed club media setting (#14957)
- fixed lost focus when Next button is clicked (#14846)
- po updates

* Thu Mar 24 2005 Daouda LO <daouda@mandrakesoft.com> 1.1-18mdk
- set_transient on real window (#14944)

* Wed Mar 16 2005 Daouda LO <daouda@mandrakesoft.com> 1.1-17mdk
- don't set background
- requires root capabilities for drakclub

* Fri Jan 21 2005 Daouda LO <daouda@mandrakesoft.com> 1.1-16mdk
- main loop fix

* Wed Oct 13 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.1-15mdk
- Fix wizard navigation with network off

* Sat Oct 09 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.1-14mdk
- New Italian and German translations
- Fix wizard navigation for powerpacks

* Fri Oct 08 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.1-13mdk
- Update translations and description

* Tue Oct 05 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.1-12mdk
- Rebuild for dependencies

* Tue Oct 05 2004 Pablo Saratxaga <pablo@mandrakesoft.com> 1.1-11mdk
- updated translations

* Fri Oct 01 2004 Daouda LO <daouda@mandrakesoft.com> 1.1-10mdk
- privacy test new layout
- same gui behaviour for download and powerpack firstboot wizard
- config file changed to 'noreplace'.
- po updates

* Sat Sep 25 2004 Daouda LO <daouda@mandrakesoft.com> 1.1-9mdk
- fall cleanups
- final layout
- po updates

* Wed Sep 15 2004 Daouda LO <daouda@mandrakesoft.com> 1.1-8mdk
- fixes in fr.po
- remove trailing '1' in vboxes

* Tue Sep 14 2004 Daouda LO <daouda@mandrakesoft.com> 1.1-7mdk
- new questionnaire
- cosmetics changes 
- update po

* Tue Sep 07 2004 Daouda LO <daouda@mandrakesoft.com> 1.1-6mdk
- requires on hwdb_clients
- upload config to hardware db

* Sat Sep 04 2004 Frederic Lepied <flepied@mandrakesoft.com> 1.1-5mdk
- fixed cursor
- fixed startup
- fixed l10n
- everything back in cvs

* Thu Sep 02 2004 Daouda LO <daouda@mandrakesoft.com> 1.1-4mdk
- firstboot replaces firsttime (launched by system before dm greetings)
- cleanups 
- xsetup file to launch firstboot before (*dm greeters)
- Merging with mdkonline stuffs

* Wed Aug 11 2004 Daouda LO <daouda@mandrakesoft.com> 1.1-3mdk
- require perl-IO-Stty

* Wed Aug 11 2004 Daouda LO <daouda@mandrakesoft.com> 1.1-2mdk
- resync with cvs
- daoudapo fixes

* Tue Aug 10 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.1-1mdk
- survey:
  o use OptionMenu rather than editable Combo
  o preselect the country that was choosen at install time
  o reuse drakx country list
  o reuse drakx for guessing iso country code from string (#10664, #10665)
- big translation updates

* Sat Aug 07 2004 Daouda LO <daouda@mandrakesoft.com> 1.0-3.100mdk
- use dmrc file (removed obsoleted .wmrc, and .gnome2/gdm)

* Fri Jun 04 2004 Pixel <pixel@mandrakesoft.com> 1.0-2.100mdk
- rebuild (and get correct requires)

* Sat May 08 2004 Pablo Saratxaga <pablo@mandrakesoft.com> 1.0-1.100mdk
- Integrated Basque translations

