%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Shows the periodic system of the elements
Name:		kalzium
Version:	15.04.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://edu.kde.org/kalzium
Source0:	ftp://ftp.kde.org/pub/kde/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
%ifnarch %{arm}
BuildRequires:	pkgconfig(avogadro)
%endif
BuildRequires:	pkgconfig(eigen2)
BuildRequires:	pkgconfig(eigen3)
BuildRequires:	pkgconfig(openbabel-2.0)
BuildRequires:	chemical-mime-data
BuildRequires:	facile
BuildRequires:	ocaml
Requires:	libkdeedu = %{version}
Requires:	openbabel
%ifnarch %{arm}
Requires:	avogadro
%endif
Requires:	chemical-mime-data
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
%{_kde_applicationsdir}/kalzium.desktop
%{_kde_applicationsdir}/kalzium_cml.desktop
%{_kde_appsdir}/kalzium
%{_kde_appsdir}/libkdeedu/data/elements.xml
%{_kde_appsdir}/libkdeedu/data/isotopes.xml
%{_kde_appsdir}/libkdeedu/data/spectra.xml
%{_kde_appsdir}/libkdeedu/data/symbols.csv
%{_kde_appsdir}/libkdeedu/data/symbols2.csv
%{_kde_bindir}/kalzium
%{_kde_configdir}/kalzium.knsrc
%{_kde_datadir}/appdata/kalzium.appdata.xml
%{_kde_datadir}/config.kcfg/kalzium.kcfg
%{_kde_iconsdir}/hicolor/*/apps/kalzium.*
%{_kde_libdir}/kde4/concentrationCalculator.so
%{_kde_libdir}/kde4/gasCalculator.so
%{_kde_libdir}/kde4/nuclearCalculator.so
%{_kde_libdir}/kde4/plasma_applet_molmassCalculator.so
%{_kde_mandir}/man1/kalzium.1.*
%{_kde_services}/concentrationCalculator.desktop
%{_kde_services}/gasCalculator.desktop
%{_kde_services}/nuclearCalculator.desktop
%{_kde_services}/plasma-applet-Molmasscalculator.desktop

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
Requires:	pkgconfig(eigen2)
Requires:	pkgconfig(eigen3)
Requires:	pkgconfig(openbabel-2.0)
Requires:	%{libcompoundviewer} = %{EVRD}
Requires:	%{libscience} = %{EVRD}
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

%changelog
* Tue Nov 11 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.14.3-1
- New version 4.14.3

* Wed Oct 15 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.14.2-1
- New version 4.14.2

* Mon Sep 29 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.14.1-1
- New version 4.14.1
- Requires also eigen3 now
- Update files

* Tue Jul 15 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.13.3-1
- New version 4.13.3

* Wed Jun 11 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.13.2-1
- New version 4.13.2

* Wed Apr 02 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.12.4-1
- New version 4.12.4

* Wed Mar 12 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.12.3-2
- Don't require avogadro for arm because it's not ready yet there

* Tue Mar 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.12.3-1
- New version 4.12.3

* Tue Feb 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.12.2-1
- New version 4.12.2

* Tue Jan 14 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.12.1-1
- New version 4.12.1

* Wed Dec 04 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.11.4-1
- New version 4.11.4

* Wed Nov 06 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.11.3-1
- New version 4.11.3

* Wed Oct 02 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.11.2-1
- New version 4.11.2

* Tue Sep 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.11.1-1
- New version 4.11.1

* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.11.0-1
- New version 4.11.0

* Wed Jul 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.5-1
- New version 4.10.5

* Wed Jun 05 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.4-1
- New version 4.10.4

* Tue May 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.3-1
- New version 4.10.3

* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.1-1
- New version 4.10.1

* Thu Feb 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.0-1
- New version 4.10.0
- Add chemical-mime-data to BuildRequires and Requires
- Update files

* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.4-1
- New version 4.9.4

* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.3-1
- New version 4.9.3

* Thu Oct 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.2-1
- New version 4.9.2

* Sat Sep 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.1-1
- New version 4.9.1

* Tue Aug 14 2012 Andrey Bondrov <andrey.bonrov@rosalab.ru> 4.9.0-1
- New version 4.9.0

* Thu Jul 19 2012 Andrey Bondrov <andrey.bonrov@rosalab.ru> 4.8.97-1
- New version 4.8.97

* Tue Jul 03 2012 Andrey Bondrov <andrey.bonrov@rosalab.ru> 4.8.95-1
- New version 4.8.95

* Fri Jun 08 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 4.8.4-69.1mib2010.2
- New version 4.8.4
- MIB (Mandriva International Backports)

* Fri May 04 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 4.8.3-69.1mib2010.2
- New version 4.8.3
- MIB (Mandriva International Backports)

* Wed Apr 04 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 4.8.2-69.1mib2010.2
- New version 4.8.2
- MIB (Mandriva International Backports)

* Wed Mar 07 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 4.8.1-69.1mib2010.2
- New version 4.8.1
- MIB (Mandriva International Backports)

* Mon Feb 20 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 4.8.0-69.1mib2010.2
+ Revision: 762448
- Backport to 2010.2 for MIB users
- MIB (Mandriva International Backports)

* Thu Jan 19 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.8.0-1
+ Revision: 762448
- New upstream tarball

* Fri Jan 06 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.97-1
+ Revision: 758040
- New upstream tarball

* Thu Dec 22 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.95-1
+ Revision: 744523
- New upstream tarball

* Fri Dec 09 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.90-1
+ Revision: 739351
- New upstream tarball

* Sat Nov 19 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.80-1
+ Revision: 731867
- New upstream tarball 4.7.80

* Mon Nov 14 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.41-1
+ Revision: 730548
- Fix typo in URL
- Import package

