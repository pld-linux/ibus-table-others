Summary:	Various tables for IBus Table engine
Summary(pl.UTF-8):	Różne tablice dla silnika IBus Table
Name:		ibus-table-others
Version:	1.3.0.20100907
Release:	1
License:	GPL v3
Group:		Libraries
Source0:	http://nkumar.fedorapeople.org/ibus-table-others/%{name}-%{version}.tar.bz2
# Source0-md5:	a6866d910853038a20c5c0b0dea8ee0c
Patch0:		%{name}-emoji.patch
URL:		http://github.com/moebiuscurve/ibus-table-others
BuildRequires:	ibus-table-devel >= 1.2.0
Requires:	ibus-table >= 1.2.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ibus-table-others contains various IBus-Tables which include languages
of Latin-America, Europe, Southeast Asia, as well as math and other
symbols. The actual tables are in individual ibus-table-* packages.

%description -l pl.UTF-8
ibus-table-others zawiera różne tablice dla silnika IBus Table,
obejmujące języki Ameryki Łacińskiej, Europy, Azji
Południowo-Wschodniej, a także symbole matematyczne i inne. Właściwe
tablice są w poszczególnych pakietach ibus-table-*.

%package -n ibus-table-code
Summary:	Ibus-Tables for LaTeX, CNS11643 & Emoji
Summary(pl.UTF-8):	Tablice IBus Table dla LaTeXa, CNS11643 i Emoji
Group:		Libraries
Requires:	ibus-table >= 1.2.0

%description -n ibus-table-code
The package contains ibus-tables for LaTeX, CNS11643, Emoji.

%description -n ibus-table-code -l pl.UTF-8
Ten pakiet zawiera tablice IBus Table dla LaTeXa, CNS11643 i Emoji.

%package -n ibus-table-cyrillic
Summary:	Ibus-Tables for Cyrillic
Summary(pl.UTF-8):	Tablice IBus Table dla cyrylicy
Group:		Libraries
Requires:	ibus-table >= 1.2.0

%description -n ibus-table-cyrillic
The Cyrillic rustrad & yawerty tables for IBus Table.

%description -n ibus-table-cyrillic -l pl.UTF-8
Tablice cyrylicy rustrad i yawerty dla silnika IBus Table.

%package -n ibus-table-latin
Summary:	Ibus-Tables for Latin
Summary(pl.UTF-8):	Tablice IBus Table dla łacinki
Group:		Libraries
Requires:	ibus-table >= 1.2.0

%description -n ibus-table-latin
The Latin compose & ipa-x-sampa tables for Ibus-Table.

%description -n ibus-table-latin -l pl.UTF-8
Tablice łacińskie compose oraz ipa-x-sampa dla silnika IBus Table.

%package -n ibus-table-mathwriter
Summary:	Ibus-Tables for Unicode mathematics symbols
Summary(pl.UTF-8):	Tablice IBus Table dla unikodowych symboli matematycznych
Group:		Libraries
Requires:	ibus-table >= 1.2.0

%description -n ibus-table-mathwriter
The package contains IBus Table for writing Unicode mathematics
symbols.

%description -n ibus-table-mathwriter -l pl.UTF-8
Ten pakiet zawiera tablicę IBus Table do pisania przy użyciu
unikodowych symboli matematycznych.

%package -n ibus-table-translit
Summary:	Ibus-Tables for Russian Translit
Summary(pl.UTF-8):	Tablice IBus Table dla transliteracji rosyjskiej
Group:		Libraries
Requires:	ibus-table >= 1.2.0

%description -n ibus-table-translit
The Cyrillic translit & translit-ua tables for IBus-Table.

%description -n ibus-table-translit -l pl.UTF-8
Tablice cyrylicy translit i translit-ua dla silnika IBus Table.

%package -n ibus-table-tv
Summary:	Ibus-Tables for Thai and Viqr (Vietnamese)
Summary(pl.UTF-8):	Tablice IBus Table dla tajskiego i wietnamskiego
Group:		Libraries
Requires:	ibus-table >= 1.2.0

%description -n ibus-table-tv
The Thai and Viqr (Vietnamese) tables for IBus-Table.

%description -n ibus-table-tv -l pl.UTF-8
Tablice tajska i Viqr (wietnamska) dla silnika IBus Table.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--enable-cns11643 \
	--enable-compose \
	--enable-emoji \
	--enable-ipaxsampa \
	--enable-latex \
	--enable-rustrad \
	--enable-thai \
	--enable-translit \
	--enable-translitua \
	--enable-viqr \
	--enable-yawerty \
	--enable-mathwriter

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

for db in $RPM_BUILD_ROOT%{_datadir}/ibus-table/tables/*.db ; do
	%{_bindir}/ibus-table-createdb -i -n $db
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README

%files -n ibus-table-code
%defattr(644,root,root,755)
%{_datadir}/ibus-table/tables/latex.db
%{_datadir}/ibus-table/tables/cns11643.db
%{_datadir}/ibus-table/tables/emoji-table.db
%{_datadir}/ibus-table/icons/latex.svg
%{_datadir}/ibus-table/icons/cns11643.png
%{_datadir}/ibus-table/icons/ibus-emoji.svg

%files -n ibus-table-cyrillic
%defattr(644,root,root,755)
%{_datadir}/ibus-table/tables/rustrad.db
%{_datadir}/ibus-table/tables/yawerty.db
%{_datadir}/ibus-table/icons/rustrad.png
%{_datadir}/ibus-table/icons/yawerty.png

%files -n ibus-table-latin
%defattr(644,root,root,755)
%{_datadir}/ibus-table/tables/compose.db
%{_datadir}/ibus-table/tables/ipa-x-sampa.db
%{_datadir}/ibus-table/icons/compose.svg
%{_datadir}/ibus-table/icons/ipa-x-sampa.png

%files -n ibus-table-mathwriter
%defattr(644,root,root,755)
%{_datadir}/ibus-table/tables/mathwriter-ibus.db
%{_datadir}/ibus-table/icons/mathwriter.png

%files -n ibus-table-translit
%defattr(644,root,root,755)
%{_datadir}/ibus-table/tables/translit.db
%{_datadir}/ibus-table/tables/translit-ua.db
%{_datadir}/ibus-table/icons/translit.png
%{_datadir}/ibus-table/icons/translit-ua.png

%files -n ibus-table-tv
%defattr(644,root,root,755)
%{_datadir}/ibus-table/tables/thai.db
%{_datadir}/ibus-table/tables/viqr.db
%{_datadir}/ibus-table/icons/thai.png
%{_datadir}/ibus-table/icons/viqr.png
