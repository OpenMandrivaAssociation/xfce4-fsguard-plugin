%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	Disk space plugin for the Xfce panel
Name:		xfce4-fsguard-plugin
Version:	1.0.1
Release:	2
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-fsguard-plugin
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-fsguard-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
Requires:	xfce4-panel >= 4.8.0
BuildRequires:	pkgconfig(libxfce4panel-1.0)
BuildRequires:	perl(XML::Parser)
BuildRequires:	pkgconfig(libxfce4ui-1)

%description
Disk space panel plugin for the Xfce Desktop Environment.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

chmod +x %{buildroot}%{_libdir}/xfce4/panel/plugins/*.so
rm -rf %{buildroot}%{_iconsdir}/hicolor/icon-theme.cache

%find_lang %{name}

%files -f %{name}.lang
%doc README NEWS AUTHORS ChangeLog
%{_libdir}/xfce4/panel/plugins/*
%{_datadir}/xfce4/panel/plugins/*
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/scalable/apps/*.svg


%changelog
* Tue Apr 17 2012 Crispin Boylan <crisb@mandriva.org> 1.0.0-3mdv2012.0
+ Revision: 791555
- Rebuild

* Mon Apr 09 2012 Crispin Boylan <crisb@mandriva.org> 1.0.0-2
+ Revision: 790052
- Rebuild for xfce 4.10

* Wed Jan 26 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.0-1
+ Revision: 632778
- update to new version 1.0.0
- update url for Source0
- drop old scriplets

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.1 packages

* Fri May 07 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.2-4mdv2010.1
+ Revision: 543425
- rebuild for mdv 2010.1

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 0.4.2-3mdv2010.0
+ Revision: 446021
- rebuild

* Thu Mar 05 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.2-2mdv2009.1
+ Revision: 349454
- rebuild for xfce-4.6.0

* Mon Nov 24 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.2-1mdv2009.1
+ Revision: 306369
- update to new version 0.4.2

* Sat Oct 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.1-5mdv2009.1
+ Revision: 294995
- rebuild for new Xfce4.6 beta1

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 0.4.1-4mdv2009.0
+ Revision: 262358
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.4.1-3mdv2009.0
+ Revision: 256867
- rebuild

* Fri Jan 25 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.1-1mdv2008.1
+ Revision: 157747
- new version
- correct buildrequires
- spec file clean
- do not package COPYING, add ChangeLog to the docs
- use upstream tarball name as a real name
- use upstream name

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Oct 27 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.0-2mdv2008.1
+ Revision: 102610
- fix postun scriplet
- new license policy

* Fri Oct 26 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.0-1mdv2008.1
+ Revision: 102240
- update to the final version

* Mon Oct 22 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.99.2-1mdv2008.1
+ Revision: 101097
- new prerelease

* Wed Oct 17 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.99.1-1mdv2008.1
+ Revision: 99592
- remove not needed file
- fix file list
- new version (0.4.0-rc1)

* Thu May 31 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.0-5mdv2008.0
+ Revision: 33223
- spec file clean
- update url

