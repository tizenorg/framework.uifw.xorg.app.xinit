%define _unpackaged_files_terminate_build 0

Summary:   X.Org X11 X Window System xinit startup scripts
Name:      xorg-x11-xinit
Version:   1.4.5
Release:   5
VCS:       framework/uifw/xorg/app/xinit#REBASE-11-gf137e6d3cf419ecb36561df4d542550e10b9cb18
License:   MIT
Group:     User Interface/X
URL:       http://www.x.org

Source: %{name}-%{version}.tar.gz
#Source0:  ftp://ftp.x.org/pub/individual/app/%{pkgname}-%{version}.tar.bz2
#Source10: xinitrc-common
#Source11: xinitrc
#Source12: Xclients
#Source13: Xmodmap
#Source14: Xresources
# NOTE: Xsession is used by xdm/kdm/gdm and possibly others, so we keep it
#       here instead of the xdm package.
#Source16: Xsession
#Source17: localuser.sh
#Source18: xinit-compat.desktop
#Source19: xinit-compat

# Fedora specific patches

#Patch1: xinit-1.0.2-client-session.patch
#Patch3: xinit-1.0.9-unset.patch

BuildRequires: pkgconfig
BuildRequires: libX11-devel
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: dbus-devel
BuildRequires: libtool
BuildRequires: xorg-x11-xutils-dev
# NOTE: startx needs xauth in order to run, but that is not picked up
#       automatically by rpm.  (Bug #173684)
#Requires: xorg-x11-xauth
# next two are for localuser.sh
#Requires: coreutils
Requires: xorg-x11-server-utils
Requires: xkeyboard-config

%package session
Summary: Display manager support for ~/.xsession and ~/.Xclients
Group: User Interface/X

%description
X.Org X11 X Window System xinit startup scripts

%description session
Allows legacy ~/.xsession and ~/.Xclients files to be used from display managers

%prep
%setup -q
#%setup -q -n %{pkgname}-%{version}
#%patch1 -p1 -b .client-session
#%patch3 -p1 -b .unset

%build
autoreconf
./configure --prefix=%{_prefix} CFLAGS="${CFLAGS} -g -D_F_EXIT_AFTER_XORG_AND_XCLIENT_LAUNCHED_ -D_F_LAUNCH_WM_AFTER_LAUNCHING_SERVER_ -D_F_SET_DELAY_TIME_TO_WAIT_SERVER_ "

# FIXME: Upstream should default to XINITDIR being this.  Make a patch to
# Makefile.am and submit it in a bug report or check into CVS.
make %{?jobs:-j%jobs} XINITDIR=%{_sysconfdir}/X11/xinit

%install
# FIXME: Upstream should default to XINITDIR being this.  Make a patch to
# Makefile.am and submit it in a bug report or check into CVS.
#make install DESTDIR=$RPM_BUILD_ROOT XINITDIR=%{_sysconfdir}/X11/xinit
#install -p -m644 -D %{SOURCE18} $RPM_BUILD_ROOT%{_datadir}/xsessions/xinit-compat.desktop
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/usr/share/license
cp -af COPYING %{buildroot}/usr/share/license/%{name}
make install DESTDIR=$RPM_BUILD_ROOT

# Install Red Hat custom xinitrc, etc.
#{
#    mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/X11/xinit
#
#    install -p -m 644 %{SOURCE10} $RPM_BUILD_ROOT%{_sysconfdir}/X11/xinit/xinitrc-common
#
#    for script in %{SOURCE11} %{SOURCE12} %{SOURCE16} ; do
#        install -p -m 755 $script $RPM_BUILD_ROOT%{_sysconfdir}/X11/xinit/${script##*/}
#    done
#
#    install -p -m 644 %{SOURCE13} $RPM_BUILD_ROOT%{_sysconfdir}/X11/Xmodmap
#    install -p -m 644 %{SOURCE14} $RPM_BUILD_ROOT%{_sysconfdir}/X11/Xresources
#
#    mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/X11/xinit/xinitrc.d
#    install -p -m 755 %{SOURCE17} $RPM_BUILD_ROOT%{_sysconfdir}/X11/xinit/xinitrc.d/localuser.sh
#
#    mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/X11/xinit/Xclients.d
#
#    mkdir -p $RPM_BUILD_ROOT%{_libexecdir}
#    install -p -m 755 %{SOURCE19} $RPM_BUILD_ROOT%{_libexecdir}
#}

%remove_docs

%files
%manifest xinit.manifest
%defattr(-,root,root,-)
/usr/share/license/%{name}
#%doc COPYING README ChangeLog
#%{_bindir}/startx
%{_bindir}/xinit
#%dir %{_sysconfdir}/X11/xinit
#%{_sysconfdir}/X11/xinit/xinitrc
#%{_sysconfdir}/X11/xinit/xinitrc-common
#%config(noreplace) %{_sysconfdir}/X11/Xmodmap
#%config(noreplace) %{_sysconfdir}/X11/Xresources
#%dir %{_sysconfdir}/X11/xinit/Xclients.d
#%{_sysconfdir}/X11/xinit/Xclients
#%{_sysconfdir}/X11/xinit/Xsession
#%dir %{_sysconfdir}/X11/xinit/xinitrc.d
#%{_sysconfdir}/X11/xinit/xinitrc.d/*
#%{_mandir}/man1/startx.1*
#%{_mandir}/man1/xinit.1*

#%files session
#%defattr(-, root, root,-)
#%{_libexecdir}/xinit-compat
#%{_datadir}/xsessions/xinit-compat.desktop
