%define module	Data-LetterTree
%define name	perl-%{module}
%define version 0.1
%define release %mkrel 3

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Native letter tree Perl binding 
License:	GPL or Artistic
Group:		Development/Perl
Source:		http://search.cpan.org/CPAN/authors/id/G/GR/GROUSSE/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}/
Buildrequires:	perl-devel
Buildrequires:  liblettertree-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This module provides perl binding over a native implementation of a letter
tree, allowing to index any kind of perl scalar variable by a large set of
string with a reduced memory footprint over native perl hashes by sharing their
prefixes.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%check
%{__make} test

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README Changes
%{perl_vendorarch}/Data
%{perl_vendorarch}/auto/Data
%{_mandir}/*/*

