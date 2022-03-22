create database images;
use images;
CREATE TABLE images_tab (
title VARCHAR(250),
link VARCHAR(1000),
description VARCHAR(1000)
);
INSERT INTO images_tab
(title, link, description)
VALUES
('The structure of the DNA double helix', 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/DNA_Structure%2BKey%2BLabelled.pn_NoBB.png/1024px-DNA_Structure%2BKey%2BLabelled.pn_NoBB.png', 'The atoms in the structure are colour-coded by element and the detailed structures of two base pairs are shown in the bottom right.'), 
('DNA replication', 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/DNA_replication_en.svg/1280px-DNA_replication_en.svg.png','The double helix is unwound by a helicase and topo­iso­merase. Next, one DNA polymerase produces the leading strand copy. Another DNA polymerase binds to the lagging strand. This enzyme makes discontinuous segments (called Okazaki fragments) before DNA ligase joins them together.');