%define		_rel 0.1
Summary:	The JavaScript Minifier
Name:		jsmin
Version:	0
Release:	0.20070522.%{_rel}
License:	Freeware
Group:		Applications
Source0:	http://www.crockford.com/javascript/%{name}.c
# Source0-md5:	e764a543ec870d1ede2478236ecd7e98
URL:		http://javascript.crockford.com/jsmin.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JSMin is a filter which removes comments and unnecessary whitespace
from JavaScript files. It typically reduces filesize by half,
resulting in faster downloads. It also encourages a more expressive
programming style because it eliminates the download cost of clean,
literate self-documentation.

%prep
%setup -qcT
cp -a %{SOURCE0} .

%build
%{__cc} %{rpmcflags} jsmin.c -o jsmin

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install jsmin $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/jsmin
