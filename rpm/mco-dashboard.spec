%define name              mco-dashboard
%define summary           MCollective Web Dashboard
%define license           MIT License
%define group             Applications/System
%define url               https://github.com/mmornati/mco-dashboard
%define packager          Marco Mornati

Name:      %{name}
Summary:   %{summary}
Version:   %{version}
Release:   %{release}
License:   %{license}
Group:     %{group}
Source:    %{name}-%{version}.tar.gz
BuildArch: %{arch}
Provides:  %{name}
URL:       %{url}
Buildroot: %{buildroot}

%description
%{summary}

%prep
%setup -q -n %{name}

%install
%{__mkdir} -p $RPM_BUILD_ROOT/usr/share/mco-dashboard

%{__cp} -R * $RPM_BUILD_ROOT/usr/share/mco-dashboard

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%attr(0755,root,root) %dir /usr/share/mco-dashboard
/usr/share/mco-dashboard/*
#%config /etc/sysconfing/mco-dashboard

