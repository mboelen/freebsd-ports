# Created by: Gasol Wu <gasol.wu@gmail.com>
# $FreeBSD$

PORTNAME=	PHP_PMD
PORTVERSION=	1.4.1
CATEGORIES=	devel pear
MASTER_SITES=	http://pear.phpmd.org/get/
PKGNAMEPREFIX=	pear-

MAINTAINER=	gasol.wu@gmail.com
COMMENT=	PHP Mess Detector

LICENSE=	BSD

BUILD_DEPENDS=	${PEARDIR}/.channels/pear.phpmd.org.reg:${PORTSDIR}/devel/pear-channel-phpmd
RUN_DEPENDS=	${PEARDIR}/.channels/pear.phpmd.org.reg:${PORTSDIR}/devel/pear-channel-phpmd

USES=	pear
PEAR_CHANNEL=	phpmd
USE_PHP=	dom simplexml

.include <bsd.port.mk>
