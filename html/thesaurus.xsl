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
            </head>
            <body>
                <xsl:copy-of select="."/>
                <xsl:apply-templates select="root"/>
            </body>
        </html>
    </xsl:template>


    <xsl:template match="root">
        <xsl:choose>
            <xsl:when test="term != ''">
                <h2>Term: <xsl:value-of select="term"/></h2>
                <p>ID: <xsl:value-of select="id"/><br/>
                Status: <xsl:value-of select="status"/><br/>
                Thesaurus: <xsl:value-of select="thesname"/></p>
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
