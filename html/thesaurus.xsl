<?xml version="1.0" encoding="utf-8"?>

<xsl:stylesheet
    version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <xsl:output method="text" indent="no"/>
    <xsl:strip-space elements="*"/>

    <xsl:param name="title"/>
    <xsl:param name="id"/>

    <xsl:template match="/">
        <html>
            <head>
                <title>
                    <xsl:value-of select="'SWIM'"/>
                </title>
                <link rel="stylesheet" type="text/css" href="/styles.css"/>
<!--                <script type="text/javascript" src="/js/thesaurus.js"/>-->
            </head>
            <body onload="init()">
<!--                <xsl:copy-of select="."/>-->
                <xsl:apply-templates select="root"/>
            </body>
        </html>
    </xsl:template>


    <xsl:template match="root">
        <xsl:choose>
            <xsl:when test="term != ''">
                <h2>Thesaurus: <xsl:value-of select="thesname"/></h2>

                <p id="term"><xsl:value-of select="term"/></p>

                <p id="id">ID: <xsl:value-of select="id"/><br/>
                Status: <xsl:value-of select="status"/></p>

                <p><xsl:call-template name="link">
                    <xsl:with-param name="title" select="'BT'"/>
                    <xsl:with-param name="name" select="bt"/>
                    <xsl:with-param name="id" select="bt_id"/>
                </xsl:call-template></p>

                <p><xsl:call-template name="link">
                    <xsl:with-param name="title" select="'NT'"/>
                    <xsl:with-param name="name" select="nt"/>
                    <xsl:with-param name="id" select="nt_id"/>
                </xsl:call-template></p>

                <p><xsl:call-template name="link">
                    <xsl:with-param name="title" select="'RT'"/>
                    <xsl:with-param name="name" select="rt"/>
                    <xsl:with-param name="id" select="rt_id"/>
                </xsl:call-template></p>

                <p><xsl:call-template name="link">
                    <xsl:with-param name="title" select="'US'"/>
                    <xsl:with-param name="name" select="us"/>
                    <xsl:with-param name="id" select="us_id"/>
                </xsl:call-template></p>

                <p><xsl:call-template name="link">
                    <xsl:with-param name="title" select="'UF'"/>
                    <xsl:with-param name="name" select="uf"/>
                    <xsl:with-param name="id" select="uf_id"/>
                </xsl:call-template></p>

                <p id="sn">Scopenote: <xsl:value-of select="scopenote"/></p>
            </xsl:when>
            <xsl:otherwise>
                <h2>
                    <xsl:text>No term for id </xsl:text>
                    <xsl:value-of select="$id"/>
                </h2>
            </xsl:otherwise>
        </xsl:choose>
    </xsl:template>

    <xsl:template name="link">
        <xsl:param name="title"/>
        <xsl:param name="name"/>
        <xsl:param name="id"/>

        <xsl:value-of select="$title"/><xsl:text>: </xsl:text>

        <xsl:if test="$id">
            <a>
                <xsl:attribute name="href">
                    <xsl:text>index.html?id=</xsl:text>
                    <xsl:value-of select="$id"/>
                </xsl:attribute>

                <xsl:value-of select="$name"/>
                <xsl:text> (</xsl:text><xsl:value-of select="$id"/><xsl:text>)</xsl:text>
            </a>
        </xsl:if>
    </xsl:template> 

</xsl:stylesheet>
