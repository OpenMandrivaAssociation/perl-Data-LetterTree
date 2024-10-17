%define upstream_name	 Data-LetterTree
%define upstream_version 0.1

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	Native letter tree Perl binding 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/G/GR/GROUSSE/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	liblettertree-devel
BuildRequires:	perl-devel

%description
This module provides perl binding over a native implementation of a letter
tree, allowing to index any kind of perl scalar variable by a large set of
string with a reduced memory footprint over native perl hashes by sharing their
prefixes.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files 
%doc README Changes
%{perl_vendorarch}/Data
%{perl_vendorarch}/auto/Data
%{_mandir}/*/*

