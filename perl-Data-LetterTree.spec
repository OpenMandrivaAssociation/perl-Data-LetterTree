%define upstream_name	 Data-LetterTree
%define upstream_version 0.1

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Native letter tree Perl binding 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/G/GR/GROUSSE/%{upstream_name}-%{upstream_version}.tar.bz2

Buildrequires:  liblettertree-devel
Buildrequires:	perl-devel

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This module provides perl binding over a native implementation of a letter
tree, allowing to index any kind of perl scalar variable by a large set of
string with a reduced memory footprint over native perl hashes by sharing their
prefixes.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README Changes
%{perl_vendorarch}/Data
%{perl_vendorarch}/auto/Data
%{_mandir}/*/*
