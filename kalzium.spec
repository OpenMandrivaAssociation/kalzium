#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

%define __noautoreq '^devel\\(libAvogadro.*$'


Summary:	Shows the periodic system of the elements
Name:		kalzium
Version:	26.08.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://edu.kde.org/kalzium
Source1:	kalzium.rpmlintrc
%if 0%{?git:1}
Source0:	https://invent.kde.org/education/kalzium/-/archive/%{gitbranch}/kalzium-%{gitbranchd}.tar.bz2#/kalzium-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kalzium-%{version}.tar.xz
%endif
Patch0:		kalzium-ocaml-5.0.patch
# AvogadroLibs needs JKQTPlotter6 which is not in cooker currently
# BuildRequires:	cmake(AvogadroLibs)
BuildRequires:	pkgconfig(eigen3)
BuildRequires:	pkgconfig(openbabel-3)
BuildRequires:	pkgconfig(chemical-mime-data)
BuildRequires:	facile
BuildRequires:	ocaml
BuildRequires:	ocaml-compiler
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
BuildRequires:	cmake(Qt6OpenGLWidgets)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Core5Compat)
BuildRequires:	cmake(Qt6StateMachine)
BuildRequires:	cmake(Qt6Scxml)
# BuildRequires:	cmake(JKQTPlotter6)  # not in cooker currently
BuildRequires:	pkgconfig(glu)

Requires:	chemical-mime-data
Requires:	ocaml
Conflicts:	cantor < 4.6.90
Conflicts:	kdeedu4-core < 4.6.90
Obsoletes:	plasma-engine-kalzium < %{EVRD}
Obsoletes:	plasma-applet-didyouknow < %{EVRD}

%rename plasma6-kalzium

BuildSystem:	cmake
BuildOption:	-DBUILD_PYTHON_BINDINGS:BOOL=OFF
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
BuildOption:	-DQT_MAJOR_VERSION=6
BuildOption:	-DCMAKE_DISABLE_FIND_PACKAGE_JKQTPlotter6=ON
BuildOption:	-DCMAKE_DISABLE_FIND_PACKAGE_AvogadroLibs=ON

%description
Kalzium is an application which will show you some information about the
periodic system of the elements. Therefore you could use it as an
information database.


%install -a
# Optional features may be absent when Avogadro/JKQT are disabled
: > kalzium-optional.files
for f in %{buildroot}%{_libdir}/libcompoundviewer.so*; do
	[ -e "$f" ] && echo "${f#%{buildroot}}" >> kalzium-optional.files
done
if [ -e %{buildroot}%{_datadir}/knsrcfiles/kalzium.knsrc ]; then
	echo "%{_datadir}/knsrcfiles/kalzium.knsrc" >> kalzium-optional.files
fi
if [ -e %{buildroot}%{_datadir}/libkdeedu/data ]; then
	echo "%{_datadir}/libkdeedu/data/*" >> kalzium-optional.files
fi

%files -f kalzium.lang -f kalzium-optional.files
# No headers for this library -- so splitting it and having -devel
# doesn't make sense
%{_datadir}/applications/org.kde.kalzium.desktop
%{_datadir}/applications/org.kde.kalzium_cml.desktop
%{_bindir}/kalzium
%{_datadir}/metainfo/org.kde.kalzium.appdata.xml
%{_datadir}/config.kcfg/kalzium.kcfg
%{_datadir}/icons/*/*/*/*.*
%{_mandir}/man1/kalzium.1.*
%{_datadir}/kalzium
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
