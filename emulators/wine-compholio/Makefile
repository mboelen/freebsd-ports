# Created by: Kris Moore <kmoore@FreeBSD.org>
# $FreeBSD$

COMMENT=	Wine built with the compholio patchset

SLAVE_PORT=	wine-devel

CONFLICTS=	wine-[0-9]* wine-devel-[0-9]*

OPTIONS_SET=	COMPHOLIO LIBXSLT MPG123 GNUTLS HAL V4L X11

MASTERDIR=	${.CURDIR}/../wine-devel
PLIST=		${MASTERDIR}/pkg-plist

.include "${MASTERDIR}/Makefile"

PKGNAMESUFFIX=	-compholio
