# Created by: Sean Bruno <sbruno@freebsd.org>
# $FreeBSD$

PORTNAME=	idjc
PORTVERSION=	0.8.14
PORTREVISION=	1
CATEGORIES=	audio python
MASTER_SITES=	SF/idjc/idjc/0.8

MAINTAINER=	sbruno@FreeBSD.org
COMMENT=	Shoutcast/Icecast DJ Console

LICENSE=	LGPL20

LIB_DEPENDS=	libavcodec.so:${PORTSDIR}/multimedia/ffmpeg \
		libavutil.so:${PORTSDIR}/multimedia/ffmpeg \
		libjack.so:${PORTSDIR}/audio/jack \
		libtwolame.so:${PORTSDIR}/audio/twolame \
		libspeex.so:${PORTSDIR}/audio/speex \
		libsndfile.so:${PORTSDIR}/audio/libsndfile \
		libmpg123.so:${PORTSDIR}/audio/mpg123 \
		libFLAC.so:${PORTSDIR}/audio/flac \
		libmp3lame.so:${PORTSDIR}/audio/lame \
		libvorbis.so:${PORTSDIR}/audio/libvorbis \
		libshout-idjc.so:${PORTSDIR}/audio/shout-idjc
RUN_DEPENDS=	oggenc:${PORTSDIR}/audio/vorbis-tools \
		${PYTHON_PKGNAMEPREFIX}mutagen>=0:${PORTSDIR}/audio/py-mutagen \
		${PYTHON_PKGNAMEPREFIX}dbus>=0.8:${PORTSDIR}/devel/py-dbus

OPTIONS_DEFINE=	DOCS

USES=		compiler:nestedfct desktop-file-utils gettext gmake \
		libtool pathfix pkgconfig
LDFLAGS=	-L${LOCALBASE}/lib
MAKE_JOBS_UNSAFE=	yes
GNU_CONFIGURE=		yes
USE_PYTHON=		2.7
USE_PYTHON_PREFIX=	yes
USE_GNOME=		glib20 pygtk2

PLIST_SUB+=		PORTVERSION="${PORTVERSION}"

DOCSDIR=	${PREFIX}/share/doc/${PORTNAME}-${PORTVERSION}
pre-install:
	${REINPLACE_CMD} 's|libvorbis.so.0|libvorbis.so|' \
		${WRKSRC}/python/format.py
	${REINPLACE_CMD} 's|#! /usr/local/bin/python2.72.7|#\!${LOCALBASE}/bin/${PYTHON_VERSION}|' \
		${WRKSRC}/idjc

.include <bsd.port.mk>
