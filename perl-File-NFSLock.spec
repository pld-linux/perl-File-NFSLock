#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define	pdir	File
%define	pnam	NFSLock
Summary:	File::NFSLock - Perl module to do NFS (or not) locking
Summary(pl.UTF-8):	File::NFSLock - moduł Perla do zakładania (lub nie) blokad na NFS-ie
Name:		perl-File-NFSLock
Version:	1.21
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8067802ce7247d0697d6203e26cb7bd7
URL:		http://search.cpan.org/dist/File-NFSLock/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Program based of concept of hard linking of files being atomic across
NFS. This concept was mentioned in Mail::Box::Locker (which was
originally presented in Mail::Folder::Maildir). Some routine flow is
taken from there - particularly the idea of creating a random local
file, hard linking a common file to the local file, and then checking
the nlink status. Some ideologies were not complete (uncache
mechanism, shared locking) and some coding was even incorrect (wrong
stat index). File::NFSLock was written to be light, generic, and fast.

%description -l pl.UTF-8
Program oparty jest na idei twardych dowiązań plików, będących
atomowymi po NFS-ie. Idea ta była wspomniana w Mail::Box::Locker
(oryginalnie zaprezentowanym w Mail::Folder::Maildir). Część kodu jest
wzięta stamtąd - w szczególności pomysł tworzenia losowego pliku
lokalnie, tworzenia twardego dowiązania wspólnego pliku do pliku
lokalnego i następnie sprawdzania stanu liczby dowiązań. Niektóre
pomysły nie były kompletne (mechanizm uncache, blokowanie
współdzielone), a niektóre były zakodowane niepoprawnie (zły indeks
stat). File::NFSLock został napisany by być lekkim, ogólnym i szybkim.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/File/*.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
