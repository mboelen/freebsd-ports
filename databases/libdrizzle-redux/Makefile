# Created by: Jim Ohlstein <jim@ohlste.in>
# $FreeBSD$

PORTNAME=	libdrizzle
PORTVERSION=	5.1.4
PORTREVISION=	1
CATEGORIES=	databases
MASTER_SITES=	http://launchpadlibrarian.net/138246183/
PKGNAMESUFFIX=	-redux
DISTFILES=	${DISTNAME}${EXTRACT_SUFX}
EXTRACT_ONLY=	libdrizzle-5.1.4.tar.gz

MAINTAINER=	jim@ohlste.in
COMMENT=	Client and protocol library for the Drizzle database

LICENSE=	BSD2CLAUSE

GNU_CONFIGURE=	yes
USES=		gmake libtool
USE_LDCONFIG=	yes

CONFLICTS=	libdrizzle-[0-9]*

OPTIONS_DEFINE=	DOCS

.include <bsd.port.options.mk>

.if ${PORT_OPTIONS:MDOCS}
MASTER_SITES+=	http://launchpadlibrarian.net/138246206/
DISTFILES+=	libdrizzle.pdf
PLIST_SUB+=	PORTDOCS=""
.endif

post-install:
.if !empty(PORT_OPTIONS:MDOCS)
	${MKDIR} ${STAGEDIR}${DOCSDIR}
	${INSTALL_DATA} ${DISTDIR}/libdrizzle.pdf ${STAGEDIR}${DOCSDIR}
.endif

.include <bsd.port.mk>
