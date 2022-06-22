Name:       python3-distro
Summary:    Provides information about the OS distribution it runs on
Version:    1.5.0
Release:    1
License:    ASL 2.0
URL:        https://github.com/sailfishos/python3-distro
BuildArch:  noarch
Source0:    %{name}-%{version}.tar.bz2
Requires:   python3-base
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
distro provides information about the OS distribution it runs on,
such as a reliable machine-readable ID, or version information.

It is the recommended replacement for Python's original
platform.linux_distribution function (which will be removed in
Python 3.8). It also provides much more functionality which isn't
necessarily Python bound, like a command-line interface.

%package tools
Summary:    PulseAudio components needed for starting x11 User session
Requires:   %{name} = %{version}-%{release}

%description tools
Command-line interface to distro.

%prep
%setup -q -n %{name}-%{version}/distro

%build
%{py3_build}

%install
rm -rf %{buildroot}
%{py3_install}

%files
%defattr(-,root,root,-)
%{python3_sitelib}/distro.py
%{python3_sitelib}/distro-*.egg-info
%{python3_sitelib}/__pycache__/*

%files tools
%defattr(-,root,root,-)
%{_bindir}/distro
