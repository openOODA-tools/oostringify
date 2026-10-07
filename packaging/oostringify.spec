Name:           oostringify
Version:        0.1.0
Release:        1%{?dist}
Summary:        Turns nested data structures into human-readable formatted terminal tables.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oostringify
Source0:        oostringify-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oostringify is a sovereign, capability-bounded DATA FORMATTER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oostringify
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oostringify-uninstall

%files
/usr/bin/oostringify
/usr/bin/oostringify-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
