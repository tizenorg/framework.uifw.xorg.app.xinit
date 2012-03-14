%define pkgname xinit

Summary:   X.Org X11 X Window System xinit startup scripts
Name:      xorg-app-%{pkgname}
Version:   1.1.0
Release:   4
License:   MIT/X11
Group:     User Interface/X
URL:       http://www.x.org

Source0:  ftp://ftp.x.org/pub/individual/app/%{pkgname}-%{version}.tar.gz

BuildRequires: pkgconfig
BuildRequires: pkgconfig(x11)
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: pkgconfig(xorg-macros)
Requires: xauth

%description
X.Org X11 X Window System xinit startup scripts

%prep
%setup -q -n %{pkgname}-%{version}

%build
export CFLAGS="${CFLAGS} -D_F_EXIT_AFTER_XORG_AND_XCLIENT_LAUNCHED_"
./autogen.sh
./configure --prefix=%{_prefix}

make %{?jobs:-j%jobs}


%install
%make_install

%docs_package

%files
%{_bindir}/xinit
%{_libdir}/X11/xinit/xinitrc

