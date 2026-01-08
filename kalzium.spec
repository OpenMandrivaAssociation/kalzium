#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

%define __noautoreq '^devel\\(libAvogadro.*$'


Summary:	Shows the periodic system of the elements
Name:		kalzium
Version:	25.12.1
Release:	%{?git:0.%{git}.}1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://edu.kde.org/kalzium
%if 0%{?git:1}
Source0:	https://invent.kde.org/education/kalzium/-/archive/%{gitbranch}/kalzium-%{gitbranchd}.tar.bz2#/kalzium-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kalzium-%{version}.tar.xz
%endif
Patch0:		kalzium-ocaml-5.0.patch
%ifnarch %{arm}
BuildRequires:	cmake(AvogadroLibs)
%endif
BuildRequires:	pkgconfig(eigen3)
BuildRequires:	pkgconfig(openbabel-3)
BuildRequires:	pkgconfig(chemical-mime-data)
BuildRequires:	facile
BuildRequires:	ocaml
BuildRequires:	cmake(KF6Completion)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6ItemViews)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6Plotting)
BuildRequires:	cmake(KF6NewStuff)
BuildRequires:	cmake(KF6TextWidgets)
BuildRequires:	cmake(KF6UnitConversion)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Concurrent)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(Qt6OpenGL)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Core5Compat)
BuildRequires:	cmake(Qt6StateMachine)
BuildRequires:	cmake(Qt6Scxml)
BuildRequires:	cmake(JKQTPlotter6)
BuildRequires:	pkgconfig(glu)

Requires:	openbabel
Requires:	chemical-mime-data
Requires:	ocaml
Conflicts:	cantor < 4.6.90
Conflicts:	kdeedu4-core < 4.6.90
Obsoletes:	plasma-engine-kalzium < %{EVRD}
Obsoletes:	plasma-applet-didyouknow < %{EVRD}

%rename plasma6-kalzium

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
BuildOption:	-DQT_MAJOR_VERSION=6

%description
Kalzium is an application which will show you some information about the
periodic system of the elements. Therefore you could use it as an
information database.

%files -f kalzium.lang
# No headers for this library -- so splitting it and having -devel
# doesn't make sense
%{_libdir}/libcompoundviewer.so*
%{_datadir}/applications/org.kde.kalzium.desktop
%{_datadir}/applications/org.kde.kalzium_cml.desktop
%{_bindir}/kalzium
%{_datadir}/metainfo/org.kde.kalzium.appdata.xml
%{_datadir}/config.kcfg/kalzium.kcfg
%{_datadir}/icons/*/*/*/*.*
%{_mandir}/man1/kalzium.1.*
%{_datadir}/kalzium
%{_datadir}/knsrcfiles/kalzium.knsrc
%{_datadir}/libkdeedu/data/*
%{_datadir}/qlogging-categories6/kalzium.categories

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
Requires:	pkgconfig(eigen3)
Requires:	pkgconfig(openbabel-3)
Requires:	%{libscience} = %{EVRD}
Conflicts:	kdeedu4-devel < 4.6.90
%rename plasma6-kalzium-devel

%description devel
Files needed to build applications based on %{name}.

%files devel
%{_includedir}/libkdeedu
%{_libdir}/libscience.so
