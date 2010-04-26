Summary:	The JavaScript Minifier
Summary(pl.UTF-8):	Zmniejszacz JavaScriptu
Name:		jsmin
Version:	20080803
Release:	1
License:	Freeware
Group:		Development/Tools
Source0:	http://www.crockford.com/javascript/%{name}.c
# Source0-md5:	8847fd99576468d6c9e76420da0b6b55
URL:		http://javascript.crockford.com/jsmin.html
BuildRequires:	rpmbuild(macros) >= 1.553
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JSMin is a filter which removes comments and unnecessary whitespace
from JavaScript files. It typically reduces filesize by half,
resulting in faster downloads. It also encourages a more expressive
programming style because it eliminates the download cost of clean,
literate self-documentation.

%description -l pl.UTF-8
JSMin to filtr usuwający komentarze i zbędne odstępy z plików w
JavaScripcie. Zwykle zmniejsza rozmiar pliku o połowę, co skutkuje
szybszym ściąganiem. Zachęca także do bardziej ekspresywnego stylu
programowania, ponieważ eliminuje koszt ściągania czystego,
samodokumentującego się kodu.

%prep
%setup -qcT
cp -a %{SOURCE0} .
%undos *.c

version=$(sed -n 2p jsmin.c | xargs)
if [ "$(echo "$version" | tr -d -)" != %{version} ]; then
	: %%{version} mismatch
	exit 1
fi

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
