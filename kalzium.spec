%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Shows the periodic system of the elements
Name:		kalzium
Version:	17.03.80
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://edu.kde.org/kalzium
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
%ifnarch %{arm}
BuildRequires:	pkgconfig(avogadro)
%endif
BuildRequires:	pkgconfig(eigen3)
BuildRequires:	pkgconfig(openbabel-2.0)
BuildRequires:	pkgconfig(chemical-mime-data)
BuildRequires:	facile
BuildRequires:	ocaml
BuildRequires:	cmake(KF5Completion)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5ItemViews)
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	cmake(KF5KHtml)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Plotting)
BuildRequires:	cmake(KF5TextWidgets)
BuildRequires:	cmake(KF5UnitConversion)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Script)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Xml)
Requires:	openbabel
%ifnarch %{arm}
Requires:	avogadro
%endif
Requires:	chemical-mime-data
Requires:	ocaml
Conflicts:	cantor < 4.6.90
Conflicts:	kdeedu4-core < 4.6.90
Obsoletes:	plasma-engine-kalzium < %{EVRD}
Obsoletes:	plasma-applet-didyouknow < %{EVRD}

%description
Kalzium is an application which will show you some information about the
periodic system of the elements. Therefore you could use it as an
information database.

%files
%doc COPYING COPYING.LIB COPYING.DOC
%doc %{_kde_docdir}/HTML/en/kalzium
%{_sysconfdir}/xdg/kalzium.knsrc
%{_datadir}/applications/org.kde.kalzium.desktop
%{_datadir}/applications/org.kde.kalzium_cml.desktop
%{_bindir}/kalzium
%{_datadir}/metainfo/org.kde.kalzium.appdata.xml
%{_datadir}/config.kcfg/kalzium.kcfg
%{_datadir}/icons/*/*/*/*.*
%{_mandir}/man1/kalzium.1.*
%{_datadir}/kalzium
%{_datadir}/kxmlgui5/kalzium
%{_datadir}/libkdeedu/data/*

#----------------------------------------------------------------------------

%define science_major 5
%define libscience %mklibname science %{science_major}

%package -n %{libscience}
Summary:	Runtime library for KDE Education Application
Group:		System/Libraries

%description -n %{libscience}
libscience is a library that provides classes for chemical data.This library is
mainly used by kalzium.

%files -n %{libscience}
%{_libdir}/libscience.so.%{science_major}*

#-----------------------------------------------------------------------------

%package devel
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	pkgconfig(eigen2)
Requires:	pkgconfig(eigen3)
Requires:	pkgconfig(openbabel-2.0)
Requires:	%{libscience} = %{EVRD}
Conflicts:	kdeedu4-devel < 4.6.90

%description devel
Files needed to build applications based on %{name}.

%files devel
%{_includedir}/libkdeedu
%{_libdir}/libscience.so

#----------------------------------------------------------------------

%prep
%setup -q
%apply_patches

%build
%cmake_kde5
%ninja

%install
%ninja_install -C build
