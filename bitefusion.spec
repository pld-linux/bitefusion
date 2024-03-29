Summary:	A snake game
Summary(pl.UTF-8):	Gra typu wąż
Name:		bitefusion
Version:	1.0.2
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://www.junoplay.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	0d7fc10ad0d08f8f90de07fe3bcd8f26
URL:		http://www.junoplay.com/
BuildRequires:	SDL-devel >= 1.2
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A snake game with 15 levels. Great if you need to shut off your brain
for a few minutes and occupy your hands in the meantime. Guaranteed no
adrenaline rush!

%description -l pl.UTF-8
Gra typu wąż z 15 poziomami. Spróbuj wysilić swój umysł na parę minut
i w międzyczasie pracować rękami. Gwarantowana porządna dawka
adrenaliny!

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_bindir}/*
