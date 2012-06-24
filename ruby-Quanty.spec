Summary:	Library to convert quantities in various units
Summary(pl.UTF-8):	Biblioteka do przeliczania wielkości w różnych jednostkach
Name:		ruby-Quanty
Version:	1.2
Release:	2
License:	Ruby's
Group:		Development/Languages
Source0:	http://www.ir.isas.ac.jp/~masa/ruby/dist/quanty-%{version}.tar.gz
# Source0-md5:	e802a3c5e919b7ef192ea81ec84725d8
Patch0:		%{name}-datadir.patch
URL:		http://www.ir.isas.ac.jp/~masa/ruby/index-e.html
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
BuildRequires:	setup.rb
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Quantity class containing "value" and "unit", providing automatic
unit conversion and calculation. GNU/units data and Racc parser are
employed.

%description -l pl.UTF-8
Klasa Quantity zawiera "value" i "unit", udostępniające automatyczną
konwersję i przeliczanie jednostek. Używane są dane GNU/units oraz
parser Racc.

%prep
%setup -q -n quanty-%{version}
%patch0 -p1
cp %{_datadir}/setup.rb .

mkdir -p data/ruby/quanty

%build
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

cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc/*
%{ruby_rubylibdir}/*.rb
%{ruby_rubylibdir}/quanty
%{ruby_ridir}/Quanty
%{_datadir}/ruby/quanty
