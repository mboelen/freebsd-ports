# Created by: TAOKA Fumiyoshi <fmysh@iijmio-mail.jp>
# $FreeBSD$

PORTNAME=	pyshapelib
PORTVERSION=	0.3
CATEGORIES=	devel python geography
MASTER_SITES=	http://ftp.intevation.de/users/bh/pyshapelib/:py \
		http://dl.maptools.org/dl/shapelib/:c
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}
DISTFILES=	${DISTNAME}${EXTRACT_SUFX}:py ${SHAPELIB}${EXTRACT_SUFX}:c

MAINTAINER=	fmysh@iijmio-mail.jp
COMMENT=	Python bindings for Shapelib

LICENSE=	LGPL20

USE_PYTHON=		yes
USE_PYDISTUTILS=	yes

SHAPELIB=	shapelib-1.2.10
USE_LDCONFIG=	yes

PORTDOCS=	NEWS README
PORTEXAMPLES=	pytest.py

OPTIONS_DEFINE=	DOCS EXAMPLES

post-extract:
	${LN} -s ${WRKDIR}/${SHAPELIB} ${WRKDIR}/shapelib

post-install:
	${MKDIR} ${STAGEDIR}${DOCSDIR}
.for f in ${PORTDOCS}
	${INSTALL_MAN} ${WRKSRC}/$f ${STAGEDIR}${DOCSDIR}
.endfor

	${MKDIR} ${STAGEDIR}${EXAMPLESDIR}
.for f in ${PORTEXAMPLES}
	${INSTALL_DATA} ${WRKSRC}/$f ${STAGEDIR}${EXAMPLESDIR}
.endfor

.include <bsd.port.mk>
