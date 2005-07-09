%define	ruby_archdir	%(ruby -r rbconfig -e 'print Config::CONFIG["archdir"]')
%define ruby_rubylibdir %(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
%define	ruby_ridir	%(ruby -r rbconfig -e 'include Config; print File.join(CONFIG["datadir"], "ri", CONFIG["ruby_version"], "system")')
Summary:	Library to convert quantities in various units
Name:		ruby-Quanty
Version:	1.2
Release:	1
License:	Ruby's
Group:		Development/Languages
Source0:	http://www.ir.isas.ac.jp/~masa/ruby/dist/quanty-%{version}.tar.gz
# Source0-md5:	e802a3c5e919b7ef192ea81ec84725d8
Patch0:	%{name}-datadir.patch
URL:		http://www.ir.isas.ac.jp/~masa/ruby/index-e.html
BuildRequires:	ruby
BuildRequires:	ruby-devel
BuildRequires:	setup.rb
Requires:	ruby
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Quantity class containing "value" and "unit", providing automatic unit conversion and calculation. GNU/units data and Racc parser are employed.

%prep
%setup -q -n quanty-%{version}
%patch0 -p1

%build
cp %{_datadir}/setup.rb .

mkdir data/ruby/quanty -p
ruby mkdump.rb units.dump
mv units.dump data/ruby/quanty

ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc --op rdoc lib
rdoc --ri --op ri lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_ridir}}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc/*
%{ruby_rubylibdir}/*.rb
%{ruby_rubylibdir}/quanty
%{ruby_ridir}/Quanty
%{_datadir}/ruby/quanty
