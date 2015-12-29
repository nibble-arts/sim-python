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
                    <xsl:value-of select="$title"/>
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

                <p id="bt">BT: <xsl:value-of select="bt"/></p>
                <p id="nt">NT: <xsl:value-of select="nt"/></p>
                <p id="rt">RT: <xsl:value-of select="rt"/></p>
                <p id="us">US: <xsl:value-of select="us"/></p>
                <p id="uf">UF: <xsl:value-of select="uf"/></p>

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

</xsl:stylesheet>
