# Created by: Toshihiko SHIMOKAWA <toshi@tea.forus.or.jp> & ELISA Font Project
# $FreeBSD$

PORTNAME=	elisa8x8
PORTVERSION=	1.0
PORTREVISION=	4
CATEGORIES=	japanese x11-fonts
MASTER_SITES=	http://www.bsdbbq.org/~toshi/distfiles/
DISTNAME=	elisat10

MAINTAINER=	toshi@tea.forus.or.jp
COMMENT=	X11 8-dot Kanji font 'elisa font'

BUILD_DEPENDS=	bdftopcf:${PORTSDIR}/x11-fonts/bdftopcf \
		mkfontdir:${PORTSDIR}/x11-fonts/mkfontdir \
		mkfontscale:${PORTSDIR}/x11-fonts/mkfontscale

NO_WRKSUBDIR=	yes

BDFTOPCF_CMD=	${PREFIX}/bin/bdftopcf
MKFONTDIR_CMD=	${PREFIX}/bin/mkfontdir
FONTSDIR=	lib/X11/fonts/local
INSTALLDIR=	${PREFIX}/${FONTSDIR}
MYPORTDOCS=	elisa100.doc elisat10.doc elisat10.html
PLIST_SUB=	FONTSDIR=${FONTSDIR}

OPTIONS_DEFINE=	DOCS

do-build:
	@(cd ${WRKDIR}; \
	${BDFTOPCF_CMD} elisat10.bdf   | ${GZIP_CMD} -c > elisat10.pcf.gz ;\
	${BDFTOPCF_CMD} jpnhn4-jis.bdf | ${GZIP_CMD} -c > jpnhn4-jis.pcf.gz ;\
	${BDFTOPCF_CMD} jpnhn4-iso.bdf | ${GZIP_CMD} -c > jpnhn4-iso.pcf.gz ;\
	)

do-install:
	@${MKDIR} ${STAGEDIR}${INSTALLDIR}
	(cd ${WRKSRC} ;\
	${INSTALL_DATA} elisat10.pcf.gz ${STAGEDIR}${INSTALLDIR} ;\
	${INSTALL_DATA} jpnhn4-jis.pcf.gz ${STAGEDIR}${INSTALLDIR} ;\
	${INSTALL_DATA} jpnhn4-iso.pcf.gz ${STAGEDIR}${INSTALLDIR} ;\
	)

post-install:
	@${MKDIR} ${STAGEDIR}${DOCSDIR}
	${INSTALL_DATA} ${MYPORTDOCS:S,^,${WRKSRC}/,} ${STAGEDIR}${DOCSDIR}

.include <bsd.port.mk>
