# Created by: Will Andrews <andrews@technologist.com>
# $FreeBSD$

PORTNAME=	robodoc
PORTVERSION=	4.99.41
CATEGORIES=	devel
MASTER_SITES=	http://rfsber.home.xs4all.nl/Robo/ \
		http://seis.bris.ac.uk/~mexas/distfiles/

MAINTAINER=	ports@FreeBSD.org
COMMENT=	Code reference program similar to cxref that produces HTML

LICENSE=	GPLv3

GNU_CONFIGURE=	yes
MAKEFILE=	makefile

OPTIONS_DEFINE=	DOCS EXAMPLES
DOCS_FILES=	AUTHORS ChangeLog NEWS README \
		Docs/manual.html Docs/manual.css Docs/robodoc_example.rc

.include <bsd.port.options.mk>

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/Source/robodoc ${STAGEDIR}${PREFIX}/bin
	${INSTALL_PROGRAM} ${WRKSRC}/Source/robohdrs ${STAGEDIR}${PREFIX}/bin
	${INSTALL_MAN} ${WRKSRC}/Docs/robodoc.1 ${STAGEDIR}${MANPREFIX}/man/man1
	${INSTALL_MAN} ${WRKSRC}/Docs/robohdrs.1 ${STAGEDIR}${MANPREFIX}/man/man1
	${MKDIR} ${STAGEDIR}${DOCSDIR}
	${INSTALL_DATA} ${DOCS_FILES:S,^,${WRKSRC}/,} ${STAGEDIR}${DOCSDIR}
	${MKDIR} ${STAGEDIR}${EXAMPLESDIR}
	${CP} -R ${WRKSRC}/Examples/* ${STAGEDIR}${EXAMPLESDIR}

.include <bsd.port.mk>
