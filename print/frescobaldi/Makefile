# Created by: martin.dieringer@gmx.de
# $FreeBSD$

PORTNAME=	frescobaldi
PORTVERSION=	2.0.15
PORTREVISION=	2
CATEGORIES=	print kde
MASTER_SITES=	https://github.com/wbsoft/frescobaldi/releases/download/v${PORTVERSION}/

MAINTAINER=	martin.dieringer@gmx.de
COMMENT=	Music score editor for lilypond

LICENSE=	GPLv2 GPLv3
LICENSE_COMB=	dual

RUN_DEPENDS=	lilypond:${PORTSDIR}/print/lilypond \
		${PYTHON_PKGNAMEPREFIX}poppler-qt4>=0:${PORTSDIR}/graphics/py-poppler-qt4

USES=		gettext
INSTALLS_ICONS=	yes
USE_KDE4=	kdeprefix kdelibs pykde4_build pykde4_run
USE_PYTHON=	yes
USE_PYDISTUTILS=yes
PYDISTUTILS_AUTOPLIST=yes

post-patch:
	@${REINPLACE_CMD} '/install-script=frescobaldi-wininst.py/d' ${WRKSRC}/setup.cfg

.include <bsd.port.mk>
