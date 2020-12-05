

""" CREATE TABLE IF NOT EXISTS  OGR_LISTE  (
    OGR_ID          INTEGER      PRIMARY KEY AUTOINCREMENT
                                 NOT NULL,
    OGR_ADI         VARCHAR      NOT NULL,
    OGR_SOYADI      VARCHAR      NOT NULL,
    OGR_BABAADI     VARCHAR (20),
    OGR_EPOSTA      VARCHAR      NOT NULL,
    OGR_AP          INT          NOT NULL
                                 DEFAULT (1),
    OGR_KAYIT_ZAMAN DATETIME     NOT NULL
                                 DEFAULT (datetime() ) 
);"""

