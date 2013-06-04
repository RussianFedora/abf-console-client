Summary:        Console client for ABF (https://abf.rosalinux.ru)
Name:           abf-console-client
Version:        1.11.1
Release:        1%{?dist}

Group:          Development/Tools
License:        GPLv2
URL:            http://wiki.rosalab.ru/en/index.php/ABF_Console_Client
Source0:        %{name}-%{version}.tar.gz

Requires:       python-abf >= %{version}-%{release}
Requires:       python-beaker
Requires:       rpm-python
Requires:       git
Requires:       PyYAML
Requires:       python-magic
Requires:       tar >= 1.26

BuildArch:      noarch

%description
Console client for ABF (https://abf.rosalinux.ru). 


%package -n     python-abf
Summary:        Python API for ABF (https://abf.rosalinux.ru)
Group:          Development/Libraries
Provides:       python-abf = %{version}-%{release}

%description -n python-abf
%{name} is the python API to ABF (https://abf.rosalinux.ru).
It contains a set of basic operations, done with either HTML 
parsing or through ABF json API. It also provides datamodel to
operate with.


%prep
%setup -q -n %{name}

%build
# nothing to build

%install
rm -rf %{buildroot}
make install DESTDIR=$RPM_BUILD_ROOT
mv %{buildroot}%{_datadir}/bash-completion/abf %{buildroot}/%{_sysconfdir}/bash_completion.d/abf
rmdir %{buildroot}%{_datadir}/bash-completion/


%files
%defattr(-,root,root,-)
%doc README
%{python_sitelib}/abf/console/*
%{_bindir}/abf
%config(noreplace) %{_sysconfdir}/bash_completion.d/abf
%config(noreplace) %{_sysconfdir}/profile.d/abfcd.sh
%dir %{_sysconfdir}/abf/mock-urpm/configs/
%config(noreplace) %{_sysconfdir}/abf/mock-urpm/configs/*
%dir %{_localstatedir}/cache/abf/
%dir %{_localstatedir}/cache/abf/mock-urpm/
%dir %{_localstatedir}/lib/abf/mock-urpm/src
%dir %{_localstatedir}/lib/abf/
%dir %{_localstatedir}/lib/abf/mock-urpm


%files -n python-abf
%defattr(-,root,root,-)
%doc README
%{python_sitelib}/abf/*.py*
%{python_sitelib}/abf/api/*.py*


%changelog
* Tue Jun  4 2013 Arkady L. Shane <ashejn@russianfedora.ru> - 1.11.1-1.R
- update to 1.11.1

* Wed Feb 13 2013 Arkady L. Shane <ashejn@russianfedora.ru> - 1.9-1.R
- initial build
