# Created by: J.R. Oldroyd <fbsd@opal.com>
# $FreeBSD$

PORTNAME=	libisofs
PORTVERSION=	1.3.6
PORTREVISION=	1
CATEGORIES=	devel
MASTER_SITES=	http://files.libburnia-project.org/releases/

MAINTAINER=	delphij@FreeBSD.org
COMMENT=	Libburnia ISO9660 filesystem creation library

LICENSE=	GPLv2
LICENSE_FILE=	${WRKSRC}/COPYING

LIB_DEPENDS=	libburn.so:${PORTSDIR}/devel/libburn

GNU_CONFIGURE=	yes
USES=		iconv libtool
USE_LDCONFIG=	yes

.include <bsd.port.mk>
