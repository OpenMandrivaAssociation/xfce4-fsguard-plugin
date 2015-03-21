%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	Disk space plugin for the Xfce panel
Name:		xfce4-fsguard-plugin
Version:	1.0.1
Release:	3
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
