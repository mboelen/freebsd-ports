# $FreeBSD$

PORTNAME=	mpd
PORTVERSION=	0.1
CATEGORIES=	audio
PKGNAMEPREFIX=	${LUA_PKGNAMEPREFIX}

MAINTAINER=	demelier.david@gmail.com
COMMENT=	Lua library for musicpd

RUN_DEPENDS=	${LUA_MODLIBDIR}/socket/core.so:${PORTSDIR}/net/luasocket

OPTIONS_DEFINE=	DOCS
DOCSDIR=	${PREFIX}/share/doc/${UNIQUENAME}

GH_ACCOUNT=	silentbicycle
GH_PROJECT=	lua-mpd
GH_TAGNAME=	v0.1

USES=		lua:51
USE_GITHUB=	yes
NO_BUILD=	yes

WRKSRC=		${WRKDIR}/${GH_ACCOUNT}-lua-${PORTNAME}-ca32f43

do-install:
	@${MKDIR} ${STAGEDIR}${LUA_MODSHAREDIR}
	${INSTALL_DATA} ${WRKSRC}/mpd.lua ${STAGEDIR}${LUA_MODSHAREDIR}
	@${MKDIR} ${STAGEDIR}${DOCSDIR} ${STAGEDIR}${DOCSDIR}/modules ${STAGEDIR}${DOCSDIR}/files
	${INSTALL_DATA} ${WRKSRC}/index.html ${STAGEDIR}${DOCSDIR}
	${INSTALL_DATA} ${WRKSRC}/luadoc.css ${STAGEDIR}${DOCSDIR}
	${INSTALL_DATA} ${WRKSRC}/files/mpd.html ${STAGEDIR}${DOCSDIR}/files
	${INSTALL_DATA} ${WRKSRC}/modules/mpd.html ${STAGEDIR}${DOCSDIR}/modules

.include <bsd.port.mk>
