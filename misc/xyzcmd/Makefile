# Created by: Veniamin Gvozdikov <vg@FreeBSD.org>
# $FreeBSD$

PORTNAME=	xyzcmd
PORTVERSION=	0.0.5
CATEGORIES=	misc python
MASTER_SITES=	GOOGLE_CODE

MAINTAINER=	vg@FreeBSD.org
COMMENT=	Pure console visual file manager

LICENSE=	LGPL3

BUILD_DEPENDS=	${PYTHON_SITELIBDIR}/urwid/raw_display.py:${PORTSDIR}/devel/py-urwid
RUN_DEPENDS=	${PYTHON_SITELIBDIR}/urwid/raw_display.py:${PORTSDIR}/devel/py-urwid

USE_PYTHON=	yes
USE_PYDISTUTILS=yes
INSTALLS_EGGINFO=yes
USES=		tar:bzip2

OPTIONS_DEFINE=	DOCS

post-install:
	@${MKDIR} ${STAGEDIR}${DOCSDIR}
	cd ${WRKSRC}/doc && ${COPYTREE_SHARE} api ${STAGEDIR}${DOCSDIR} && \
		${COPYTREE_SHARE} user-manual ${STAGEDIR}${DOCSDIR} && \
		${INSTALL_DATA} ../ChangeLog overview.pdf ${STAGEDIR}${DOCSDIR}

.include <bsd.port.mk>
