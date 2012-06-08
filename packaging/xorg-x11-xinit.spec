Summary:   X.Org X11 X Window System xinit startup scripts
Name:      xorg-x11-xinit
Version:   1.1.0
Release:   1
License:   MIT/X11
Group:     User Interface/X
URL:       http://www.x.org

Source0:  %{name}-%{version}.tar.gz
Source1001: packaging/xorg-x11-xinit.manifest 

BuildRequires: pkgconfig
BuildRequires: libx11-devel
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: xorg-x11-util-macros
Requires: xauth

%description
X.Org X11 X Window System xinit startup scripts

%prep
%setup -q

%build
cp %{SOURCE1001} .
export CFLAGS="${CFLAGS} -D_F_EXIT_AFTER_XORG_AND_XCLIENT_LAUNCHED_"
./autogen.sh
./configure --prefix=%{_prefix}

make %{?jobs:-j%jobs}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT



%remove_docs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%manifest xorg-x11-xinit.manifest
%{_bindir}/xinit
%{_libdir}/X11/xinit/xinitrc

