Name:               loiq
Version:            0.3.1a
Release:            1%{?dist}.R
Summary:            LOIQ stands for Low Orbit Ion Cannon in Qt
Summary(ru):        LOIQ это аналог Low Orbit Ion Cannon на Qt

Source:             %{name}-%{version}.tar.bz2
Source1:            loiq.desktop
URL:                http://loiq.sourceforge.net/
Group:              Applications/Internet
License:            GPLv3

BuildRequires:      qt4-devel


%description
LOIQ stands for Low Orbit Ion Cannon in Qt. It is an attempt to port the famous
public-domain server stress-testing tool from C#/.Net to C++/Qt4, thus making it
available for the vast community of GNU/Linux users, as well as for the rest of
us *NIXoids.

%description -l ru
LOIQ это аналог Low Orbit Ion Cannon на Qt. Это попытка портировать известное
открытое средства для стресс-тестирования серверов с C#/.Net на C++/Qt4, и
сделать его доступным для широкого сообщества пользователей GNU/Linux, а
так же для всех *NIXoid'дов.


%prep
%setup -q
qmake-qt4 -o Makefile loiq.pro
make clean

%build
make %{?_smp_mflags}

%install
make INSTALL_ROOT=%{buildroot} INSTALL="install -p" CP="cp -p" install
install -D -m0644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop


%postun
update-desktop-database -q


%files 
%defattr(-,root,root,-)
%doc COPYING README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop


%changelog
* Tue Nov 22 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 1.3.1a-2.R
- Added description in russian language

* Fri Jul  8 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 0.3.1a-1.R
- initial build
