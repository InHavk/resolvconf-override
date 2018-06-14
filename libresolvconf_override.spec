Summary: Library to override DNS settings
Name: libresolvconf-override
Version: 1.0
Release: 1%{?dist}
License: GNU LGPL v2.1
VCS:        {{{ git_vcs }}}

Source: {{{ git_pack }}}

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool

%description
The shared library overrides the gethostbyname(), getaddrinfo() and res_init() system calls. It does not support IPv6, and might be lacking particular system calls overrides for all applications to work as expected.

%prep
{{{ git_setup_macro }}}

%build
cd $RPM_BUILD_DIR/-
./autogen.sh --prefix="/usr"
make

%install
cd $RPM_BUILD_DIR/-
make install DESTDIR=$RPM_BUILD_ROOT

%clean
cd $RPM_BUILD_DIR/-
make clean

%files
/usr/lib/libresolvconf_override.so

%post

%preun

%postun

%changelog
{{{ git_changelog }}}
