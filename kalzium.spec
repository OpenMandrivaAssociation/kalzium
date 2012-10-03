%define eigen_version 2.0.3

Name:		kalzium
Summary:	Shows the periodic system of the elements
Version: 4.9.2
Release: 1
Group:		Graphical desktop/KDE
License:	GPLv2 LGPLv2 GFDL
URL:		http://edu.kde.org/kalzium
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(eigen2) >= %{eigen_version}
BuildRequires:	pkgconfig(openbabel-2.0)
BuildRequires:	avogadro-devel
BuildRequires:	ocaml
BuildRequires:	facile
Requires:	libkdeedu = %{version}
Requires:	openbabel
Requires:	avogadro
Requires:	ocaml
Conflicts:	cantor < 4.6.90
Conflicts:	kdeedu4-core < 4.6.90

%description
Kalzium is an application which will show you some information about the
periodic system of the elements. Therefore you could use it as an
information database.

%files
%doc COPYING COPYING.LIB COPYING.DOC
%doc %{_kde_docdir}/HTML/en/kalzium
%{_kde_bindir}/kalzium
%{_kde_appsdir}/kalzium
%{_kde_iconsdir}/hicolor/*/apps/kalzium.png
%{_kde_iconsdir}/hicolor/scalable/apps/kalzium.svgz
%{_kde_libdir}/kde4/plasma_applet_molmassCalculator.so
%{_kde_libdir}/kde4/concentrationCalculator.so
%{_kde_libdir}/kde4/gasCalculator.so
%{_kde_libdir}/kde4/nuclearCalculator.so
%{_kde_applicationsdir}/kalzium.desktop
%{_kde_services}/plasma-applet-Molmasscalculator.desktop
%{_kde_datadir}/config.kcfg/kalzium.kcfg
%{_kde_configdir}/kalzium.knsrc
%{_kde_appsdir}/libkdeedu/data/elements.xml
%{_kde_appsdir}/libkdeedu/data/isotopes.xml
%{_kde_appsdir}/libkdeedu/data/spectra.xml
%{_kde_appsdir}/libkdeedu/data/symbols.csv
%{_kde_appsdir}/libkdeedu/data/symbols2.csv
%{_kde_services}/concentrationCalculator.desktop
%{_kde_services}/gasCalculator.desktop
%{_kde_services}/nuclearCalculator.desktop
%{_kde_mandir}/man1/kalzium.1.*

#-----------------------------------------------------------------------------

%package -n plasma-engine-kalzium
Summary:	plasma didyouknow Applet
Group:		Graphical desktop/KDE
Requires:	kdebase4-runtime
Provides:	plasma-applet

%description -n plasma-engine-kalzium
kalzium engine applet

%files -n plasma-engine-kalzium
%{_kde_libdir}/kde4/plasma_engine_kalzium.so
%{_kde_services}/plasma-dataengine-kalzium.desktop

#------------------------------------------------------------------------------

%package -n plasma-applet-didyouknow
Summary:	plasma didyouknow Applet
Group:		Graphical desktop/KDE
Requires:	kdebase4-runtime
Provides:	plasma-applet

%description -n plasma-applet-didyouknow
Plasma applet where you can answer questions

%files -n plasma-applet-didyouknow
%{_kde_libdir}/kde4/plasma_applet_didyouknow.so
%{_kde_services}/plasma_didyouknow.desktop
%{_kde_appsdir}/desktoptheme/default/widgets/chalkboard.svg

#------------------------------------------------------------------------------

%define compoundviewer_major 4
%define libcompoundviewer %mklibname compoundviewer %{compoundviewer_major}

%package -n %{libcompoundviewer}
Summary:	Kalzium runtime library
Group:		System/Libraries

%description -n %{libcompoundviewer}
Kalzium runtime library.

%files -n %{libcompoundviewer}
%{_kde_libdir}/libcompoundviewer.so.%{compoundviewer_major}*

#----------------------------------------------------------------------------

%define science_major 4
%define libscience %mklibname science %{science_major}

%package -n %{libscience}
Summary:	Runtime library for KDE Education Application
Group:		System/Libraries

%description -n %{libscience}
libscience is a library that provides classes for chemical data.This library is
mainly used by kalzium.

%files -n %{libscience}
%{_kde_libdir}/libscience.so.%{science_major}*

#-----------------------------------------------------------------------------

%package devel
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	pkgconfig(eigen2) >= %{eigen_version}
Requires:	pkgconfig(openbabel-2.0)
Requires:	%{libscience} = %{version}-%{release}
Requires:	%{libcompoundviewer} = %{version}-%{release}
Conflicts:	kdeedu4-devel < 4.6.90

%description devel
Files needed to build applications based on %{name}.

%files devel
%{_kde_libdir}/libcompoundviewer.so
%{_includedir}/libkdeedu
%{_kde_libdir}/libscience.so

#----------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

