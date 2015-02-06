%define upstream_name    Data-Section
%define upstream_version 0.101621

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Read multiple hunks of data out of your DATA section
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Data/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::ISA)
BuildRequires:	perl(MRO::Compat)
BuildRequires:	perl(Sub::Exporter)

BuildArch:	noarch

%description
Data::Section provides an easy way to access multiple named chunks of
line-oriented data in your module's DATA section. It was written to allow
modules to store their own templates, but probably has other uses.

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
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Mon May 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.101.621-1mdv2011.0
+ Revision: 662054
- update to new version 0.101621

* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 0.101.620-2
+ Revision: 658525
- rebuild for updated spec-helper

* Wed Jul 14 2010 Jérôme Quelin <jquelin@mandriva.org> 0.101.620-1mdv2011.0
+ Revision: 553088
- update to 0.101620

* Mon Mar 22 2010 Jérôme Quelin <jquelin@mandriva.org> 0.100.770-1mdv2010.1
+ Revision: 526436
- update to 0.100770

* Fri Jan 29 2010 Jérôme Quelin <jquelin@mandriva.org> 0.100.270-1mdv2010.1
+ Revision: 498066
- adding missing buildrequires:
- update to 0.100270

* Tue Dec 08 2009 Jérôme Quelin <jquelin@mandriva.org> 0.93.410-1mdv2010.1
+ Revision: 474740
- update to 0.093410

* Tue Dec 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.93.330-1mdv2010.1
+ Revision: 472240
- update to 0.093330

* Sun Jul 12 2009 Jérôme Quelin <jquelin@mandriva.org> 0.91.820-1mdv2010.0
+ Revision: 395132
- update to 0.091820
- using %%perl_convert_version
- fixed license field

* Fri Nov 07 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.005-1mdv2009.1
+ Revision: 300690
- import perl-Data-Section


* Fri Nov 07 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.005-1mdv2009.1
- initial mdv release, generated with cpan2dist

