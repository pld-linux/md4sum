Summary:	Generate or check MD4 message digests
Summary(pl.UTF-8):   Generowanie i sprawdzanie skrótów MD4
Name:		md4sum
Version:	0.02.01
Release:	1
License:	GPL
Group:		Applications/File
Source0:	ftp://ibiblio.org/pub/Linux/utils/file/%{name}-%{version}.tar.gz
# Source0-md5:	f8c060c61231429f0efb7860da1423f6
Patch0:		%{name}-Makefile.patch
URL:		http://linux.xulin.de/c/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
md4sum is a small utility used to generate or check MD4 message 
digests. It can be used also for ed2k links.

%description -l pl.UTF-8
md4sum jest to małe narzędzie służące do generowania lub sprawdzania 
skrótów MD4. Może także posłużyć do zarządzania odnośnikami ed2k.

%prep
%setup -q
%patch0 -p1

%build
./configure
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install md4sum $RPM_BUILD_ROOT%{_bindir}
install md4sum.1  $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
