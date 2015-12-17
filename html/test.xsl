<?xml version="1.0" encoding="utf-8"?>

<xsl:stylesheet
    version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <xsl:output method="html"/>

    <xsl:param name="title"/>


    <xsl:template match="/">
        <body>
            <header>
                <xsl:value-of select="$title"/>
            </header>
            <xsl:apply-templates select="root"/>
        </body>
    </xsl:template>


    <xsl:template match="root">

        <h2>Term: <xsl:value-of select="term"/></h2>
        <p>ID: <xsl:value-of select="id"/><br/>
        Status: <xsl:value-of select="status"/><br/>
        Thesaurus: <xsl:value-of select="thesname"/></p>

    </xsl:template>

</xsl:stylesheet>
