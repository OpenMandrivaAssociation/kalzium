%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

%define __noautoreq '^devel\\(libAvogadro.*$'


Summary:	Shows the periodic system of the elements
Name:		kalzium
Version:	18.08.1
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://edu.kde.org/kalzium
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
%ifnarch %{arm}
BuildRequires:	cmake(AvogadroLibs)
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
BuildRequires:	cmake(KF5NewStuff)
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
BuildRequires:	cmake(Qt5Quick)

Requires:	openbabel
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

%files -f all.lang
%doc COPYING COPYING.LIB COPYING.DOC
%{_sysconfdir}/xdg/kalzium.knsrc
%{_datadir}/applications/org.kde.kalzium.desktop
%{_datadir}/applications/org.kde.kalzium_cml.desktop
%{_bindir}/kalzium
%{_datadir}/metainfo/org.kde.kalzium.appdata.xml
%{_datadir}/config.kcfg/kalzium.kcfg
%{_datadir}/icons/*/*/*/*.*
%{_mandir}/man1/kalzium.1.*
%lang(ca) %{_mandir}/ca/man1/kalzium.1*
%lang(da) %{_mandir}/da/man1/kalzium.1*
%lang(de) %{_mandir}/de/man1/kalzium.1*
%lang(es) %{_mandir}/es/man1/kalzium.1*
%lang(et) %{_mandir}/et/man1/kalzium.1*
%lang(fr) %{_mandir}/fr/man1/kalzium.1*
%lang(gl) %{_mandir}/gl/man1/kalzium.1*
%lang(it) %{_mandir}/it/man1/kalzium.1*
%lang(nl) %{_mandir}/nl/man1/kalzium.1*
%lang(pl) %{_mandir}/pl/man1/kalzium.1*
%lang(pt) %{_mandir}/pt/man1/kalzium.1*
%lang(pt_BR) %{_mandir}/pt_BR/man1/kalzium.1*
%lang(ru) %{_mandir}/ru/man1/kalzium.1*
%lang(sv) %{_mandir}/sv/man1/kalzium.1*
%lang(uk) %{_mandir}/uk/man1/kalzium.1*
%{_datadir}/kalzium
%{_datadir}/kxmlgui5/kalzium
%{_datadir}/libkdeedu/data/*
%doc %{_docdir}/HTML/en/kalzium
%lang(ca) %doc %{_docdir}/HTML/ca/kalzium
%lang(de) %doc %{_docdir}/HTML/de/kalzium
%lang(es) %doc %{_docdir}/HTML/es/kalzium
%lang(fr) %doc %{_docdir}/HTML/fr/kalzium
%lang(gl) %doc %{_docdir}/HTML/gl/kalzium
%lang(it) %doc %{_docdir}/HTML/it/kalzium
%lang(nl) %doc %{_docdir}/HTML/nl/kalzium
%lang(pl) %doc %{_docdir}/HTML/pl/kalzium
%lang(pt) %doc %{_docdir}/HTML/pt/kalzium
%lang(pt_BR) %doc %{_docdir}/HTML/pt_BR/kalzium
%lang(ru) %doc %{_docdir}/HTML/ru/kalzium
%lang(sv) %doc %{_docdir}/HTML/sv/kalzium
%lang(uk) %doc %{_docdir}/HTML/uk/kalzium

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

#----------------------------------------------------------------------------
%ifnarch %{arm}

%define compoundviewer_major 5
%define libcompoundviewer %mklibname compoundviewer %{compoundviewer_major}

%package -n %{libcompoundviewer}
Summary:        Runtime library for KDE Education Application
Group:          System/Libraries

%description -n %{libcompoundviewer}
libcompoundviewer is a library that provides classes for chemical data. This 
library is mainly used by kalzium.

%files -n %{libcompoundviewer}
%{_libdir}/libcompoundviewer.so.%{compoundviewer_major}*

%endif
#-----------------------------------------------------------------------------

%package devel
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	pkgconfig(eigen3)
Requires:	pkgconfig(openbabel-2.0)
Requires:	%{libscience} = %{EVRD}
%ifnarch %{arm}
Requires:	%{libcompoundviewer} = %{EVRD}
%endif
Conflicts:	kdeedu4-devel < 4.6.90

%description devel
Files needed to build applications based on %{name}.

%files devel
%{_includedir}/libkdeedu
%{_libdir}/libscience.so
%{_libdir}/libcompoundviewer.so

#----------------------------------------------------------------------

%prep
%setup -q
%apply_patches
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name}
%find_lang plasma_applet_Molmasscalculator
%find_lang plasma_applet_concentrationCalculator
%find_lang plasma_applet_gasCalculator
%find_lang plasma_applet_kalzium
%find_lang plasma_applet_nuclearCalculator
%find_lang plasma_engine_kalzium
cat *.lang >all.lang
