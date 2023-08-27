<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <xsl:template match="/">
    <html>
      <head>
        <title>Product Catalog</title>
      </head>
      <body>
        <h1>Product Catalog</h1>
        <xsl:apply-templates select="products/product"/>
      </body>
    </html>
  </xsl:template>

  <xsl:template match="product">
    <div style="border: 1px solid black; padding: 10px; margin: 10px;">
      <h2><xsl:value-of select="name"/></h2>
      <p><strong>Price:</strong> $<xsl:value-of select="price"/></p>
      <p><strong>Description:</strong> <xsl:value-of select="description"/></p>
      <p><strong>Category:</strong> <xsl:value-of select="@category"/></p>
    </div>
  </xsl:template>

</xsl:stylesheet>
