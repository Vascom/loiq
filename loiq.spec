Summary:            LOIQ stands for Low Orbit Ion Cannon in Qt.
Name:               loiq
Version:            0.3.1a
Release:            1%{?dist}.R

Source:             %{name}-%{version}.tar.bz2
Source1:            loiq.desktop
URL:                http://loiq.sourceforge.net/
Group:              Applications/Network
License:            GPLv3

BuildRequires:      qt4-devel


%description
LOIQ stands for Low Orbit Ion Cannon in Qt. It is an attempt to port the famous
public-domain server stress-testing tool from C#/.Net to C++/Qt4, thus making it
available for the vast community of GNU/Linux users, as well as for the rest of
us *NIXoids.


%prep
%setup -q

%build
rm -f loiq
qmake-qt4 -o Makefile loiq.pro
make %{?_smp_mflags}

%install
rm -r %{buildroot}
make INSTALL_ROOT=%{buildroot} INSTALL="install -p" CP="cp -p" install
install -D -m0644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop
#rm -r %{buildroot}%{_docdir}/loiq
#rm -f %{buildroot}%{_infodir}/dir
#%find_lang %{name}


%post


%preun


%postun
update-desktop-database -q


%files 
#-f %{name}.lang
%defattr(-,root,root,-)
%doc COPYING README
#%doc doc/*.html doc/*.jpg doc/*.png
%{_bindir}/%{name}
#%{_mandir}/man1/%{name}.1*
#%{_infodir}/%{name}*
%{_datadir}/applications/%{name}.desktop


%changelog
* Fri Jul  8 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 0.3.1a-1.R
- initial build
