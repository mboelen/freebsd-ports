# Created by: Peter Pentchev <roam@FreeBSD.org>
# $FreeBSD$

PORTNAME=	s5
PORTVERSION=	1.1
PORTREVISION=	2
CATEGORIES=	textproc
MASTER_SITES=	http://meyerweb.com/eric/tools/s5/v/${PORTVERSION}/
DISTNAME=	${PORTNAME}-${PORTVERSION:S/.//g}

MAINTAINER=	ports@FreeBSD.org
COMMENT=	Simple HTML-based presentation system

LICENSE=	BSD2CLAUSE

BUILD_DEPENDS=	unzip:${PORTSDIR}/archivers/unzip

USES=		dos2unix zip
DOS2UNIX_REGEX=	.*\.(css|htc|html|js|txt)
WRKSRC=		${WRKDIR}
NO_BUILD=	yes

S5_DIR=		${PREFIX}/share/${PORTNAME}
S5_SUBDIRS=	pix primer s5-blank ui

post-extract:
	cd ${WRKSRC} && ${TAR} -xf s5-blank.zip
	${SED} -e "s,/usr/local,${PREFIX}," ${FILESDIR}/s5.sh > ${WRKDIR}/s5
	${SED} -e "s,/usr/local,${PREFIX}," ${FILESDIR}/s5.1 > ${WRKDIR}/s5.1
	${FIND} ${WRKDIR} -type f -name .DS_Store -delete

do-install:
	${MKDIR} ${STAGEDIR}${S5_DIR}
	(cd ${WRKDIR} && \
		${COPYTREE_SHARE} "*.html ${S5_SUBDIRS}" ${STAGEDIR}${S5_DIR})
	${INSTALL_SCRIPT} ${WRKDIR}/s5 ${STAGEDIR}${PREFIX}/bin/s5
	${INSTALL_DATA} ${WRKDIR}/s5.1 ${STAGEDIR}${PREFIX}/man/man1/s5.1

.include <bsd.port.mk>
