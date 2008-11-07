
%define module   Data-Section
%define version    0.005
%define release    %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    read multiple hunks of data out of your DATA section
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Data/%{module}-%{version}.tar.gz
BuildRequires: perl(Class::ISA)
BuildRequires: perl(Sub::Exporter)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Data::Section provides an easy way to access multiple named chunks of
line-oriented data in your module's DATA section. It was written to allow
modules to store their own templates, but probably has other uses.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*

