#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	File
%define	pnam	NFSLock
Summary:	File::NFSLock - Perl module to do NFS (or not) locking
Summary(pl):	File::NFSLock - modu³ Perla do zak³adania (lub nie) blokad na NFS-ie
Name:		perl-File-NFSLock
Version:	1.20
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	68bddc5e2c32d9748ae689f398fc1147
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

%description -l pl
Program oparty jest na idei twardych dowi±zañ plików, bêd±cych
atomowymi po NFS-ie. Idea ta by³a wspomniana w Mail::Box::Locker
(oryginalnie zaprezentowanym w Mail::Folder::Maildir). Czê¶æ kodu jest
wziêta stamt±d - w szczególno¶ci pomys³ tworzenia losowego pliku
lokalnie, tworzenia twardego dowi±zania wspólnego pliku do pliku
lokalnego i nastêpnie sprawdzania stanu liczby dowi±zañ. Niektóre
pomys³y nie by³y kompletne (mechanizm uncache, blokowanie
wspó³dzielone), a niektóre by³y zakodowane niepoprawnie (z³y indeks
stat). File::NFSLock zosta³ napisany by byæ lekkim, ogólnym i szybkim.

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
