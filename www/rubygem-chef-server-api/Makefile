# Created by: Scott Sanders <scott@jssjr.com>
# $FreeBSD$

PORTNAME=	chef-server-api
PORTVERSION=	10.30.2
CATEGORIES=	www rubygems
MASTER_SITES=	RG

MAINTAINER=	ruby@FreeBSD.org
COMMENT=	Systems integration framework. Server API

LICENSE=	APACHE20

RUN_DEPENDS=	rubygem-dep_selector>=0.0.3:${PORTSDIR}/devel/rubygem-dep_selector \
		rubygem-extlib>=0.9.16:${PORTSDIR}/devel/rubygem-extlib \
		rubygem-merb-assets>=1.1.0:${PORTSDIR}/www/rubygem-merb-assets \
		rubygem-merb-core>=1.1.0:${PORTSDIR}/www/rubygem-merb-core \
		rubygem-merb-helpers>=1.1.0:${PORTSDIR}/www/rubygem-merb-helpers \
		rubygem-merb-param-protection>=1.1.0:${PORTSDIR}/www/rubygem-merb-param-protection \
		rubygem-mixlib-authentication>=1.1.3:${PORTSDIR}/devel/rubygem-mixlib-authentication \
		rubygem-thin>=0:${PORTSDIR}/www/rubygem-thin \
		rubygem-uuidtools>=2.1.1:${PORTSDIR}/devel/rubygem-uuidtools

DEPRECATED=	Depends on broken rubygem-dep_selector
EXPIRATION_DATE=	2014-09-25

USE_RUBY=	yes
USE_RUBYGEMS=	yes
RUBYGEM_AUTOPLIST=	yes

PLIST_FILES=	bin/chef-server

.include <bsd.port.mk>
