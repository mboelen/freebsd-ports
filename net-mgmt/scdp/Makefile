# Created by: arved@FreeBSD.org
# $FreeBSD$

PORTNAME=	scdp
PORTVERSION=	1.0.b
PORTREVISION=	3
CATEGORIES=	net-mgmt
MASTER_SITES=	SF/${PORTNAME}/${PORTNAME}/1.0b
DISTNAME=	scdp-${PORTVERSION:S/.b/b/}

MAINTAINER=	arved@FreeBSD.org
COMMENT=	Tool that sends CDP (CISCO Discovery Protocol) Packets

DEPRECATED=	Depends on expired net/libnet10
EXPIRATION_DATE=	2014-09-30

BUILD_DEPENDS=	${LIBNET_CONFIG}:${PORTSDIR}/net/libnet10

LICENSE=	GPLv2

USES=		gmake
GNU_CONFIGURE=	yes
CONFIGURE_ENV=	libnet_config="${LIBNET_CONFIG}"
CFLAGS+=	`${LIBNET_CONFIG} --cflags`
PLIST_FILES=	bin/scdp

LIBNET_CONFIG?=	${LOCALBASE}/bin/libnet10-config

post-patch:
	${REINPLACE_CMD} -e 's,malloc.h,stdlib.h,' ${WRKSRC}/scdp.c
	${REINPLACE_CMD} -e 's|libnet-config|${LIBNET_CONFIG}|' \
		${CONFIGURE_WRKSRC}/${CONFIGURE_SCRIPT}

.include <bsd.port.mk>
